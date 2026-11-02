# BDIX-IPTV Analytics Gateway

This optional Cloudflare Worker + D1 service counts requests made through its playlist URLs. It does **not** measure channel playback or prove that one request equals one viewer.

## What it measures

- Requests to the main and international M3U gateway endpoints.
- Daily unique client estimates, deduplicated by a salted hash of the source IP + user-agent for that UTC day.
- Cloudflare country code, without storing the source IP or user-agent.
- 90-day retention (daily scheduled cleanup).

Obvious crawlers and monitoring bots are excluded. This is a best-effort filter, not a guarantee that all requests are human. Unique clients are estimates: shared networks, VPNs, changing IPs and user agents affect the count.

## Deploy (one-time setup)

Requires a Cloudflare account with Workers and D1 enabled, Node.js/npm, and Wrangler.

1. Create a D1 database:
   `npx wrangler d1 create bdix-iptv-analytics`
2. Copy the returned database ID into `wrangler.toml`.
3. Create the table:
   `npx wrangler d1 execute bdix-iptv-analytics --file=schema.sql`
4. Set a long random privacy salt (keep it secret; never commit it):
   `npx wrangler secret put ANALYTICS_SALT`
5. Deploy:
   `npx wrangler deploy`
6. Open the deployed `https://<worker-name>.<account-subdomain>.workers.dev/` dashboard. Check `/health`.

## Playlist URLs after deployment

Replace `<WORKER_HOST>` with the exact workers.dev hostname printed by Wrangler:

- Main: `https://<WORKER_HOST>/main.m3u`
- International: `https://<WORKER_HOST>/international.m3u`
- Dashboard: `https://<WORKER_HOST>/`

**Important:** Requests to the existing `raw.githubusercontent.com` URLs bypass this gateway and cannot be counted by this service. To measure usage, distribute the Worker URLs in the README, player setup instructions and any external listing. Keep the raw GitHub URLs as direct fallback links.

## API

- `GET /api/stats?days=14` — totals and daily request/unique-client counts (1–90 days).
- `GET /health` — health check.

No cookies, browser fingerprinting, advertising identifiers or raw IP storage are used. The gateway logs request timestamp, playlist type, salted daily client hash and country code. Consider adding a short privacy notice wherever the tracked URLs are distributed.
