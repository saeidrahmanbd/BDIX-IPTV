# Stream Health Report

Generated: **2026-10-15T09:37:04+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1037**
- Reachable: **1009**
- Failed this check: **28**
- Persistent failures (3+ consecutive): **11**
- Intermittent failures: **17**
- Primary tested: **652**
- Backup tested: **385**

## Failure Classification

- HTTP 401/403 (auth): **6**
- HTTP 404 (not found): **11**
- HTTP 5xx (server): **5**
- TLS: **1**
- Timeout: **5**
## Persistent Failures

- **Ananda TV** — Backup — consecutive failures: **4** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **76** — HTTP 403
- **Shanson TV** — Backup — consecutive failures: **3** — HTTP 403
- **Channel 16** — Bangladesh — consecutive failures: **12** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **210** — HTTP 403
- **Oli TV** — Indian Entertainment — consecutive failures: **4** — Timeout
- **Suriyan TV** — Indian Entertainment — consecutive failures: **4** — HTTP 523
- **Cook & Bake** — International — consecutive failures: **16** — HTTP 504
- **HBO** — International — consecutive failures: **198** — HTTP 403
- **Teleritmo** — International — consecutive failures: **16** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **76** — HTTP 403

## Failed This Check

- **Ananda TV** — Backup — streak 4 — HTTP 404
- **Disney Channel India** — Backup — streak 76 — HTTP 403
- **Duronto TV** — Backup — streak 1 — Timeout
- **G TV** — Backup — streak 1 — TLS
- **Goldmines** — Backup — streak 1 — HTTP 404
- **Goldmines** — Backup — streak 1 — HTTP 404
- **Shanson TV** — Backup — streak 3 — HTTP 403
- **Star Jalsha** — Backup — streak 1 — HTTP 404
- **Star Jalsha** — Backup — streak 1 — HTTP 404
- **Star Movies Select** — Backup — streak 1 — HTTP 404
- **Channel 16** — Bangladesh — streak 12 — HTTP 404
- **Channel 9** — Bangladesh — streak 1 — HTTP 404
- **Nagorik TV** — Bangladesh — streak 1 — HTTP 404
- **Jalsha Movies** — Indian Bangla — streak 1 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 210 — HTTP 403
- **Flowers US** — Indian Entertainment — streak 1 — HTTP 504
- **Oli TV** — Indian Entertainment — streak 4 — Timeout
- **Suriyan TV** — Indian Entertainment — streak 4 — HTTP 523
- **K Cine** — Indian Movies — streak 1 — Timeout
- **South Movies** — Indian Movies — streak 1 — HTTP 502
- **Afrobeats** — International — streak 1 — HTTP 404
- **Cook & Bake** — International — streak 16 — HTTP 504
- **HBO** — International — streak 198 — HTTP 403
- **Teleritmo** — International — streak 16 — HTTP 403
- **Doraemon TV** — Kids — streak 2 — HTTP 502
- **Teen Nick** — Kids — streak 76 — HTTP 403
- **FOX Cricket 501** — Sports — streak 1 — Timeout
- **Ten Sports** — Sports — streak 1 — Timeout

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
