# Reliability Worker — Shadow Mode

This Worker creates expected-run obligations in a dedicated Cloudflare D1 database.
It does **not** dispatch GitHub Actions, modify repository files, or publish playlists.

## Required bindings and secrets

- D1 binding: `RELIABILITY_DB`
- Worker variable: `REGISTRY_JSON` (contents of `automation/reliability/workflow_registry.json`)
- Worker variable: `GITHUB_APP_ID`
- Worker variable: `GITHUB_INSTALLATION_ID`
- Secret: `GITHUB_APP_PRIVATE_KEY` (GitHub App PEM private key)
- Secret: `RECONCILE_BEARER_TOKEN` (high-entropy value)
- Optional secret/variable: `HEALTHCHECKS_PING_URL` (Healthchecks ping URL)

The App must be installed only on `saeidrahmanbd/BDIX-IPTV`, with repository
Actions: read and write permission and Metadata: read-only. The Worker never
stores an installation token; it mints one on demand and keeps it in memory.

## Safe GitHub App authentication check

After deploying the reviewed Worker code, call:

`POST /github-check`

with the existing reconciliation bearer token in the Authorization header.
This endpoint:
1. Signs a short-lived RS256 GitHub App JWT from the Cloudflare private-key secret.
2. Requests a short-lived installation access token.
3. Uses that token to read only `saeidrahmanbd/BDIX-IPTV`.
4. Confirms the token reports Actions: write permission.
5. Returns only non-secret identity and permission metadata.

It does not dispatch a workflow, change repository contents, or return the token.
Never paste the bearer token, PEM key, JWT or installation token into chat.

## Setup / deployment

1. Keep the dedicated D1 binding and migration unchanged.
2. Set `GITHUB_APP_ID` and `GITHUB_INSTALLATION_ID` as variables.
3. Set `GITHUB_APP_PRIVATE_KEY` and `RECONCILE_BEARER_TOKEN` as secrets.
4. Keep `MODE = "shadow"`; do not enable dispatch.
5. Deploy the Worker and verify `GET /healthz`.
6. Run the protected `POST /github-check` endpoint and inspect the safe response.
7. Continue observing shadow reconciliation before any separately reviewed dispatch phase.

The one-minute Cron Trigger and protected HTTP reconciliation endpoint use the same
idempotent reconciler. The reconciler creates obligations for today through two
calendar days ahead in Asia/Dhaka. A unique workflow/date key prevents duplicate
expected rows.

## Safety boundary

Mode is hard-coded as `shadow` in the response and `dispatched` remains zero.
The GitHub App authentication endpoint is read-only after token minting. No
`workflow_dispatch` endpoint is called. The Worker has no Contents: write permission
and cannot publish or edit playlists.
