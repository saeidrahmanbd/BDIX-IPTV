# Stream Health Report

Generated: **2026-10-15T09:13:00+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1037**
- Reachable: **1017**
- Failed this check: **20**
- Persistent failures (3+ consecutive): **9**
- Intermittent failures: **11**
- Primary tested: **652**
- Backup tested: **385**

## Failure Classification

- HTTP 401/403 (auth): **6**
- HTTP 404 (not found): **8**
- HTTP 5xx (server): **5**
- Timeout: **1**
## Persistent Failures

- **Disney Channel India** — Backup — consecutive failures: **74** — HTTP 403
- **Kalaignar Murasu** — Backup — consecutive failures: **8** — HTTP 404
- **Channel 16** — Bangladesh — consecutive failures: **10** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **208** — HTTP 403
- **Kalaignar Murasu** — Indian Entertainment — consecutive failures: **10** — HTTP 504
- **Cook & Bake** — International — consecutive failures: **14** — HTTP 504
- **HBO** — International — consecutive failures: **196** — HTTP 403
- **Teleritmo** — International — consecutive failures: **14** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **74** — HTTP 403

## Failed This Check

- **Ananda TV** — Backup — streak 2 — HTTP 404
- **Dangal 2** — Backup — streak 1 — HTTP 404
- **Dangal 2** — Backup — streak 1 — HTTP 404
- **Disney Channel India** — Backup — streak 74 — HTTP 403
- **Goldmines** — Backup — streak 2 — HTTP 404
- **Goldmines** — Backup — streak 2 — HTTP 404
- **Kalaignar Murasu** — Backup — streak 8 — HTTP 404
- **Manoranjan TV** — Backup — streak 1 — HTTP 404
- **Shanson TV** — Backup — streak 1 — HTTP 403
- **Ananda TV** — Bangladesh — streak 1 — HTTP 500
- **Channel 16** — Bangladesh — streak 10 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 208 — HTTP 403
- **Kalaignar Murasu** — Indian Entertainment — streak 10 — HTTP 504
- **Oli TV** — Indian Entertainment — streak 2 — Timeout
- **Punjabi Shorts** — Indian Entertainment — streak 1 — HTTP 504
- **Suriyan TV** — Indian Entertainment — streak 2 — HTTP 523
- **Cook & Bake** — International — streak 14 — HTTP 504
- **HBO** — International — streak 196 — HTTP 403
- **Teleritmo** — International — streak 14 — HTTP 403
- **Teen Nick** — Kids — streak 74 — HTTP 403

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
