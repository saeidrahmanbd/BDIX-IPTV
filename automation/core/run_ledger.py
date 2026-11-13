"""Deterministic run-ledger reservation policy; persistence and publishing are intentionally absent."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
import hashlib

VALID_STATUSES = {"running","succeeded","failed","cancelled"}
RUN_LEASE_MINUTES = 130
TIMEZONE = "Asia/Dhaka"

@dataclass(frozen=True)
class RunRequest:
    engine: str
    business_day: date
    baseline_commit: str
    input_fingerprint: str
    requested_at: datetime | None = None

@dataclass(frozen=True)
class LedgerEntry:
    idempotency_key: str
    engine: str
    business_day: date
    baseline_commit: str
    status: str
    attempt: int
    started_at: datetime | None = None

@dataclass(frozen=True)
class ReservationDecision:
    allowed: bool
    idempotency_key: str
    attempt: int
    reason: str

def make_idempotency_key(request: RunRequest) -> str:
    material = "|".join((request.engine.strip().casefold(),request.business_day.isoformat(),
                         request.baseline_commit.lower(),request.input_fingerprint.lower()))
    return hashlib.sha256(material.encode("utf-8")).hexdigest()

def reserve_run(request: RunRequest, entries: list[LedgerEntry],
                active_transaction_id: str | None = None) -> ReservationDecision:
    """Decide whether a run may start; does not mutate or persist the ledger."""
    if not isinstance(request.engine,str) or not request.engine.strip():
        raise ValueError("engine is required")
    engine=request.engine.strip().casefold()
    if len(request.baseline_commit) not in (40,64) or any(c not in "0123456789abcdefABCDEF" for c in request.baseline_commit):
        raise ValueError("baseline commit must be a full hexadecimal object id")
    if len(request.input_fingerprint) != 64 or any(c not in "0123456789abcdefABCDEF" for c in request.input_fingerprint):
        raise ValueError("input fingerprint must be a SHA-256 hex digest")
    key = make_idempotency_key(request)
    matching = [entry for entry in entries if entry.idempotency_key == key]
    if any(entry.status not in VALID_STATUSES for entry in matching):
        raise ValueError("ledger contains an unknown run status")
    if active_transaction_id:
        return ReservationDecision(False,key,0,"another publication transaction holds the global lock")
    now = request.requested_at or datetime.now(ZoneInfo(TIMEZONE))
    if now.tzinfo is None or now.utcoffset() is None:
        raise ValueError("requested_at must be timezone-aware")
    active_runs = []
    for entry in entries:
        if entry.engine.strip().casefold() != engine or entry.status != "running":
            continue
        # Unknown timestamps fail closed. A known lease expires only after a
        # generous window longer than the longest candidate-generation workflow.
        if entry.started_at is None or entry.started_at.tzinfo is None or entry.started_at.utcoffset() is None:
            active_runs.append(entry)
        elif now - entry.started_at <= timedelta(minutes=RUN_LEASE_MINUTES):
            active_runs.append(entry)
    if active_runs:
        return ReservationDecision(False,key,0,"another non-expired run for this engine is already running")
    if any(entry.status == "succeeded" for entry in matching):
        return ReservationDecision(False,key,0,"this exact input has already completed successfully")
    attempt = max((entry.attempt for entry in matching),default=0) + 1
    return ReservationDecision(True,key,attempt,"new run reservation may proceed; ledger persistence remains external")
