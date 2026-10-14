# Stream Health Report

Generated: **2026-10-14T06:57:00+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **912**
- Failed this check: **28**
- Persistent failures (3+ consecutive): **14**
- Intermittent failures: **14**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **6**
- HTTP 5xx (server): **9**
- TLS: **1**
- Timeout: **8**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **30** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **28** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **162** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **57** — HTTP 503
- **AXN CEE** — International — consecutive failures: **57** — HTTP 503
- **FilmBox** — International — consecutive failures: **4** — Timeout
- **HBO** — International — consecutive failures: **150** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **57** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **57** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **57** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **57** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **354** — Timeout
- **Minimax** — Kids — consecutive failures: **57** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **28** — HTTP 403

## Failed This Check

- **BHI Channel** — Backup — streak 1 — Timeout
- **Channel 16** — Backup — streak 30 — HTTP 404
- **Disney Channel India** — Backup — streak 28 — HTTP 403
- **Duronto TV** — Backup — streak 2 — Timeout
- **RTV** — Backup — streak 1 — HTTP 500
- **SA TV** — Backup — streak 1 — HTTP 500
- **Shemaroo TV** — Backup — streak 2 — HTTP 404
- **Star Jalsha** — Backup — streak 1 — HTTP 404
- **Star Jalsha** — Backup — streak 1 — HTTP 404
- **Zee TV** — Backup — streak 1 — HTTP 404
- **Zee TV** — Backup — streak 1 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 162 — HTTP 403
- **Star Gold Thrills** — Indian Movies — streak 2 — Timeout
- **AXN Black Czech Republic** — International — streak 57 — HTTP 503
- **AXN CEE** — International — streak 57 — HTTP 503
- **FON Music** — International — streak 1 — TLS
- **FilmBox** — International — streak 4 — Timeout
- **HBO** — International — streak 150 — HTTP 403
- **Music Box Classic** — International — streak 57 — HTTP 503
- **Music Box Dance** — International — streak 57 — HTTP 503
- **Music Box Hits** — International — streak 57 — HTTP 503
- **Music Box Sexy** — International — streak 57 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 354 — Timeout
- **Minimax** — Kids — streak 57 — HTTP 503
- **Teen Nick** — Kids — streak 28 — HTTP 403
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
