# Stream Risk Review

Generated: **2026-11-22T02:40:41+00:00**
IPTV-Playlist.m3u SHA-256: **7535ac5bcd4eac4cc0fd8d5d4f13254a73b76d8c1b366adaca9a6c4571ad83b1**

Generated from the current playlist and latest available stream-health report. This review is non-destructive; no stream URL was changed or deleted.

## Summary

- /streamtest/ endpoints: **12**
- Signed/token-query endpoints: **12**
- Signed endpoints with expired embedded expiry: **0**
- Signed endpoints expiring within 72 hours: **0**
- Signed endpoints with no parseable expiry: **0**
- Xtream-style credential paths (credentials redacted): **3**
- Proxy/worker-host routes: **30** (6 primary, 24 Backup)
- /api/play/ relay routes: **0**
- Expiry is parsed only from explicit Unix timestamps; opaque signatures remain UNKNOWN and are never guessed.

## Latest Stream-Health Snapshot

| Metric | Count |
|---|---:|
| Streams tested | 1389 |
| Reachable | 1172 |
| Failed this check | 217 |
| Persistent failures (3+ consecutive) | 55 |

### Persistent failures

- **Bol Entertainment** — Pakistani — consecutive failed days: **3** — HTTP 404
- **&TV** — Review — consecutive failed days: **8** — HTTP 404
- **8XM** — Review — consecutive failed days: **3** — HTTP 404
- **AMN TV** — Review — consecutive failed days: **8** — HTTP 404
- **Amar Bangla** — Review — consecutive failed days: **8** — HTTP 404
- **Animal Planet HD** — Review — consecutive failed days: **8** — HTTP 404
- **Asian TV** — Review — consecutive failed days: **8** — HTTP 404
- **B4U Movies** — Review — consecutive failed days: **8** — HTTP 404
- **B4U Music** — Review — consecutive failed days: **8** — HTTP 404
- **Bijoy TV** — Review — consecutive failed days: **8** — HTTP 404
- **Bijoy TV** — Review — consecutive failed days: **8** — HTTP 404
- **Channel 1** — Review — consecutive failed days: **8** — HTTP 404
- **Channel 1** — Review — consecutive failed days: **8** — HTTP 404
- **Channel 24** — Review — consecutive failed days: **8** — HTTP 404
- **Channel 24** — Review — consecutive failed days: **8** — HTTP 404
- **Channel 24** — Review — consecutive failed days: **8** — HTTP 404
- **Desh TV** — Review — consecutive failed days: **8** — HTTP 404
- **Dhamaal** — Review — consecutive failed days: **8** — HTTP 404
- **Discovery Channel (India)** — Review — consecutive failed days: **8** — HTTP 404
- **Ekattor TV** — Review — consecutive failed days: **8** — HTTP 404
- **Ekhon TV** — Review — consecutive failed days: **8** — HTTP 404
- **Ekhon TV** — Review — consecutive failed days: **8** — HTTP 404
- **Eurosport** — Review — consecutive failed days: **8** — HTTP 404
- **Global TV** — Review — consecutive failed days: **8** — HTTP 404
- **Green TV** — Review — consecutive failed days: **8** — HTTP 404
- **Hum TV** — Review — consecutive failed days: **8** — HTTP 404
- **Hum TV** — Review — consecutive failed days: **8** — HTTP 404
- **Islamic TV** — Review — consecutive failed days: **8** — HTTP 404
- **Jalwa TV** — Review — consecutive failed days: **3** — HTTP 404
- **Jalwa TV** — Review — consecutive failed days: **3** — HTTP 404
- **Jamuna TV** — Review — consecutive failed days: **8** — HTTP 404
- **MBC Bollywood** — Review — consecutive failed days: **6** — HTTP 404
- **MLB** — Review — consecutive failed days: **4** — HTTP 404
- **Mohona TV** — Review — consecutive failed days: **8** — HTTP 404
- **Movie Bangla** — Review — consecutive failed days: **8** — HTTP 404
- **MovieSphere** — Review — consecutive failed days: **4** — HTTP 404
- **Nexus TV** — Review — consecutive failed days: **8** — HTTP 404
- **Rajdhani TV** — Review — consecutive failed days: **8** — HTTP 404
- **Rakuten TV Action Movies UK** — Review — consecutive failed days: **5** — HTTP 404
- **Rakuten TV Comedy Movies UK** — Review — consecutive failed days: **4** — HTTP 404
- **Rupashi Bangla TV** — Review — consecutive failed days: **5** — HTTP 404
- **Sananda** — Review — consecutive failed days: **8** — HTTP 404
- **Somoy TV** — Review — consecutive failed days: **8** — HTTP 404
- **Sony Aath** — Review — consecutive failed days: **8** — HTTP 404
- **Sony Aath** — Review — consecutive failed days: **8** — HTTP 404
- **Sony Max 2** — Review — consecutive failed days: **8** — HTTP 404
- **Sony SAB** — Review — consecutive failed days: **8** — HTTP 404
- **Stadium** — Review — consecutive failed days: **4** — HTTP 404
- **T Sports** — Review — consecutive failed days: **4** — HTTP 404
- **Thanthi One** — Review — consecutive failed days: **8** — HTTP 404
- **Zee Bangla** — Review — consecutive failed days: **8** — HTTP 404
- **Zee Bangla Cinema** — Review — consecutive failed days: **8** — HTTP 404
- **Zee Bollywood** — Review — consecutive failed days: **8** — HTTP 404
- **Zee Cinema** — Review — consecutive failed days: **8** — HTTP 404
- **Zee TV** — Review — consecutive failed days: **8** — HTTP 404

## /streamtest/ Endpoints

| Channel | Group | Host | Path |
|---|---|---|---|
| 8XM | Pakistani | vodzong.mjunoon.tv:8087 | /streamtest/8XM-131/playlist.m3u8 |
| Ary Digital | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/84M/chunks.m3u8 |
| Bol Entertainment | Pakistani | vodzong.mjunoon.tv:8087 | /streamtest/Channel5-159-4/playlist.m3u8 |
| Green Entertainment | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/166M/chunks.m3u8 |
| See TV | Pakistani | vodzong.mjunoon.tv:8087 | /streamtest/SeeTV-156/playlist.m3u8 |
| Paighan TV | Religious | cdn4.mjunoon.tv:8087 | /streamtest/107M/chunks.m3u8 |
| Animal Planet | Backup | vodzong.mjunoon.tv:8087 | /streamtest/Animal-Planet-158-3/playlist.m3u8 |
| Hum TV | Backup | cdn4.mjunoon.tv:8087 | /streamtest/82M/chunks.m3u8 |
| 8XM | Review | cdn4.mjunoon.tv:8087 | /streamtest/131M/chunks.m3u8 |
| Jalwa TV | Review | cdn4.mjunoon.tv:8087 | /streamtest/135M/chunks.m3u8 |
| Jalwa TV | Review | vodzong.mjunoon.tv:8087 | /streamtest/JalwaTV-135/live/135M/chunks.m3u8 |
| Waseb TV | Review | vodzong.mjunoon.tv:8087 | /streamtest/WASEB-130/playlist.m3u8 |

## Signed / Token-Query Endpoints

Query values are omitted because they may be expiring signatures or access tokens.

Expiry is classified only when a numeric Unix timestamp is explicitly present (including the exp field inside hdnts). No signature/token values are written to this report.

| Channel | Group | Host | Parameter names | Expiry status | Expiry (UTC) |
|---|---|---|---|---|---|
| ETV Cinema | Indian Movies | yupplivegcpusa.yuppcdn.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| Boogle Bollywood | Indian Music | yuppnimrestreammum.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| Songdew TV | Indian Music | yuppnimrestreammum.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| Wah Punjabi | Indian Music | yuppnimrestreammum.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| Colors Super | Indian Entertainment | d1rc86nwwc9fag.cloudfront.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| Jaihind TV | Indian Entertainment | yuppnimrestreammum.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| Zee Kannada | Indian Entertainment | yuppnimresmum.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| WOW Kidz Hindi | Kids | yuppparoriglin.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| WOW Kidz Tamil | Kids | yuppparoriglin.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| WOW Kidz Telugu | Kids | yuppparoriglin.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| Major League Cricket | Sports | bl.rutube.ru | e | FUTURE | 2035-09-29T13:14:34+00:00 |
| Studio Yuva | Backup | d2gvyg6lvauoko.cloudfront.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |

## Xtream-Style Credential Paths

Credentials are intentionally redacted; only the host and safe route pattern are shown.

| Channel | Group | Host | Redacted path |
|---|---|---|---|
| Independent TV | Bangladesh | premiumtvs.space | /live/[REDACTED]/[REDACTED]/423.ts |
| Disney Channel | Backup | rgkkw.live | /live/[REDACTED]/[REDACTED]/19741.ts |
| Zee Bangla | Backup | rgkkw.live:80 | /live/[REDACTED]/[REDACTED]/98881.ts |

## Proxy / Worker-Host Routes

Worker routes are relayed endpoints, not direct broadcaster sources. The Sananda primary is the highest-priority route to replace with a verified direct source. Backup candidates are retained pending verification.

| Channel | Group | Host |
|---|---|---|
| ATN Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| ATN News | Backup | iptv-proxy.ahmed-bd-org.workers.dev |
| Bangla TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Bangla Vision | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Bhojpuri Cinema | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Boishakhi TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel I | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel S | Backup | iptvlive.ahmed-bd-org.workers.dev |
| DBC News | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Enter TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Epic Music | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Jago News 24 | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Jamuna TV | Backup | iptv-proxy.ahmed-bd-org.workers.dev |
| Jamuna TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Movie Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| News 24 | Backup | iptvlive.ahmed-bd-org.workers.dev |
| NTV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| PTC Music | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Rongeen TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| SA TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| SA TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Sananda | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Somoy TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Zee Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel 16 | Review | iptvlive.ahmed-bd-org.workers.dev |
| Channel 24 | Review | iptvlive.ahmed-bd-org.workers.dev |
| Enterr10 Bangla | Review | iptvlive.ahmed-bd-org.workers.dev |
| ME TV | Review | iptvlive.ahmed-bd-org.workers.dev |
| ME TV | Review | iptvlive.ahmed-bd-org.workers.dev |
| ME TV | Review | iptvlive.ahmed-bd-org.workers.dev |

## Hosted /api/play/ Relay Routes

| Channel | Group | Host | Route type |
|---|---|---|---|
| — | — | — | — |

## Recommendations

- Keep fragile routes unchanged until a working, authorized replacement is confirmed.
- Test streamtest endpoints in the target IPTV player; the path name alone does not prove a route is dead.
- Do not strip or rewrite signed query parameters blindly; they may be source/session-bound.
- Move Xtream credentials out of the public playlist when authorized replacement routing exists, and rotate exposed credentials as appropriate.
- Replace primary proxy/worker routes with verified direct URLs where possible; do not silently delete Backup entries.
