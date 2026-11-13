"""Compose one daily probe with durable ledger serialization and lifecycle streak calculation."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from automation.engines.international.probe_ledger import parse_ledger, probes_for, record_probe
from automation.engines.international.stream_failure_policy import Probe, consecutive_definitive_failure_days
from automation.engines.international.stream_probe import probe_stream

@dataclass(frozen=True)
class ObservationResult:
    identity: str
    probe_status: int | None
    failure_streak: int
    ledger_json: str
    already_probed_today: bool = False

def probe_and_record(ledger_text: str | None, identity: str, url: str,
                     today: date, timeout: int = 8) -> ObservationResult:
    """Record at most one probe per channel per Bangladesh calendar day."""
    key=identity.strip()
    if not key:
        raise ValueError("channel identity is required")
    ledger=parse_ledger(ledger_text)
    existing=probes_for(ledger,key)
    if any(item.day == today for item in existing):
        latest=next(item for item in reversed(existing) if item.day == today)
        streak=consecutive_definitive_failure_days(list(existing),today)
        return ObservationResult(key,latest.status_code,streak,ledger_text or "",True)
    if timeout < 1 or timeout > 30:
        raise ValueError("probe timeout must be between 1 and 30 seconds")
    try:
        observation=probe_stream(url,today,timeout)
    except ValueError:
        # Malformed or unsafe URLs are inconclusive; they must never abort the batch or count as failure.
        observation=Probe(today,None,network_error=True)
    updated=record_probe(ledger_text,key,observation)
    streak=consecutive_definitive_failure_days(list(probes_for(parse_ledger(updated),key)),today)
    return ObservationResult(key,observation.status_code,streak,updated,False)
