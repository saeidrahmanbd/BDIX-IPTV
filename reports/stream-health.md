# Stream Health Report

Generated: **2026-10-14T12:16:12+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **917**
- Failed this check: **23**
- Persistent failures (3+ consecutive): **15**
- Intermittent failures: **8**
- Primary tested: **593**
- Backup tested: **347**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **8**
- HTTP 4xx (other): **1**
- HTTP 5xx (server): **8**
- Timeout: **2**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **50** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **48** — HTTP 403
- **Deepto TV** — Bangladesh — consecutive failures: **18** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **182** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **77** — HTTP 503
- **AXN CEE** — International — consecutive failures: **77** — HTTP 503
- **FilmBox** — International — consecutive failures: **12** — Timeout
- **HBO** — International — consecutive failures: **170** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **77** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **77** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **77** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **77** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **374** — Timeout
- **Minimax** — Kids — consecutive failures: **77** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **48** — HTTP 403

## Failed This Check

- **Channel 16** — Backup — streak 50 — HTTP 404
- **Channel S** — Backup — streak 1 — HTTP 500
- **Colors Bangla Cinema** — Backup — streak 2 — HTTP 404
- **Dangal 2** — Backup — streak 2 — HTTP 404
- **Disney Channel India** — Backup — streak 48 — HTTP 403
- **Shemaroo TV** — Backup — streak 2 — HTTP 404
- **Deepto TV** — Bangladesh — streak 18 — HTTP 404
- **Bangla Cinema** — Indian Bangla — streak 2 — HTTP 404
- **Star Bangla** — Indian Bangla — streak 2 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 182 — HTTP 403
- **AXN Black Czech Republic** — International — streak 77 — HTTP 503
- **AXN CEE** — International — streak 77 — HTTP 503
- **FilmBox** — International — streak 12 — Timeout
- **HBO** — International — streak 170 — HTTP 403
- **Music Box Classic** — International — streak 77 — HTTP 503
- **Music Box Dance** — International — streak 77 — HTTP 503
- **Music Box Hits** — International — streak 77 — HTTP 503
- **Music Box Sexy** — International — streak 77 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 374 — Timeout
- **Minimax** — Kids — streak 77 — HTTP 503
- **Sonic Bangla** — Kids — streak 2 — HTTP 429
- **Teen Nick** — Kids — streak 48 — HTTP 403
- **Peace TV Bangla** — Religious — streak 2 — HTTP 404

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
