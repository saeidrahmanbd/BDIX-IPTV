# BDIX-IPTV Analytics Gateway

This optional Cloudflare Worker + D1 service counts requests made through its playlist URLs. It does **not** measure channel playback or prove that one request equals one viewer.

## What it measures

- Requests to the main and international M3U gateway endpoints.
- Unique-client estimates across the selected period, deduplicated by a salted hash of the source IP + user-agent. Daily breakdowns deduplicate within each UTC day.
- Cloudflare country code, without storing the source IP or user-agent.
- 90-day retention (daily scheduled cleanup).

Obvious crawlers and monitoring bots are excluded. This is a best-effort filter, not a guarantee that all requests are human. Unique clients are estimates: shared networks, VPNs, changing IPs and user agents affect the count.

## Deploy (automated)

The repository includes [Deploy IPTV Analytics](../.github/workflows/deploy-analytics.yml). It automatically:

1. Reuses or creates the `bdix-iptv-analytics` D1 database.
2. Applies the idempotent D1 schema.
3. Populates the database binding in the deployment workspace (the placeholder in the committed TOML is intentional).
4. Deploys the Worker and verifies its dashboard, API and both playlist routes.

The workflow uses the existing GitHub Actions secrets `CLOUDFLARE_ANALYTICS_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`, also used by the Xtream deployment. The account-owned Cloudflare API token must include **D1:Edit** and **Workers product Admin** permissions for the initial creation of the Worker. This matches Cloudflare's current Wrangler authorization guidance. After the Worker is created, the Workers role may be reduced to **Editor** for subsequent deployments if no additional Worker creation is needed. Keep the existing `CLOUDFLARE_API_TOKEN` secret unchanged; it may be used by the separate Xtream deployment. It must also be allowed to use the account's Workers.dev subdomain.

The client-hash salt is generated once by the Worker and stored in D1; no extra secret needs to be entered or committed. The first request initializes it. Analytics failures are deliberately non-fatal: the playlist still serves if a database write fails.

After a successful workflow run, open `https://bdix-iptv-analytics.saeidrahman.workers.dev/` and check `/health`.

## Playlist URLs after deployment

The configured deployment hostname is `bdix-iptv-analytics.saeidrahman.workers.dev`:

- Main: `https://bdix-iptv-analytics.saeidrahman.workers.dev/main.m3u`
- International: `https://bdix-iptv-analytics.saeidrahman.workers.dev/international.m3u`
- Dashboard: `https://bdix-iptv-analytics.saeidrahman.workers.dev/`

**Important:** Requests to the existing `raw.githubusercontent.com` URLs bypass this gateway and cannot be counted by this service. To measure usage, distribute the Worker URLs in the README, player setup instructions and any external listing. Keep the raw GitHub URLs as direct fallback links.

## API

- `GET /api/stats?days=14` — totals and daily request/unique-client counts (1–90 days).
- `GET /health` — health check.

No cookies, browser fingerprinting, advertising identifiers or raw IP storage are used. The gateway logs request timestamp, playlist type, salted pseudonymous client hash and country code. The random salt is held in the private D1 database. Consider adding a short privacy notice wherever the tracked URLs are distributed.
