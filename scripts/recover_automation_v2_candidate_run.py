#!/usr/bin/env python3
"""Dispatch Automation V2 shadow candidates when today's scheduled run is missing or failed.

The scheduler is read-only except for workflow_dispatch. It never writes playlists,
EPG, logos, or durable state. The candidate runner's durable ledger remains the
idempotency authority; this script only recovers missed/failed GitHub schedule events.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import json
import os
import sys
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

API = "https://api.github.com"
TIMEZONE = ZoneInfo("Asia/Dhaka")
WORKFLOW = "automation-v2-candidate-bundle.yml"


def request_json(url: str, token: str, method: str = "GET", payload: dict | None = None):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url, data=data, method=method,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
            "User-Agent": "BDIX-IPTV-AutomationV2-Scheduler",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            raw = response.read()
            return response.status, json.loads(raw.decode("utf-8")) if raw else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"GitHub API {method} failed with HTTP {exc.code}: {detail}") from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError("GitHub API unavailable; refusing to dispatch blindly") from exc


def decide_dispatch(runs: list[dict], main_sha: str, today) -> tuple[bool, str]:
    same_day = []
    for run in runs:
        created = run.get("created_at")
        if not isinstance(created, str):
            continue
        try:
            local_day = datetime.fromisoformat(created.replace("Z", "+00:00")).astimezone(TIMEZONE).date()
        except ValueError:
            continue
        if local_day == today and run.get("head_sha") == main_sha:
            same_day.append(run)
    if not same_day:
        return True, "no candidate-bundle run exists today for the current main commit"
    same_day.sort(key=lambda item: item.get("run_number", 0), reverse=True)
    latest = same_day[0]
    status = latest.get("status")
    conclusion = latest.get("conclusion")
    if status != "completed":
        return False, f"candidate-bundle run #{latest.get('run_number')} is {status}; do not overlap it"
    if conclusion == "success":
        return False, f"candidate-bundle run #{latest.get('run_number')} already succeeded for today's main commit"
    return True, f"latest candidate-bundle run #{latest.get('run_number')} concluded {conclusion}; retry is due"


def run(token: str, repository: str, now: datetime | None = None, dispatch: bool = True) -> str:
    if not token or "/" not in repository:
        raise ValueError("GITHUB_TOKEN and owner/repository are required")
    today = (now or datetime.now(TIMEZONE)).astimezone(TIMEZONE).date()
    _, main = request_json(f"{API}/repos/{repository}/commits/main", token)
    main_sha = main.get("sha") if isinstance(main, dict) else None
    if not isinstance(main_sha, str) or len(main_sha) not in (40, 64):
        raise RuntimeError("GitHub returned no valid current main commit")
    _, payload = request_json(
        f"{API}/repos/{repository}/actions/workflows/{WORKFLOW}/runs?branch=main&per_page=100",
        token,
    )
    runs = payload.get("workflow_runs", []) if isinstance(payload, dict) else []
    if not isinstance(runs, list):
        raise RuntimeError("GitHub returned an invalid workflow-run list")
    should_dispatch, reason = decide_dispatch(runs, main_sha, today)
    if not should_dispatch:
        return "SKIP: " + reason
    if not dispatch:
        return "DRY RUN: " + reason
    request_json(
        f"{API}/repos/{repository}/actions/workflows/{WORKFLOW}/dispatches",
        token, method="POST", payload={"ref": "main"},
    )
    return "DISPATCHED: " + reason


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        result = run(
            os.environ.get("GITHUB_TOKEN", ""),
            os.environ.get("GITHUB_REPOSITORY", ""),
            dispatch=not args.dry_run,
        )
    except Exception as exc:
        print(f"::error::{exc}", file=sys.stderr)
        return 1
    print(result, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
