#!/usr/bin/env python3
"""Release only demonstrably stale V2 bundle reservations after checking live Actions runs."""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import replace
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from automation.core.github_state_store import store_from_environment
from automation.core.run_ledger import RUN_LEASE_MINUTES
from automation.core.run_ledger_store import parse_run_ledger_json, serialize_run_ledger

API = "https://api.github.com"
TZ = ZoneInfo("Asia/Dhaka")


def live_actions_runs(repository: str, token: str) -> list[dict]:
    url = f"{API}/repos/{repository}/actions/workflows/automation-v2-candidate-bundle.yml/runs?status=in_progress&per_page=100"
    request = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "BDIX-IPTV-Automation-V2",
    })
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, urllib.error.HTTPError) as exc:
        raise RuntimeError("cannot verify live GitHub Actions runs; refusing ledger recovery") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("workflow_runs"), list):
        raise RuntimeError("GitHub Actions returned an invalid in-progress run listing")
    if payload.get("total_count", 0) > 100:
        raise RuntimeError("more than 100 active candidate-bundle runs; pagination is required, refusing recovery")
    return payload["workflow_runs"]


def is_stale_bundle_reservation(entry, now: datetime) -> bool:
    if entry.engine != "bundle" or entry.status != "running":
        return False
    if entry.started_at is None:
        return True
    return now - entry.started_at > timedelta(minutes=RUN_LEASE_MINUTES)


def reconcile(now: datetime | None = None) -> dict:
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    token = os.environ.get("GITHUB_TOKEN", "") or os.environ.get("GH_TOKEN", "")
    if not repository or not token:
        raise RuntimeError("repository and GitHub token are required")
    active = live_actions_runs(repository, token)
    if active:
        identifiers = [str(run.get("id", "unknown")) for run in active]
        raise RuntimeError("live GitHub Actions runs exist; refusing recovery: " + ", ".join(identifiers))

    store = store_from_environment()
    snapshot = store.load()
    entries = parse_run_ledger_json(json.dumps(snapshot.state["run_ledger"]))
    current = now or datetime.now(TZ)
    if current.tzinfo is None or current.utcoffset() is None:
        raise ValueError("reconciliation time must be timezone-aware")

    recovered = []
    updated_entries = []
    for entry in entries:
        if is_stale_bundle_reservation(entry, current):
            updated_entries.append(replace(entry, status="failed"))
            recovered.append({
                "idempotency_key": entry.idempotency_key,
                "attempt": entry.attempt,
                "business_day": entry.business_day.isoformat(),
                "started_at": entry.started_at.isoformat() if entry.started_at else None,
                "reason": "no GitHub Actions runs are in progress; reservation exceeded lease or lacked a timestamp",
            })
        else:
            updated_entries.append(entry)

    if recovered:
        updated = dict(snapshot.state)
        updated["run_ledger"] = json.loads(serialize_run_ledger(updated_entries))
        store.save(updated, snapshot.blob_sha)
    return {"recovered_count": len(recovered), "recovered": recovered,
            "active_actions_runs": 0, "state_updated": bool(recovered)}


if __name__ == "__main__":
    try:
        result = reconcile()
        print(json.dumps(result, indent=2, sort_keys=True))
    except Exception as exc:
        print(f"SAFE RECOVERY ABORTED: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(1)
