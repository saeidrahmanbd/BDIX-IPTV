# Stream Risk Review

Generated: **2026-11-06T16:35:04+00:00**
IPTV-Playlist.m3u SHA-256: **92a045f671165942d728082edaac08bdaa83c0320afde042d00ed9b6ea1da67a**

Generated from the current playlist and latest available stream-health report. This review is non-destructive; no stream URL was changed or deleted.

## Summary

- /streamtest/ endpoints: **10**
- Signed/token-query endpoints: **9**
- Xtream-style credential paths (credentials redacted): **0**
- Proxy/worker-host routes: **40** (2 primary, 38 Backup)
- /api/play/ relay routes: **0**

## Latest Stream-Health Snapshot

| Metric | Count |
|---|---:|
| Streams tested | 1121 |
| Reachable | 978 |
| Failed this check | 143 |
| Persistent failures (3+ consecutive) | 124 |
| HTTP 404 (not found) | 16 |
| HTTP 5xx (server) | 8 |
| Timeout | 17 |

### Persistent failures

- **9X Jalwa** — Backup — consecutive failures: **26** — HTTP 403
- **Aakaash Aath** — Backup — consecutive failures: **26** — HTTP 403
- **Animal Planet** — Backup — consecutive failures: **10** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **26** — HTTP 403
- **Epic Bhojpuri** — Backup — consecutive failures: **26** — HTTP 403
- **Goldmines 2** — Backup — consecutive failures: **26** — HTTP 403
- **Goldmines Action** — Backup — consecutive failures: **26** — HTTP 403
- **Goldmines Bollywood** — Backup — consecutive failures: **26** — HTTP 403
- **Kairali TV** — Backup — consecutive failures: **26** — HTTP 403
- **Khushboo Bangla** — Backup — consecutive failures: **26** — HTTP 403
- **MH One Dil Se** — Backup — consecutive failures: **26** — HTTP 403
- **MH One Movies** — Backup — consecutive failures: **26** — HTTP 403
- **MH One Movies** — Backup — consecutive failures: **26** — HTTP 403
- **Madhimugam TV** — Backup — consecutive failures: **26** — HTTP 403
- **Mazhavil Manorama** — Backup — consecutive failures: **26** — HTTP 403
- **Ramdhenu** — Backup — consecutive failures: **26** — HTTP 403
- **Star Sports 2** — Backup — consecutive failures: **14** — HTTP 403
- **Zee Bangla Sonar** — Backup — consecutive failures: **10** — DNS
- **Zee Cinema** — Backup — consecutive failures: **10** — DNS
- **Zee Tamil** — Backup — consecutive failures: **10** — HTTP 403
- **Aakaash Aath** — Indian Bangla — consecutive failures: **26** — HTTP 403
- **Khushboo Bangla** — Indian Bangla — consecutive failures: **26** — HTTP 403
- **Asianet Middle East** — Indian Entertainment — consecutive failures: **26** — HTTP 403
- **Food Food** — Indian Entertainment — consecutive failures: **26** — HTTP 403
- **Kairali Arabia** — Indian Entertainment — consecutive failures: **26** — HTTP 403
- **Kalika TV** — Indian Entertainment — consecutive failures: **11** — HTTP 404
- **Kerala Vision** — Indian Entertainment — consecutive failures: **26** — HTTP 403
- **Mahaa Max** — Indian Entertainment — consecutive failures: **26** — HTTP 403
- **Pear TV** — Indian Entertainment — consecutive failures: **26** — HTTP 403
- **Siri Kannada** — Indian Entertainment — consecutive failures: **26** — HTTP 403
- **Studio Yuva** — Indian Entertainment — consecutive failures: **26** — HTTP 403
- **Sun Surya** — Indian Entertainment — consecutive failures: **12** — HTTP 403
- **Sun TV** — Indian Entertainment — consecutive failures: **12** — HTTP 403
- **Vanitha TV** — Indian Entertainment — consecutive failures: **26** — HTTP 403
- **Epic Bhojpuri** — Indian Movies — consecutive failures: **26** — HTTP 403
- **Goldmines 2** — Indian Movies — consecutive failures: **26** — HTTP 403
- **Goldmines Action** — Indian Movies — consecutive failures: **26** — HTTP 403
- **7S Music** — Indian Music — consecutive failures: **26** — HTTP 403
- **Andy Haryana** — Indian Music — consecutive failures: **26** — HTTP 403
- **Kappa TV (Music)** — Indian Music — consecutive failures: **26** — HTTP 403
- **Raj Musix Kannada** — Indian Music — consecutive failures: **26** — HTTP 403
- **Ramdhenu** — Indian Music — consecutive failures: **26** — HTTP 403
- **Sangeet Bhojpuri** — Indian Music — consecutive failures: **26** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **86** — HTTP 504
- **Lifetime** — International — consecutive failures: **62** — HTTP 403
- **Teleritmo** — International — consecutive failures: **3** — HTTP 403
- **KidDo MATIX** — Kids — consecutive failures: **23** — HTTP 504
- **9XM** — New Backups — consecutive failures: **7** — HTTP 403
- **B4U Movies** — New Backups — consecutive failures: **7** — Timeout
- **Boishakhi TV** — New Backups — consecutive failures: **7** — TLS
- **Colors Bangla** — New Backups — consecutive failures: **7** — HTTP 403
- **Colors Cineplex** — New Backups — consecutive failures: **7** — HTTP 403
- **DBC News** — New Backups — consecutive failures: **7** — Network
- **ETV Cinema** — New Backups — consecutive failures: **7** — DNS
- **Ekhon TV** — New Backups — consecutive failures: **7** — TLS
- **Epic Music** — New Backups — consecutive failures: **7** — Timeout
- **Epic Parivar** — New Backups — consecutive failures: **7** — HTTP 403
- **Gazi TV** — New Backups — consecutive failures: **7** — Network
- **Kairali We** — New Backups — consecutive failures: **7** — HTTP 403
- **Movie Punjab** — New Backups — consecutive failures: **7** — HTTP 403
- **Movies Now** — New Backups — consecutive failures: **7** — HTTP 403
- **Sony Aath** — New Backups — consecutive failures: **7** — HTTP 403
- **Sony Entertainment TV** — New Backups — consecutive failures: **7** — HTTP 403
- **Sony Max** — New Backups — consecutive failures: **7** — HTTP 403
- **Sony PAL** — New Backups — consecutive failures: **7** — HTTP 403
- **Sony Pix** — New Backups — consecutive failures: **7** — HTTP 403
- **Star Gold** — New Backups — consecutive failures: **7** — HTTP 403
- **Star Jalsha** — New Backups — consecutive failures: **7** — HTTP 403
- **Thanthi One** — New Backups — consecutive failures: **7** — HTTP 404
- **Travelxp** — New Backups — consecutive failures: **7** — HTTP 403
- **Zee Bangla** — New Backups — consecutive failures: **7** — HTTP 403
- **Zee Bangla Sonar** — New Backups — consecutive failures: **7** — Timeout
- **Zee Cinema** — New Backups — consecutive failures: **7** — HTTP 403
- **Zee TV** — New Backups — consecutive failures: **7** — HTTP 403
- **Spondon** — New Channels — consecutive failures: **7** — TLS
- **Vokta TV** — New Channels — consecutive failures: **7** — HTTP 403
- **AMC** — Not Playing — consecutive failures: **18** — Timeout
- **Amazing Discoveries TV** — Not Playing — consecutive failures: **18** — HTTP 404
- **Captain** — Not Playing — consecutive failures: **38** — HTTP 404
- **Colors Bangla** — Not Playing — consecutive failures: **18** — Connection
- **Colors Bangla Cinema** — Not Playing — consecutive failures: **35** — HTTP 403
- **Colors Infinity** — Not Playing — consecutive failures: **35** — HTTP 403
- **Colors Rishtey** — Not Playing — consecutive failures: **18** — Connection
- **Dhamaal** — Not Playing — consecutive failures: **38** — HTTP 404
- **Disney Channel (India)** — Not Playing — consecutive failures: **38** — Timeout
- **Disney International** — Not Playing — consecutive failures: **35** — HTTP 403
- **Disney Junior (India)** — Not Playing — consecutive failures: **35** — HTTP 403
- **ETV Plus** — Not Playing — consecutive failures: **38** — DNS
- **MBC TV** — Not Playing — consecutive failures: **35** — HTTP 404
- **MTV2** — Not Playing — consecutive failures: **18** — Timeout
- **Nick Jr (India)** — Not Playing — consecutive failures: **35** — Timeout
- **Nickelodeon (India)** — Not Playing — consecutive failures: **38** — Timeout
- **Punjabi Beats** — Not Playing — consecutive failures: **26** — HTTP 404
- **Shekinah TV** — Not Playing — consecutive failures: **35** — TLS
- **Shemaroo Filmi Gaane** — Not Playing — consecutive failures: **35** — HTTP 403
- **Sonic** — Not Playing — consecutive failures: **24** — Timeout
- **Sony BBC Earth** — Not Playing — consecutive failures: **24** — Timeout
- **Sony Max 2** — Not Playing — consecutive failures: **13** — HTTP 404
- **Sony Pix** — Not Playing — consecutive failures: **13** — HTTP 404
- **Sony Sports Ten 1** — Not Playing — consecutive failures: **24** — HTTP 403
- **Sony Sports Ten 2** — Not Playing — consecutive failures: **24** — HTTP 403
- **Sony Sports Ten 3 Hindi** — Not Playing — consecutive failures: **24** — HTTP 403
- **Sony Sports Ten 4 Kannada** — Not Playing — consecutive failures: **24** — HTTP 403
- **Sony Sports Ten 5** — Not Playing — consecutive failures: **24** — HTTP 403
- **Star Gold** — Not Playing — consecutive failures: **24** — Timeout
- **Star Gold 2** — Not Playing — consecutive failures: **24** — HTTP 403
- **Star Kiran** — Not Playing — consecutive failures: **24** — HTTP 403
- **Star Plus** — Not Playing — consecutive failures: **24** — Timeout
- **Star Sports 3** — Not Playing — consecutive failures: **24** — HTTP 403
- **Star Sports Select 2** — Not Playing — consecutive failures: **24** — HTTP 403
- **Superhitz** — Not Playing — consecutive failures: **24** — HTTP 403
- **Ten Cricket** — Not Playing — consecutive failures: **24** — HTTP 403
- **Travelxp** — Not Playing — consecutive failures: **24** — HTTP 403
- **Unite8 Sports 2** — Not Playing — consecutive failures: **24** — HTTP 403
- **Zee Action** — Not Playing — consecutive failures: **3** — HTTP 404
- **Zee Bangla** — Not Playing — consecutive failures: **3** — HTTP 404
- **Zee Bangla Sonar** — Not Playing — consecutive failures: **14** — HTTP 404
- **Zee Cine Classic** — Not Playing — consecutive failures: **24** — HTTP 403
- **Zee Comedy Nation** — Not Playing — consecutive failures: **24** — HTTP 403
- **Zee Dil Se** — Not Playing — consecutive failures: **24** — HTTP 403
- **Zee Horror Nights** — Not Playing — consecutive failures: **24** — HTTP 403
- **Zee South Flix** — Not Playing — consecutive failures: **24** — HTTP 403
- **Star Sports 2** — Sports — consecutive failures: **62** — HTTP 403
- **TAPMAD** — Sports — consecutive failures: **14** — HTTP 403

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
| Songdew TV | Indian Music | yuppnimrestreammum.akamaized.net | hdnts |
| Colors Super | Indian Entertainment | d1rc86nwwc9fag.cloudfront.net | hdnts |
| Zee Kannada | Indian Entertainment | yuppnimresmum.akamaized.net | hdnts |
| Darshana TV | Backup | yuppparoriglin.akamaized.net | hdnts |
| Studio Yuva | Backup | d2gvyg6lvauoko.cloudfront.net | hdnts |
| WOW Kidz Hindi | Backup | yuppparoriglin.akamaized.net | hdnts |
| WOW Kidz Tamil | Backup | yuppparoriglin.akamaized.net | hdnts |
| WOW Kidz Telugu | Backup | yuppparoriglin.akamaized.net | hdnts |

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
