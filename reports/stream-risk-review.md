# Stream Risk Review

Generated: **2026-11-12T10:48:47+00:00**
IPTV-Playlist.m3u SHA-256: **9035b8514990d9681dc96a8d7ea6999c2c0777762e2945cdaf2edbd8fdce224e**

Generated from the current playlist and latest available stream-health report. This review is non-destructive; no stream URL was changed or deleted.

## Summary

- /streamtest/ endpoints: **12**
- Signed/token-query endpoints: **19**
- Signed endpoints with expired embedded expiry: **8**
- Signed endpoints expiring within 72 hours: **0**
- Signed endpoints with no parseable expiry: **0**
- Xtream-style credential paths (credentials redacted): **1**
- Proxy/worker-host routes: **30** (2 primary, 28 Backup)
- /api/play/ relay routes: **0**
- Expiry is parsed only from explicit Unix timestamps; opaque signatures remain UNKNOWN and are never guessed.

## Latest Stream-Health Snapshot

| Metric | Count |
|---|---:|
| Streams tested | 1242 |
| Reachable | 1032 |
| Failed this check | 210 |
| Persistent failures (3+ consecutive) | 161 |
| HTTP 404 (not found) | 66 |
| HTTP 5xx (server) | 5 |
| Timeout | 56 |

### Persistent failures

- **7S Music** — Backup — consecutive failures: **178** — HTTP 403
- **9X Jalwa** — Backup — consecutive failures: **178** — HTTP 403
- **Aakaash Aath** — Backup — consecutive failures: **178** — HTTP 403
- **Bangla TV** — Backup — consecutive failures: **25** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **178** — HTTP 403
- **Goldmines 2** — Backup — consecutive failures: **178** — HTTP 403
- **Goldmines Action** — Backup — consecutive failures: **178** — HTTP 403
- **Goldmines Bollywood** — Backup — consecutive failures: **178** — HTTP 403
- **Kappa TV (Music)** — Backup — consecutive failures: **178** — HTTP 403
- **Kerala Vision** — Backup — consecutive failures: **178** — HTTP 403
- **MH One Movies** — Backup — consecutive failures: **140** — HTTP 403
- **Mahaa Max** — Backup — consecutive failures: **178** — HTTP 403
- **Mazhavil Manorama** — Backup — consecutive failures: **178** — HTTP 403
- **NTV Europe** — Backup — consecutive failures: **21** — HTTP 404
- **Star Sports 2** — Backup — consecutive failures: **166** — HTTP 403
- **NTV Europe** — Bangladesh — consecutive failures: **21** — HTTP 404
- **News 21** — Bangladesh — consecutive failures: **21** — Timeout
- **Asianet Middle East** — Indian Entertainment — consecutive failures: **178** — HTTP 403
- **Kairali Arabia** — Indian Entertainment — consecutive failures: **178** — HTTP 403
- **MNTV (Tamil)** — Indian Entertainment — consecutive failures: **23** — HTTP 404
- **Siri Kannada** — Indian Entertainment — consecutive failures: **178** — HTTP 403
- **Sun Surya** — Indian Entertainment — consecutive failures: **164** — HTTP 403
- **Goldmines 2** — Indian Movies — consecutive failures: **178** — HTTP 403
- **Goldmines Action** — Indian Movies — consecutive failures: **178** — HTTP 403
- **MH One Movies** — Indian Movies — consecutive failures: **140** — HTTP 403
- **Andy Haryana** — Indian Music — consecutive failures: **178** — HTTP 403
- **Teleritmo** — International — consecutive failures: **147** — HTTP 403
- **Madani TV** — Religious — consecutive failures: **62** — HTTP 403
- **&TV** — Review — consecutive failures: **53** — HTTP 404
- **&pictures** — Review — consecutive failures: **116** — Connection
- **9X Jalwa** — Review — consecutive failures: **20** — HTTP 404
- **9XM** — Review — consecutive failures: **116** — HTTP 403
- **AMN TV** — Review — consecutive failures: **52** — HTTP 404
- **ATN Bangla** — Review — consecutive failures: **116** — HTTP 404
- **Aakaash Aath** — Review — consecutive failures: **116** — HTTP 404
- **Amar Bangla** — Review — consecutive failures: **105** — HTTP 404
- **Ananda TV** — Review — consecutive failures: **116** — Connection
- **Animal Planet** — Review — consecutive failures: **106** — HTTP 404
- **Asian TV** — Review — consecutive failures: **103** — HTTP 404
- **Azan TV** — Review — consecutive failures: **24** — TLS
- **B4U Movies** — Review — consecutive failures: **116** — Connection
- **B4U Movies** — Review — consecutive failures: **106** — HTTP 404
- **B4U Music** — Review — consecutive failures: **106** — HTTP 404
- **BS Film** — Review — consecutive failures: **116** — HTTP 502
- **Bangla TV** — Review — consecutive failures: **129** — HTTP 404
- **Bengali Beats** — Review — consecutive failures: **113** — Connection
- **Bijoy TV** — Review — consecutive failures: **106** — HTTP 404
- **Bijoy TV** — Review — consecutive failures: **103** — HTTP 404
- **Boishakhi TV** — Review — consecutive failures: **116** — TLS
- **Channel 1** — Review — consecutive failures: **106** — HTTP 404
- **Channel 1** — Review — consecutive failures: **104** — HTTP 404
- **Channel 24** — Review — consecutive failures: **116** — Connection
- **Channel 24** — Review — consecutive failures: **106** — HTTP 404
- **Channel 24** — Review — consecutive failures: **103** — HTTP 404
- **Channel 24** — Review — consecutive failures: **103** — HTTP 404
- **Channel I** — Review — consecutive failures: **64** — HTTP 504
- **Colors** — Review — consecutive failures: **116** — Connection
- **Colors Bangla** — Review — consecutive failures: **116** — Timeout
- **Colors Bangla Cinema** — Review — consecutive failures: **116** — Connection
- **Colors Cineplex [UK]** — Review — consecutive failures: **116** — Connection
- **DBC News** — Review — consecutive failures: **116** — Network
- **DD National** — Review — consecutive failures: **141** — HTTP 403
- **Dangal** — Review — consecutive failures: **53** — Timeout
- **Deen TV** — Review — consecutive failures: **64** — Timeout
- **Deepto TV** — Review — consecutive failures: **116** — Connection
- **Deewana** — Review — consecutive failures: **113** — Connection
- **Desh TV** — Review — consecutive failures: **104** — HTTP 404
- **Deshe Bideshe** — Review — consecutive failures: **24** — TLS
- **Dhamaal** — Review — consecutive failures: **116** — HTTP 404
- **Discovery Channel (India)** — Review — consecutive failures: **106** — HTTP 404
- **Discovery Channel (India)** — Review — consecutive failures: **106** — HTTP 404
- **Duronto TV** — Review — consecutive failures: **116** — Connection
- **ETV Cinema** — Review — consecutive failures: **116** — DNS
- **ETV Plus** — Review — consecutive failures: **116** — DNS
- **Ekattor TV** — Review — consecutive failures: **103** — HTTP 404
- **Ekhon TV** — Review — consecutive failures: **106** — HTTP 404
- **Ekhon TV** — Review — consecutive failures: **103** — HTTP 404
- **Ekhon TV** — Review — consecutive failures: **116** — TLS
- **Epic Music** — Review — consecutive failures: **116** — Timeout
- **Eurosport** — Review — consecutive failures: **106** — HTTP 404
- **G TV** — Review — consecutive failures: **116** — Connection
- **G TV** — Review — consecutive failures: **116** — Network
- **Global TV** — Review — consecutive failures: **104** — HTTP 404
- **Green TV** — Review — consecutive failures: **129** — HTTP 404
- **Hum TV** — Review — consecutive failures: **106** — HTTP 404
- **Hum TV** — Review — consecutive failures: **104** — HTTP 404
- **Independent TV** — Review — consecutive failures: **116** — Connection
- **Independent TV** — Review — consecutive failures: **105** — Timeout
- **Independent TV** — Review — consecutive failures: **106** — HTTP 404
- **Independent TV** — Review — consecutive failures: **5** — HTTP 404
- **Iqra Bangla** — Review — consecutive failures: **64** — Timeout
- **Islamic TV** — Review — consecutive failures: **106** — HTTP 404
- **Jalsha Movies** — Review — consecutive failures: **116** — Connection
- **Jamuna TV** — Review — consecutive failures: **103** — HTTP 404
- **Jhankar TV** — Review — consecutive failures: **24** — TLS
- **MTV India** — Review — consecutive failures: **62** — HTTP 403
- **Maasranga TV** — Review — consecutive failures: **116** — HTTP 404
- **Madani TV** — Review — consecutive failures: **64** — Timeout
- **Mohona TV** — Review — consecutive failures: **104** — HTTP 404
- **Movie Bangla** — Review — consecutive failures: **104** — HTTP 404
- **Nat Geo TV** — Review — consecutive failures: **116** — Connection
- **Nexus TV** — Review — consecutive failures: **104** — HTTP 404
- **Nick Bangla** — Review — consecutive failures: **116** — Connection
- **PK Sports** — Review — consecutive failures: **113** — HTTP 502
- **PTV Sports** — Review — consecutive failures: **116** — Connection
- **Pogo** — Review — consecutive failures: **56** — HTTP 404
- **RTV** — Review — consecutive failures: **116** — HTTP 404
- **RTV** — Review — consecutive failures: **53** — HTTP 404
- **Raj Digital Plus** — Review — consecutive failures: **24** — TLS
- **Raj Musix Tamil** — Review — consecutive failures: **24** — TLS
- **Raj TV** — Review — consecutive failures: **24** — HTTP 504
- **Raj TV** — Review — consecutive failures: **24** — TLS
- **Rajdhani TV** — Review — consecutive failures: **106** — HTTP 404
- **Rakuten Movies** — Review — consecutive failures: **62** — HTTP 504
- **Sananda** — Review — consecutive failures: **51** — HTTP 404
- **Shemaroo Filmi Gaane** — Review — consecutive failures: **116** — HTTP 403
- **Somoy TV** — Review — consecutive failures: **106** — HTTP 404
- **Sonic** — Review — consecutive failures: **116** — Timeout
- **Sony Aath** — Review — consecutive failures: **116** — Timeout
- **Sony Aath** — Review — consecutive failures: **106** — HTTP 404
- **Sony Aath** — Review — consecutive failures: **104** — HTTP 404
- **Sony Entertainment TV** — Review — consecutive failures: **116** — Connection
- **Sony Max** — Review — consecutive failures: **116** — Connection
- **Sony Max 2** — Review — consecutive failures: **106** — HTTP 404
- **Sony Pal** — Review — consecutive failures: **116** — HTTP 403
- **Sony SAB** — Review — consecutive failures: **106** — HTTP 404
- **Sony Yay!** — Review — consecutive failures: **105** — HTTP 404
- **Sooriyan TV** — Review — consecutive failures: **113** — Connection
- **Spondon** — Review — consecutive failures: **116** — TLS
- **Star Bharat** — Review — consecutive failures: **116** — Connection
- **Star Gold** — Review — consecutive failures: **109** — Connection
- **Star Gold** — Review — consecutive failures: **116** — Timeout
- **Star Jalsha** — Review — consecutive failures: **116** — Connection
- **Star Jalsha** — Review — consecutive failures: **6** — HTTP 458
- **Star Movies** — Review — consecutive failures: **116** — Connection
- **Star Movies Select** — Review — consecutive failures: **116** — Connection
- **Star News** — Review — consecutive failures: **116** — Connection
- **Star Plus** — Review — consecutive failures: **116** — Connection
- **Star Plus** — Review — consecutive failures: **116** — Timeout
- **Star Sports Select 1** — Review — consecutive failures: **116** — Connection
- **Star Sports Select 2** — Review — consecutive failures: **116** — HTTP 404
- **Sun Bangla** — Review — consecutive failures: **116** — Connection
- **Sun TV** — Review — consecutive failures: **164** — HTTP 403
- **T Sports** — Review — consecutive failures: **116** — Connection
- **Thanthi One** — Review — consecutive failures: **116** — HTTP 404
- **Zee Bangla** — Review — consecutive failures: **53** — HTTP 404
- **Zee Bangla Cinema** — Review — consecutive failures: **53** — HTTP 404
- **Zee Bangla Sonar** — Review — consecutive failures: **116** — Connection
- **Zee Bangla Sonar** — Review — consecutive failures: **116** — Timeout
- **Zee Bollywood** — Review — consecutive failures: **53** — HTTP 404
- **Zee Cine Classic** — Review — consecutive failures: **116** — HTTP 403
- **Zee Cinema** — Review — consecutive failures: **116** — Connection
- **Zee Cinema** — Review — consecutive failures: **53** — HTTP 404
- **Zee Comedy Nation** — Review — consecutive failures: **116** — HTTP 403
- **Zee Dil Se** — Review — consecutive failures: **116** — HTTP 403
- **Zee Horror Nights** — Review — consecutive failures: **116** — HTTP 403
- **Zee South Flix** — Review — consecutive failures: **116** — HTTP 403
- **Zee TV** — Review — consecutive failures: **116** — Connection
- **Zee TV** — Review — consecutive failures: **15** — HTTP 404
- **Zee Tamil** — Review — consecutive failures: **116** — HTTP 403
- **Star Sports 2** — Sports — consecutive failures: **214** — HTTP 403

## /streamtest/ Endpoints

| Channel | Group | Host | Path |
|---|---|---|---|
| 8XM | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/131M/chunks.m3u8 |
| Ary Digital | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/84M/chunks.m3u8 |
| Bol Entertainment | Pakistani | vodzong.mjunoon.tv:8087 | /streamtest/Channel5-159-4/playlist.m3u8 |
| Green Entertainment | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/166M/chunks.m3u8 |
| Jalwa TV | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/135M/chunks.m3u8 |
| Paighan TV | Pakistani | cdn4.mjunoon.tv:8087 | /streamtest/107M/chunks.m3u8 |
| See TV | Pakistani | vodzong.mjunoon.tv:8087 | /streamtest/SeeTV-156/playlist.m3u8 |
| Waseb TV | Pakistani | vodzong.mjunoon.tv:8087 | /streamtest/WASEB-130/playlist.m3u8 |
| Animal Planet | Documentary & Wildlife | vodzong.mjunoon.tv:8087 | /streamtest/Animal-Planet-158-3/playlist.m3u8 |
| 8XM | Backup | vodzong.mjunoon.tv:8087 | /streamtest/8XM-131/playlist.m3u8 |
| Hum TV | Backup | cdn4.mjunoon.tv:8087 | /streamtest/82M/chunks.m3u8 |
| Jalwa TV | Backup | vodzong.mjunoon.tv:8087 | /streamtest/JalwaTV-135/live/135M/chunks.m3u8 |

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
| Zee Kannada | Indian Entertainment | yuppnimresmum.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| WOW Kidz Hindi | Kids | yuppparoriglin.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| WOW Kidz Tamil | Kids | yuppparoriglin.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| WOW Kidz Telugu | Kids | yuppparoriglin.akamaized.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| Madani TV | Religious | tvsen7.aynaott.com | e, token | EXPIRED | 2026-07-15T08:02:48+00:00 |
| Major League Cricket | Sports | bl.rutube.ru | e | FUTURE | 2035-09-29T13:14:34+00:00 |
| Deepto TV | Backup | tvsen5.aynaott.com | e, token | EXPIRED | 2026-07-15T08:02:43+00:00 |
| Studio Yuva | Backup | d2gvyg6lvauoko.cloudfront.net | hdnts | FUTURE | 2028-03-05T19:51:28+00:00 |
| 9X Jalwa | Review | tvsen6.aynaott.com | e, token | EXPIRED | 2026-07-15T08:03:11+00:00 |
| Dangal | Review | tvsen6.aynaott.com | e, token | EXPIRED | 2026-07-15T08:03:14+00:00 |
| Independent TV | Review | tvsen6.aynaott.com | e, token | EXPIRED | 2026-07-15T08:02:16+00:00 |
| Manoranjan TV | Review | tvsen6.aynaott.com | e, token | EXPIRED | 2026-07-15T08:03:18+00:00 |
| Shemaroo TV | Review | tvsen6.aynaott.com | e, token | EXPIRED | 2026-07-15T08:03:15+00:00 |
| The Q | Review | tvsen6.aynaott.com | e, token | EXPIRED | 2026-07-15T08:03:16+00:00 |

## Xtream-Style Credential Paths

Credentials are intentionally redacted; only the host and safe route pattern are shown.

| Channel | Group | Host | Redacted path |
|---|---|---|---|
| Zee Bangla | Backup | rgkkw.live:80 | /live/[REDACTED]/[REDACTED]/98881.ts |

## Proxy / Worker-Host Routes

Worker routes are relayed endpoints, not direct broadcaster sources. The Sananda primary is the highest-priority route to replace with a verified direct source. Backup candidates are retained pending verification.

| Channel | Group | Host |
|---|---|---|
| Sananda | Indian Bangla | iptvlive.ahmed-bd-org.workers.dev |
| ATN Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| ATN News | Backup | iptv-proxy.ahmed-bd-org.workers.dev |
| Bangla TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Bangla Vision | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Bhojpuri Cinema | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Boishakhi TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel 16 | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel I | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel S | Backup | iptvlive.ahmed-bd-org.workers.dev |
| DBC News | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Enter TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Enter10 Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Epic Music | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Jago News 24 | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Jamuna TV | Backup | iptv-proxy.ahmed-bd-org.workers.dev |
| Jamuna TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| ME TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| ME TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| ME TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Movie Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| News 24 | Backup | iptvlive.ahmed-bd-org.workers.dev |
| NTV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| PTC Music | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Rongeen TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| SA TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| SA TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Somoy TV | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Zee Bangla | Backup | iptvlive.ahmed-bd-org.workers.dev |
| Channel 24 | Review | iptvlive.ahmed-bd-org.workers.dev |

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
