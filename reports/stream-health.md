# Stream Health Report

Generated: **2026-10-14T10:56:19+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **915**
- Failed this check: **25**
- Persistent failures (3+ consecutive): **16**
- Intermittent failures: **9**
- Primary tested: **593**
- Backup tested: **347**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **4**
- HTTP 5xx (server): **9**
- Other: **1**
- Timeout: **7**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **46** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **44** — HTTP 403
- **Deepto TV** — Bangladesh — consecutive failures: **14** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **178** — HTTP 403
- **MNTV (Tamil)** — Indian Entertainment — consecutive failures: **12** — HTTP 404
- **AXN Black Czech Republic** — International — consecutive failures: **73** — HTTP 503
- **AXN CEE** — International — consecutive failures: **73** — HTTP 503
- **FilmBox** — International — consecutive failures: **8** — Timeout
- **HBO** — International — consecutive failures: **166** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **73** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **73** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **73** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **73** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **370** — Timeout
- **Minimax** — Kids — consecutive failures: **73** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **44** — HTTP 403

## Failed This Check

- **Channel 16** — Backup — streak 46 — HTTP 404
- **Channel S** — Backup — streak 1 — HTTP 500
- **Disney Channel India** — Backup — streak 44 — HTTP 403
- **Duronto TV** — Backup — streak 2 — Timeout
- **Deepto TV** — Bangladesh — streak 14 — HTTP 404
- **Green TV** — Bangladesh — streak 1 — HTTP 500
- **Assam Talks** — Indian Entertainment — streak 178 — HTTP 403
- **MNTV (Tamil)** — Indian Entertainment — streak 12 — HTTP 404
- **Star Gold Thrills** — Indian Movies — streak 2 — Timeout
- **Raj Music Telugu** — Indian Music — streak 2 — HTTP 404
- **AXN Black Czech Republic** — International — streak 73 — HTTP 503
- **AXN CEE** — International — streak 73 — HTTP 503
- **FON Music** — International — streak 1 — Other
- **FilmBox** — International — streak 8 — Timeout
- **HBO** — International — streak 166 — HTTP 403
- **Music Box Classic** — International — streak 73 — HTTP 503
- **Music Box Dance** — International — streak 73 — HTTP 503
- **Music Box Hits** — International — streak 73 — HTTP 503
- **Music Box Sexy** — International — streak 73 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 370 — Timeout
- **Minimax** — Kids — streak 73 — HTTP 503
- **Teen Nick** — Kids — streak 44 — HTTP 403
- **Astro Cricbuzz** — Sports — streak 2 — Timeout
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
