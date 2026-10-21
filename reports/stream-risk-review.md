# Stream Risk Review

Generated: **2026-10-21T00:08:43+00:00**
IPTV-Playlist.m3u SHA-256: **ee851e7cc4586db6af2ed6053089b2b6847adfba5ccf91fd7f69e56f36d0b819**

Generated from the current playlist and latest available stream-health report. This review is non-destructive; no stream URL was changed or deleted.

## Summary

- /streamtest/ endpoints: **11**
- Signed/token-query endpoints: **11**
- Xtream-style credential paths (credentials redacted): **0**
- Proxy/worker-host routes: **41** (3 primary, 38 Backup)
- /api/play/ relay routes: **13**

## Latest Stream-Health Snapshot

| Metric | Count |
|---|---:|
| Streams tested | 1094 |
| Reachable | 1032 |
| Failed this check | 62 |
| Persistent failures (3+ consecutive) | 38 |
| HTTP 401/403 (auth) | 12 |
| HTTP 404 (not found) | 13 |
| HTTP 5xx (server) | 2 |
| Timeout | 35 |

### Persistent failures

- **ATN Bangla** — Backup — consecutive failures: **3** — Timeout
- **Aakaash Aath** — Backup — consecutive failures: **3** — Timeout
- **CBN TV USA** — Backup — consecutive failures: **18** — HTTP 404
- **Channel 52** — Backup — consecutive failures: **25** — HTTP 404
- **Channel S** — Backup — consecutive failures: **26** — Timeout
- **Channel S** — Backup — consecutive failures: **25** — HTTP 404
- **Channel S** — Backup — consecutive failures: **25** — HTTP 404
- **Channel S** — Backup — consecutive failures: **26** — Timeout
- **Desh TV** — Backup — consecutive failures: **13** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **10** — HTTP 403
- **ESPN** — Backup — consecutive failures: **10** — HTTP 403
- **G TV** — Backup — consecutive failures: **10** — Timeout
- **G TV** — Backup — consecutive failures: **10** — Timeout
- **G TV** — Backup — consecutive failures: **10** — Timeout
- **Green TV** — Backup — consecutive failures: **26** — Timeout
- **Green TV** — Backup — consecutive failures: **25** — HTTP 404
- **Green TV** — Backup — consecutive failures: **25** — HTTP 500
- **Green TV** — Backup — consecutive failures: **25** — HTTP 404
- **Green TV** — Backup — consecutive failures: **25** — HTTP 404
- **Maasranga TV** — Backup — consecutive failures: **3** — Timeout
- **Maasranga TV** — Backup — consecutive failures: **3** — Timeout
- **RTV** — Backup — consecutive failures: **3** — Timeout
- **Shanson TV** — Backup — consecutive failures: **6** — HTTP 403
- **Somoy TV** — Backup — consecutive failures: **3** — Timeout
- **Ananda TV** — Bangladesh — consecutive failures: **3** — Timeout
- **Assam Talks** — Indian Entertainment — consecutive failures: **236** — HTTP 403
- **Star Gold** — Indian Movies — consecutive failures: **14** — HTTP 404
- **CMAC TV** — International — consecutive failures: **18** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **42** — HTTP 504
- **HBO** — International — consecutive failures: **224** — HTTP 403
- **Lifetime** — International — consecutive failures: **18** — HTTP 403
- **Teleritmo** — International — consecutive failures: **42** — HTTP 403
- **Nick** — Kids — consecutive failures: **14** — Timeout
- **Teen Nick** — Kids — consecutive failures: **102** — HTTP 403
- **PTV** — Sports — consecutive failures: **3** — Timeout
- **Star Sports 2** — Sports — consecutive failures: **18** — HTTP 403
- **T Sports** — Sports — consecutive failures: **18** — HTTP 403
- **Willow TV** — Sports — consecutive failures: **18** — HTTP 403

## /streamtest/ Endpoints

| Channel | Group | Host | Path |
|---|---|---|---|
| 8XM | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/131M/chunks.m3u8 |
| Jalwa TV | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/135M/chunks.m3u8 |
| Paighan TV | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/107M/chunks.m3u8 |
| See TV | Pakistani | vodzong.mjunoon.tv:8087 | /streamtest/SeeTV-156/playlist.m3u8 |
| Waseb TV | Pakistani | vodzong.mjunoon.tv:8087 | /streamtest/WASEB-130/playlist.m3u8 |
| MINI | Kids | vodzong.mjunoon.tv:8087 | /streamtest/disckids-157-1/playlist.m3u8 |
| 8XM | Backup | vodzong.mjunoon.tv:8087 | /streamtest/8XM-131/playlist.m3u8 |
| Animal Planet | Backup | vodzong.mjunoon.tv:8087 | /streamtest/Animal-Planet-158-3/playlist.m3u8 |
| Cartoon Network | Backup | vodzong.mjunoon.tv:8087 | /streamtest/cartoon-network-87/playlist.m3u8 |
| Hum TV | Backup | cdn4.mjunoon.tv:8087 | /streamtest/82M/chunks.m3u8 |
| Jalwa TV | Backup | vodzong.mjunoon.tv:8087 | /streamtest/JalwaTV-135/live/135M/chunks.m3u8 |

## Signed / Token-Query Endpoints

Query values are omitted because they may be expiring signatures or access tokens.

| Channel | Group | Host | Parameter names |
|---|---|---|---|
| ETV Cinema | Indian Movies | yupplivegcpusa.yuppcdn.net | hdnts |
| Star Gold | Indian Movies | 103.114.11.37:8081 | token |
| Colors Super | Indian Entertainment | d1rc86nwwc9fag.cloudfront.net | hdnts |
| Darshana TV | Indian Entertainment | yuppparoriglin.akamaized.net | hdnts |
| Zee Kannada | Indian Entertainment | yuppnimresmum.akamaized.net | hdnts |
| Songdew TV | International | yuppnimrestreammum.akamaized.net | hdnts |
| WOW Kidz Hindi | Kids | yuppparoriglin.akamaized.net | hdnts |
| WOW Kidz Tamil | Kids | yuppparoriglin.akamaized.net | hdnts |
| WOW Kidz Telugu | Kids | yuppparoriglin.akamaized.net | hdnts |
| Colors | Backup | 103.114.11.37:8081 | token |
| Studio Yuva | Backup | d2gvyg6lvauoko.cloudfront.net | hdnts |

## Xtream-Style Credential Paths

Credentials are intentionally redacted; only the host and safe route pattern are shown.

| Channel | Group | Host | Redacted path |
|---|---|---|---|
| — | — | — | — |

## Proxy / Worker-Host Routes

Worker routes are relayed endpoints, not direct broadcaster sources. The Sananda primary is the highest-priority route to replace with a verified direct source. Backup candidates are retained pending verification.

| Channel | Group | Host |
|---|---|---|
| Channel 16 | Bangladesh | iptvlive.ahmed-bd-org.workers.dev |
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
| Channel 24 | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel I | Backup | iptv-proxy.ahmed-bd-org.workers.dev |
| Channel I | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel I | Backup | iptvlive.ahmed-bd-org.workers.dev |
| DBC News | Backup | iptv-proxy.ahmed-bd-org.workers.dev |
| DBC News | Backup | iptvlive.ahmed-bd-org.workers.dev |
| DBC News | Backup | iptvlive.ahmed-bd-org.workers.dev |
| DD Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Enter10 Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Enter TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
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
| Channel S | Not Playing | iptvlive.ahmed-bd-org.workers.dev |

## Hosted /api/play/ Relay Routes

| Channel | Group | Host | Route type |
|---|---|---|---|
| BTV National | Bangladesh | homair-tv-production.up.railway.app | /api/play/ |
| Star Gold Select | Indian Movies | homair-tv-production.up.railway.app | /api/play/ |
| Star Movies | Indian Movies | homair-tv-production.up.railway.app | /api/play/ |
| Star Utsav Movies | Indian Movies | homair-tv-production.up.railway.app | /api/play/ |
| Manoranjan Grand | Indian Entertainment | homair-tv-production.up.railway.app | /api/play/ |
| Star Bharat | Indian Entertainment | homair-tv-production.up.railway.app | /api/play/ |
| Star Utsav | Indian Entertainment | homair-tv-production.up.railway.app | /api/play/ |
| BTV Chattogram | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Colors Cineplex [UK] | Backup | homair-tv-production.up.railway.app | /api/play/ |
| HBO | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Desh TV | Not Playing | homair-tv-production.up.railway.app | /api/play/ |
| Nick | Not Playing | homair-tv-production.up.railway.app | /api/play/ |
| Star Gold | Not Playing | homair-tv-production.up.railway.app | /api/play/ |

## Recommendations

- Keep fragile routes unchanged until a working, authorized replacement is confirmed.
- Test streamtest endpoints in the target IPTV player; the path name alone does not prove a route is dead.
- Do not strip or rewrite signed query parameters blindly; they may be source/session-bound.
- Move Xtream credentials out of the public playlist when authorized replacement routing exists, and rotate exposed credentials as appropriate.
- Replace primary proxy/worker routes with verified direct URLs where possible; do not silently delete Backup entries.
