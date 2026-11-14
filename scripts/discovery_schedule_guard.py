#!/usr/bin/env python3
"""Idempotent daily guard and fallback dispatcher for the official discovery workflows.

The 07:00 Asia/Dhaka schedule remains the primary trigger. GitHub documents that
schedule events at the top of an hour can be delayed or dropped before a run is
created. The watchdog only dispatches an official discovery workflow if no run
for that workflow exists on the current Bangladesh calendar date. The workflow guard ensures that a late scheduled event cannot run a second time that day.
An explicit manual dispatch may rerun discovery after a completed daily run, but
will not overlap another active discovery run.
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
    "iptv-maintenance.yml", "new-channel-discovery.yml",
    "international-channel-discovery.yml", "playlist-logo-localization.yml",
    "international-stream-health.yml", "epg-refresh.yml",
}
REQUIRED_JOB_BY_WORKFLOW = {
    "iptv-maintenance.yml": "maintain",
    "new-channel-discovery.yml": "discover",
    "international-channel-discovery.yml": "discover",
    "playlist-logo-localization.yml": "localize",
    "international-stream-health.yml": "check",
    "epg-refresh.yml": "refresh",
}
REQUIRED_STEP_BY_WORKFLOW = {
    "iptv-maintenance.yml": "Run maintenance",
    "new-channel-discovery.yml": "Discover Bangladesh and India candidates into manual-review queues",
    "international-channel-discovery.yml": "Reorganize International playlist and enforce unique primary IDs",
    "playlist-logo-localization.yml": "Localize and commit logos",
    "international-stream-health.yml": "Probe all International streams and apply three-day policy",
    "epg-refresh.yml": "Regenerate, validate and publish XMLTV",
}
RECOVERY_AFTER_LOCAL = {
    "iptv-maintenance.yml": (7, 30),
    "new-channel-discovery.yml": (7, 30),
    "international-channel-discovery.yml": (7, 30),
    "playlist-logo-localization.yml": (8, 30),
    "international-stream-health.yml": (9, 15),
    "epg-refresh.yml": (9, 30),
}


def recovery_is_due(workflow_file: str, now: datetime | None = None) -> bool:
    if workflow_file not in RECOVERY_AFTER_LOCAL:
        raise ValueError(f"Unsupported recovery workflow: {workflow_file}")
    current = now or datetime.now(BD_TZ)
    current = current.replace(tzinfo=BD_TZ) if current.tzinfo is None else current.astimezone(BD_TZ)
    hour, minute = RECOVERY_AFTER_LOCAL[workflow_file]
    return (current.hour, current.minute) >= (hour, minute)



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


def is_manual_retry(
    event: str | None,
    run_attempt: Any = 1,
    workflow_file: str | None = None,
    commit_message: str = "",
) -> bool:
    """Recognize explicit dispatches, reruns, and a workflow-scoped push marker."""
    try:
        attempt = int(run_attempt or 1)
    except (TypeError, ValueError):
        attempt = 1
    if str(event or "").casefold() == "workflow_dispatch" or attempt > 1:
        return True
    markers = {
        "international-channel-discovery.yml": "[manual-international-discovery]",
        "new-channel-discovery.yml": "[manual-new-channel-discovery]",
    }
    marker = markers.get(str(workflow_file or "").strip())
    return (
        str(event or "").casefold() == "push"
        and bool(marker)
        and marker in str(commit_message or "")
    )


def runs_for_date(runs: list[dict[str, Any]], target_date: date) -> list[dict[str, Any]]:
    """Include every event/status for the date; pending and failed runs count too."""
    return [
        run for run in runs
        if run.get("created_at") and bangladesh_date(run["created_at"]) == target_date
    ]


def successful_required_job(jobs: list[dict[str, Any]], workflow_file: str) -> bool:
    """Require success of the workflow's real writer/probe step, not a guard-only no-op."""
    required_job = REQUIRED_JOB_BY_WORKFLOW.get(workflow_file, "discover")
    required_step = REQUIRED_STEP_BY_WORKFLOW.get(workflow_file)
    if not required_step:
        return False
    for job in jobs:
        if str(job.get("name") or "").casefold() != required_job.casefold():
            continue
        if str(job.get("status") or "").casefold() != "completed":
            continue
        if str(job.get("conclusion") or "").casefold() not in {"success", "neutral"}:
            return False
        steps = job.get("steps") or []
        return any(
            str(step.get("name") or "").casefold() == required_step.casefold()
            and str(step.get("conclusion") or "").casefold() in {"success", "neutral"}
            for step in steps
        )
    return False


def successful_discovery_job(jobs: list[dict[str, Any]]) -> bool:
    """Backward-compatible discovery-job predicate used by daily guards."""
    return successful_required_job(jobs, "new-channel-discovery.yml")


def run_blocks_retry(run: dict[str, Any], client=None, workflow_file: str = "new-channel-discovery.yml") -> bool:
    """Only an active run or a successful *discovery job* owns today's execution.

    A workflow can conclude successfully when its discover job was skipped by
    the daily guard. Such no-op runs must not suppress the watchdog or later
    recovery attempts; inspect the job-level conclusion before treating a
    completed workflow run as the daily owner.
    """
    status = str(run.get("status") or "").casefold()
    conclusion = str(run.get("conclusion") or "").casefold()
    if status != "completed":
        return True
    if conclusion not in {"success", "neutral"}:
        return False
    jobs = client.workflow_run_jobs(int(run["id"])) if client is not None else run.get("jobs", [])
    return successful_required_job(jobs if isinstance(jobs, list) else [], workflow_file)


def watchdog_run_blocks_retry(
    run: dict[str, Any],
    client=None,
    workflow_file: str = "new-channel-discovery.yml",
) -> bool:
    """Decide whether a completed run satisfies the watchdog's daily obligation.

    EPG's canonical daily refresh is scheduled for 09:00 Asia/Dhaka. A
    successful push/workflow_run before 09:00 may have built yesterday's
    inputs, so it must not suppress the 09:30 recovery dispatch when the
    scheduled run was missed. Active runs still block overlapping dispatches;
    successful EPG runs created at/after 09:00 satisfy the daily obligation.
    """
    if workflow_file == "epg-refresh.yml":
        status = str(run.get("status") or "").casefold()
        if status == "completed":
            created_at = run.get("created_at")
            if not created_at:
                return False
            local_created = parse_github_timestamp(created_at).astimezone(BD_TZ)
            if (local_created.hour, local_created.minute) < (9, 0):
                return False
    return run_blocks_retry(run, client, workflow_file)


def first_run_id(runs: list[dict[str, Any]], client=None, workflow_file: str = "new-channel-discovery.yml") -> int | None:
    """Return the earliest active or genuinely successful discovery run."""
    owner_check = watchdog_run_blocks_retry if workflow_file == "epg-refresh.yml" else run_blocks_retry
    eligible = [run for run in runs if owner_check(run, client, workflow_file)]
    if not eligible:
        return None
    ordered = sorted(
        eligible,
        key=lambda run: (parse_github_timestamp(run["created_at"]), int(run["id"])),
    )
    return int(ordered[0]["id"])


def should_current_run_execute(
    runs: list[dict[str, Any]],
    current_run_id: int | str,
    target_date: date,
    client=None,
    event: str | None = None,
    workflow_file: str = "new-channel-discovery.yml",
) -> bool:
    """Choose a daily owner from competing runs, excluding this run from self-checks.

    GitHub can expose stale job-level state for an in-flight run. The current
    run is therefore not qualified by its own writer-step status. Completed
    successful writer runs block duplicates; the earliest active run owns the
    slot. Manual dispatches may retry after completed runs but cannot overlap.
    """
    current_id = int(current_run_id)
    todays = runs_for_date(runs, target_date)
    current = next((run for run in todays if int(run.get("id") or -1) == current_id), None)
    if current is None:
        return False

    others = [run for run in todays if int(run.get("id") or -1) != current_id]
    manual = str(event or "").casefold() == "workflow_dispatch"
    active_others = [
        run for run in others
        if str(run.get("status") or "").casefold() != "completed"
    ]
    if manual:
        return not active_others

    # EPG has a fixed 09:00 Asia/Dhaka daily refresh. Push/workflow_run events
    # can legitimately rebuild the guide before that time, but they must not
    # consume the scheduled run's daily slot. The scheduled event therefore
    # takes priority over earlier non-scheduled successes; once it succeeds,
    # later automatic events are suppressed for the rest of the Bangladesh day.
    if workflow_file == "epg-refresh.yml":
        successful_scheduled = [
            run for run in others
            if str(run.get("event") or "").casefold() == "schedule"
            and run_blocks_retry(run, client, workflow_file)
        ]
        if successful_scheduled:
            return False

        current_created = parse_github_timestamp(current["created_at"])
        if str(event or "").casefold() == "schedule":
            earlier_active = [
                run for run in active_others
                if parse_github_timestamp(run["created_at"]) <= current_created
            ]
            return not earlier_active

        earlier_scheduled_active = [
            run for run in active_others
            if str(run.get("event") or "").casefold() == "schedule"
            and parse_github_timestamp(run["created_at"]) < current_created
        ]
        if earlier_scheduled_active:
            return False

    owner_check = watchdog_run_blocks_retry if workflow_file == "epg-refresh.yml" else run_blocks_retry
    successful_others = [
        run for run in others
        if str(run.get("status") or "").casefold() == "completed"
        and owner_check(run, client, workflow_file)
    ]
    if successful_others:
        return False
    if not active_others:
        return True

    owner = min(
        active_others + [current],
        key=lambda run: (parse_github_timestamp(run["created_at"]), int(run["id"])),
    )
    return int(owner["id"]) == current_id

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

    def workflow_run_jobs(self, run_id: int) -> list[dict[str, Any]]:
        """Return job-level outcomes so guard-only successes are not mistaken for discoveries."""
        result = self.request("GET", f"actions/runs/{int(run_id)}/jobs?per_page=100")
        jobs = result.get("jobs", []) if isinstance(result, dict) else []
        return jobs if isinstance(jobs, list) else []

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
    client = GitHubActions(repository, token)

    # Query the current run directly instead of relying on the eventually
    # consistent workflow-runs collection. This also anchors the Bangladesh
    # date to when GitHub created the run, not when a queued job finally starts.
    current_run = client.request("GET", f"actions/runs/{current_run_id}")
    if not isinstance(current_run, dict) or not current_run.get("created_at"):
        raise RuntimeError(f"Could not retrieve creation time for current run {current_run_id}.")
    expected_path = f".github/workflows/{workflow_file}"
    if current_run.get("path") and current_run["path"].split("@", 1)[0] != expected_path:
        raise RuntimeError(
            f"Current run {current_run_id} belongs to {current_run.get('path')}, "
            f"not {expected_path}."
        )
    target_date = bangladesh_date(current_run["created_at"])

    # Merge the directly fetched run into the collection so it is always
    # considered, even if the list endpoint has not indexed it yet.
    runs = client.workflow_runs(workflow_file)
    by_id = {int(run["id"]): run for run in runs if run.get("id") is not None}
    by_id[int(current_run_id)] = current_run
    todays = runs_for_date(list(by_id.values()), target_date)

    event = str(current_run.get("event") or "").casefold()
    head_commit = current_run.get("head_commit") or {}
    manual_retry = is_manual_retry(
        event,
        current_run.get("run_attempt", 1),
        workflow_file,
        str(head_commit.get("message") or ""),
    )
    execution_event = "workflow_dispatch" if manual_retry else event
    execute = should_current_run_execute(
        todays, current_run_id, target_date, client, event=execution_event,
        workflow_file=workflow_file,
    )
    write_output("should_run", "true" if execute else "false")
    if execute and manual_retry:
        action = "dispatch" if event == "workflow_dispatch" else "rerun"
        print(
            f"Manual discovery {action} accepted: run {current_run_id} may refresh "
            f"{workflow_file} for Bangladesh date {target_date}; completed daily runs "
            f"do not block an explicit manual retry."
        )
    elif execute:
        print(
            f"Daily discovery owner confirmed: run {current_run_id} is the first "
            f"{workflow_file} run for Bangladesh date {target_date}."
        )
    else:
        if manual_retry:
            blockers = [
                run for run in todays
                if int(run.get("id") or -1) != int(current_run_id)
                and str(run.get("status") or "").casefold() != "completed"
            ]
            winner = min(
                blockers,
                key=lambda run: (parse_github_timestamp(run["created_at"]), int(run["id"])),
            )
            print(
                f"Skipping manual discovery run {current_run_id}: active run "
                f"{winner['id']} ({winner.get('event')}, {winner.get('status')}) "
                f"is already running {workflow_file} for Bangladesh date {target_date}."
            )
        else:
            first_id = first_run_id(todays, client, workflow_file)
            winner = next(run for run in todays if int(run["id"]) == first_id)
            print(
                f"Skipping duplicate daily discovery: run {first_id} "
                f"({winner.get('event')}, {winner.get('status')}) already owns "
                f"{workflow_file} for Bangladesh date {target_date}."
            )
    return 0


def wait_for_epg_runs_to_settle(
    client,
    target_date: date,
    runs: list[dict[str, Any]],
    max_polls: int = 8,
    poll_interval: int = 10,
    sleep_fn=time.sleep,
) -> list[dict[str, Any]]:
    """Wait for same-day EPG runs to finish before deciding whether recovery is needed.

    A workflow_run/push event may still be active at the 09:30 watchdog checkpoint
    even though its daily guard will skip the actual refresh. Waiting lets the
    watchdog distinguish a real post-09:00 publication from a guard-only no-op.
    """
    def active_today(items):
        return [
            run for run in runs_for_date(items, target_date)
            if str(run.get("status") or "").casefold() != "completed"
        ]

    active = active_today(runs)
    for poll in range(max_polls):
        if not active:
            return runs
        print(
            f"Waiting for {len(active)} same-day EPG run(s) to settle "
            f"before recovery decision ({poll + 1}/{max_polls})."
        )
        sleep_fn(poll_interval)
        runs = client.workflow_runs("epg-refresh.yml")
        active = active_today(runs)

    if active:
        print(
            f"EPG recovery deferred: {len(active)} same-day run(s) remain active "
            f"after {max_polls * poll_interval} seconds; the next watchdog checkpoint will re-check."
        )
    return runs


def watchdog(workflow_files: list[str]) -> int:
    if os.environ.get("GITHUB_EVENT_NAME", "").casefold() == "push":
        print("Push-triggered workflows own this commit; watchdog will not dispatch duplicates.")
        return 0
    repository = os.environ["GITHUB_REPOSITORY"]
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    target_date = today_in_bangladesh()
    client = GitHubActions(repository, token)

    for workflow_file in workflow_files:
        if not recovery_is_due(workflow_file):
            hour, minute = RECOVERY_AFTER_LOCAL[workflow_file]
            print(f"Recovery deferred for {workflow_file} until {hour:02d}:{minute:02d} Asia/Dhaka.")
            continue
        runs = client.workflow_runs(workflow_file)
        if workflow_file == "epg-refresh.yml":
            runs = wait_for_epg_runs_to_settle(client, target_date, runs)
        todays = runs_for_date(runs, target_date)
        blocking = [
            run for run in todays
            if watchdog_run_blocks_retry(run, client, workflow_file)
        ]
        if blocking:
            owner = min(
                blocking,
                key=lambda run: (parse_github_timestamp(run["created_at"]), int(run["id"])),
            )
            owner_id = int(owner["id"])
            newest = max(blocking, key=lambda run: parse_github_timestamp(run["created_at"]))
            print(
                f"No dispatch needed for {workflow_file}: "
                f"{len(blocking)} active/successful run(s) exist for {target_date}; "
                f"owner={owner_id}, latest={newest['id']} "
                f"event={newest.get('event')} status={newest.get('status')} "
                f"conclusion={newest.get('conclusion')}."
            )
            continue
        if todays:
            print(
                f"Retrying {workflow_file}: today's prior attempts all ended unsuccessfully "
                f"({len(todays)} run(s)); dispatching recovery run."
            )
        print(
            f"No active or successful required job exists for {workflow_file} on Bangladesh date {target_date}; "
            f"dispatching the repository's official workflow on {DEFAULT_BRANCH}."
        )
        client.dispatch(workflow_file)
        print(f"Dispatch accepted for {workflow_file}.")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        raise SystemExit(
            "Usage: discovery_schedule_guard.py guard <workflow.yml> | "
            "watchdog <workflow1.yml> <workflow2.yml> [workflow3.yml ...]"
        )
    mode = argv[0]
    if mode == "guard" and len(argv) == 2:
        return guard(argv[1])
    if mode == "watchdog" and len(argv) >= 3:
        return watchdog(argv[1:])
    raise SystemExit("Invalid arguments")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
