# Xtream Gateway

BDIX-IPTV provides optional Xtream-compatible access to the curated playlists through two Cloudflare Worker deployments.

## Workers

| Worker | Playlist | Configuration |
|---|---|---|
| `xtream-main` | `IPTV-Playlist.m3u` | [`xtream-main/wrangler.toml`](../xtream-main/wrangler.toml) |
| `xtream-bdix` | `BDIX-Playlist.m3u` | [`xtream-bdix/wrangler.toml`](../xtream-bdix/wrangler.toml) |

The workers read the public raw playlist URLs configured in their respective `wrangler.toml` files and expose Xtream-style endpoints for compatible IPTV clients.

## Source tree

- [`xtream-main/`](../xtream-main/) — main IPTV worker source and configuration
- [`xtream-bdix/`](../xtream-bdix/) — BDIX worker source and configuration
- [`xtream/`](./) — this documentation and gateway policy

## Optional relay example

The `assets/relay/` directory contains an optional Docker Compose / Nginx relay example. It is separate from the hosted Cloudflare Workers and is not used by the standard Xtream deployment. Review `assets/relay/docker-compose.yml`, `assets/relay/nginx.conf`, and `assets/relay/config/` before use. Keep real upstream credentials in deployment secrets or local environment files; never commit them or expose private upstreams publicly.

## Security

- Xtream credentials are supplied through deployment secrets; do not commit usernames or passwords.
- Do not place real credentials in this repository or in example configuration files.
- The workers are downstream consumers of the published playlist data.
- Review the repository's [stream-risk review](../reports/stream-risk-review.md), [stream-health report](../reports/stream-health.md), and [pre-publish gate](../reports/pre-publish-gate.md) before enabling a deployment. These are generated snapshots: verify the report timestamp and source playlist fingerprint; a historical `PASS` does not certify the current playlist.

## Deployment

The repository's GitHub Actions workflows handle deployment/checking of the Xtream workers. The worker source lives in [`xtream-main/`](../xtream-main/) and [`xtream-bdix/`](../xtream-bdix/).

For a safe local configuration example, see [`assets/examples/sample-config.md`](../assets/examples/sample-config.md).

## Client use

After deployment, use the worker's documented Xtream base URL with a compatible IPTV client such as XCIPTV. Keep the deployment URL and credentials private when they are intended for personal use.

## Maintenance

The Xtream workers are downstream consumers of the curated playlists. Playlist discovery, metadata normalization, local-logo enforcement, EPG generation, stream health checks, backup-independence review, and publish gates are maintained by the main repository workflows.
