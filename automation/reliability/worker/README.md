# Reliability Worker — Shadow Mode

This Worker creates expected-run obligations in a dedicated Cloudflare D1 database.
It does **not** dispatch GitHub Actions, modify repository files, or publish playlists.

## Required bindings and secrets

- D1 binding: `RELIABILITY_DB`
- Worker variable: `REGISTRY_JSON` (paste the contents of `automation/reliability/workflow_registry.json`)
- Secret: `RECONCILE_BEARER_TOKEN` (high-entropy value)
- Optional secret/variable: `HEALTHCHECKS_PING_URL` (Healthchecks ping URL)

## Setup (not yet performed)

1. Create a dedicated D1 database in Cloudflare.
2. Replace the placeholder `database_id` in `wrangler.toml` with that database ID.
3. Apply `migrations/0001_reliability_ledger.sql` to that database.
4. Set `REGISTRY_JSON` and `RECONCILE_BEARER_TOKEN` in Worker settings.
5. Set `HEALTHCHECKS_PING_URL` only after configuring the Healthchecks check.
6. Deploy as a separate Worker and verify `GET /healthz`.
7. Test `POST /reconcile` with the bearer token and inspect D1 rows.

The one-minute Cron Trigger and protected HTTP endpoint call the same idempotent reconciler.
The reconciler creates obligations for today through two calendar days ahead in Asia/Dhaka.
A unique workflow/date key prevents duplicate expected rows.

## Safety boundary

Mode is hard-coded as `shadow` in this phase. `dispatched` is always zero.
No GitHub App, dispatch permission, production workflow modification, or production playlist access is required.
