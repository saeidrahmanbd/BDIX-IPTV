# Stream Health Report

Generated: **2026-10-14T04:21:56+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **904**
- Failed this check: **36**
- Persistent failures (3+ consecutive): **18**
- Intermittent failures: **18**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **4**
- HTTP 5xx (server): **9**
- Timeout: **19**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **8** — Timeout
- **Dangal 2** — Backup — consecutive failures: **6** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **6** — HTTP 403
- **Goldmines Bollywood** — Backup — consecutive failures: **4** — HTTP 404
- **Goldmines Movies** — Backup — consecutive failures: **8** — HTTP 404
- **Ananda TV** — Bangladesh — consecutive failures: **3** — Timeout
- **Assam Talks** — Indian Entertainment — consecutive failures: **140** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **35** — HTTP 503
- **AXN CEE** — International — consecutive failures: **35** — HTTP 503
- **FilmBox** — International — consecutive failures: **8** — Timeout
- **HBO** — International — consecutive failures: **128** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **35** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **35** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **35** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **35** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **332** — Timeout
- **Minimax** — Kids — consecutive failures: **35** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **6** — HTTP 403

## Failed This Check

- **Channel 1** — Backup — streak 2 — Timeout
- **Channel 16** — Backup — streak 8 — Timeout
- **Channel S** — Backup — streak 2 — Timeout
- **Channel S** — Backup — streak 2 — Timeout
- **Dangal 2** — Backup — streak 6 — HTTP 404
- **Disney Channel India** — Backup — streak 6 — HTTP 403
- **Ekhon TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **Goldmines Bollywood** — Backup — streak 4 — HTTP 404
- **Goldmines Movies** — Backup — streak 8 — HTTP 404
- **Movie Bangla** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 2 — Timeout
- **RTV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **Sony Aath** — Backup — streak 1 — HTTP 404
- **Ananda TV** — Bangladesh — streak 3 — Timeout
- **Green TV** — Bangladesh — streak 2 — Timeout
- **Assam Talks** — Indian Entertainment — streak 140 — HTTP 403
- **AXN Black Czech Republic** — International — streak 35 — HTTP 503
- **AXN CEE** — International — streak 35 — HTTP 503
- **FilmBox** — International — streak 8 — Timeout
- **HBO** — International — streak 128 — HTTP 403
- **Music Box Classic** — International — streak 35 — HTTP 503
- **Music Box Dance** — International — streak 35 — HTTP 503
- **Music Box Hits** — International — streak 35 — HTTP 503
- **Music Box Sexy** — International — streak 35 — HTTP 503
- **Doraemon TV** — Kids — streak 1 — HTTP 502
- **ETV Bal Bharat** — Kids — streak 332 — Timeout
- **Minimax** — Kids — streak 35 — HTTP 503
- **Motu Patlu** — Kids — streak 1 — HTTP 502
- **Teen Nick** — Kids — streak 6 — HTTP 403
- **Islamic TV** — Religious — streak 2 — Timeout
- **Makkah Live** — Religious — streak 2 — Timeout

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
