# Stream Health Report

Generated: **2026-10-15T07:50:28+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1043**
- Reachable: **1024**
- Failed this check: **19**
- Persistent failures (3+ consecutive): **13**
- Intermittent failures: **6**
- Primary tested: **635**
- Backup tested: **408**

## Failure Classification

- HTTP 401/403 (auth): **6**
- HTTP 404 (not found): **6**
- HTTP 4xx (other): **1**
- HTTP 5xx (server): **6**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **4** — HTTP 404
- **Dangal** — Backup — consecutive failures: **4** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **4** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **4** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **68** — HTTP 403
- **Manoranjan TV** — Backup — consecutive failures: **4** — HTTP 404
- **Shanson TV** — Backup — consecutive failures: **8** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **202** — HTTP 403
- **Kalaignar Murasu** — Indian Entertainment — consecutive failures: **4** — HTTP 504
- **Cook & Bake** — International — consecutive failures: **8** — HTTP 504
- **HBO** — International — consecutive failures: **190** — HTTP 403
- **Teleritmo** — International — consecutive failures: **8** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **68** — HTTP 403

## Failed This Check

- **Channel 16** — Backup — streak 4 — HTTP 404
- **Channel S** — Backup — streak 1 — HTTP 500
- **Channel S** — Backup — streak 1 — HTTP 500
- **Dangal** — Backup — streak 4 — HTTP 404
- **Dangal 2** — Backup — streak 4 — HTTP 404
- **Dangal 2** — Backup — streak 4 — HTTP 404
- **Deewana** — Backup — streak 1 — HTTP 502
- **Disney Channel India** — Backup — streak 68 — HTTP 403
- **Kalaignar Murasu** — Backup — streak 2 — HTTP 404
- **Manoranjan TV** — Backup — streak 4 — HTTP 404
- **RTV** — Backup — streak 1 — HTTP 500
- **Shanson TV** — Backup — streak 8 — HTTP 403
- **Assam Talks** — Indian Entertainment — streak 202 — HTTP 403
- **Kalaignar Murasu** — Indian Entertainment — streak 4 — HTTP 504
- **Cook & Bake** — International — streak 8 — HTTP 504
- **HBO** — International — streak 190 — HTTP 403
- **Teleritmo** — International — streak 8 — HTTP 403
- **Sonic Bangla** — Kids — streak 1 — HTTP 429
- **Teen Nick** — Kids — streak 68 — HTTP 403

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
