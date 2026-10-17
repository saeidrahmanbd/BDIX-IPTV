# Stream Risk Review

Generated from the current playlist and latest available stream-health report. This review is non-destructive; no stream URL was changed or deleted.

## Summary

- /streamtest/ endpoints: **11**
- Signed/token-query endpoints: **11**
- Xtream-style credential paths (credentials redacted): **0**
- Proxy/worker-host routes: **41** (2 primary, 39 Backup)
- /api/play/ relay routes: **15**

## Latest Stream-Health Snapshot

| Metric | Count |
|---|---:|
| Streams tested | 1094 |
| Reachable | 1053 |
| Failed this check | 41 |
| Persistent failures (3+ consecutive) | 31 |
| HTTP 401/403 (auth) | 12 |
| HTTP 404 (not found) | 14 |
| HTTP 5xx (server) | 5 |
| Timeout | 9 |

### Persistent failures

- **CBN TV USA** — Backup — consecutive failures: **16** — HTTP 404
- **Channel 52** — Backup — consecutive failures: **23** — HTTP 404
- **Channel S** — Backup — consecutive failures: **24** — HTTP 404
- **Channel S** — Backup — consecutive failures: **23** — HTTP 404
- **Channel S** — Backup — consecutive failures: **23** — HTTP 404
- **Channel S** — Backup — consecutive failures: **24** — HTTP 404
- **Desh TV** — Backup — consecutive failures: **11** — Timeout
- **Disney Channel India** — Backup — consecutive failures: **8** — HTTP 403
- **ESPN** — Backup — consecutive failures: **8** — HTTP 403
- **G TV** — Backup — consecutive failures: **8** — HTTP 500
- **G TV** — Backup — consecutive failures: **8** — HTTP 404
- **G TV** — Backup — consecutive failures: **8** — TLS
- **G TV** — Backup — consecutive failures: **8** — HTTP 500
- **Green TV** — Backup — consecutive failures: **24** — HTTP 404
- **Green TV** — Backup — consecutive failures: **23** — HTTP 404
- **Green TV** — Backup — consecutive failures: **23** — HTTP 404
- **Green TV** — Backup — consecutive failures: **23** — HTTP 404
- **Green TV** — Backup — consecutive failures: **23** — HTTP 404
- **Shanson TV** — Backup — consecutive failures: **4** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **234** — HTTP 403
- **Star Gold** — Indian Movies — consecutive failures: **12** — HTTP 404
- **CMAC TV** — International — consecutive failures: **16** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **40** — HTTP 504
- **HBO** — International — consecutive failures: **222** — HTTP 403
- **Lifetime** — International — consecutive failures: **16** — HTTP 403
- **Teleritmo** — International — consecutive failures: **40** — HTTP 403
- **Nick** — Kids — consecutive failures: **12** — Timeout
- **Teen Nick** — Kids — consecutive failures: **100** — HTTP 403
- **Star Sports 2** — Sports — consecutive failures: **16** — HTTP 403
- **T Sports** — Sports — consecutive failures: **16** — HTTP 403
- **Willow TV** — Sports — consecutive failures: **16** — HTTP 403

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
| Colors Super | Indian Entertainment | d1rc86nwwc9fag.cloudfront.net | hdnts |
| Darshana TV | Indian Entertainment | yuppparoriglin.akamaized.net | hdnts |
| Zee Kannada | Indian Entertainment | yuppnimresmum.akamaized.net | hdnts |
| Songdew TV | International | yuppnimrestreammum.akamaized.net | hdnts |
| WOW Kidz Hindi | Kids | yuppparoriglin.akamaized.net | hdnts |
| WOW Kidz Tamil | Kids | yuppparoriglin.akamaized.net | hdnts |
| WOW Kidz Telugu | Kids | yuppparoriglin.akamaized.net | hdnts |
| Colors | Backup | 103.114.11.37:8081 | token |
| Star Gold | Backup | 103.114.11.37:8081 | token |
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
| Channel S | Backup | iptvlive.ahmed-bd-org.workers.dev |
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

## Hosted /api/play/ Relay Routes

| Channel | Group | Host | Route type |
|---|---|---|---|
| BTV National | Bangladesh | homair-tv-production.up.railway.app | /api/play/ |
| Star Gold | Indian Movies | homair-tv-production.up.railway.app | /api/play/ |
| Star Gold Select | Indian Movies | homair-tv-production.up.railway.app | /api/play/ |
| Star Movies | Indian Movies | homair-tv-production.up.railway.app | /api/play/ |
| Star Utsav Movies | Indian Movies | homair-tv-production.up.railway.app | /api/play/ |
| Manoranjan Grand | Indian Entertainment | homair-tv-production.up.railway.app | /api/play/ |
| Star Bharat | Indian Entertainment | homair-tv-production.up.railway.app | /api/play/ |
| Star Utsav | Indian Entertainment | homair-tv-production.up.railway.app | /api/play/ |
| Nick | Kids | homair-tv-production.up.railway.app | /api/play/ |
| Nick Jr | Kids | homair-tv-production.up.railway.app | /api/play/ |
| Sonic | Kids | homair-tv-production.up.railway.app | /api/play/ |
| BTV Chattogram | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Colors Cineplex [UK] | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Desh TV | Backup | homair-tv-production.up.railway.app | /api/play/ |
| HBO | Backup | homair-tv-production.up.railway.app | /api/play/ |

## Recommendations

- Keep fragile routes unchanged until a working, authorized replacement is confirmed.
- Test streamtest endpoints in the target IPTV player; the path name alone does not prove a route is dead.
- Do not strip or rewrite signed query parameters blindly; they may be source/session-bound.
- Move Xtream credentials out of the public playlist when authorized replacement routing exists, and rotate exposed credentials as appropriate.
- Replace primary proxy/worker routes with verified direct URLs where possible; do not silently delete Backup entries.
