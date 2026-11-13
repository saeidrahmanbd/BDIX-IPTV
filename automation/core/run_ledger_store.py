"""Validated JSON persistence and serialized run reservations; local atomic writes only, no Git/network."""
from __future__ import annotations
from dataclasses import replace
from datetime import date, datetime
from zoneinfo import ZoneInfo
import json
from pathlib import Path
from automation.core.atomic_output import atomic_write_v2_output, atomic_write_v2_output_locked, transaction_lock
from automation.core.run_ledger import LedgerEntry, RunRequest, ReservationDecision, reserve_run

SCHEMA_VERSION=1
TIMEZONE="Asia/Dhaka"
LEDGER_PATH="reports/automation-v2/state/run-ledger.json"

def _ledger_path(root: str | Path) -> Path:
    base=Path(root).resolve()
    state=base/"reports"/"automation-v2"/"state"
    if state.is_symlink() or not state.resolve().is_relative_to(base):
        raise ValueError("run ledger state directory escapes repository root")
    path=state/"run-ledger.json"
    if path.is_symlink():
        raise ValueError("run ledger file cannot be a symlink")
    return path

def _validate_entry(item: dict) -> LedgerEntry:
    if not isinstance(item,dict):
        raise ValueError("run ledger entry must be an object")
    try:
        key=item["idempotency_key"]
        engine=item["engine"]
        day=date.fromisoformat(item["business_day"])
        baseline=item["baseline_commit"]
        status=item["status"]
        attempt=item["attempt"]
        started_raw=item.get("started_at")
    except (KeyError,TypeError,ValueError) as exc:
        raise ValueError("run ledger entry is incomplete or invalid") from exc
    if not isinstance(key,str) or len(key)!=64 or any(c not in "0123456789abcdef" for c in key):
        raise ValueError("run ledger idempotency key must be a SHA-256 hex digest")
    if not isinstance(engine,str) or engine not in {"iptv","international","epg","bundle"}:
        raise ValueError("run ledger engine is invalid")
    if not isinstance(baseline,str) or len(baseline) not in (40,64) or any(c not in "0123456789abcdefABCDEF" for c in baseline):
        raise ValueError("run ledger baseline commit is invalid")
    if not isinstance(status,str) or status not in {"running","succeeded","failed","cancelled"}:
        raise ValueError("run ledger status is invalid")
    if not isinstance(attempt,int) or isinstance(attempt,bool) or attempt<1:
        raise ValueError("run ledger attempt must be a positive integer")
    try:
        started_at = datetime.fromisoformat(started_raw) if started_raw else None
    except (TypeError, ValueError) as exc:
        raise ValueError("run ledger started_at timestamp is invalid") from exc
    if started_at is not None and (started_at.tzinfo is None or started_at.utcoffset() is None):
        raise ValueError("run ledger started_at must include a timezone")
    return LedgerEntry(key,engine,day,baseline,status,attempt,started_at)

def parse_run_ledger_json(text: str | None) -> list[LedgerEntry]:
    if not text:
        return []
    try:
        data=json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"run ledger JSON is malformed: {exc}") from exc
    if not isinstance(data,dict) or data.get("schema_version")!=SCHEMA_VERSION or data.get("timezone")!=TIMEZONE or not isinstance(data.get("entries"),list):
        raise ValueError("run ledger schema or timezone is unsupported")
    entries=[_validate_entry(item) for item in data["entries"]]
    seen=set()
    for entry in entries:
        identity=(entry.idempotency_key,entry.attempt)
        if identity in seen:
            raise ValueError("duplicate run ledger attempt")
        seen.add(identity)
    return entries

def serialize_run_ledger(entries: list[LedgerEntry]) -> str:
    validated=[_validate_entry({
        "idempotency_key":e.idempotency_key,"engine":e.engine,"business_day":e.business_day.isoformat(),
        "baseline_commit":e.baseline_commit,"status":e.status,"attempt":e.attempt,"started_at":e.started_at.isoformat() if e.started_at else None
    }) for e in entries]
    identities=[(e.idempotency_key,e.attempt) for e in validated]
    if len(set(identities))!=len(identities):
        raise ValueError("duplicate run ledger attempt")
    payload={"schema_version":SCHEMA_VERSION,"timezone":TIMEZONE,"entries":[
        {"idempotency_key":e.idempotency_key,"engine":e.engine,"business_day":e.business_day.isoformat(),
         "baseline_commit":e.baseline_commit,"status":e.status,"attempt":e.attempt,"started_at":e.started_at.isoformat() if e.started_at else None}
        for e in sorted(validated,key=lambda x:(x.business_day,x.engine,x.idempotency_key,x.attempt))
    ]}
    return json.dumps(payload,sort_keys=True,indent=2)+"\n"

def load_run_ledger(root: str | Path) -> list[LedgerEntry]:
    path=_ledger_path(root)
    if not path.exists():
        return []
    return parse_run_ledger_json(path.read_text(encoding="utf-8"))

def save_run_ledger(root: str | Path, entries: list[LedgerEntry]) -> Path:
    return atomic_write_v2_output(root,LEDGER_PATH,serialize_run_ledger(entries))

def reserve_persisted_run(root: str | Path, request: RunRequest,
                          active_transaction_id: str | None = None) -> ReservationDecision:
    """Serialize load/check/reserve/save under the shared lock to prevent duplicate scheduled runs."""
    with transaction_lock(root):
        entries=load_run_ledger(root)
        decision=reserve_run(request,entries,active_transaction_id)
        if decision.allowed:
            entries.append(LedgerEntry(decision.idempotency_key,request.engine.strip().casefold(),
                                       request.business_day,request.baseline_commit.lower(),"running",decision.attempt,request.requested_at or datetime.now(ZoneInfo(TIMEZONE))))
            atomic_write_v2_output_locked(root,LEDGER_PATH,serialize_run_ledger(entries))
        return decision

def finish_persisted_run(root: str | Path, idempotency_key: str, attempt: int,
                         status: str) -> LedgerEntry:
    """Finalize exactly one running attempt; terminal attempts cannot be silently rewritten."""
    if status not in {"succeeded","failed","cancelled"}:
        raise ValueError("final run status must be succeeded, failed or cancelled")
    if not isinstance(attempt,int) or isinstance(attempt,bool) or attempt<1:
        raise ValueError("attempt must be a positive integer")
    with transaction_lock(root):
        entries=load_run_ledger(root)
        matches=[i for i,e in enumerate(entries) if e.idempotency_key==idempotency_key and e.attempt==attempt]
        if len(matches)!=1:
            raise ValueError("run attempt does not exist exactly once")
        index=matches[0]
        current=entries[index]
        if current.status!="running":
            raise ValueError("only a running attempt can be finalized")
        updated=replace(current,status=status)
        entries[index]=updated
        atomic_write_v2_output_locked(root,LEDGER_PATH,serialize_run_ledger(entries))
        return updated
