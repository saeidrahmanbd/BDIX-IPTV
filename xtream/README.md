# BDIX-IPTV Xtream Gateway

This directory contains a lightweight Xtream Codes-compatible API gateway for the master IPTV Playlist.m3u.

The Worker reads the GitHub playlist, exposes Xtream-style API endpoints, and redirects live playback requests to the original stream URL. It does not re-host or transcode video.

## XCIPTV

Use your deployed Worker URL as Server URL, then enter the XTREAM_USERNAME and XTREAM_PASSWORD configured as Cloudflare Worker Secrets.

Supported endpoints:
- /player_api.php?username=USER&password=PASS
- /player_api.php?username=USER&password=PASS&action=get_live_categories
- /player_api.php?username=USER&password=PASS&action=get_live_streams
- /player_api.php?username=USER&password=PASS&action=get_live_streams&category_id=ID
- /get.php?username=USER&password=PASS&type=m3u_plus&output=m3u8
- /xmltv.php?username=USER&password=PASS

## Deployment

1. Install Node.js.
2. Run: npx wrangler login
3. From this directory run: npx wrangler deploy
4. Set secrets:
   npx wrangler secret put XTREAM_USERNAME
   npx wrangler secret put XTREAM_PASSWORD
5. Deploy again if required: npx wrangler deploy

Use a URL-safe username/password: letters, numbers, dot, dash or underscore.

Cloudflare recommends Worker Secrets for sensitive values. Do not put the Xtream password in wrangler.toml or Git.

## Categories

The gateway preserves the playlist category structure, including Bangladesh, Indian Bangla, Indian Movies, Indian Music, Indian Entertainment, International, Documentary & Wildlife, Kids, Religious, Sports, Backup and New Channels.

## EPG

The current playlist does not contain a complete programme schedule, so XMLTV/EPG currently returns an empty EPG structure. Channel logos, names, categories and tvg-id values are preserved.

## Updates

The Worker reads the current GitHub playlist with a short cache. No separate playlist-sync job is required.

## Limitation

Playback uses HTTP 302 redirects to the original stream URLs instead of proxying video through the Worker. Sources that require special Referer/User-Agent headers may need a dedicated proxy later.