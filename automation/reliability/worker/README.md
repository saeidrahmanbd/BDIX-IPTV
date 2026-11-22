# BDIX-IPTV Reliability Worker

The Worker reconciles expected schedule obligations with real GitHub Actions runs and their configured critical jobs. It stores the results in the dedicated Cloudflare D1 ledger.

## Current safety setting

Keep Cloudflare `MODE=shadow`. Shadow mode creates idempotent obligations for the previous three, current, and next two Bangladesh dates; reads workflow run/job history; and records verified, running, failed, skipped, missing, or missed executions with policy-based recommendations. It does not dispatch workflows or modify playlists, stream URLs, logos, metadata, or EPG files.

## Recovery policies

- New Channel Discovery: missed business dates require manual review.
- International Discovery: same-day catch-up only when no run exists for that Bangladesh date; the existing workflow policy and daily guard still decide whether the job may execute.
- Stream Health: never backfill; missed days reset the streak.
- Logo repair and playlist maintenance: one same-day retry after a missing or failed run; workflow validations remain authoritative.
- EPG: same-day catch-up only when no run exists; the existing last-known-good validation and publication gates remain mandatory. Failed or guard-skipped EPG runs are sent to manual review.
- Historical dates that the existing workflows cannot replay safely are marked for manual review.

A successful date is verified only when the workflow run and the required job named in the registry both conclude successfully. A skipped required job is never treated as a successful execution.

## Dispatch safety

Dispatch is hard-gated by `MODE === "active"`, today's Bangladesh date, an eligible registry policy, a `RETRY_WAIT` result, and a conditional D1 transition with zero previous Worker dispatch attempts. Safe latest-state workflows may retry one missing or failed run. International Discovery and EPG may catch up only when no run exists for that date; existing policy, daily-guard, and last-known-good publication gates remain authoritative. A skipped required job is never automatically retried. Dispatch attempts are recorded before the GitHub request and linked to the resulting run when it appears. Dispatch failures move to manual review; uncertain requests are not retried blindly.

**Do not change Cloudflare MODE to active yet.** First deploy this reviewed source while remaining in shadow mode and inspect its reconciliation output. Do not enable automatic dispatch until several real shadow cycles have been checked.

## Cloudflare configuration

- D1 binding: `RELIABILITY_DB`
- Variables: `REGISTRY_JSON`, `MODE=shadow`, `WATCHDOG_TRIGGER_MODE`, `GITHUB_APP_ID`, `GITHUB_INSTALLATION_ID`
- Secrets: `GITHUB_APP_PRIVATE_KEY`, `RECONCILE_BEARER_TOKEN`, `HEALTHCHECKS_PING_URL` (the private HTTPS ping URL from the dedicated Healthchecks.io check).
- Cron: every minute

The GitHub App needs repository Actions: write and Metadata: read-only. It does not need Contents: write. The installation token is short-lived, kept only in memory, and never returned by the Worker.

## Endpoints

- `GET /healthz`: health and current mode.
- `POST /github-check`: validates App installation and Actions permission.
- `POST /watchdog-dispatch`: manual recovery. Dispatches the GitHub watchdog now (`?dry_run=1` records the decision only).
- `POST /watchdog-status`: the 20 most recent watchdog trigger records.
- `POST /reconcile`: writes obligations and evaluates run/job history. A successful reconciliation sends a Healthchecks.io success ping; a reconciliation failure sends a `/fail` ping before returning HTTP 503.
- The one-minute scheduled handler uses the same heartbeat wrapper. Heartbeats are sent only after reconciliation completes; `/healthz` and `/github-check` do not count as successful reconciliation heartbeats.
- Configure `HEALTHCHECKS_PING_URL` as a Cloudflare Worker secret. Never commit or share the private URL. If the secret is absent, reconciliation remains functional but Healthchecks receives no heartbeat.

The POST endpoints require the existing bearer token in the Authorization header. Never expose the bearer token, App private key, JWT, or installation token.

Run `npm test` in this directory. Tests cover Dhaka dates, registry recovery policy, required-job verification, dispatch gating, App JWT signing, repository scope, Actions history reads, and dispatch request shape.

## External watchdog trigger (independent of GitHub schedule events)

GitHub `schedule` events for this repository arrive hours late (3.4–9.9 h on every day from 14 to 22 Nov 2026) and sometimes not at all, and the watchdog's own checkpoints are schedule events too. The one-minute Cloudflare cron therefore also fires the GitHub **Discovery Schedule Watchdog** through `workflow_dispatch` at fixed Bangladesh-time checkpoints:

`05:25, 05:35, 05:50, 06:00, 06:15, 06:50, 07:30, 09:00, 12:00` (Asia/Dhaka). Each sits just after a recovery threshold in `scripts/discovery_schedule_guard.py`; a contract test keeps them aligned.

What the Worker does and does not do:

- It dispatches **only** `discovery-schedule-watchdog.yml`. It never dispatches the playlist, discovery, logo, health, EPG or Xtream workflows, and it is independent of `MODE` (which stays `shadow`).
- The watchdog keeps every decision: Bangladesh calendar-date checks, required-job verification (a guard-only no-op run does not count), the per-workflow limit of 2 automatic dispatches per day, the single-writer concurrency lock, and (for Xtream) deferral while a playlist writer is active. Dispatching it is idempotent, so a duplicate or retried trigger cannot create duplicate writer runs.
- Each checkpoint is claimed once in D1 (`watchdog_triggers`, unique key `YYYY-MM-DDTHH:MM`), so a cron that fires every minute, overlapping isolates, or a restart cannot dispatch it twice. A checkpoint can still fire up to 20 minutes late.
- It skips when a watchdog run is already queued or running, or one succeeded in the last 5 minutes. Transient failures (HTTP 429, 5xx, network) retry on later minutes up to 3 attempts; permission or configuration failures (401/403/404/422) are recorded and not retried.
- Caps: 12 checkpoint dispatches and 10 manual dispatches per Bangladesh day.
- The trigger and reconciliation run independently: a failure in one never stops the other. Errors are reduced to a short message; no token, key or bearer value is logged or returned.

Modes (`WATCHDOG_TRIGGER_MODE`): `off` (default if unset), `dry_run` (records decisions, never contacts GitHub; used for preview deployments) and `active` (production).

### Owner steps (no secret is ever pasted into chat or committed)

1. Confirm the existing secrets are set on the Worker: `GITHUB_APP_PRIVATE_KEY`, `RECONCILE_BEARER_TOKEN` (and optionally `HEALTHCHECKS_PING_URL`). If one is missing, run `npx wrangler secret put <NAME>` in this directory and paste the value into the prompt that appears.
2. Optional: `npx wrangler d1 migrations apply bdix-iptv-reliability --remote` (the Worker also creates the table on demand).
3. Deploy: `npx wrangler deploy`.
4. Verify without dispatching anything:
   - `GET /healthz` must show `"watchdog_trigger":"active"`.
   - `POST /github-check` with `Authorization: Bearer <RECONCILE_BEARER_TOKEN>` must report `actions_permission: "write"`.
   - `POST /watchdog-dispatch?dry_run=1` must return `"action":"dry_run"`.
5. Manual recovery any time: `POST /watchdog-dispatch` with the bearer header (or run the watchdog from the GitHub Actions tab).
6. Check results: `POST /watchdog-status`, and the watchdog runs with event `workflow_dispatch` in GitHub Actions at the checkpoint times above.
7. Roll back instantly by setting `WATCHDOG_TRIGGER_MODE = "off"` in `wrangler.toml` and redeploying.
