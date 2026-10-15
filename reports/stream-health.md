# Stream Health Report

Generated: **2026-10-15T07:19:19+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1043**
- Reachable: **1023**
- Failed this check: **20**
- Persistent failures (3+ consecutive): **9**
- Intermittent failures: **11**
- Primary tested: **635**
- Backup tested: **408**

## Failure Classification

- HTTP 401/403 (auth): **6**
- HTTP 404 (not found): **8**
- HTTP 5xx (server): **3**
- TLS: **1**
- Timeout: **2**
## Persistent Failures

- **Disney Channel India** — Backup — consecutive failures: **66** — HTTP 403
- **Goldmines** — Backup — consecutive failures: **6** — HTTP 404
- **Goldmines** — Backup — consecutive failures: **6** — HTTP 404
- **Shanson TV** — Backup — consecutive failures: **6** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **200** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **6** — HTTP 504
- **HBO** — International — consecutive failures: **188** — HTTP 403
- **Teleritmo** — International — consecutive failures: **6** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **66** — HTTP 403

## Failed This Check

- **Channel 16** — Backup — streak 2 — HTTP 404
- **Dangal** — Backup — streak 2 — HTTP 404
- **Dangal 2** — Backup — streak 2 — HTTP 404
- **Dangal 2** — Backup — streak 2 — HTTP 404
- **Disney Channel India** — Backup — streak 66 — HTTP 403
- **G TV** — Backup — streak 1 — HTTP 500
- **G TV** — Backup — streak 1 — TLS
- **Goldmines** — Backup — streak 6 — HTTP 404
- **Goldmines** — Backup — streak 6 — HTTP 404
- **Goldmines Movies** — Backup — streak 2 — HTTP 404
- **Manoranjan TV** — Backup — streak 2 — HTTP 404
- **Shanson TV** — Backup — streak 6 — HTTP 403
- **Assam Talks** — Indian Entertainment — streak 200 — HTTP 403
- **Kalaignar Murasu** — Indian Entertainment — streak 2 — HTTP 504
- **Cook & Bake** — International — streak 6 — HTTP 504
- **HBO** — International — streak 188 — HTTP 403
- **Teleritmo** — International — streak 6 — HTTP 403
- **Teen Nick** — Kids — streak 66 — HTTP 403
- **FOX Cricket 501** — Sports — streak 2 — Timeout
- **Ten Sports** — Sports — streak 2 — Timeout

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
