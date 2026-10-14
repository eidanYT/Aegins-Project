"""Analisis SI sintetico para SRR. Python 3, biblioteca estandar; no controla equipo.

Ejecutar desde este directorio: python calculos.py
Resultados deterministas; no ensayos ni certificacion. Ver README y fuentes.
"""
import csv
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(a, s):
    return tuple(x * s for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def norm(a):
    return math.sqrt(dot(a, a))


def rz(v, q):
    c, s = math.cos(q), math.sin(q)
    return (c*v[0]-s*v[1], s*v[0]+c*v[1], v[2])


def ry(v, q):
    c, s = math.cos(q), math.sin(q)
    return (c*v[0]+s*v[2], v[1], -s*v[0]+c*v[2])


def write_csv(name, fields, rows):
    with (ROOT/name).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    raw = (ROOT/"entradas.json").read_bytes()
    input_document = json.loads(raw)
    canonical_input = json.dumps(input_document, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode("utf-8")
    entries = input_document["parameters"]
    p = {k: v["value"] for k, v in entries.items()}
    if any(v <= 0 for k, v in p.items() if k != "base_x"):
        raise ValueError("Las dimensiones, condiciones y recursos deben ser positivos")
    a = p["edge"]
    vertices = [(-a/2,-a/2,0), (a/2,-a/2,0), (a/2,a/2,0),
                (-a/2,a/2,0), (0,0,a/math.sqrt(2)), (0,0,-a/math.sqrt(2))]
    faces = []
    for apex in (4, 5):
        for i in range(4):
            ids = [i, (i+1) % 4, apex]
            v0, v1, v2 = (vertices[j] for j in ids)
            n = cross(sub(v1,v0), sub(v2,v0))
            centroid = scale(add(add(v0,v1),v2), 1/3)
            if dot(n,centroid) < 0:
                ids[0], ids[1] = ids[1], ids[0]
            faces.append(ids)
    edges = sorted({tuple(sorted((ids[i],ids[(i+1)%3]))) for ids in faces for i in range(3)})
    normals, face_areas = [], []
    for ids in faces:
        v0,v1,v2 = (vertices[j] for j in ids)
        n = cross(sub(v1,v0), sub(v2,v0))
        face_areas.append(norm(n)/2)
        normals.append(scale(n,1/norm(n)))
    area = sum(face_areas)
    volume = sum(dot(vertices[ids[0]], cross(vertices[ids[1]],vertices[ids[2]]))/6 for ids in faces)
    edge_length = sum(norm(sub(vertices[i],vertices[j])) for i,j in edges)
    wire_area = math.pi*p["bead_diameter"]**2/4
    q_wire = wire_area*p["speed"]
    q_face = p["track_width"]*p["wall_height"]*p["speed"]
    # Raster geometrico: lineas en los puntos medios de N bandas; sin uniones.
    h = math.sqrt(3)*a/2
    n_tracks = math.ceil(h/p["track_width"])
    segments = []
    for face_id, ids in enumerate(faces):
        v0,v1,v2 = (vertices[j] for j in ids)
        for k in range(n_tracks):
            frac = (k+0.5)/n_tracks
            start = add(scale(v0,1-frac),scale(v2,frac))
            end = add(scale(v1,1-frac),scale(v2,frac))
            if k % 2:
                start,end = end,start
            segments.append((face_id,k,start,end))
    raster_length = sum(norm(sub(t,s)) for _,_,s,t in segments)
    time_wire = edge_length/p["speed"]
    time_face = raster_length/p["speed"]
    wire_volume = wire_area*edge_length
    face_volume = raster_length*p["track_width"]*p["wall_height"]
    # Suma sin descontar intersecciones: inventario ilustrativo de aristas + caras.
    total_deposit = wire_volume+face_volume
    reserve = total_deposit*p["reserve_fraction"]
    hydraulic_rows = []
    for mode, q in (("aristas",q_wire), ("caras",q_face)):
        nozzle_dp = 8*p["reference_viscosity"]*p["nozzle_length"]*q/(math.pi*p["nozzle_radius"]**4)
        tube_dp = 8*p["reference_viscosity"]*p["tube_length"]*q/(math.pi*p["tube_radius"]**4)
        dp = nozzle_dp+tube_dp
        piston_area = math.pi*p["piston_diameter"]**2/4
        hydraulic_rows.append({"mode":mode,"q_m3_s":q,"nozzle_dp_Pa":nozzle_dp,
                               "tube_dp_Pa":tube_dp,"total_dp_Pa":dp,
                               "ideal_piston_force_N":dp*piston_area,
                               "piston_speed_m_s":q/piston_area,
                               "wall_shear_rate_s_inv":4*q/(math.pi*p["nozzle_radius"]**3),
                               "hydraulic_power_W":dp*q})
    # Posicion + direccion con 5 R: Rz(q1), Ry(q2), Ry(q3), Rz(q4), Ry(q5).
    # Enlaces +x; herramienta +z. q3 rama codo positiva. No hay cuerpos ni colisiones.
    base = (p["base_x"],0,0)
    l1,l2,tool = p["link_1"],p["link_2"],p["tool_length"]
    pose_rows = []
    for face_id,k,start,end in segments:
        normal = normals[face_id]
        direction = scale(normal,-1)
        for sample, frac in enumerate((0,0.5,1)):
            surface = add(scale(start,1-frac),scale(end,frac))
            tip = add(surface,scale(normal,p["standoff"]))
            wrist = sub(sub(tip,base),scale(direction,tool))
            rho = math.hypot(wrist[0],wrist[1])
            c3 = (dot(wrist,wrist)-l1*l1-l2*l2)/(2*l1*l2)
            if abs(c3) > 1:
                raise ValueError("Pose fuera del alcance radial ideal")
            q1 = math.atan2(wrist[1],wrist[0])
            q3 = math.acos(c3)
            q2 = math.atan2(-wrist[2],rho)-math.atan2(l2*math.sin(q3),l1+l2*math.cos(q3))
            local = ry(rz(direction,-q1),-(q2+q3))
            q4 = math.atan2(local[1],local[0])
            q5 = math.acos(max(-1,min(1,local[2])))
            qs = (q1,q2,q3,q4,q5)
            wrist_fk = rz(add(ry((l1,0,0),q2),ry((l2,0,0),q2+q3)),q1)
            direction_fk = rz(ry(rz(ry((0,0,1),q5),q4),q2+q3),q1)
            tip_fk = add(add(base,wrist_fk),scale(direction_fk,tool))
            limit_ok = abs(q3) <= p["elbow_limit"] and all(abs(q)<=p["other_joint_limit"] for q in qs)
            pose_rows.append({"face":face_id,"track":k,"sample":sample,
                              "x_m":tip[0],"y_m":tip[1],"z_m":tip[2],
                              "q1_rad":q1,"q2_rad":q2,"q3_rad":q3,"q4_rad":q4,"q5_rad":q5,
                              "position_residual_m":norm(sub(tip_fk,tip)),
                              "direction_residual":norm(sub(direction_fk,direction)),
                              "within_proposed_limits":limit_ok,
                              "wrist_singularity_indicator":abs(math.sin(q5))})
    led_electric = p["led_count"]*p["led_current"]*p["led_voltage"]
    led_optical = p["led_count"]*p["led_radiant_power"]
    uv_time = p["uv_length"]/p["speed"]
    checks = {
        "edges_equal_input": all(math.isclose(norm(sub(vertices[i],vertices[j])),a,rel_tol=1e-12) for i,j in edges),
        "mesh_is_closed": all(sum((i in ids and j in ids) for ids in faces)==2 for i,j in edges),
        "euler_relation": len(vertices)-len(edges)+len(faces)==2,
        "mesh_area_vs_equilateral_formula": math.isclose(area,2*math.sqrt(3)*a*a,rel_tol=1e-12),
        "mesh_volume_vs_two_pyramids": math.isclose(volume,math.sqrt(2)*a**3/3,rel_tol=1e-12),
        "raster_lengths_vs_band_sum": math.isclose(raster_length,8*a*n_tracks/2,rel_tol=1e-12),
        "unit_volume_round_trip": math.isclose(q_wire*1e6*60/60/1e6,q_wire,rel_tol=1e-12),
        "unit_dose_round_trip": math.isclose((p["irradiance"]*uv_time)*0.1/0.1,p["irradiance"]*uv_time,rel_tol=1e-12),
        "ik_forward_position": max(row["position_residual_m"] for row in pose_rows)<1e-12,
        "ik_forward_direction": max(row["direction_residual"] for row in pose_rows)<1e-12,
        "ik_proposed_limits": all(row["within_proposed_limits"] for row in pose_rows),
        "led_energy_partition": 0<=led_optical<=led_electric
    }
    out = {
        "metadata":{"version":"0.1.0","inputs_sha256":hashlib.sha256(canonical_input).hexdigest(),
                    "hash_basis":"JSON canonical UTF-8, sort_keys, compact separators, ensure_ascii=False",
                    "status":"EJEMPLO/TBR","method":"A: analisis sintetico, comprobacion interna del autor",
                    "independent_review":"PENDIENTE; no ensayo fisico"},
        "geometry":{"vertices":len(vertices),"edges":len(edges),"faces":len(faces),
                    "bounds_m":[a,a,math.sqrt(2)*a],"surface_area_m2":area,"enclosed_volume_m3":volume,
                    "wire_length_m":edge_length,"face_normals":normals},
        "deposition":{"wire_q_m3_s":q_wire,"face_q_m3_s":q_face,
                      "raster_tracks_per_face":n_tracks,"raster_spacing_m":h/n_tracks,
                      "raster_length_m":raster_length,"wire_time_s":time_wire,"face_time_s":time_face,
                      "deposit_time_without_transits_s":time_wire+time_face,
                      "wire_volume_m3":wire_volume,"face_volume_m3":face_volume,
                      "first_order_shell_volume_m3":area*p["wall_height"],
                      "sum_without_overlap_correction_m3":total_deposit,
                      "reserve_m3":reserve,"resin_with_reserve_mass_kg":(total_deposit+reserve)*p["resin_density"],
                      "reservoir_resin_mass_kg":p["reservoir_volume"]*p["resin_density"],
                      "ideal_piston_stroke_m":p["reservoir_volume"]/(math.pi*p["piston_diameter"]**2/4),
                      "retained_tube_volume_m3":math.pi*p["tube_radius"]**2*p["tube_length"]},
        "hydraulics_sensitivity_not_design_pressure":hydraulic_rows,
        "kinematics":{"pose_samples":len(pose_rows),"limits_passed":sum(row["within_proposed_limits"] for row in pose_rows),
                      "max_position_residual_m":max(row["position_residual_m"] for row in pose_rows),
                      "max_direction_residual":max(row["direction_residual"] for row in pose_rows),
                      "min_wrist_singularity_indicator":min(row["wrist_singularity_indicator"] for row in pose_rows),
                      "q_min_rad":[min(row[f"q{i}_rad"] for row in pose_rows) for i in range(1,6)],
                      "q_max_rad":[max(row[f"q{i}_rad"] for row in pose_rows) for i in range(1,6)]},
        "uv_thermal":{"exposure_time_s":uv_time,"nominal_dose_J_m2":p["irradiance"]*uv_time,
                      "fixed_positive_z_face_factors":[max(0,n[2]) for n in normals],
                      "led_electric_W_typical":led_electric,"led_optical_W_typical":led_optical,
                      "led_junction_heat_W_typical":led_electric-led_optical,
                      "led_energy_for_deposition_J_typical":led_electric*(time_wire+time_face),
                      "steady_delta_K_only_led_junction":[{"conductance_W_K":g,"delta_K":(led_electric-led_optical)/g} for g in (p["conductance_1"],p["conductance_2"],p["conductance_3"])]},
        "internal_checks":checks
    }
    (ROOT/"resultados.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
    write_csv("poses.csv",list(pose_rows[0]),pose_rows)
    write_csv("raster.csv",["face","track","start_x_m","start_y_m","start_z_m","end_x_m","end_y_m","end_z_m"],
              [{"face":f,"track":k,**{f"start_{axis}_m":s[i] for i,axis in enumerate("xyz")},
                **{f"end_{axis}_m":t[i] for i,axis in enumerate("xyz")}} for f,k,s,t in segments])
    obj = ["# EJEMPLO/TBR; unidades m; superficie externa ideal, sin espesor ni anclaje"]
    obj += ["v " + " ".join(f"{v:.12g}" for v in vertex) for vertex in vertices]
    obj += ["f " + " ".join(str(i+1) for i in ids) for ids in faces]
    (ROOT/"bipiramide.obj").write_text("\n".join(obj)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({"internal_checks":checks,"pose_samples":len(pose_rows),"deposit_time_s":time_wire+time_face}))
    if not all(checks.values()):
        raise SystemExit("Hay comprobaciones internas fallidas; no dar por listo")


if __name__ == "__main__":
    main()
