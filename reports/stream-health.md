# Stream Health Report

Generated: **2026-10-14T05:37:02+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **917**
- Failed this check: **23**
- Persistent failures (3+ consecutive): **13**
- Intermittent failures: **10**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **2**
- HTTP 5xx (server): **10**
- Timeout: **7**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **20** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **18** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **152** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **47** — HTTP 503
- **AXN CEE** — International — consecutive failures: **47** — HTTP 503
- **HBO** — International — consecutive failures: **140** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **47** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **47** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **47** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **47** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **344** — Timeout
- **Minimax** — Kids — consecutive failures: **47** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **18** — HTTP 403

## Failed This Check

- **Ananda TV** — Backup — streak 1 — HTTP 404
- **Channel 1** — Backup — streak 1 — HTTP 500
- **Channel 16** — Backup — streak 20 — HTTP 404
- **Channel S** — Backup — streak 1 — HTTP 500
- **Disney Channel India** — Backup — streak 18 — HTTP 403
- **Duronto TV** — Backup — streak 2 — Timeout
- **Jago News 24** — Backup — streak 1 — HTTP 500
- **Assam Talks** — Indian Entertainment — streak 152 — HTTP 403
- **Star Gold Thrills** — Indian Movies — streak 2 — Timeout
- **AXN Black Czech Republic** — International — streak 47 — HTTP 503
- **AXN CEE** — International — streak 47 — HTTP 503
- **FilmBox** — International — streak 2 — Timeout
- **HBO** — International — streak 140 — HTTP 403
- **Music Box Classic** — International — streak 47 — HTTP 503
- **Music Box Dance** — International — streak 47 — HTTP 503
- **Music Box Hits** — International — streak 47 — HTTP 503
- **Music Box Sexy** — International — streak 47 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 344 — Timeout
- **Minimax** — Kids — streak 47 — HTTP 503
- **Teen Nick** — Kids — streak 18 — HTTP 403
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
