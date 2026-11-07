#!/usr/bin/env python3
"""Idempotent daily guard and fallback dispatcher for the official discovery workflows.

The 07:00 Asia/Dhaka schedule remains the primary trigger. GitHub documents that
schedule events at the top of an hour can be delayed or dropped before a run is
created. The watchdog only dispatches an official discovery workflow if no run
for that workflow exists on the current Bangladesh calendar date. The workflow
guard ensures that a late scheduled event cannot run a second time that day.
"""
from __future__ import annotations

import json
import os
import sys
import time
from datetime import date, datetime, timezone
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

BD_TZ = ZoneInfo("Asia/Dhaka")
API = "https://api.github.com"
DEFAULT_BRANCH = "main"
VALID_WORKFLOWS = {
    "new-channel-discovery.yml",
    "international-channel-discovery.yml",
}


def parse_github_timestamp(value: str) -> datetime:
    """Parse an Actions API ISO timestamp and normalize it to aware UTC."""
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def bangladesh_date(value: str) -> date:
    """Return the Asia/Dhaka calendar date for a GitHub created_at timestamp."""
    return parse_github_timestamp(value).astimezone(BD_TZ).date()


def today_in_bangladesh(now: datetime | None = None) -> date:
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError("now must be timezone-aware")
    return now.astimezone(BD_TZ).date()


def runs_for_date(runs: list[dict[str, Any]], target_date: date) -> list[dict[str, Any]]:
    """Return successful or still-running attempts for the Bangladesh calendar date.

    Failed, timed-out, cancelled and skipped runs do not consume the day's
    discovery slot: the watchdog must be able to dispatch a retry.
    """
    active_statuses = {"queued", "in_progress", "waiting", "pending", "requested"}
    eligible = []
    for run in runs:
        if not run.get("created_at") or bangladesh_date(run["created_at"]) != target_date:
            continue
        status = str(run.get("status") or "").casefold()
        conclusion = str(run.get("conclusion") or "").casefold()
        if status in active_statuses or (status == "completed" and conclusion == "success"):
            eligible.append(run)
    return eligible


def first_run_id(runs: list[dict[str, Any]]) -> int | None:
    """Return the earliest run ID for the date, with ID as a deterministic tie-break."""
    if not runs:
        return None
    ordered = sorted(
        runs,
        key=lambda run: (parse_github_timestamp(run["created_at"]), int(run["id"])),
    )
    return int(ordered[0]["id"])


def should_current_run_execute(
    runs: list[dict[str, Any]], current_run_id: int | str, target_date: date
) -> bool:
    """Permit only the earliest run for the workflow on a Bangladesh calendar date."""
    todays = runs_for_date(runs, target_date)
    if not todays:
        return False
    return first_run_id(todays) == int(current_run_id)


class GitHubActions:
    def __init__(self, repository: str, token: str):
        if "/" not in repository:
            raise ValueError("GITHUB_REPOSITORY must be owner/repo")
        if not token:
            raise ValueError("GITHUB_TOKEN is unavailable")
        self.repository = repository
        self.token = token

    def request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> Any:
        body = json.dumps(payload).encode("utf-8") if payload is not None else None
        request = Request(
            f"{API}/repos/{self.repository}/{path.lstrip('/')}",
            data=body,
            method=method,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "BDIX-IPTV-Discovery-Schedule-Guard",
                **({"Content-Type": "application/json"} if body is not None else {}),
            },
        )
        try:
            with urlopen(request, timeout=25) as response:
                raw = response.read()
                if not raw:
                    return None
                return json.loads(raw.decode("utf-8"))
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:1000]
            raise RuntimeError(f"GitHub API {method} {path} failed: HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise RuntimeError(f"GitHub API {method} {path} failed: {exc}") from exc

    def workflow_runs(self, workflow_file: str) -> list[dict[str, Any]]:
        if workflow_file not in VALID_WORKFLOWS:
            raise ValueError(f"Unsupported discovery workflow: {workflow_file}")
        path = f"actions/workflows/{quote(workflow_file)}/runs"
        all_runs: list[dict[str, Any]] = []
        for page in range(1, 6):
            result = self.request("GET", f"{path}?per_page=100&page={page}")
            page_runs = result.get("workflow_runs", []) if isinstance(result, dict) else []
            all_runs.extend(page_runs)
            if len(page_runs) < 100:
                break
        return all_runs

    def dispatch(self, workflow_file: str) -> None:
        if workflow_file not in VALID_WORKFLOWS:
            raise ValueError(f"Unsupported discovery workflow: {workflow_file}")
        self.request(
            "POST",
            f"actions/workflows/{quote(workflow_file)}/dispatches",
            {"ref": DEFAULT_BRANCH},
        )


def write_output(name: str, value: str) -> None:
    output_file = os.environ.get("GITHUB_OUTPUT")
    if output_file:
        with open(output_file, "a", encoding="utf-8") as stream:
            stream.write(f"{name}={value}\n")


def guard(workflow_file: str) -> int:
    repository = os.environ["GITHUB_REPOSITORY"]
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    current_run_id = os.environ["GITHUB_RUN_ID"]
    target_date = today_in_bangladesh()
    client = GitHubActions(repository, token)

    # A newly-created Actions run should already be visible to the REST API.
    # Retry briefly, then fail closed rather than risk a duplicate playlist writer.
    todays: list[dict[str, Any]] = []
    for attempt in range(5):
        todays = runs_for_date(client.workflow_runs(workflow_file), target_date)
        if any(int(run["id"]) == int(current_run_id) for run in todays):
            break
        if attempt < 4:
            time.sleep(2)
    if not any(int(run["id"]) == int(current_run_id) for run in todays):
        raise RuntimeError(
            f"Current run {current_run_id} is not visible in GitHub's run history; "
            "failing closed to protect against duplicate daily discovery."
        )

    first_id = first_run_id(todays)
    execute = first_id == int(current_run_id)
    write_output("should_run", "true" if execute else "false")
    if execute:
        print(
            f"Daily discovery owner confirmed: run {current_run_id} is the first "
            f"{workflow_file} run for Bangladesh date {target_date}."
        )
    else:
        winner = next(run for run in todays if int(run["id"]) == first_id)
        print(
            f"Skipping duplicate daily discovery: run {first_id} "
            f"({winner.get('event')}, {winner.get('status')}) already owns "
            f"{workflow_file} for Bangladesh date {target_date}."
        )
    return 0


def watchdog(workflow_files: list[str]) -> int:
    repository = os.environ["GITHUB_REPOSITORY"]
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    target_date = today_in_bangladesh()
    client = GitHubActions(repository, token)

    for workflow_file in workflow_files:
        runs = client.workflow_runs(workflow_file)
        todays = runs_for_date(runs, target_date)
        if todays:
            first_id = first_run_id(todays)
            newest = max(todays, key=lambda run: parse_github_timestamp(run["created_at"]))
            print(
                f"No dispatch needed for {workflow_file}: "
                f"{len(todays)} run(s) exist for {target_date}; "
                f"earliest={first_id}, latest={newest['id']} "
                f"event={newest.get('event')} status={newest.get('status')} "
                f"conclusion={newest.get('conclusion')}."
            )
            continue
        print(
            f"No {workflow_file} run exists for Bangladesh date {target_date}; "
            f"dispatching the repository's official workflow on {DEFAULT_BRANCH}."
        )
        client.dispatch(workflow_file)
        print(f"Dispatch accepted for {workflow_file}.")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        raise SystemExit(
            "Usage: discovery_schedule_guard.py guard <workflow.yml> | "
            "watchdog <workflow1.yml> <workflow2.yml>"
        )
    mode = argv[0]
    if mode == "guard" and len(argv) == 2:
        return guard(argv[1])
    if mode == "watchdog" and len(argv) == 3:
        return watchdog(argv[1:])
    raise SystemExit("Invalid arguments")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
