"""GitHub-branch-backed durable Automation V2 state; fail-closed on concurrent updates."""
from __future__ import annotations

import base64
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Callable

STATE_PATH = "automation-v2-state.json"
SCHEMA_VERSION = 1
TIMEZONE = "Asia/Dhaka"
API_ROOT = "https://api.github.com"


@dataclass(frozen=True)
class StateSnapshot:
    state: dict
    blob_sha: str | None


def empty_state() -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "timezone": TIMEZONE,
        "run_ledger": {"schema_version": 1, "timezone": TIMEZONE, "entries": []},
        "international_probe_ledger": {
            "schema_version": 1, "timezone": TIMEZONE, "channels": {}
        },
    }


def validate_state(state: dict) -> dict:
    if not isinstance(state, dict):
        raise ValueError("durable state must be a JSON object")
    if state.get("schema_version") != SCHEMA_VERSION or state.get("timezone") != TIMEZONE:
        raise ValueError("durable state schema or timezone is unsupported")
    run = state.get("run_ledger")
    probe = state.get("international_probe_ledger")
    if not isinstance(run, dict) or run.get("schema_version") != 1 or run.get("timezone") != TIMEZONE or not isinstance(run.get("entries"), list):
        raise ValueError("durable run ledger is invalid")
    if not isinstance(probe, dict) or probe.get("schema_version") != 1 or probe.get("timezone") != TIMEZONE or not isinstance(probe.get("channels"), dict):
        raise ValueError("durable International probe ledger is invalid")
    # Import validators lazily to keep the transport layer lightweight.
    from automation.core.run_ledger_store import parse_run_ledger_json
    from automation.engines.international.probe_ledger import parse_ledger
    parse_run_ledger_json(json.dumps(run))
    parse_ledger(json.dumps(probe))
    return state


class GitHubStateStore:
    """Small Contents-API adapter. A dedicated branch and Actions concurrency group serialize writers."""

    def __init__(self, repository: str, branch: str, token: str,
                 opener: Callable = urllib.request.urlopen):
        if not repository or "/" not in repository or not branch or not token:
            raise ValueError("repository, state branch and token are required")
        self.repository = repository
        self.branch = branch
        self.token = token
        self.opener = opener
        self.url = f"{API_ROOT}/repos/{repository}/contents/{STATE_PATH}"

    def _request(self, method: str, url: str, payload: dict | None = None):
        body = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(url, data=body, method=method, headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
            "User-Agent": "BDIX-IPTV-Automation-V2",
        })
        try:
            with self.opener(request, timeout=20) as response:
                return response.status, json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code == 404 and method == "GET":
                return 404, None
            if exc.code in (409, 422) and method == "PUT":
                raise RuntimeError("durable state changed concurrently; refusing to overwrite it") from exc
            raise RuntimeError(f"GitHub state API request failed with HTTP {exc.code}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            raise RuntimeError("GitHub state API is unavailable; refusing to continue without durable state") from exc

    def load(self) -> StateSnapshot:
        query = urllib.parse.urlencode({"ref": self.branch})
        status, result = self._request("GET", f"{self.url}?{query}")
        if status == 404:
            return StateSnapshot(empty_state(), None)
        if not isinstance(result, dict) or not result.get("sha") or not result.get("content"):
            raise RuntimeError("state branch returned an incomplete state file")
        try:
            raw = base64.b64decode(result["content"], validate=False).decode("utf-8")
            state = validate_state(json.loads(raw))
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise RuntimeError("durable state file is corrupt or unsupported; refusing to reset it") from exc
        return StateSnapshot(state, result["sha"])

    def save(self, state: dict, expected_blob_sha: str | None) -> str:
        validate_state(state)
        payload = {
            "message": "chore(automation-v2): persist validated run state",
            "content": base64.b64encode((json.dumps(state, sort_keys=True, indent=2) + "\n").encode("utf-8")).decode("ascii"),
            "branch": self.branch,
        }
        if expected_blob_sha:
            payload["sha"] = expected_blob_sha
        status, result = self._request("PUT", self.url, payload)
        content = result.get("content") if isinstance(result, dict) else None
        if not isinstance(content, dict) or not content.get("sha"):
            raise RuntimeError("GitHub did not confirm the durable state commit")
        return content["sha"]


def store_from_environment() -> GitHubStateStore:
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    branch = os.environ.get("AUTOMATION_V2_STATE_BRANCH", "automation-v2-state")
    token = os.environ.get("GITHUB_TOKEN", "") or os.environ.get("GH_TOKEN", "")
    return GitHubStateStore(repository, branch, token)


def reserve_remote_run(store: GitHubStateStore, request, active_transaction_id: str | None = None):
    """Reserve one run against cross-run state; a failed remote write aborts the run."""
    from automation.core.run_ledger import LedgerEntry, reserve_run
    from automation.core.run_ledger_store import parse_run_ledger_json, serialize_run_ledger

    snapshot = store.load()
    entries = parse_run_ledger_json(json.dumps(snapshot.state["run_ledger"]))
    decision = reserve_run(request, entries, active_transaction_id)
    if not decision.allowed:
        return decision
    entries.append(LedgerEntry(
        decision.idempotency_key,
        request.engine.strip().casefold(),
        request.business_day,
        request.baseline_commit.lower(),
        "running",
        decision.attempt,
    ))
    updated = dict(snapshot.state)
    updated["run_ledger"] = json.loads(serialize_run_ledger(entries))
    store.save(updated, snapshot.blob_sha)
    return decision


def finish_remote_run(store: GitHubStateStore, idempotency_key: str, attempt: int, status: str):
    """Finalize one exact remote running attempt using compare-and-swap."""
    from dataclasses import replace
    from automation.core.run_ledger_store import parse_run_ledger_json, serialize_run_ledger

    if status not in {"succeeded", "failed", "cancelled"}:
        raise ValueError("final run status must be succeeded, failed or cancelled")
    snapshot = store.load()
    entries = parse_run_ledger_json(json.dumps(snapshot.state["run_ledger"]))
    matches = [i for i, entry in enumerate(entries)
               if entry.idempotency_key == idempotency_key and entry.attempt == attempt]
    if len(matches) != 1 or entries[matches[0]].status != "running":
        raise ValueError("remote run attempt must exist exactly once and still be running")
    entries[matches[0]] = replace(entries[matches[0]], status=status)
    updated = dict(snapshot.state)
    updated["run_ledger"] = json.loads(serialize_run_ledger(entries))
    store.save(updated, snapshot.blob_sha)
    return entries[matches[0]]


def record_remote_probe(store: GitHubStateStore, identity: str, probe):
    """Persist an International probe observation in the same cross-run state document."""
    from automation.engines.international.probe_ledger import record_probe, parse_ledger

    snapshot = store.load()
    probe_text = json.dumps(snapshot.state["international_probe_ledger"])
    updated_probe = parse_ledger(record_probe(probe_text, identity, probe))
    updated = dict(snapshot.state)
    updated["international_probe_ledger"] = updated_probe
    store.save(updated, snapshot.blob_sha)
    return updated_probe


def execute_remote_run(store: GitHubStateStore, request, operation):
    """Run a candidate operation under a durable idempotency reservation."""
    decision = reserve_remote_run(store, request)
    if not decision.allowed:
        return decision, None
    try:
        result = operation()
    except Exception:
        finish_remote_run(store, decision.idempotency_key, decision.attempt, "failed")
        raise
    finish_remote_run(store, decision.idempotency_key, decision.attempt, "succeeded")
    return decision, result
