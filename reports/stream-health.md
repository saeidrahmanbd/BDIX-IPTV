# Stream Health Report

Generated: **2026-10-15T08:14:20+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1043**
- Reachable: **1022**
- Failed this check: **21**
- Persistent failures (3+ consecutive): **13**
- Intermittent failures: **8**
- Primary tested: **635**
- Backup tested: **408**

## Failure Classification

- HTTP 401/403 (auth): **6**
- HTTP 404 (not found): **7**
- HTTP 5xx (server): **6**
- Timeout: **2**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **6** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **6** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **6** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **70** — HTTP 403
- **Kalaignar Murasu** — Backup — consecutive failures: **4** — HTTP 404
- **Manoranjan TV** — Backup — consecutive failures: **6** — HTTP 404
- **Shanson TV** — Backup — consecutive failures: **10** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **204** — HTTP 403
- **Kalaignar Murasu** — Indian Entertainment — consecutive failures: **6** — HTTP 504
- **Cook & Bake** — International — consecutive failures: **10** — HTTP 504
- **HBO** — International — consecutive failures: **192** — HTTP 403
- **Teleritmo** — International — consecutive failures: **10** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **70** — HTTP 403

## Failed This Check

- **Ananda TV** — Backup — streak 1 — HTTP 500
- **Balle Balle** — Backup — streak 1 — HTTP 404
- **Channel 16** — Backup — streak 6 — HTTP 404
- **Dangal** — Backup — streak 1 — HTTP 404
- **Dangal 2** — Backup — streak 6 — HTTP 404
- **Dangal 2** — Backup — streak 6 — HTTP 404
- **Disney Channel India** — Backup — streak 70 — HTTP 403
- **Jalwa TV** — Backup — streak 2 — Timeout
- **Kalaignar Murasu** — Backup — streak 4 — HTTP 404
- **Manoranjan TV** — Backup — streak 6 — HTTP 404
- **SA TV** — Backup — streak 1 — HTTP 500
- **Shanson TV** — Backup — streak 10 — HTTP 403
- **ATN Bangla UK** — Bangladesh — streak 1 — HTTP 500
- **Assam Talks** — Indian Entertainment — streak 204 — HTTP 403
- **Kalaignar Murasu** — Indian Entertainment — streak 6 — HTTP 504
- **Cook & Bake** — International — streak 10 — HTTP 504
- **HBO** — International — streak 192 — HTTP 403
- **Teleritmo** — International — streak 10 — HTTP 403
- **Teen Nick** — Kids — streak 70 — HTTP 403
- **Sony Sports Ten 3** — Sports — streak 2 — Timeout
- **talkSPORT** — Sports — streak 1 — HTTP 504

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
