# BDIX-IPTV Reliability Worker

The Worker reconciles expected schedule obligations with real GitHub Actions runs and their configured critical jobs. It stores the results in the dedicated Cloudflare D1 ledger.

## Current safety setting

Keep Cloudflare \`MODE=shadow\`. Shadow mode creates idempotent obligations for the previous three, current, and next two Bangladesh dates; reads workflow run/job history; and records verified, running, failed, skipped, missing, or missed executions with policy-based recommendations. It does not dispatch workflows or modify playlists, stream URLs, logos, metadata, or EPG files.

## Recovery policies

- New Channel Discovery: missed business dates require manual review.
- International Discovery: same-day catch-up only, subject to the workflow's own policy filters.
- Stream Health: never backfill; missed days reset the streak.
- Logo repair and playlist maintenance: same-day latest-state reconciliation only.
- EPG: same-day catch-up only; its existing last-known-good validation and publication gates remain mandatory.
- Historical dates that the existing workflows cannot replay safely are marked for manual review.

A successful date is verified only when the workflow run and the required job named in the registry both conclude successfully. A skipped required job is never treated as a successful execution.

## Dispatch safety

Dispatch is hard-gated by \`MODE === "active"\`, today's Bangladesh date, an eligible registry policy, no observed run for that date, and a conditional D1 transition with zero previous dispatch attempts. The attempt is recorded before the GitHub dispatch request. Failures move to manual review; uncertain dispatches are not blindly retried.

**Do not change Cloudflare MODE to active yet.** First deploy this reviewed source while remaining in shadow mode and inspect its reconciliation output. Do not enable automatic dispatch until several real shadow cycles have been checked.

## Cloudflare configuration

- D1 binding: \`RELIABILITY_DB\`
- Variables: \`REGISTRY_JSON\`, \`MODE=shadow\`, \`GITHUB_APP_ID\`, \`GITHUB_INSTALLATION_ID\`
- Secrets: \`GITHUB_APP_PRIVATE_KEY\`, \`RECONCILE_BEARER_TOKEN\`
- Cron: every minute

The GitHub App needs repository Actions: write and Metadata: read-only. It does not need Contents: write. The installation token is short-lived, kept only in memory, and never returned by the Worker.

## Endpoints

- \`GET /healthz\`: health and current mode.
- \`POST /github-check\`: validates App installation and Actions permission.
- \`POST /reconcile\`: writes obligations and evaluates run/job history.

The POST endpoints require the existing bearer token in the Authorization header. Never expose the bearer token, App private key, JWT, or installation token.

Run \`npm test\` in this directory. Tests cover Dhaka dates, registry recovery policy, required-job verification, dispatch gating, App JWT signing, repository scope, Actions history reads, and dispatch request shape.
