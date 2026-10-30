# Stream Risk Review

Generated: **2026-10-30T02:23:29+00:00**
IPTV-Playlist.m3u SHA-256: **7f2fa0e3b0ff34ceb5823b465b75dc99e6fb3fc8f1fac5a8c5f88b0ed52663ab**

Generated from the current playlist and latest available stream-health report. This review is non-destructive; no stream URL was changed or deleted.

## Summary

- /streamtest/ endpoints: **9**
- Signed/token-query endpoints: **10**
- Xtream-style credential paths (credentials redacted): **0**
- Proxy/worker-host routes: **41** (3 primary, 38 Backup)
- /api/play/ relay routes: **8**

## Latest Stream-Health Snapshot

| Metric | Count |
|---|---:|
| Streams tested | 1159 |
| Reachable | 1013 |
| Failed this check | 146 |
| Persistent failures (3+ consecutive) | 56 |
| HTTP 404 (not found) | 40 |
| HTTP 5xx (server) | 5 |
| Timeout | 21 |

### Persistent failures

- **Bahrain Sports 2** — Backup — consecutive failures: **3** — HTTP 404
- **Dangal** — Backup — consecutive failures: **4** — HTTP 404
- **Music India** — Backup — consecutive failures: **10** — HTTP 500
- **Sangeet Bangla** — Backup — consecutive failures: **10** — HTTP 500
- **Sangeet Bhojpuri** — Backup — consecutive failures: **10** — HTTP 500
- **Assam Talks** — Indian Entertainment — consecutive failures: **246** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **52** — HTTP 504
- **Teleritmo** — International — consecutive failures: **52** — HTTP 403
- **Disney Channel India** — New Channels — consecutive failures: **4** — Timeout
- **Nickelodeon (India)** — New Channels — consecutive failures: **4** — Timeout
- **Vokta TV** — New Channels — consecutive failures: **4** — HTTP 403
- **&TV** — Not Playing — consecutive failures: **4** — HTTP 403
- **&TV** — Not Playing — consecutive failures: **4** — HTTP 403
- **9XM** — Not Playing — consecutive failures: **4** — HTTP 403
- **ATN Music** — Not Playing — consecutive failures: **4** — HTTP 404
- **AmarUjala** — Not Playing — consecutive failures: **4** — HTTP 404
- **Ananda TV** — Not Playing — consecutive failures: **4** — Timeout
- **Asom Live 24** — Not Playing — consecutive failures: **4** — HTTP 404
- **Bollywood Film** — Not Playing — consecutive failures: **10** — HTTP 403
- **Captain** — Not Playing — consecutive failures: **4** — HTTP 404
- **Colors Bangla** — Not Playing — consecutive failures: **4** — Timeout
- **Colors Cineplex [UK]** — Not Playing — consecutive failures: **4** — HTTP 403
- **Colors Cineplex [UK]** — Not Playing — consecutive failures: **10** — HTTP 404
- **DBC News** — Not Playing — consecutive failures: **4** — Network
- **Desh TV** — Not Playing — consecutive failures: **23** — HTTP 404
- **Dhamaal** — Not Playing — consecutive failures: **4** — HTTP 404
- **ETV Bal Bharat** — Not Playing — consecutive failures: **4** — Timeout
- **ETV Cinema** — Not Playing — consecutive failures: **4** — DNS
- **ETV Life** — Not Playing — consecutive failures: **4** — HTTP 404
- **ETV Music** — Not Playing — consecutive failures: **4** — HTTP 404
- **ETV Plus** — Not Playing — consecutive failures: **4** — DNS
- **ETV Telugu** — Not Playing — consecutive failures: **4** — HTTP 404
- **Ekhon TV** — Not Playing — consecutive failures: **4** — TLS
- **Gazi TV** — Not Playing — consecutive failures: **4** — Network
- **Hungama TV** — Not Playing — consecutive failures: **4** — Timeout
- **Jalsha Movies** — Not Playing — consecutive failures: **4** — Timeout
- **Jaya Plus** — Not Playing — consecutive failures: **4** — HTTP 404
- **Lifetime** — Not Playing — consecutive failures: **28** — HTTP 403
- **Madani TV** — Not Playing — consecutive failures: **10** — DNS
- **Manoranjan Grand** — Not Playing — consecutive failures: **10** — HTTP 404
- **Manoranjan TV** — Not Playing — consecutive failures: **12** — HTTP 404
- **Sony Aath** — Not Playing — consecutive failures: **4** — Timeout
- **Sony Max** — Not Playing — consecutive failures: **4** — Timeout
- **Sony PAL** — Not Playing — consecutive failures: **4** — HTTP 403
- **Sony Yay** — Not Playing — consecutive failures: **4** — Timeout
- **Star Bharat** — Not Playing — consecutive failures: **10** — HTTP 404
- **Star Gold** — Not Playing — consecutive failures: **4** — Timeout
- **Star Gold** — Not Playing — consecutive failures: **24** — HTTP 404
- **Star Gold Select** — Not Playing — consecutive failures: **10** — HTTP 404
- **Star Movies** — Not Playing — consecutive failures: **4** — Timeout
- **Star Plus** — Not Playing — consecutive failures: **4** — HTTP 403
- **Star Utsav** — Not Playing — consecutive failures: **10** — HTTP 404
- **Star Utsav Movies** — Not Playing — consecutive failures: **10** — HTTP 404
- **Suriyan TV** — Not Playing — consecutive failures: **4** — TLS
- **Star Sports 2** — Sports — consecutive failures: **28** — HTTP 403
- **T Sports** — Sports — consecutive failures: **28** — HTTP 403

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
| Star Gold | Indian Movies | 103.114.11.37:8081 | token |
| Colors Super | Indian Entertainment | d1rc86nwwc9fag.cloudfront.net | hdnts |
| Darshana TV | Indian Entertainment | yuppparoriglin.akamaized.net | hdnts |
| Zee Kannada | Indian Entertainment | yuppnimresmum.akamaized.net | hdnts |
| Songdew TV | International | yuppnimrestreammum.akamaized.net | hdnts |
| WOW Kidz Hindi | Kids | yuppparoriglin.akamaized.net | hdnts |
| WOW Kidz Tamil | Kids | yuppparoriglin.akamaized.net | hdnts |
| WOW Kidz Telugu | Kids | yuppparoriglin.akamaized.net | hdnts |
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
| Boishakhi TV | Not Playing | iptvlive.ahmed-bd-org.workers.dev |

## Hosted /api/play/ Relay Routes

| Channel | Group | Host | Route type |
|---|---|---|---|
| Colors Cineplex [UK] | Not Playing | homair-tv-production.up.railway.app | /api/play/ |
| Desh TV | Not Playing | homair-tv-production.up.railway.app | /api/play/ |
| Manoranjan Grand | Not Playing | homair-tv-production.up.railway.app | /api/play/ |
| Star Bharat | Not Playing | homair-tv-production.up.railway.app | /api/play/ |
| Star Gold | Not Playing | homair-tv-production.up.railway.app | /api/play/ |
| Star Gold Select | Not Playing | homair-tv-production.up.railway.app | /api/play/ |
| Star Utsav | Not Playing | homair-tv-production.up.railway.app | /api/play/ |
| Star Utsav Movies | Not Playing | homair-tv-production.up.railway.app | /api/play/ |

## Recommendations

- Keep fragile routes unchanged until a working, authorized replacement is confirmed.
- Test streamtest endpoints in the target IPTV player; the path name alone does not prove a route is dead.
- Do not strip or rewrite signed query parameters blindly; they may be source/session-bound.
- Move Xtream credentials out of the public playlist when authorized replacement routing exists, and rotate exposed credentials as appropriate.
- Replace primary proxy/worker routes with verified direct URLs where possible; do not silently delete Backup entries.
