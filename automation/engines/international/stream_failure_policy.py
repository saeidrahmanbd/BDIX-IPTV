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

def is_definitive_failure(probe: Probe) -> bool:
    return (not probe.network_error and not probe.auth_error and not probe.rate_limited
            and not probe.geo_blocked and probe.status_code in DEFINITIVE_HTTP_FAILURES)

def consecutive_definitive_failure_days(probes: list[Probe], today: date) -> int:
    """Count only a complete, consecutive Bangladesh-calendar-day streak ending today."""
    by_day = {probe.day: probe for probe in probes}
    count = 0
    day = today
    while day in by_day and is_definitive_failure(by_day[day]):
        count += 1
        day -= timedelta(days=1)
    return count

def action_for_failure_streak(streak: int) -> str:
    if streak <= 0:
        return "KEEP_CURRENT_GROUP"
    if streak < 3:
        return "MOVE_TO_REVIEW"
    return "ELIGIBLE_FOR_REMOVAL_REVIEW"
