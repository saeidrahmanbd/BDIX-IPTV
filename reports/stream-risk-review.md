# Stream Risk Review

Generated: **2026-10-21T05:16:38+00:00**
IPTV-Playlist.m3u SHA-256: **61199b5845086edf9deb98a51a4e794c6757999358847fa5c1ad1e43e9357a3e**

Generated from the current playlist and latest available stream-health report. This review is non-destructive; no stream URL was changed or deleted.

## Summary

- /streamtest/ endpoints: **10**
- Signed/token-query endpoints: **11**
- Xtream-style credential paths (credentials redacted): **0**
- Proxy/worker-host routes: **41** (3 primary, 38 Backup)
- /api/play/ relay routes: **13**

## Latest Stream-Health Snapshot

| Metric | Count |
|---|---:|
| Streams tested | 1088 |
| Reachable | 1015 |
| Failed this check | 73 |
| Persistent failures (3+ consecutive) | 43 |
| HTTP 401/403 (auth) | 13 |
| HTTP 404 (not found) | 29 |
| HTTP 5xx (server) | 5 |
| Timeout | 24 |

### Persistent failures

- **Ananda TV** — Backup — consecutive failures: **3** — Timeout
- **Channel 1** — Backup — consecutive failures: **3** — Timeout
- **Channel 1** — Backup — consecutive failures: **3** — Timeout
- **Desh TV** — Backup — consecutive failures: **3** — Timeout
- **Disney Channel India** — Backup — consecutive failures: **11** — HTTP 403
- **ESPN** — Backup — consecutive failures: **11** — HTTP 403
- **Ekhon TV** — Backup — consecutive failures: **3** — Timeout
- **Ekushey TV** — Backup — consecutive failures: **3** — Timeout
- **G TV** — Backup — consecutive failures: **11** — Timeout
- **G TV** — Backup — consecutive failures: **11** — Timeout
- **Global TV** — Backup — consecutive failures: **3** — Timeout
- **Green TV** — Backup — consecutive failures: **27** — Timeout
- **Manoranjan TV** — Backup — consecutive failures: **3** — HTTP 404
- **Medina Live** — Backup — consecutive failures: **3** — Timeout
- **Movie Bangla** — Backup — consecutive failures: **3** — Timeout
- **Movie Bangla** — Backup — consecutive failures: **3** — Timeout
- **My TV** — Backup — consecutive failures: **3** — Timeout
- **My TV** — Backup — consecutive failures: **3** — Timeout
- **RTV** — Backup — consecutive failures: **3** — Timeout
- **SA TV** — Backup — consecutive failures: **3** — Timeout
- **SA TV** — Backup — consecutive failures: **3** — Timeout
- **Shanson TV** — Backup — consecutive failures: **7** — HTTP 403
- **Ananda TV** — Bangladesh — consecutive failures: **4** — Timeout
- **Channel 16** — Bangladesh — consecutive failures: **3** — Timeout
- **Cook & Bake** — International — consecutive failures: **43** — HTTP 504
- **HBO** — International — consecutive failures: **225** — HTTP 403
- **Lifetime** — International — consecutive failures: **19** — HTTP 403
- **Teleritmo** — International — consecutive failures: **43** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **103** — HTTP 403
- **Assam Talks** — Not Playing — consecutive failures: **237** — HTTP 403
- **CBN TV USA** — Not Playing — consecutive failures: **19** — HTTP 404
- **Channel S** — Not Playing — consecutive failures: **27** — Timeout
- **Channel S** — Not Playing — consecutive failures: **26** — HTTP 404
- **Channel S** — Not Playing — consecutive failures: **26** — HTTP 404
- **Channel S** — Not Playing — consecutive failures: **27** — Timeout
- **Desh TV** — Not Playing — consecutive failures: **14** — HTTP 404
- **G TV** — Not Playing — consecutive failures: **11** — Timeout
- **Nick** — Not Playing — consecutive failures: **15** — HTTP 404
- **Star Gold** — Not Playing — consecutive failures: **15** — HTTP 404
- **Makkah Live** — Religious — consecutive failures: **3** — Timeout
- **Star Sports 2** — Sports — consecutive failures: **19** — HTTP 403
- **T Sports** — Sports — consecutive failures: **19** — HTTP 403
- **Willow TV** — Sports — consecutive failures: **19** — HTTP 403

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
