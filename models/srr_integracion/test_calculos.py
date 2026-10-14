import json
import math
import unittest
from pathlib import Path
from fractions import Fraction
import calculos as calc
from control_conceptual import State, REQUIRED, transition

class CalculationTests(unittest.TestCase):
    def test_existing_example_checked_in_mm_and_ms(self):
        # Independent arithmetic in the display units: 5 mm/s * 50 ms.
        expected_m = float(Fraction(5, 1000) * Fraction(50, 1000))
        self.assertEqual(calc.temporal_displacement_bound_m(0.005, [0.05]), expected_m)

    def test_delay_allocation_checked_by_rational_arithmetic(self):
        self.assertEqual(calc.maximum_total_delay_s(0.0001, 0.005), float(Fraction(1, 10000) / Fraction(5, 1000)))

    def test_pixel_scale_checked_by_mm_conversion(self):
        expected_m = float(Fraction(100, 1920) / 1000)
        self.assertAlmostEqual(calc.nominal_pixel_scale_m(0.1, 1920), expected_m, places=15)

    def test_existing_config_not_changed_by_model(self):
        root = Path(__file__).resolve().parents[2]
        before = (root / "config/caso_demo.json").read_bytes()
        result = calc.illustrative_results(root)
        self.assertEqual((root / "config/caso_demo.json").read_bytes(), before)
        self.assertEqual(result["status"], "EJEMPLO_NO_APROBADO")

    def test_chamber_mass_balance_and_initial_condition(self):
        self.assertEqual(calc.closed_chamber_concentration_kg_m3(3, 2, 0, 4), 3)
        # Generic mathematical inputs, not payload emission/material estimates.
        self.assertEqual(calc.closed_chamber_concentration_kg_m3(3, 2, 4, 4) * 4, 3 * 4 + 2 * 4)

    def test_concentration_increases_with_generation_and_time(self):
        self.assertGreater(calc.closed_chamber_concentration_kg_m3(0, 2, 3, 4),
                           calc.closed_chamber_concentration_kg_m3(0, 1, 3, 4))

    def test_uncertainty_uses_standard_components(self):
        self.assertEqual(calc.combined_uncertainty_m([0.003, 0.004]), 0.005)

    def test_timeline_energy_sums_segments(self):
        self.assertEqual(calc.active_energy_J([(2, 3), (4, 5)]), 26)

    def test_invalid_inputs_fail(self):
        for x in (float("nan"), float("inf"), -1, True):
            with self.subTest(x=x), self.assertRaises(ValueError):
                calc.temporal_displacement_bound_m(x, [0.1])
        with self.assertRaises(ValueError):
            calc.maximum_total_delay_s(1, 0)
        with self.assertRaises(ValueError):
            calc.nominal_pixel_scale_m(1, 2.5)
        with self.assertRaises(ValueError):
            calc.closed_chamber_concentration_kg_m3(0, 1, 1, 0)

class ConceptualControlTests(unittest.TestCase):
    def setUp(self):
        self.guards = {key: True for key in REQUIRED}

    def test_nominal_cycle(self):
        s = State.IDLE
        for e in ("check_requested", "checks_passed", "prime_requested",
                  "prime_completed", "print_completed", "postprocess_completed",
                  "inspection_completed"):
            s = transition(s, e, self.guards)
        self.assertEqual(s, State.IDLE)

    def test_cannot_print_directly_from_idle(self):
        with self.assertRaises(ValueError):
            transition(State.IDLE, "prime_completed", self.guards)

    def test_open_chamber_blocks_process_start(self):
        self.guards["chamber_closed"] = False
        with self.assertRaises(ValueError):
            transition(State.READY, "prime_requested", self.guards)

    def test_invalid_measurement_blocks_checks_passed(self):
        self.guards["sensors_valid"] = False
        with self.assertRaises(ValueError):
            transition(State.CHECK, "checks_passed", self.guards)

    def test_fault_requires_recovery_authorization(self):
        s = transition(State.PRINT, "data_stale")
        self.assertEqual(s, State.HOLD)
        with self.assertRaises(ValueError):
            transition(s, "prime_completed", self.guards)
        with self.assertRaises(ValueError):
            transition(s, "recovery_authorized", self.guards)
        self.guards["recovery_authorized"] = True
        self.assertEqual(transition(s, "recovery_authorized", self.guards), State.CHECK)

    def test_loss_of_power_is_not_claimed_handled_by_running_software(self):
        # This is a logical event only; passive hardware/energy-loss response remains TBD.
        self.assertEqual(transition(State.PRINT, "power_lost"), State.HOLD)

if __name__ == "__main__":
    unittest.main()
