"""SRR calculations in SI. Illustrative models only; no hardware controller."""
import json
import math
from pathlib import Path

def number(value, name, *, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(name + " must be a finite number")
    if value < 0 or (positive and value == 0):
        raise ValueError(name + " must be positive" if positive else name + " must be nonnegative")
    return value

def temporal_displacement_bound_m(speed_bound_m_s, delay_components_s):
    """Integral distance bound if speed_bound applies over the full interval."""
    v = number(speed_bound_m_s, "speed_bound_m_s")
    parts = list(delay_components_s)
    if not parts:
        raise ValueError("At least one delay component is required")
    return v * math.fsum(number(x, "delay_component_s") for x in parts)

def maximum_total_delay_s(error_allocation_m, speed_bound_m_s):
    return number(error_allocation_m, "error_allocation_m") / number(speed_bound_m_s, "speed_bound_m_s", positive=True)

def nominal_pixel_scale_m(fov_width_m, horizontal_pixels):
    """Ideal image-plane scale; not reconstruction uncertainty."""
    if isinstance(horizontal_pixels, bool) or not isinstance(horizontal_pixels, int) or horizontal_pixels <= 0:
        raise ValueError("horizontal_pixels must be a positive integer")
    return number(fov_width_m, "fov_width_m", positive=True) / horizontal_pixels

def combined_uncertainty_m(standard_components_m):
    """RSS for uncorrelated standard components already expressed in output m."""
    terms = list(standard_components_m)
    if not terms:
        raise ValueError("Uncertainty budget cannot be empty")
    values = [number(x, "standard_component_m") for x in terms]
    return math.hypot(*values)

def closed_chamber_concentration_kg_m3(initial_kg_m3, generation_kg_s, elapsed_s, free_volume_m3):
    """Well-mixed, constant-volume, constant-source case, no removal/leaks."""
    c0 = number(initial_kg_m3, "initial_kg_m3")
    g = number(generation_kg_s, "generation_kg_s")
    t = number(elapsed_s, "elapsed_s")
    v = number(free_volume_m3, "free_volume_m3", positive=True)
    return c0 + g * t / v

def active_energy_J(segments):
    """Nonoverlapping timeline segments with average electrical power in W."""
    items = list(segments)
    if not items:
        raise ValueError("Timeline cannot be empty")
    return math.fsum(number(p, "average_power_W") * number(t, "duration_s") for p, t in items)

def ideal_box_shell_mass_kg(length_m, width_m, height_m, thickness_m, density_kg_m3):
    """Thin-wall closed rectangular shell; excludes apertures, mounts, sealing."""
    l, w, h, t, rho = [number(x, name, positive=True) for x, name in
                       [(length_m, "length_m"), (width_m, "width_m"), (height_m, "height_m"),
                        (thickness_m, "thickness_m"), (density_kg_m3, "density_kg_m3")]]
    if 2 * t >= min(l, w, h):
        raise ValueError("Thickness incompatible with thin-wall envelope")
    return 2 * (l * w + l * h + w * h) * t * rho

def illustrative_results(repo_root):
    case = json.loads((Path(repo_root) / "config/caso_demo.json").read_text(encoding="utf-8"))
    p = case["parameters"]
    speed, offset = p["path_speed"]["value"], p["timing_offset"]["value"]
    # Inputs below already appear in system/ejemplo_trazabilidad.md.
    return {"status": "EJEMPLO_NO_APROBADO", "case": case["id"],
            "temporal_displacement_m": temporal_displacement_bound_m(speed, [offset]),
            "illustrative_error_allocation_m": 0.0001,
            "illustrative_total_delay_s": maximum_total_delay_s(0.0001, speed),
            "illustrative_fov_width_m": 0.1, "illustrative_horizontal_pixels": 1920,
            "nominal_pixel_scale_m": nominal_pixel_scale_m(0.1, 1920),
            "limitations": ["Speed from DEMO is not a validated mission maximum.",
                            "Pixel scale is not metrological accuracy.",
                            "No chamber emission/material/volume numbers are assumed."]}

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    print(json.dumps(illustrative_results(root), indent=2, ensure_ascii=False))
