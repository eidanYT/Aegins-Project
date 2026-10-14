"""Generate nominal square-bipyramid edges and faces; no thickness or robot path."""
import json
import math
from pathlib import Path

def square_bipyramid(edge_m):
    if isinstance(edge_m, bool) or not isinstance(edge_m, (int, float)) or not math.isfinite(edge_m) or edge_m <= 0:
        raise ValueError("edge_m must be finite and positive")
    half, height = edge_m / 2, edge_m / math.sqrt(2)
    vertices = [(-half, -half, 0), (half, -half, 0), (half, half, 0), (-half, half, 0),
                (0, 0, height), (0, 0, -height)]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)] + [(i, tip) for tip in (4, 5) for i in range(4)]
    return vertices, edges

def export_obj(vertices, edges):
    lines = ["# SRR-GEO-001; units m; nominal edges and closed surface, zero thickness; not a robot trajectory"]
    lines += ["v " + " ".join(format(x, ".12g") for x in point) for point in vertices]
    lines += ["l " + str(a + 1) + " " + str(b + 1) for a, b in edges]
    # Consistent outward orientation of all eight triangular faces.
    faces = [(0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4),
             (1, 0, 5), (2, 1, 5), (3, 2, 5), (0, 3, 5)]
    lines += ["f " + " ".join(str(i + 1) for i in face) for face in faces]
    return "\n".join(lines) + "\n"

def export_svg(vertices, edges, edge_m):
    # Orthographic illustrative projection; drawing is intentionally labelled unscaled.
    azimuth, elevation, scale = math.radians(35), math.radians(25), 3850
    points = [(430 + scale * (math.cos(azimuth) * x - math.sin(azimuth) * y),
               300 + scale * (math.sin(elevation) * (math.sin(azimuth) * x + math.cos(azimuth) * y)
                              - math.cos(elevation) * z)) for x, y, z in vertices]
    lines = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 590">',
             '<rect width="860" height="590" fill="#f7fafc"/>',
             '<text x="34" y="46" font-family="Arial" font-size="25" fill="#16324f">Pieza nominal para SRR — bipirámide de base cuadrada</text>',
             '<text x="34" y="78" font-family="Arial" font-size="16" fill="#526579">TBR · Geometría nominal · Sin robot, anclaje ni trayectoria aprobados</text>']
    for a, b in edges:
        x1, y1 = points[a]; x2, y2 = points[b]
        color = "#0c8599" if a < 4 and b < 4 else "#345d9d"
        lines.append(f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="{color}" stroke-width="3"/>')
    for i, (x, y) in enumerate(points):
        lines.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="4" fill="#16324f"/>')
        lines.append(f'<text x="{x+8:.3f}" y="{y-8:.3f}" font-family="Arial" font-size="15" fill="#16324f">V{i+1}</text>')
    lines += [f'<text x="34" y="490" font-family="Arial" font-size="18" fill="#16324f">Arista nominal: {edge_m*1000:.3f} mm · 12 aristas únicas · 6 vértices</text>',
              f'<text x="34" y="522" font-family="Arial" font-size="18" fill="#16324f">Envolvente alineada: {edge_m*1000:.3f} × {edge_m*1000:.3f} × {math.sqrt(2)*edge_m*1000:.3f} mm</text>',
              '<text x="34" y="558" font-family="Arial" font-size="15" fill="#526579">8 caras cerradas solicitadas · Espesor TBD · Proyección ilustrativa sin trayectoria.</text>',
              '</svg>']
    return "\n".join(lines) + "\n"

def main():
    root = Path(__file__).resolve().parents[2]
    case = json.loads((root / "system/caso_srr.json").read_text(encoding="utf-8"))
    length = case["geometry"]["edge_length_m"]
    vertices, edges = square_bipyramid(length)
    (root / "cad/pieza_srr_bipiramide.obj").write_text(export_obj(vertices, edges), encoding="utf-8")
    (root / "cad/pieza_srr_bipiramide.svg").write_text(export_svg(vertices, edges, length), encoding="utf-8")
    print(json.dumps({"case":case["id"],"status":"TBR","edge_length_m":length,"half_height_m":length/math.sqrt(2),
                      "height_m":math.sqrt(2)*length,"total_unique_edge_length_m":len(edges)*length,
                      "vertex_count":len(vertices),"edge_count":len(edges)}, indent=2))

if __name__ == "__main__":
    main()
