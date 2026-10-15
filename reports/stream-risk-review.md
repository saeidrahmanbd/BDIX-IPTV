# Stream Risk Review

Generated from the current playlist and latest available stream-health report. This review is non-destructive; no stream URL was changed or deleted.

## Summary

- /streamtest/ endpoints: **9**
- Signed/token-query endpoints: **9**
- Xtream-style credential paths (credentials redacted): **8**
- Proxy/worker-host routes: **41** (2 primary, 39 Backup)
- /api/play/ relay routes: **19**

## Latest Stream-Health Snapshot

| Metric | Count |
|---|---:|
| Streams tested | 1037 |
| Reachable | 966 |
| Failed this check | 71 |
| Persistent failures (3+ consecutive) | 66 |
| HTTP 401/403 (auth) | 6 |
| HTTP 404 (not found) | 8 |
| HTTP 5xx (server) | 7 |
| Timeout | 50 |

### Persistent failures

- **ATN Bangla UK** — Backup — consecutive failures: **4** — Timeout
- **Amar Bangla Digital** — Backup — consecutive failures: **4** — Timeout
- **Ananda TV** — Backup — consecutive failures: **5** — Timeout
- **Ananda TV** — Backup — consecutive failures: **9** — Timeout
- **Channel 1** — Backup — consecutive failures: **5** — Timeout
- **Channel 1** — Backup — consecutive failures: **5** — Timeout
- **Channel 52** — Backup — consecutive failures: **4** — HTTP 404
- **Channel S** — Backup — consecutive failures: **5** — Timeout
- **Channel S** — Backup — consecutive failures: **4** — Timeout
- **Channel S** — Backup — consecutive failures: **4** — Timeout
- **Channel S** — Backup — consecutive failures: **5** — Timeout
- **Deen TV** — Backup — consecutive failures: **4** — Timeout
- **Desh TV** — Backup — consecutive failures: **5** — Timeout
- **Discover Pakistan** — Backup — consecutive failures: **4** — Timeout
- **Disney Channel India** — Backup — consecutive failures: **81** — HTTP 403
- **Ekhon TV** — Backup — consecutive failures: **5** — Timeout
- **Ekushey TV** — Backup — consecutive failures: **5** — Timeout
- **G TV** — Backup — consecutive failures: **5** — Timeout
- **G TV** — Backup — consecutive failures: **4** — Timeout
- **G TV** — Backup — consecutive failures: **6** — Timeout
- **G TV** — Backup — consecutive failures: **5** — Timeout
- **Global TV** — Backup — consecutive failures: **5** — Timeout
- **Green TV** — Backup — consecutive failures: **4** — Timeout
- **Green TV** — Backup — consecutive failures: **4** — HTTP 523
- **Green TV** — Backup — consecutive failures: **4** — Timeout
- **Green TV** — Backup — consecutive failures: **4** — HTTP 404
- **Jago News 24** — Backup — consecutive failures: **4** — Timeout
- **Jago News 24** — Backup — consecutive failures: **4** — Timeout
- **Medina Live** — Backup — consecutive failures: **5** — Timeout
- **Movie Bangla** — Backup — consecutive failures: **5** — Timeout
- **Movie Bangla** — Backup — consecutive failures: **5** — Timeout
- **My TV** — Backup — consecutive failures: **5** — Timeout
- **My TV** — Backup — consecutive failures: **5** — Timeout
- **My TV** — Backup — consecutive failures: **4** — Timeout
- **NTV Europe** — Backup — consecutive failures: **4** — Timeout
- **RTV** — Backup — consecutive failures: **5** — Timeout
- **SA TV** — Backup — consecutive failures: **5** — Timeout
- **SA TV** — Backup — consecutive failures: **5** — Timeout
- **Shanson TV** — Backup — consecutive failures: **3** — HTTP 403
- **ATN Bangla UK** — Bangladesh — consecutive failures: **4** — HTTP 523
- **Ananda TV** — Bangladesh — consecutive failures: **5** — Timeout
- **Channel 16** — Bangladesh — consecutive failures: **17** — Timeout
- **Channel S** — Bangladesh — consecutive failures: **4** — HTTP 523
- **Channel S UK** — Bangladesh — consecutive failures: **4** — Timeout
- **G TV** — Bangladesh — consecutive failures: **4** — Timeout
- **Green TV** — Bangladesh — consecutive failures: **5** — Timeout
- **Jago News 24** — Bangladesh — consecutive failures: **4** — Timeout
- **Jonmobhumi TV** — Bangladesh — consecutive failures: **4** — HTTP 404
- **NRB TV** — Bangladesh — consecutive failures: **4** — Timeout
- **NTV Europe** — Bangladesh — consecutive failures: **4** — Timeout
- **Time Television** — Bangladesh — consecutive failures: **4** — Timeout
- **Amar Bangla** — Indian Bangla — consecutive failures: **4** — Timeout
- **Channel 52** — Indian Bangla — consecutive failures: **4** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **215** — HTTP 403
- **Oli TV** — Indian Entertainment — consecutive failures: **9** — Timeout
- **Suriyan TV** — Indian Entertainment — consecutive failures: **9** — HTTP 523
- **K Cine** — Indian Movies — consecutive failures: **6** — Timeout
- **Afrobeats** — International — consecutive failures: **6** — HTTP 404
- **Cook & Bake** — International — consecutive failures: **21** — HTTP 504
- **HBO** — International — consecutive failures: **203** — HTTP 403
- **Teleritmo** — International — consecutive failures: **21** — HTTP 403
- **iON TV UK** — International — consecutive failures: **4** — Timeout
- **Teen Nick** — Kids — consecutive failures: **81** — HTTP 403
- **Iqra Bangla** — Religious — consecutive failures: **4** — Timeout
- **Islamic TV** — Religious — consecutive failures: **5** — Timeout
- **Makkah Live** — Religious — consecutive failures: **5** — Timeout

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
| BTV National | Bangladesh | homair-tv-production.up.railway.app | /api/play/ |
| BTV World | Bangladesh | homair-tv-production.up.railway.app | /api/play/ |
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
| Super Hungama | Kids | homair-tv-production.up.railway.app | /api/play/ |
| BTV Chattogram | Backup | homair-tv-production.up.railway.app | /api/play/ |
| BTV News | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Colors Cineplex [UK] | Backup | homair-tv-production.up.railway.app | /api/play/ |
| Desh TV | Backup | homair-tv-production.up.railway.app | /api/play/ |
| HBO | Backup | homair-tv-production.up.railway.app | /api/play/ |
| HUM Masala | Backup | homair-tv-production.up.railway.app | /api/play/ |

## Recommendations

- Keep fragile routes unchanged until a working, authorized replacement is confirmed.
- Test streamtest endpoints in the target IPTV player; the path name alone does not prove a route is dead.
- Do not strip or rewrite signed query parameters blindly; they may be source/session-bound.
- Move Xtream credentials out of the public playlist when authorized replacement routing exists, and rotate exposed credentials as appropriate.
- Replace primary proxy/worker routes with verified direct URLs where possible; do not silently delete Backup entries.
