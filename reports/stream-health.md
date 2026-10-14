# Stream Health Report

Generated: **2026-10-14T06:30:16+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **922**
- Failed this check: **18**
- Persistent failures (3+ consecutive): **14**
- Intermittent failures: **4**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **4**
- HTTP 5xx (server): **7**
- Timeout: **3**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **28** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **26** — HTTP 403
- **Goldmines Bollywood** — Backup — consecutive failures: **6** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **160** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **55** — HTTP 503
- **AXN CEE** — International — consecutive failures: **55** — HTTP 503
- **HBO** — International — consecutive failures: **148** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **55** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **55** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **55** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **55** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **352** — Timeout
- **Minimax** — Kids — consecutive failures: **55** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **26** — HTTP 403

## Failed This Check

- **Balle Balle** — Backup — streak 2 — HTTP 404
- **Channel 16** — Backup — streak 28 — HTTP 404
- **Disney Channel India** — Backup — streak 26 — HTTP 403
- **Goldmines Bollywood** — Backup — streak 6 — HTTP 404
- **Goldmines Movies** — Backup — streak 1 — HTTP 404
- **Thikana** — Backup — streak 1 — Timeout
- **Assam Talks** — Indian Entertainment — streak 160 — HTTP 403
- **AXN Black Czech Republic** — International — streak 55 — HTTP 503
- **AXN CEE** — International — streak 55 — HTTP 503
- **FilmBox** — International — streak 2 — Timeout
- **HBO** — International — streak 148 — HTTP 403
- **Music Box Classic** — International — streak 55 — HTTP 503
- **Music Box Dance** — International — streak 55 — HTTP 503
- **Music Box Hits** — International — streak 55 — HTTP 503
- **Music Box Sexy** — International — streak 55 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 352 — Timeout
- **Minimax** — Kids — streak 55 — HTTP 503
- **Teen Nick** — Kids — streak 26 — HTTP 403

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
