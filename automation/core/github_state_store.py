"""GitHub-branch-backed durable Automation V2 state; fail-closed on concurrent updates."""
from __future__ import annotations

import base64
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
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
