# Stream Health Report

Generated: **2026-10-15T04:01:22+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **908**
- Failed this check: **32**
- Persistent failures (3+ consecutive): **15**
- Intermittent failures: **17**
- Primary tested: **593**
- Backup tested: **347**

## Failure Classification

- HTTP 401/403 (auth): **10**
- HTTP 404 (not found): **4**
- HTTP 4xx (other): **1**
- HTTP 5xx (server): **7**
- TLS: **1**
- Timeout: **9**
## Persistent Failures

- **Disney Channel India** — Backup — consecutive failures: **56** — HTTP 403
- **Goldmines Movies** — Backup — consecutive failures: **8** — HTTP 404
- **Nan TV** — Backup — consecutive failures: **4** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **190** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **85** — HTTP 503
- **AXN CEE** — International — consecutive failures: **85** — HTTP 503
- **FilmBox** — International — consecutive failures: **20** — Timeout
- **HBO** — International — consecutive failures: **178** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **85** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **85** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **85** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **85** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **382** — Timeout
- **Minimax** — Kids — consecutive failures: **85** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **56** — HTTP 403

## Failed This Check

- **Aakaash Aath** — Backup — streak 2 — Timeout
- **Desh TV** — Backup — streak 1 — HTTP 403
- **Disney Channel India** — Backup — streak 56 — HTTP 403
- **Goldmines Movies** — Backup — streak 8 — HTTP 404
- **Maasranga TV** — Backup — streak 2 — Timeout
- **Maasranga TV** — Backup — streak 2 — Timeout
- **Maasranga TV** — Backup — streak 2 — Timeout
- **Nan TV** — Backup — streak 4 — HTTP 404
- **Nexus TV** — Backup — streak 1 — HTTP 403
- **Shemaroo Josh** — Backup — streak 2 — HTTP 404
- **Shemaroo TV** — Backup — streak 2 — HTTP 404
- **Somoy TV** — Backup — streak 2 — Timeout
- **Sony Max** — Backup — streak 1 — HTTP 403
- **Zee Action** — Backup — streak 1 — HTTP 403
- **Zee Bangla Cinema** — Backup — streak 1 — HTTP 403
- **Zee Bollywood** — Backup — streak 1 — HTTP 403
- **ATN Bangla** — Bangladesh — streak 2 — Timeout
- **RTV** — Bangladesh — streak 2 — Timeout
- **Assam Talks** — Indian Entertainment — streak 190 — HTTP 403
- **AXN Black Czech Republic** — International — streak 85 — HTTP 503
- **AXN CEE** — International — streak 85 — HTTP 503
- **FON Music** — International — streak 1 — TLS
- **FilmBox** — International — streak 20 — Timeout
- **HBO** — International — streak 178 — HTTP 403
- **Music Box Classic** — International — streak 85 — HTTP 503
- **Music Box Dance** — International — streak 85 — HTTP 503
- **Music Box Hits** — International — streak 85 — HTTP 503
- **Music Box Sexy** — International — streak 85 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 382 — Timeout
- **Minimax** — Kids — streak 85 — HTTP 503
- **Sonic Bangla** — Kids — streak 2 — HTTP 429
- **Teen Nick** — Kids — streak 56 — HTTP 403

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
