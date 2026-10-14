# Stream Health Report

Generated: **2026-10-14T05:48:42+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **918**
- Failed this check: **22**
- Persistent failures (3+ consecutive): **14**
- Intermittent failures: **8**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **1**
- HTTP 5xx (server): **11**
- TLS: **2**
- Timeout: **4**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **22** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **20** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **154** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **49** — HTTP 503
- **AXN CEE** — International — consecutive failures: **49** — HTTP 503
- **FilmBox** — International — consecutive failures: **4** — Timeout
- **HBO** — International — consecutive failures: **142** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **49** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **49** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **49** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **49** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **346** — Timeout
- **Minimax** — Kids — consecutive failures: **49** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **20** — HTTP 403

## Failed This Check

- **Channel 16** — Backup — streak 22 — HTTP 404
- **Disney Channel India** — Backup — streak 20 — HTTP 403
- **G TV** — Backup — streak 1 — HTTP 500
- **G TV** — Backup — streak 1 — HTTP 500
- **Movie Bangla** — Backup — streak 1 — HTTP 500
- **Movie Bangla** — Backup — streak 1 — HTTP 500
- **Anand TV** — Indian Entertainment — streak 1 — TLS
- **Assam Talks** — Indian Entertainment — streak 154 — HTTP 403
- **Mei Alai TV** — Indian Entertainment — streak 2 — Timeout
- **AXN Black Czech Republic** — International — streak 49 — HTTP 503
- **AXN CEE** — International — streak 49 — HTTP 503
- **FON Music** — International — streak 1 — TLS
- **FilmBox** — International — streak 4 — Timeout
- **HBO** — International — streak 142 — HTTP 403
- **Music Box Classic** — International — streak 49 — HTTP 503
- **Music Box Dance** — International — streak 49 — HTTP 503
- **Music Box Hits** — International — streak 49 — HTTP 503
- **Music Box Sexy** — International — streak 49 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 346 — Timeout
- **Minimax** — Kids — streak 49 — HTTP 503
- **Teen Nick** — Kids — streak 20 — HTTP 403
- **Sony Sports Ten 3** — Sports — streak 2 — Timeout

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
