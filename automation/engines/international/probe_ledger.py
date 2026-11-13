"""Durable, deterministic International probe ledger serialization; no filesystem or Git side effects."""
from __future__ import annotations
from datetime import date
import json
import hashlib
from automation.engines.international.stream_failure_policy import Probe

SCHEMA_VERSION = 1
TIMEZONE = "Asia/Dhaka"

def url_fingerprint(url: str) -> str:
    return hashlib.sha256(url.strip().encode("utf-8")).hexdigest()

def empty_ledger() -> dict:
    return {"schema_version":SCHEMA_VERSION,"timezone":TIMEZONE,"channels":{}}

def parse_ledger(text: str | None) -> dict:
    if not text:
        return empty_ledger()
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"probe ledger JSON is malformed: {exc}") from exc
    if data.get("schema_version") != SCHEMA_VERSION or data.get("timezone") != TIMEZONE:
        raise ValueError("probe ledger schema or timezone is unsupported")
    if not isinstance(data.get("channels"),dict):
        raise ValueError("probe ledger channels must be an object")
    for identity, observations in data["channels"].items():
        if not isinstance(identity,str) or not identity.strip() or not isinstance(observations,list):
            raise ValueError("probe ledger channel entry is invalid")
        for item in observations:
            _validate_observation(item)
    return data

def _validate_observation(item: dict) -> None:
    if not isinstance(item,dict):
        raise ValueError("probe observation must be an object")
    try:
        date.fromisoformat(item["day"])
    except (KeyError,TypeError,ValueError) as exc:
        raise ValueError("probe observation has invalid Bangladesh calendar date") from exc
    status = item.get("status_code")
    if status is not None and (not isinstance(status,int) or status < 100 or status > 599):
        raise ValueError("probe HTTP status must be 100..599 or null")
    if item.get("stream_state","unknown") not in {"verified","dead","unknown"}:
        raise ValueError("probe stream_state is invalid")
    fingerprint = item.get("url_fingerprint", "")
    if fingerprint and (
        not isinstance(fingerprint,str)
        or len(fingerprint) != 64
        or any(char not in "0123456789abcdef" for char in fingerprint)
    ):
        raise ValueError("probe URL fingerprint must be a lowercase SHA-256 digest")
    if not isinstance(item.get("reason",""),str):
        raise ValueError("probe reason must be text")
    for key in ("network_error","auth_error","rate_limited","geo_blocked"):
        if not isinstance(item.get(key,False),bool):
            raise ValueError(f"probe flag {key} must be boolean")

def probes_for(ledger: dict, identity: str) -> tuple[Probe,...]:
    """Read one channel's observations from an already validated ledger."""
    if not isinstance(ledger,dict) or not isinstance(ledger.get("channels"),dict):
        raise ValueError("probe ledger must be parsed before reading channel observations")
    records = ledger["channels"].get(identity,[])
    return tuple(Probe(date.fromisoformat(item["day"]),item.get("status_code"),
                       item.get("network_error",False),item.get("auth_error",False),
                       item.get("rate_limited",False),item.get("geo_blocked",False),
                       item.get("stream_state","unknown"),item.get("reason",""),item.get("url_fingerprint",""))
                 for item in records)

def _probe_record(probe: Probe) -> dict:
    item={
        "day":probe.day.isoformat(),
        "status_code":probe.status_code,
        "network_error":probe.network_error,
        "auth_error":probe.auth_error,
        "rate_limited":probe.rate_limited,
        "geo_blocked":probe.geo_blocked,
        "stream_state":probe.stream_state,
        "reason":probe.reason,
        "url_fingerprint":probe.url_fingerprint,
    }
    _validate_observation(item)
    return item

def record_probes(ledger_text: str | None, observations: list[tuple[str,Probe]]) -> str:
    """Append a batch of observations with one parse/serialize cycle."""
    ledger=parse_ledger(ledger_text)
    touched=set()
    for identity,probe in observations:
        key=identity.strip()
        if not key:
            raise ValueError("channel identity is required")
        ledger["channels"].setdefault(key,[]).append(_probe_record(probe))
        touched.add(key)
    for key in touched:
        ledger["channels"][key].sort(key=lambda item:item["day"])
    return json.dumps(ledger,sort_keys=True,indent=2) + "\n"

def record_probe(ledger_text: str | None, identity: str, probe: Probe) -> str:
    """Append one observation; duplicate same-day probes are retained to fail closed."""
    return record_probes(ledger_text,[(identity,probe)])
