# Stream Health Report

Generated: **2026-10-15T08:24:19+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1043**
- Reachable: **1021**
- Failed this check: **22**
- Persistent failures (3+ consecutive): **11**
- Intermittent failures: **11**
- Primary tested: **635**
- Backup tested: **408**

## Failure Classification

- HTTP 401/403 (auth): **5**
- HTTP 404 (not found): **13**
- HTTP 5xx (server): **3**
- TLS: **1**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **8** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **8** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **8** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **72** — HTTP 403
- **Kalaignar Murasu** — Backup — consecutive failures: **6** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **206** — HTTP 403
- **Kalaignar Murasu** — Indian Entertainment — consecutive failures: **8** — HTTP 504
- **Cook & Bake** — International — consecutive failures: **12** — HTTP 504
- **HBO** — International — consecutive failures: **194** — HTTP 403
- **Teleritmo** — International — consecutive failures: **12** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **72** — HTTP 403

## Failed This Check

- **Channel 16** — Backup — streak 8 — HTTP 404
- **Dangal 2** — Backup — streak 8 — HTTP 404
- **Dangal 2** — Backup — streak 8 — HTTP 404
- **Disney Channel India** — Backup — streak 72 — HTTP 403
- **G TV** — Backup — streak 2 — TLS
- **Goldmines Movies** — Backup — streak 2 — HTTP 404
- **Kalaignar Murasu** — Backup — streak 6 — HTTP 404
- **Movies Now** — Backup — streak 2 — HTTP 404
- **Star Movies Select** — Backup — streak 2 — HTTP 404
- **Jalsha Movies HD** — Indian Bangla — streak 1 — HTTP 404
- **Zee Bangla** — Indian Bangla — streak 2 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 206 — HTTP 403
- **Colors Infinity** — Indian Entertainment — streak 2 — HTTP 404
- **Kalaignar Murasu** — Indian Entertainment — streak 8 — HTTP 504
- **Sooriyan TV** — Indian Entertainment — streak 1 — HTTP 502
- **Movies Now** — Indian Movies — streak 2 — HTTP 404
- **Star Gold 2** — Indian Movies — streak 1 — HTTP 404
- **Star Movies Select** — Indian Movies — streak 2 — HTTP 404
- **Cook & Bake** — International — streak 12 — HTTP 504
- **HBO** — International — streak 194 — HTTP 403
- **Teleritmo** — International — streak 12 — HTTP 403
- **Teen Nick** — Kids — streak 72 — HTTP 403

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
