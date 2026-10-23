"""Conceptual event/guard model. Does not issue commands to hardware."""
from enum import Enum

class State(str, Enum):
    IDLE = "IDLE"
    CHECK = "CHECK"
    READY = "READY"
    PRIME = "PRIME"
    PRINT = "PRINT"
    FINISH = "FINISH"
    INSPECT = "INSPECT"
    HOLD = "HOLD"

NOMINAL = {
    (State.IDLE, "check_requested"): State.CHECK,
    (State.CHECK, "checks_passed"): State.READY,
    (State.READY, "prime_requested"): State.PRIME,
    (State.PRIME, "prime_completed"): State.PRINT,
    (State.PRINT, "print_completed"): State.FINISH,
    (State.PRINT, "stop_requested"): State.FINISH,
    (State.FINISH, "postprocess_completed"): State.INSPECT,
    (State.INSPECT, "inspection_completed"): State.IDLE,
}
FAULT_EVENTS = {"containment_lost", "pressure_invalid", "temperature_invalid",
                "data_stale", "clock_invalid", "heartbeat_lost",
                "power_lost", "motion_fault", "uv_fault", "material_fault"}
GUARDED = {"checks_passed", "prime_requested", "prime_completed"}
REQUIRED = {"chamber_closed", "containment_path_defined", "sensors_valid",
            "calibration_current", "time_mapping_valid", "fault_response_defined"}

def transition(state, event, guards=None):
    state = State(state)
    if event in FAULT_EVENTS:
        return State.HOLD
    if state == State.HOLD:
        # No automatic restart. Human/host authorization is a proposal, not a safe recovery certificate.
        if event != "recovery_authorized":
            raise ValueError("HOLD does not resume automatically")
        if not guards or guards.get("recovery_authorized") is not True:
            raise ValueError("Recovery authorization missing")
        if not all(guards.get(k) is True for k in REQUIRED):
            raise ValueError("Recovery conditions not satisfied")
        return State.CHECK
    if event in GUARDED and (not guards or not all(guards.get(k) is True for k in REQUIRED)):
        raise ValueError("Operation guards not satisfied")
    try:
        return NOMINAL[(state, event)]
    except KeyError:
        raise ValueError("Transition not permitted") from None
