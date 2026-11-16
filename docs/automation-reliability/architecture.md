# BDIX-IPTV Automation Reliability Architecture

**Status:** Phase 1 foundation proposal  
**Timezone:** `Asia/Dhaka`  
**Scope:** Scheduling, execution tracking, recovery, verification and alerting. This project does not authorize playlist-policy changes.

## Goals

1. Detect a missed expected run even when GitHub Actions scheduled events are unavailable.
2. Dispatch approved workflows at most once per business-date obligation, with bounded retries.
3. Distinguish workflow completion from successful publication and independent verification.
4. Preserve the existing GitHub Actions writer locks, validation gates and playlist ownership rules.
5. Retain missed obligations across Bangladesh calendar dates and reconcile them according to workflow-specific replay policies.
6. Alert the owner by email when a scheduler, workflow, publication, verifier or recovery path is unhealthy.

No third-party scheduler can guarantee zero downtime. The design aims to make failures observable and recoverable rather than promise uninterrupted service.

### Playlist ownership boundary

The reliability layer does not authorize content changes to either `IPTV-Playlist.m3u` or `International-Playlist.m3u`. In particular, the main IPTV playlist remains owner-curated: existing stream URLs, group assignments, channel numbers, row order and primary/Backup/Review placement must not be changed by scheduler or recovery logic. Only the existing workflow-specific validation and explicitly approved discovery-queue behavior may run. The International playlist continues to follow its separately defined automation policy; this reliability project does not broaden or replace that policy.

## Current production workflow registry

The machine-readable source of expected schedules and stable identifiers is `automation/reliability/workflow_registry.json`.

All six current production schedules were verified against their workflow files on 2026-11-16:

| Stable ID | Workflow | Bangladesh time | UTC cron | Required job |
|---|---|---:|---|---|
| `iptv_new_channel_discovery` | IPTV New Channel Discovery | 05:00 | `0 23 * * *` | `discover` |
| `international_channel_discovery` | International Channel Discovery | 05:10 | `10 23 * * *` | `discover` |
| `playlist_logo_localization` | Playlist Logo Repair and Localization | 05:25 | `25 23 * * *` | `localize` |
| `international_stream_health` | International Stream Health | 05:35 | `35 23 * * *` | `check` |
| `iptv_playlist_maintenance` | IPTV Playlist Update | 05:50 | `50 23 * * *` | `maintain` |
| `epg_refresh` | Refresh IPTV EPG | 06:10 | `10 0 * * *` | `refresh` |

The job identifiers above are GitHub Actions job IDs, not display names. Future completion contracts must use stable machine-readable fields and must not depend on mutable step display names.

## Target architecture

- **Primary scheduler:** one Cloudflare Worker Cron Trigger, invoked every minute. It reads the registry, computes due obligations in `Asia/Dhaka`, reserves them in D1, and dispatches eligible GitHub workflows.
- **Authoritative ledger:** one Cloudflare D1 database. D1 is the source of truth for expected executions, attempts, event history and verification state. The Git branch-backed Automation V2 state store remains a legacy/project-specific state store until a separately reviewed migration; it must not be dual-written as a second live scheduling ledger.
- **Secondary trigger:** cron-job.org calls a protected reconciliation endpoint every 15 minutes. It does not create a second schedule or independently dispatch arbitrary jobs; it asks the Worker to reconcile overdue obligations through the same idempotent ledger.
- **Independent heartbeat:** Healthchecks.io receives a heartbeat only after the Worker successfully completes a reconciliation cycle. Missing heartbeats trigger email notifications. cron-job.org can also notify by email when its HTTP call fails.
- **Dispatch identity:** a dedicated GitHub App installation token with repository Actions: write permission for workflow dispatch. The token is minted on demand and kept only in Worker memory. The App private key is a Cloudflare secret, never a cron-job.org header or repository file.
- **Production execution:** existing GitHub Actions workflows continue to own all playlist, logo and EPG writes. External orchestration may dispatch them but may not bypass their daily guards, the shared `iptv-playlist-main-writer-v5` concurrency group, or their validators.
- **Completion verification:** each workflow will eventually emit a versioned JSON completion artifact. A separate verifier will inspect the actual run jobs, artifact and published repository commit/files before marking the obligation `VERIFIED`.

### Important independence boundary

Cloudflare Cron is independent of GitHub Actions scheduling. cron-job.org is independent of both GitHub's scheduler and Cloudflare Cron delivery, but its reconciliation endpoint still runs on Cloudflare. If Cloudflare itself is unavailable, cron-job.org can detect the endpoint failure and email the owner, but cannot execute Cloudflare-hosted recovery logic. A separately hosted emergency dispatcher is a later optional resilience tier and should be added only if the owner wants protection against Cloudflare-wide outages.

## Ledger and idempotency

The initial D1 schema is `automation/reliability/schema.sql`.

- One row in `reliability_executions` represents one workflow obligation for one Bangladesh calendar date.
- `UNIQUE(workflow_id, business_date)` prevents duplicate obligations.
- `reliability_attempts` records every dispatch attempt without replacing prior evidence.
- `reliability_events` is append-only operational history.
- All persisted timestamps are UTC ISO-8601 values. Business dates and schedule calculations are explicitly Bangladesh-local.
- The execution key is deterministic from the stable workflow ID and Bangladesh business date; it is not derived from a mutable Git commit or workflow display name.
- D1 transactions and conditional state updates must reserve an obligation before dispatch. A failed or ambiguous dispatch is reconciled against GitHub before retrying; never blindly issue duplicate dispatches.
- If D1 is unavailable, the scheduler fails closed: no dispatch, no ledger reset, no assumption of success. It reports the outage through the external monitor.

## Recovery policy

1. Create expected obligations for all due workflow/date pairs.
2. Dispatch only when the obligation is due, not already verified, not currently running, and retry policy permits.
3. After dispatch acceptance, poll GitHub for the corresponding run and associate its run ID with the attempt.
4. If the API response is ambiguous, reconcile the recent run list before attempting another dispatch.
5. Treat queued/in-progress runs as active. Treat skipped required jobs as incomplete.
6. On completion, require the stable required job result and versioned completion artifact.
7. Require independent publication verification before state becomes `VERIFIED`.
8. Use bounded retries with exponential backoff and jitter. Exhausted attempts become `MANUAL_REVIEW` and trigger email.
9. Never silently discard old expected obligations at midnight. Retain them and apply the workflow's declared replay policy.

### Workflow-specific replay safety

- Main IPTV discovery: do not replay an old date automatically; reconcile current inputs and require the existing manual-queue and owner-protection checks.
- International discovery and maintenance: replay only as a current-state reconciliation, never as an instruction to restore an old playlist snapshot.
- Logo localization: safe latest-state reconciliation after verifying authentic local assets.
- International stream health: never fabricate or backfill a missed day's probe result. A missed day resets the existing consecutive-definitive-failure streak in accordance with the current Bangladesh-calendar-day policy.
- EPG: regenerate from current inputs and publish only if the existing last-known-good quality gate passes.

## Completion contract

Target artifact name: `bdix-automation-completion-v1.json`.

Required fields:

- `schema_version`
- `workflow_id`
- `business_date`
- `github_run_id`
- `github_run_attempt`
- `source_sha`
- `required_job_id`
- `required_job_conclusion`
- `publication_sha` (nullable for a no-change verified run)
- `publication_targets`
- `validation_results`
- `completed_at_utc`

The contract must be generated from the actual workflow execution context. The verifier must reject mismatched run IDs, dates, workflow IDs, missing required validations, invalid publication SHAs or outputs that fail policy-specific checks. Step display names are not identifiers.

## State transitions

`EXPECTED -> DISPATCHING -> DISPATCHED -> RUNNING -> PUBLISHED -> VERIFYING -> VERIFIED`

Recoverable paths:

- `DISPATCHING -> RETRY_WAIT` when dispatch definitively fails.
- `DISPATCHED -> RETRY_WAIT` only after a bounded start timeout and GitHub reconciliation.
- `RUNNING -> RETRY_WAIT` after a definitive workflow failure or timeout, once the run is terminal.
- `PUBLISHED -> VERIFYING -> MANUAL_REVIEW` if the output is missing, stale or invalid.
- `RETRY_WAIT -> DISPATCHING` when retry is safe and the retry budget remains.
- `RETRY_WAIT -> MANUAL_REVIEW` when attempts are exhausted or the failure is unsafe to retry.
- `VERIFIED` is terminal for that business-date obligation. A later correction is a new explicit reconciliation event, not mutation of historical evidence.

## Security

- Create a dedicated GitHub App installed only on `saeidrahmanbd/BDIX-IPTV`.
- Grant only repository Actions: write for workflow dispatch and Metadata: read if required by the selected API calls. Do not grant Contents: write or Workflows: write to the external scheduler.
- Confirm the exact GitHub App permission matrix with a test installation before production. GitHub's workflow-dispatch endpoint documents Actions: write for installation tokens.
- Store the App private key and endpoint authentication secret as Cloudflare Worker secrets.
- cron-job.org receives only a high-entropy rotating endpoint secret; it never receives a GitHub token or App private key.
- Validate method, content type, timestamp, request nonce and HMAC or bearer secret; reject replayed nonces and stale requests.
- Never log tokens, private keys, authorization headers, stream URLs or secrets.
- Use HTTPS, bounded request bodies, rate limiting and an allowlist of registry workflow IDs.

## Email alerting

The owner selected email. Configure Healthchecks.io email notifications for missing scheduler heartbeats and cron-job.org email notifications for failed HTTP calls. The Worker's own failure alert should use a separate email delivery provider or a provider-supported email integration; do not assume Healthchecks heartbeat alone can report an exception if the Worker cannot reach Healthchecks. Email addresses and API keys must be entered by the owner in provider dashboards and stored as secrets, not committed.

## Failure-injection acceptance tests

Before production enablement, demonstrate:

1. GitHub Actions cron unavailable for 24 hours: external scheduler detects all six due obligations and dispatches safe work.
2. Cloudflare Cron disabled: cron-job.org reconciliation still reaches the Worker and can recover overdue work.
3. Cloudflare endpoint unavailable: cron-job.org emails an alert; no false success is recorded.
4. D1 unavailable or daily limit exceeded: dispatch fails closed and external monitor alerts.
5. Dispatch API returns an ambiguous network error: reconcile run history before retry.
6. Duplicate secondary and primary trigger: one obligation and one active attempt only.
7. Required job skipped while wrapper succeeds: execution remains incomplete.
8. Workflow times out or runner disappears: bounded recovery after confirming no active run.
9. Publication succeeds but verification fails: never mark `VERIFIED`.
10. EPG is empty, stale or degraded: last-known-good guide remains untouched.
11. Main playlist owner-protection check fails: no automated publication.
12. International health misses a Bangladesh day: no invented failure sample; streak reset rule remains intact.
13. UTC midnight boundary: each execution is assigned to the correct `Asia/Dhaka` business date.
14. A previous date remains overdue: it remains visible and is reconciled according to its replay policy.

## Phased rollout

1. **Foundation (this PR):** registry, schema, documentation and static validation only.
2. **Cloudflare application:** Worker skeleton, D1 migrations, local tests and development environment. No production dispatch.
3. **GitHub App:** create the App, install on the repository and validate minimal permissions.
4. **Secondary monitor:** configure cron-job.org and Healthchecks.io email alerts.
5. **Completion contracts:** add versioned artifacts to workflows, preserving their existing writers and validation gates.
6. **Shadow mode:** observe schedule decisions and compare them with GitHub runs without dispatching.
7. **Controlled dispatch:** enable one workflow at a time, retaining existing GitHub cron and watchdog.
8. **Resilience tests:** perform outage simulations and verify email alerts.
9. **Retirement:** only after sustained evidence, separately propose removal or reduction of redundant GitHub-only watchdog logic.

## Rollback

- Disable external dispatch at the Worker configuration level.
- Preserve the D1 ledger and all event history.
- Keep all existing GitHub schedules and watchdog triggers active throughout rollout.
- Revoke the GitHub App installation or rotate its key if credentials are suspected compromised.
- Do not delete D1 data as part of rollback.
- Never revert playlist commits or EPG publications as an automatic scheduler rollback.

## Owner actions required later

- Confirm Cloudflare account zone/account access and create a dedicated Worker and D1 database.
- Create and install the dedicated GitHub App.
- Configure cron-job.org with the protected reconciliation URL.
- Configure Healthchecks.io and email notification destination.
- Decide whether an additional separately hosted emergency dispatcher is worth its cost and maintenance.

No external account configuration or production dispatch is performed by this foundation change.
