# Stream Health Report

Generated: **2026-10-15T08:38:31+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1035**
- Reachable: **1008**
- Failed this check: **27**
- Persistent failures (3+ consecutive): **11**
- Intermittent failures: **16**
- Primary tested: **632**
- Backup tested: **403**

## Failure Classification

- HTTP 401/403 (auth): **5**
- HTTP 404 (not found): **7**
- HTTP 5xx (server): **4**
- TLS: **1**
- Timeout: **10**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **9** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **73** — HTTP 403
- **G TV** — Backup — consecutive failures: **3** — TLS
- **Goldmines Movies** — Backup — consecutive failures: **3** — HTTP 404
- **Kalaignar Murasu** — Backup — consecutive failures: **7** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **207** — HTTP 403
- **Kalaignar Murasu** — Indian Entertainment — consecutive failures: **9** — HTTP 504
- **Cook & Bake** — International — consecutive failures: **13** — HTTP 504
- **HBO** — International — consecutive failures: **195** — HTTP 403
- **Teleritmo** — International — consecutive failures: **13** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **73** — HTTP 403

## Failed This Check

- **ATN Bangla** — Backup — streak 1 — Timeout
- **Aakaash Aath** — Backup — streak 1 — Timeout
- **Ananda TV** — Backup — streak 1 — HTTP 500
- **Ananda TV** — Backup — streak 1 — HTTP 404
- **Channel 16** — Backup — streak 9 — HTTP 404
- **Dangal** — Backup — streak 1 — HTTP 404
- **Disney Channel India** — Backup — streak 73 — HTTP 403
- **Duronto TV** — Backup — streak 1 — Timeout
- **G TV** — Backup — streak 3 — TLS
- **Goldmines** — Backup — streak 1 — HTTP 404
- **Goldmines** — Backup — streak 1 — HTTP 404
- **Goldmines Movies** — Backup — streak 3 — HTTP 404
- **Kalaignar Murasu** — Backup — streak 7 — HTTP 404
- **Maasranga TV** — Backup — streak 1 — Timeout
- **Maasranga TV** — Backup — streak 1 — Timeout
- **Maasranga TV** — Backup — streak 2 — Timeout
- **RTV** — Backup — streak 1 — Timeout
- **Somoy TV** — Backup — streak 1 — Timeout
- **Assam Talks** — Indian Entertainment — streak 207 — HTTP 403
- **Kalaignar Murasu** — Indian Entertainment — streak 9 — HTTP 504
- **Oli TV** — Indian Entertainment — streak 1 — Timeout
- **Suriyan TV** — Indian Entertainment — streak 1 — HTTP 523
- **Cook & Bake** — International — streak 13 — HTTP 504
- **HBO** — International — streak 195 — HTTP 403
- **Teleritmo** — International — streak 13 — HTTP 403
- **Teen Nick** — Kids — streak 73 — HTTP 403
- **Astro Cricbuzz** — Sports — streak 1 — Timeout

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
