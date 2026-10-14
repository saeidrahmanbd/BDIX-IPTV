# Stream Health Report

Generated: **2026-10-14T04:27:54+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **901**
- Failed this check: **39**
- Persistent failures (3+ consecutive): **33**
- Intermittent failures: **6**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **4**
- HTTP 5xx (server): **9**
- Timeout: **22**
## Persistent Failures

- **Channel 1** — Backup — consecutive failures: **4** — Timeout
- **Channel 16** — Backup — consecutive failures: **10** — Timeout
- **Channel S** — Backup — consecutive failures: **4** — Timeout
- **Channel S** — Backup — consecutive failures: **4** — Timeout
- **Dangal 2** — Backup — consecutive failures: **8** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **8** — HTTP 403
- **Ekhon TV** — Backup — consecutive failures: **4** — Timeout
- **G TV** — Backup — consecutive failures: **4** — Timeout
- **G TV** — Backup — consecutive failures: **4** — Timeout
- **Goldmines Bollywood** — Backup — consecutive failures: **6** — HTTP 404
- **Goldmines Movies** — Backup — consecutive failures: **10** — HTTP 404
- **Movie Bangla** — Backup — consecutive failures: **4** — Timeout
- **Movie Bangla** — Backup — consecutive failures: **4** — Timeout
- **My TV** — Backup — consecutive failures: **4** — Timeout
- **RTV** — Backup — consecutive failures: **4** — Timeout
- **SA TV** — Backup — consecutive failures: **4** — Timeout
- **SA TV** — Backup — consecutive failures: **4** — Timeout
- **Ananda TV** — Bangladesh — consecutive failures: **5** — Timeout
- **Green TV** — Bangladesh — consecutive failures: **4** — Timeout
- **Assam Talks** — Indian Entertainment — consecutive failures: **142** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **37** — HTTP 503
- **AXN CEE** — International — consecutive failures: **37** — HTTP 503
- **FilmBox** — International — consecutive failures: **10** — Timeout
- **HBO** — International — consecutive failures: **130** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **37** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **37** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **37** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **37** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **334** — Timeout
- **Minimax** — Kids — consecutive failures: **37** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **8** — HTTP 403
- **Islamic TV** — Religious — consecutive failures: **4** — Timeout
- **Makkah Live** — Religious — consecutive failures: **4** — Timeout

## Failed This Check

- **Channel 1** — Backup — streak 4 — Timeout
- **Channel 16** — Backup — streak 10 — Timeout
- **Channel S** — Backup — streak 4 — Timeout
- **Channel S** — Backup — streak 4 — Timeout
- **Colors Bangla** — Backup — streak 2 — Timeout
- **Dangal 2** — Backup — streak 8 — HTTP 404
- **Disney Channel India** — Backup — streak 8 — HTTP 403
- **Ekhon TV** — Backup — streak 4 — Timeout
- **G TV** — Backup — streak 4 — Timeout
- **G TV** — Backup — streak 4 — Timeout
- **Goldmines Bollywood** — Backup — streak 6 — HTTP 404
- **Goldmines Movies** — Backup — streak 10 — HTTP 404
- **Green TV** — Backup — streak 1 — HTTP 500
- **Movie Bangla** — Backup — streak 4 — Timeout
- **Movie Bangla** — Backup — streak 4 — Timeout
- **My TV** — Backup — streak 4 — Timeout
- **RTV** — Backup — streak 4 — Timeout
- **SA TV** — Backup — streak 4 — Timeout
- **SA TV** — Backup — streak 4 — Timeout
- **Shemaroo TV** — Backup — streak 2 — HTTP 404
- **Ananda TV** — Bangladesh — streak 5 — Timeout
- **Green TV** — Bangladesh — streak 4 — Timeout
- **Colors Bangla Cinema** — Indian Bangla — streak 2 — Timeout
- **Assam Talks** — Indian Entertainment — streak 142 — HTTP 403
- **Sooriyan TV** — Indian Entertainment — streak 1 — HTTP 502
- **Star Plus** — Indian Entertainment — streak 2 — Timeout
- **AXN Black Czech Republic** — International — streak 37 — HTTP 503
- **AXN CEE** — International — streak 37 — HTTP 503
- **FilmBox** — International — streak 10 — Timeout
- **HBO** — International — streak 130 — HTTP 403
- **Music Box Classic** — International — streak 37 — HTTP 503
- **Music Box Dance** — International — streak 37 — HTTP 503
- **Music Box Hits** — International — streak 37 — HTTP 503
- **Music Box Sexy** — International — streak 37 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 334 — Timeout
- **Minimax** — Kids — streak 37 — HTTP 503
- **Teen Nick** — Kids — streak 8 — HTTP 403
- **Islamic TV** — Religious — streak 4 — Timeout
- **Makkah Live** — Religious — streak 4 — Timeout

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
