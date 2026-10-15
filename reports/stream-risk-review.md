# Stream Risk Review

Generated from the current playlist and latest available stream-health report. This review is non-destructive; no stream URL was changed or deleted.

## Summary

- /streamtest/ endpoints: **9**
- Signed/token-query endpoints: **9**
- Xtream-style credential paths (credentials redacted): **8**
- Proxy/worker-host routes: **41** (1 primary, 40 Backup)
- /api/play/ relay routes: **20**

## Latest Stream-Health Snapshot

| Metric | Count |
|---|---:|
| Streams tested | 1043 |
| Reachable | 1022 |
| Failed this check | 21 |
| Persistent failures (3+ consecutive) | 13 |
| HTTP 401/403 (auth) | 6 |
| HTTP 404 (not found) | 7 |
| HTTP 5xx (server) | 6 |
| Timeout | 2 |

### Persistent failures

- **Channel 16** — Backup — consecutive failures: **6** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **6** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **6** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **70** — HTTP 403
- **Kalaignar Murasu** — Backup — consecutive failures: **4** — HTTP 404
- **Manoranjan TV** — Backup — consecutive failures: **6** — HTTP 404
- **Shanson TV** — Backup — consecutive failures: **10** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **204** — HTTP 403
- **Kalaignar Murasu** — Indian Entertainment — consecutive failures: **6** — HTTP 504
- **Cook & Bake** — International — consecutive failures: **10** — HTTP 504
- **HBO** — International — consecutive failures: **192** — HTTP 403
- **Teleritmo** — International — consecutive failures: **10** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **70** — HTTP 403

## /streamtest/ Endpoints

| Channel | Group | Host | Path |
|---|---|---|---|
| 8XM | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/131M/chunks.m3u8 |
| Jalwa TV | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/135M/chunks.m3u8 |
| Paighan TV | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/107M/chunks.m3u8 |
| See TV | Pakistani | vodzong.mjunoon.tv:8087 | /streamtest/SeeTV-156/playlist.m3u8 |
| Waseb TV | Pakistani | vodzong.mjunoon.tv:8087 | /streamtest/WASEB-130/playlist.m3u8 |
| 8XM | Backup | vodzong.mjunoon.tv:8087 | /streamtest/8XM-131/playlist.m3u8 |
| Animal Planet | Backup | vodzong.mjunoon.tv:8087 | /streamtest/Animal-Planet-158-3/playlist.m3u8 |
| Hum TV | Backup | cdn4.mjunoon.tv:8087 | /streamtest/82M/chunks.m3u8 |
| Jalwa TV | Backup | vodzong.mjunoon.tv:8087 | /streamtest/JalwaTV-135/live/135M/chunks.m3u8 |

## Signed / Token-Query Endpoints

Query values are omitted because they may be expiring signatures or access tokens.

| Channel | Group | Host | Parameter names |
|---|---|---|---|
| ETV Cinema | Indian Movies | yupplivegcpusa.yuppcdn.net | hdnts |
| Colors Super | Indian Entertainment | d1rc86nwwc9fag.cloudfront.net | hdnts |
| Zee Kannada | Indian Entertainment | yuppnimresmum.akamaized.net | hdnts |
| Songdew TV | International | yuppnimrestreammum.akamaized.net | hdnts |
| WOW Kidz Hindi | Kids | yuppparoriglin.akamaized.net | hdnts |
| WOW Kidz Tamil | Kids | yuppparoriglin.akamaized.net | hdnts |
| WOW Kidz Telugu | Kids | yuppparoriglin.akamaized.net | hdnts |
| Darshana TV | Backup | yuppparoriglin.akamaized.net | hdnts |
| Studio Yuva | Backup | d2gvyg6lvauoko.cloudfront.net | hdnts |

## Xtream-Style Credential Paths

Credentials are intentionally redacted; only the host and safe route pattern are shown.

| Channel | Group | Host | Redacted path |
|---|---|---|---|
| Sony Max 2 [US] | Indian Movies | fortv.cc:8080 | /live/[REDACTED]/[REDACTED]/125795.ts |
| Star Gold Thrills | Indian Movies | rgkkw.live:8080 | /live/[REDACTED]/[REDACTED]/773735.ts |
| Sonic Bangla | Kids | bosstv.click:8080 | /live/[REDACTED]/[REDACTED]/92412.ts |
| Astro Cricbuzz | Sports | rgkkw.live:8080 | /live/[REDACTED]/[REDACTED]/2494.ts |
| FOX Cricket 501 | Sports | rgkkw.live:8080 | /live/[REDACTED]/[REDACTED]/4748.ts |
| Sony Sports Ten 3 | Sports | rgkkw.live:8080 | /live/[REDACTED]/[REDACTED]/98863.ts |
| Ten Sports | Sports | rgkkw.live:8080 | /live/[REDACTED]/[REDACTED]/98.ts |
| Duronto TV | Backup | rgkkw.live:8080 | /live/[REDACTED]/[REDACTED]/433.ts |

## Proxy / Worker-Host Routes

Worker routes are relayed endpoints, not direct broadcaster sources. The Sananda primary is the highest-priority route to replace with a verified direct source. Backup candidates are retained pending verification.

| Channel | Group | Host |
|---|---|---|
| Sananda | Indian Bangla | iptvlive.ahmed-bd-org.workers.dev |
| ATN Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| ATN News | Backup | iptv-proxy.ahmed-bd-org.workers.dev |
| ATN News | Backup | iptvlive.ahmed-bd-org.workers.dev |
| ATN News | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Bangla TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Bangla Vision | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Bhojpuri Cinema | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Boishakhi TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Boishakhi TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel 16 | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel 24 | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel I | Backup | iptv-proxy.ahmed-bd-org.workers.dev |
| Channel I | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel I | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel S | Backup | iptvlive.ahmed-bd-org.workers.dev |
| DBC News | Backup | iptv-proxy.ahmed-bd-org.workers.dev |
| DBC News | Backup | iptvlive.ahmed-bd-org.workers.dev |
| DBC News | Backup | iptvlive.ahmed-bd-org.workers.dev |
| DD Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Enter TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Enterr10 Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Epic Music | Backup | iptvlive.ahmed-bd-org.workers.dev |
| G TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Jago News 24 | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Jamuna TV | Backup | iptv-proxy.ahmed-bd-org.workers.dev |
| Jamuna TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| ME TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| ME TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| ME TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Movie Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| News 24 | Backup | iptvlive.ahmed-bd-org.workers.dev |
| News 24 | Backup | iptvlive.ahmed-bd-org.workers.dev |
| NTV | Backup | iptv-proxy.ahmed-bd-org.workers.dev |
| NTV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| PTC Music | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Rongeen TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| SA TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| SA TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Somoy TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Zee Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |

## Hosted /api/play/ Relay Routes

| Channel | Group | Host | Route type |
|---|---|---|---|
| BTV World | Bangladesh | homair-tv-production.up.railway.app | /api/play/ |
| Star Gold Select | Indian Movies | homair-tv-production.up.railway.app | /api/play/ |
| Star Utsav Movies | Indian Movies | homair-tv-production.up.railway.app | /api/play/ |
| Star Utsav | Indian Entertainment | homair-tv-production.up.railway.app | /api/play/ |
| B4U Movies | Backup | homair-tv-production.up.railway.app | /api/play/ |
| B4U Movies | Backup | homair-tv-production.up.railway.app | /api/play/ |
| BTV Chattogram | Backup | homair-tv-production.up.railway.app | /api/play/ |
| BTV National | Backup | homair-tv-production.up.railway.app | /api/play/ |
| BTV News | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Colors Cineplex | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Desh TV | Backup | homair-tv-production.up.railway.app | /api/play/ |
| HBO | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Hum Masala | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Nick | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Nick Jr | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Sonic | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Star Bharat | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Star Gold | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Star Movies | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Super Hungama | Backup | homair-tv-production.up.railway.app | /api/play/ |

## Recommendations

- Keep fragile routes unchanged until a working, authorized replacement is confirmed.
- Test streamtest endpoints in the target IPTV player; the path name alone does not prove a route is dead.
- Do not strip or rewrite signed query parameters blindly; they may be source/session-bound.
- Move Xtream credentials out of the public playlist when authorized replacement routing exists, and rotate exposed credentials as appropriate.
- Replace primary proxy/worker routes with verified direct URLs where possible; do not silently delete Backup entries.
