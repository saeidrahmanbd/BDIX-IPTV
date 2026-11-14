#!/usr/bin/env python3
"""Deduplicate Xtream gateway checks by Bangladesh date and source revision."""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

API = "https://api.github.com"
WORKFLOW = "check-xtream.yml"
BD_TZ = ZoneInfo("Asia/Dhaka")
REQUIRED_JOB = "check"
REQUIRED_STEP = "Check main IPTV Xtream gateway"


def parse_timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def same_day(left: dict[str, Any], right: dict[str, Any]) -> bool:
    if not left.get("created_at") or not right.get("created_at"):
        return False
    return (
        parse_timestamp(left["created_at"]).astimezone(BD_TZ).date()
        == parse_timestamp(right["created_at"]).astimezone(BD_TZ).date()
    )


def successful_check(run: dict[str, Any], client=None) -> bool:
    if str(run.get("status") or "").casefold() != "completed":
        return False
    if str(run.get("conclusion") or "").casefold() != "success":
        return False
    jobs = run.get("jobs")
    if jobs is None and client is not None:
        jobs = client.workflow_run_jobs(int(run["id"]))
    for job in jobs or []:
        if str(job.get("name") or "").casefold() != REQUIRED_JOB:
            continue
        if str(job.get("status") or "").casefold() != "completed":
            continue
        if str(job.get("conclusion") or "").casefold() != "success":
            return False
        return any(
            str(step.get("name") or "").casefold() == REQUIRED_STEP.casefold()
            and str(step.get("conclusion") or "").casefold() == "success"
            for step in job.get("steps") or []
        )
    return False


def should_current_run_execute(
    runs: list[dict[str, Any]],
    current: dict[str, Any],
    event: str = "",
    run_attempt: int = 1,
    client=None,
) -> bool:
    """Run once per Bangladesh date and commit; allow manual retries and failed retries."""
    current_id = int(current.get("id") or -1)
    current_sha = str(current.get("head_sha") or "").strip().lower()
    if len(current_sha) != 40:
        raise ValueError("Current Xtream check has no valid 40-character source commit SHA")

    comparable = [
        run for run in runs
        if int(run.get("id") or -1) != current_id
        and str(run.get("head_sha") or "").strip().lower() == current_sha
        and same_day(run, current)
    ]
    # Concurrency serializes this workflow. Still fail closed if an older
    # same-revision check is active (for example, a run started before this guard).
    if any(str(run.get("status") or "").casefold() != "completed" for run in comparable):
        return False

    manual = str(event or "").casefold() == "workflow_dispatch"
    try:
        attempt = int(run_attempt or 1)
    except (TypeError, ValueError):
        attempt = 1
    if manual or attempt > 1:
        return True

    return not any(successful_check(run, client) for run in comparable)


class GitHubActions:
    def __init__(self, repository: str, token: str):
        if "/" not in repository:
            raise ValueError("GITHUB_REPOSITORY must be owner/repo")
        if not token:
            raise ValueError("GITHUB_TOKEN is unavailable")
        self.repository = repository
        self.token = token

    def get(self, path: str) -> Any:
        request = Request(
            f"{API}/repos/{self.repository}/{path.lstrip('/')}",
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "BDIX-IPTV-Xtream-Check-Guard",
            },
        )
        try:
            with urlopen(request, timeout=25) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:1000]
            raise RuntimeError(f"GitHub API GET {path} failed: HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise RuntimeError(f"GitHub API GET {path} failed: {exc}") from exc

    def workflow_runs(self) -> list[dict[str, Any]]:
        runs = []
        for page in range(1, 4):
            result = self.get(
                f"actions/workflows/{WORKFLOW}/runs?per_page=100&page={page}"
            )
            batch = result.get("workflow_runs", []) if isinstance(result, dict) else []
            runs.extend(batch)
            if len(batch) < 100:
                break
        return runs

    def workflow_run(self, run_id: int) -> dict[str, Any]:
        return self.get(f"actions/runs/{run_id}")

    def workflow_run_jobs(self, run_id: int) -> list[dict[str, Any]]:
        result = self.get(f"actions/runs/{run_id}/jobs?per_page=100")
        return result.get("jobs", []) if isinstance(result, dict) else []


def main() -> int:
    repository = os.environ["GITHUB_REPOSITORY"]
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    run_id = int(os.environ["GITHUB_RUN_ID"])
    event = os.environ.get("GITHUB_EVENT_NAME", "")
    attempt = int(os.environ.get("GITHUB_RUN_ATTEMPT", "1"))
    client = GitHubActions(repository, token)

    current = client.workflow_run(run_id)
    runs = client.workflow_runs()
    if not any(int(run.get("id") or -1) == run_id for run in runs):
        runs.append(current)

    execute = should_current_run_execute(runs, current, event, attempt, client)
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"should_run={'true' if execute else 'false'}\\n")
    if execute:
        print(
            f"Xtream check accepted: source revision {current['head_sha']} "
            f"has no successful check for Bangladesh date "
            f"{parse_timestamp(current['created_at']).astimezone(BD_TZ).date()}."
        )
    else:
        print(
            f"Xtream check skipped: a successful or active check already covers "
            f"source revision {current['head_sha']} for this Bangladesh date."
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"::error::{exc}")
        raise
