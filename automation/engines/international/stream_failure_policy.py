"""Pure International playlist stream-failure lifecycle policy."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, timedelta

DEFINITIVE_HTTP_FAILURES = {404, 410}

@dataclass(frozen=True)
class Probe:
    day: date
    status_code: int | None
    network_error: bool = False
    auth_error: bool = False
    rate_limited: bool = False
    geo_blocked: bool = False
    stream_state: str = "unknown"
    reason: str = ""

def is_definitive_failure(probe: Probe) -> bool:
    return (not probe.network_error and not probe.auth_error and not probe.rate_limited
            and not probe.geo_blocked and probe.status_code in DEFINITIVE_HTTP_FAILURES)

def consecutive_definitive_failure_days(probes: list[Probe], today: date) -> int:
    """Count only one unambiguous definitive result per consecutive Dhaka calendar day."""
    grouped: dict[date, list[Probe]] = {}
    for probe in probes:
        grouped.setdefault(probe.day, []).append(probe)
    count = 0
    day = today
    while day in grouped:
        daily = grouped[day]
        # Duplicate observations for one day are ambiguous; fail closed and reset the streak.
        if len(daily) != 1 or not is_definitive_failure(daily[0]):
            break
        count += 1
        day -= timedelta(days=1)
    return count

def action_for_failure_streak(streak: int) -> str:
    if streak <= 0:
        return "KEEP_CURRENT_GROUP"
    if streak < 3:
        return "MOVE_TO_REVIEW"
    return "ELIGIBLE_FOR_REMOVAL_REVIEW"
