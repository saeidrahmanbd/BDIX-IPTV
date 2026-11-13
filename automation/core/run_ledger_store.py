"""Validated JSON persistence for the V2 run ledger; local atomic writes only, no Git/network."""
from __future__ import annotations
from datetime import date
import json
from pathlib import Path
from automation.core.atomic_output import atomic_write_v2_output
from automation.core.run_ledger import LedgerEntry

SCHEMA_VERSION=1
TIMEZONE="Asia/Dhaka"
LEDGER_PATH="reports/automation-v2/state/run-ledger.json"

def empty_run_ledger() -> dict:
    return {"schema_version":SCHEMA_VERSION,"timezone":TIMEZONE,"entries":[]}

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
    except (KeyError,TypeError,ValueError) as exc:
        raise ValueError("run ledger entry is incomplete or invalid") from exc
    if not isinstance(key,str) or len(key)!=64 or any(c not in "0123456789abcdef" for c in key):
        raise ValueError("run ledger idempotency key must be a SHA-256 hex digest")
    if engine not in {"iptv","international","epg"}:
        raise ValueError("run ledger engine is invalid")
    if not isinstance(baseline,str) or len(baseline) not in (40,64) or any(c not in "0123456789abcdefABCDEF" for c in baseline):
        raise ValueError("run ledger baseline commit is invalid")
    if status not in {"running","succeeded","failed","cancelled"}:
        raise ValueError("run ledger status is invalid")
    if not isinstance(attempt,int) or isinstance(attempt,bool) or attempt<1:
        raise ValueError("run ledger attempt must be a positive integer")
    return LedgerEntry(key,engine,day,baseline,status,attempt)

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
        "baseline_commit":e.baseline_commit,"status":e.status,"attempt":e.attempt
    }) for e in entries]
    identities=[(e.idempotency_key,e.attempt) for e in validated]
    if len(set(identities))!=len(identities):
        raise ValueError("duplicate run ledger attempt")
    payload={"schema_version":SCHEMA_VERSION,"timezone":TIMEZONE,"entries":[
        {"idempotency_key":e.idempotency_key,"engine":e.engine,"business_day":e.business_day.isoformat(),
         "baseline_commit":e.baseline_commit,"status":e.status,"attempt":e.attempt}
        for e in sorted(validated,key=lambda x:(x.business_day,x.engine,x.idempotency_key,x.attempt))
    ]}
    return json.dumps(payload,sort_keys=True,indent=2)+"\n"

def load_run_ledger(root: str | Path) -> list[LedgerEntry]:
    path=Path(root)/LEDGER_PATH
    if not path.exists():
        return []
    return parse_run_ledger_json(path.read_text(encoding="utf-8"))

def save_run_ledger(root: str | Path, entries: list[LedgerEntry]) -> Path:
    return atomic_write_v2_output(root,LEDGER_PATH,serialize_run_ledger(entries))
