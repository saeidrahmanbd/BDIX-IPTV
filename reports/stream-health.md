# Stream Health Report

Generated: **2026-10-15T06:33:48+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1043**
- Reachable: **1027**
- Failed this check: **16**
- Persistent failures (3+ consecutive): **10**
- Intermittent failures: **6**
- Primary tested: **634**
- Backup tested: **409**

## Failure Classification

- HTTP 401/403 (auth): **6**
- HTTP 404 (not found): **2**
- HTTP 5xx (server): **7**
- TLS: **1**
## Persistent Failures

- **Disney Channel India** — Backup — consecutive failures: **64** — HTTP 403
- **Goldmines** — Backup — consecutive failures: **4** — HTTP 404
- **Goldmines** — Backup — consecutive failures: **4** — HTTP 404
- **SA TV** — Backup — consecutive failures: **4** — HTTP 500
- **Shanson TV** — Backup — consecutive failures: **4** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **198** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **4** — HTTP 504
- **HBO** — International — consecutive failures: **186** — HTTP 403
- **Teleritmo** — International — consecutive failures: **4** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **64** — HTTP 403

## Failed This Check

- **Disney Channel India** — Backup — streak 64 — HTTP 403
- **Ekushey TV** — Backup — streak 1 — HTTP 500
- **G TV** — Backup — streak 1 — TLS
- **Goldmines** — Backup — streak 4 — HTTP 404
- **Goldmines** — Backup — streak 4 — HTTP 404
- **Medina Live** — Backup — streak 1 — HTTP 500
- **SA TV** — Backup — streak 1 — HTTP 500
- **SA TV** — Backup — streak 4 — HTTP 500
- **Shanson TV** — Backup — streak 4 — HTTP 403
- **Assam Talks** — Indian Entertainment — streak 198 — HTTP 403
- **Sooriyan TV** — Indian Entertainment — streak 2 — HTTP 502
- **Cook & Bake** — International — streak 4 — HTTP 504
- **HBO** — International — streak 186 — HTTP 403
- **Teleritmo** — International — streak 4 — HTTP 403
- **Teen Nick** — Kids — streak 64 — HTTP 403
- **Tom and Jerry** — Kids — streak 1 — HTTP 502

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
