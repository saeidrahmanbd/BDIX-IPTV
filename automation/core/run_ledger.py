"""Deterministic run-ledger reservation policy; persistence and publishing are intentionally absent."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
import hashlib

VALID_STATUSES = {"running","succeeded","failed","cancelled"}

@dataclass(frozen=True)
class RunRequest:
    engine: str
    business_day: date
    baseline_commit: str
    input_fingerprint: str

@dataclass(frozen=True)
class LedgerEntry:
    idempotency_key: str
    engine: str
    business_day: date
    baseline_commit: str
    status: str
    attempt: int

@dataclass(frozen=True)
class ReservationDecision:
    allowed: bool
    idempotency_key: str
    attempt: int
    reason: str

def make_idempotency_key(request: RunRequest) -> str:
    material = "|".join((request.engine,request.business_day.isoformat(),
                         request.baseline_commit,request.input_fingerprint))
    return hashlib.sha256(material.encode("utf-8")).hexdigest()

def reserve_run(request: RunRequest, entries: list[LedgerEntry],
                active_transaction_id: str | None = None) -> ReservationDecision:
    """Decide whether a run may start; does not mutate or persist the ledger."""
    if not request.engine.strip():
        raise ValueError("engine is required")
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
    if any(entry.engine == request.engine and entry.status == "running" for entry in entries):
        return ReservationDecision(False,key,0,"another run for this engine is already running")
    if any(entry.status == "succeeded" for entry in matching):
        return ReservationDecision(False,key,0,"this exact input has already completed successfully")
    attempt = max((entry.attempt for entry in matching),default=0) + 1
    return ReservationDecision(True,key,attempt,"new run reservation may proceed; ledger persistence remains external")
