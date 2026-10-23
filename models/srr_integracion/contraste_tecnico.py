"""Recompute selected technical results in mm/mL units, without importing its code.

Requires the published technical commit locally. Does not execute its program.
Writes arithmetic evidence only; no hardware or material qualification.
"""
import json
import math
import subprocess
from pathlib import Path

TECHNICAL_COMMIT = "97ecaa8b791a9ba015076693d992796fa5ad2276"
ROOT = Path(__file__).resolve().parents[2]


def read_snapshot(path):
    return json.loads(subprocess.check_output(["git", "show", TECHNICAL_COMMIT + ":" + path], cwd=ROOT))


def main():
    inputs = read_snapshot("models/srr_agente_tecnico/entradas.json")
    reported = read_snapshot("models/srr_agente_tecnico/resultados.json")
    p = {k: v["value"] for k, v in inputs["parameters"].items()}
    a, diameter, width, thickness, speed = [p[k] * 1000 for k in
        ("edge", "bead_diameter", "track_width", "wall_height", "speed")]
    # Reconstruct geometric and material volumes in mm / mm^3, then convert to SI.
    triangle_height = math.sqrt(a*a - (a/2)**2)
    triangle_area = a * triangle_height / 2
    enclosed_mm3 = 2 * a*a * math.sqrt(a*a - 2*(a/2)**2) / 3
    bands = math.ceil(triangle_height / width)
    lengths = [a * (1 - (k + .5)/bands) for k in range(bands)]
    raster_mm = 8 * math.fsum(lengths)
    wire_mm = 12 * a
    bead_mm2 = math.pi * (diameter/2)**2
    wire_mm3, faces_mm3 = bead_mm2 * wire_mm, raster_mm * width * thickness
    material_with_reserve_m3 = (wire_mm3 + faces_mm3) * (1+p["reserve_fraction"]) * 1e-9
    tube_ml = math.pi * (p["tube_radius"]*1000)**2 * (p["tube_length"]*1000) / 1000
    deposition_s = (wire_mm+raster_mm)/speed
    electric_W = p["led_count"] * p["led_current"] * p["led_voltage"]
    optical_W = p["led_count"] * p["led_radiant_power"]
    g, d, u = reported["geometry"], reported["deposition"], reported["uv_thermal"]
    values = [
        ("surface_area", 8*triangle_area*1e-6, g["surface_area_m2"], "m2"),
        ("enclosed_volume_not_resin", enclosed_mm3*1e-9, g["enclosed_volume_m3"], "m3"),
        ("wire_q", bead_mm2*speed*1e-9, d["wire_q_m3_s"], "m3/s"),
        ("face_q", width*thickness*speed*1e-9, d["face_q_m3_s"], "m3/s"),
        ("face_raster_length", raster_mm/1000, d["raster_length_m"], "m"),
        ("deposition_time_without_transits", deposition_s, d["deposit_time_without_transits_s"], "s"),
        ("material_with_reserve", material_with_reserve_m3, d["sum_without_overlap_correction_m3"]+d["reserve_m3"], "m3"),
        ("retained_tube_volume", tube_ml*1e-6, d["retained_tube_volume_m3"], "m3"),
        ("conditional_resin_mass", material_with_reserve_m3*p["resin_density"], d["resin_with_reserve_mass_kg"], "kg"),
        ("led_electric_power", electric_W, u["led_electric_W_typical"], "W"),
        ("led_local_heat", electric_W-optical_W, u["led_junction_heat_W_typical"], "W"),
        ("led_energy_without_driver", electric_W*deposition_s, u["led_energy_for_deposition_J_typical"], "J"),
        ("example_exposure", p["irradiance"]*(p["uv_length"]*1000/speed), u["nominal_dose_J_m2"], "J/m2"),
    ]
    comparison = [{"name": name, "value": value, "reported": original, "unit": unit,
                   "arithmetic_matches": math.isclose(value, original, rel_tol=1e-12, abs_tol=0),
                   "status": "TBR"} for name, value, original, unit in values]
    evidence = {"source_commit": TECHNICAL_COMMIT,
        "scope": "Selected arithmetic recomputed by integration agent; not independent human review or physical verification",
        "not_checked": ["sources/TDS/SDS validity", "robot poses and continuous paths", "hydraulic model applicability",
                        "face support/curing/sealing", "safety and host qualification"],
        "comparisons": comparison}
    (ROOT/"evidence/contraste_tecnico_srr.json").write_text(json.dumps(evidence, indent=2)+"\n", encoding="utf-8")
    if not all(c["arithmetic_matches"] for c in comparison):
        raise SystemExit("Arithmetic mismatch; review before integration")
    print(json.dumps({"arithmetic_comparisons_passed": len(comparison), "physical_verification": False}))


if __name__ == "__main__":
    main()
