# Stream Risk Review

Generated: **2026-11-02T10:02:07+00:00**
IPTV-Playlist.m3u SHA-256: **c83a2db794504997f9441df2faae73c5ea42a78b7bf4e7bd8f4e3c1d397f5454**

Generated from the current playlist and latest available stream-health report. This review is non-destructive; no stream URL was changed or deleted.

## Summary

- /streamtest/ endpoints: **9**
- Signed/token-query endpoints: **9**
- Xtream-style credential paths (credentials redacted): **0**
- Proxy/worker-host routes: **40** (2 primary, 38 Backup)
- /api/play/ relay routes: **0**

## Latest Stream-Health Snapshot

| Metric | Count |
|---|---:|
| Streams tested | 1066 |
| Reachable | 998 |
| Failed this check | 68 |
| Persistent failures (3+ consecutive) | 21 |
| HTTP 404 (not found) | 10 |
| HTTP 5xx (server) | 2 |
| Timeout | 5 |

### Persistent failures

- **Sun Surya** — Indian Entertainment — consecutive failures: **11** — HTTP 403
- **Sun TV** — Indian Entertainment — consecutive failures: **11** — HTTP 403
- **All Time Movies** — Indian Movies — consecutive failures: **4** — HTTP 404
- **Cook & Bake** — International — consecutive failures: **62** — HTTP 504
- **Lifetime** — International — consecutive failures: **38** — HTTP 403
- **Teleritmo** — International — consecutive failures: **62** — HTTP 403
- **Captain** — New Channels — consecutive failures: **14** — HTTP 404
- **Colors Bangla Cinema** — New Channels — consecutive failures: **11** — HTTP 403
- **Colors Infinity** — New Channels — consecutive failures: **11** — HTTP 403
- **Dhamaal** — New Channels — consecutive failures: **14** — HTTP 404
- **Disney Channel (India)** — New Channels — consecutive failures: **14** — Timeout
- **Disney International** — New Channels — consecutive failures: **11** — HTTP 403
- **Disney Junior (India)** — New Channels — consecutive failures: **11** — HTTP 403
- **ETV Plus** — New Channels — consecutive failures: **14** — DNS
- **MBC TV** — New Channels — consecutive failures: **11** — HTTP 404
- **Nick Jr (India)** — New Channels — consecutive failures: **11** — Timeout
- **Nickelodeon (India)** — New Channels — consecutive failures: **14** — Timeout
- **Shekinah TV** — New Channels — consecutive failures: **11** — TLS
- **Shemaroo Filmi Gaane** — New Channels — consecutive failures: **11** — HTTP 403
- **Vokta TV** — New Channels — consecutive failures: **14** — HTTP 403
- **Star Sports 2** — Sports — consecutive failures: **38** — HTTP 403

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
| Songdew TV | Indian Music | yuppnimrestreammum.akamaized.net | hdnts |
| Colors Super | Indian Entertainment | d1rc86nwwc9fag.cloudfront.net | hdnts |
| Darshana TV | Indian Entertainment | yuppparoriglin.akamaized.net | hdnts |
| Zee Kannada | Indian Entertainment | yuppnimresmum.akamaized.net | hdnts |
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
