# Xtream Gateway

BDIX-IPTV provides optional Xtream-compatible access to the curated playlists through two Cloudflare Worker deployments.

## Workers

| Worker | Playlist | Configuration |
|---|---|---|
| `xtream-main` | `IPTV-Playlist.m3u` | [`xtream-main/wrangler.toml`](../xtream-main/wrangler.toml) |
| `xtream-bdix` | `BDIX-Playlist.m3u` | [`xtream-bdix/wrangler.toml`](../xtream-bdix/wrangler.toml) |

The workers read the public raw playlist URLs configured in their respective `wrangler.toml` files and expose Xtream-style endpoints for compatible IPTV clients.

## Security

- Xtream credentials are supplied through deployment secrets; do not commit usernames or passwords.
- Do not place real credentials in this repository or in example configuration files.
- The workers do not make stream URLs public beyond the playlist data they are configured to serve.
- Review the repository's stream-risk and audit reports before enabling a deployment.

## Deployment

The repository's GitHub Actions workflows handle deployment/checking of the Xtream workers. The worker source lives in [`xtream-main/`](../xtream-main/) and [`xtream-bdix/`](../xtream-bdix/).

For a safe local configuration example, see [`assets/examples/sample-config.md`](../assets/examples/sample-config.md).

## Client use

After deployment, use the worker's documented Xtream base URL with a compatible IPTV client such as XCIPTV. Keep the deployment URL and credentials private when they are intended for personal use.

## Maintenance

The Xtream workers are downstream consumers of the curated playlists. Playlist discovery, metadata normalization, local-logo enforcement, EPG generation, stream health checks, and publish gates are maintained by the main repository workflows.
