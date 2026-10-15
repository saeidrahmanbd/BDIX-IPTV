# Stream Health Report

Generated: **2026-10-15T09:22:14+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1037**
- Reachable: **1019**
- Failed this check: **18**
- Persistent failures (3+ consecutive): **10**
- Intermittent failures: **8**
- Primary tested: **652**
- Backup tested: **385**

## Failure Classification

- HTTP 401/403 (auth): **6**
- HTTP 404 (not found): **2**
- HTTP 5xx (server): **9**
- Timeout: **1**
## Persistent Failures

- **Ananda TV** — Backup — consecutive failures: **3** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **75** — HTTP 403
- **Channel 16** — Bangladesh — consecutive failures: **11** — HTTP 500
- **Assam Talks** — Indian Entertainment — consecutive failures: **209** — HTTP 403
- **Oli TV** — Indian Entertainment — consecutive failures: **3** — Timeout
- **Suriyan TV** — Indian Entertainment — consecutive failures: **3** — HTTP 523
- **Cook & Bake** — International — consecutive failures: **15** — HTTP 504
- **HBO** — International — consecutive failures: **197** — HTTP 403
- **Teleritmo** — International — consecutive failures: **15** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **75** — HTTP 403

## Failed This Check

- **Ananda TV** — Backup — streak 3 — HTTP 404
- **Disney Channel India** — Backup — streak 75 — HTTP 403
- **Manoranjan TV** — Backup — streak 2 — HTTP 404
- **Shanson TV** — Backup — streak 2 — HTTP 403
- **Ananda TV** — Bangladesh — streak 2 — HTTP 500
- **Channel 16** — Bangladesh — streak 11 — HTTP 500
- **Green TV** — Bangladesh — streak 1 — HTTP 500
- **Assam Talks** — Indian Entertainment — streak 209 — HTTP 403
- **Oli TV** — Indian Entertainment — streak 3 — Timeout
- **Suriyan TV** — Indian Entertainment — streak 3 — HTTP 523
- **Hindi Movies** — Indian Movies — streak 1 — HTTP 502
- **Cook & Bake** — International — streak 15 — HTTP 504
- **HBO** — International — streak 197 — HTTP 403
- **Teleritmo** — International — streak 15 — HTTP 403
- **Bantul the Great** — Kids — streak 1 — HTTP 502
- **Doraemon TV** — Kids — streak 1 — HTTP 502
- **Motu Patlu** — Kids — streak 1 — HTTP 502
- **Teen Nick** — Kids — streak 75 — HTTP 403

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
