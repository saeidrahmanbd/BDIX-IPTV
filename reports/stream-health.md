# Stream Health Report

Generated: **2026-10-21T05:17:07+00:00**
Stream URL inventory SHA-256: **b0b8b3b2c531ad715ad5aa7bb0155f8c88f4616da50e6b6b4361e88c9859930d**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1064**
- Reachable: **1023**
- Failed this check: **41**
- Persistent failures (3+ consecutive): **19**
- Intermittent failures: **22**
- Primary tested: **652**
- Backup tested: **412**

## Failure Classification

- DNS: **2**
- HTTP 401/403 (auth): **13**
- HTTP 404 (not found): **20**
- HTTP 5xx (server): **5**
- TLS: **1**
## Persistent Failures

- **Bahrain Sports 2** — Backup — consecutive failures: **3** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **12** — HTTP 403
- **ESPN** — Backup — consecutive failures: **12** — HTTP 403
- **Manoranjan TV** — Backup — consecutive failures: **4** — HTTP 404
- **Movie Bangla** — Backup — consecutive failures: **4** — HTTP 500
- **Shanson TV** — Backup — consecutive failures: **8** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **44** — HTTP 504
- **HBO** — International — consecutive failures: **226** — HTTP 403
- **Lifetime** — International — consecutive failures: **20** — HTTP 403
- **Teleritmo** — International — consecutive failures: **44** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **104** — HTTP 403
- **Assam Talks** — Not Playing — consecutive failures: **238** — HTTP 403
- **Desh TV** — Not Playing — consecutive failures: **15** — HTTP 404
- **G TV** — Not Playing — consecutive failures: **12** — TLS
- **Nick** — Not Playing — consecutive failures: **16** — HTTP 404
- **Star Gold** — Not Playing — consecutive failures: **16** — HTTP 404
- **Star Sports 2** — Sports — consecutive failures: **20** — HTTP 403
- **T Sports** — Sports — consecutive failures: **20** — HTTP 403
- **Willow TV** — Sports — consecutive failures: **20** — HTTP 403

## Failed This Check

- **BTV Chattogram** — Backup — streak 2 — HTTP 404
- **Bahrain Sports 2** — Backup — streak 3 — HTTP 404
- **Colors Cineplex [UK]** — Backup — streak 2 — HTTP 404
- **Dangal** — Backup — streak 2 — HTTP 404
- **Disney Channel India** — Backup — streak 12 — HTTP 403
- **ESPN** — Backup — streak 12 — HTTP 403
- **HBO** — Backup — streak 2 — HTTP 404
- **MBC Bollywood** — Backup — streak 2 — HTTP 403
- **Madani TV** — Backup — streak 2 — DNS
- **Manoranjan TV** — Backup — streak 4 — HTTP 404
- **Movie Bangla** — Backup — streak 4 — HTTP 500
- **Music India** — Backup — streak 2 — HTTP 500
- **Sangeet Bangla** — Backup — streak 2 — HTTP 500
- **Sangeet Bhojpuri** — Backup — streak 2 — HTTP 500
- **Shanson TV** — Backup — streak 8 — HTTP 403
- **BTV National** — Bangladesh — streak 2 — HTTP 404
- **Terra Mater WILD English** — Documentary & Wildlife — streak 2 — DNS
- **Bangla Plus** — Indian Bangla — streak 2 — HTTP 404
- **Manoranjan Grand** — Indian Entertainment — streak 2 — HTTP 404
- **Raj TV** — Indian Entertainment — streak 2 — HTTP 404
- **Star Bharat** — Indian Entertainment — streak 2 — HTTP 404
- **Star Utsav** — Indian Entertainment — streak 2 — HTTP 404
- **Bollywood Film** — Indian Movies — streak 2 — HTTP 403
- **Raj Digital Plus** — Indian Movies — streak 2 — HTTP 404
- **Star Gold Select** — Indian Movies — streak 2 — HTTP 404
- **Star Movies** — Indian Movies — streak 2 — HTTP 404
- **Star Utsav Movies** — Indian Movies — streak 2 — HTTP 404
- **Raj Musix Tamil** — Indian Music — streak 2 — HTTP 404
- **Cook & Bake** — International — streak 44 — HTTP 504
- **HBO** — International — streak 226 — HTTP 403
- **Lifetime** — International — streak 20 — HTTP 403
- **Teleritmo** — International — streak 44 — HTTP 403
- **Teen Nick** — Kids — streak 104 — HTTP 403
- **Assam Talks** — Not Playing — streak 238 — HTTP 403
- **Desh TV** — Not Playing — streak 15 — HTTP 404
- **G TV** — Not Playing — streak 12 — TLS
- **Nick** — Not Playing — streak 16 — HTTP 404
- **Star Gold** — Not Playing — streak 16 — HTTP 404
- **Star Sports 2** — Sports — streak 20 — HTTP 403
- **T Sports** — Sports — streak 20 — HTTP 403
- **Willow TV** — Sports — streak 20 — HTTP 403

## Near-Duplicate URL Families

- **https://cdn-globecast.akamaized.net/live/REDACTED/REDACTED/hls_roku/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://shd-gcp-live.edgenextcdn.net/live/REDACTED/REDACTED/index.m3u8** — 6 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
