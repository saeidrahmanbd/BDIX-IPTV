# Stream Health Report

Generated: **2026-10-14T07:54:58+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **903**
- Failed this check: **37**
- Persistent failures (3+ consecutive): **15**
- Intermittent failures: **22**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **2**
- HTTP 5xx (server): **7**
- Timeout: **24**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **34** — Timeout
- **Disney Channel India** — Backup — consecutive failures: **32** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **166** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **61** — HTTP 503
- **AXN CEE** — International — consecutive failures: **61** — HTTP 503
- **FilmBox** — International — consecutive failures: **8** — Timeout
- **HBO** — International — consecutive failures: **154** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **61** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **61** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **61** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **61** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **358** — Timeout
- **Minimax** — Kids — consecutive failures: **61** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **32** — HTTP 403
- **Islamic TV** — Religious — consecutive failures: **3** — Timeout

## Failed This Check

- **Channel 1** — Backup — streak 2 — Timeout
- **Channel 16** — Backup — streak 34 — Timeout
- **Channel S** — Backup — streak 2 — Timeout
- **Channel S** — Backup — streak 2 — Timeout
- **Disney Channel India** — Backup — streak 32 — HTTP 403
- **Duronto TV** — Backup — streak 2 — Timeout
- **Ekhon TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 2 — Timeout
- **RTV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **Sony Entertainment TV** — Backup — streak 1 — HTTP 404
- **Ananda TV** — Bangladesh — streak 2 — Timeout
- **Deepto TV** — Bangladesh — streak 2 — HTTP 404
- **Green TV** — Bangladesh — streak 2 — Timeout
- **Assam Talks** — Indian Entertainment — streak 166 — HTTP 403
- **Star Gold Thrills** — Indian Movies — streak 2 — Timeout
- **AXN Black Czech Republic** — International — streak 61 — HTTP 503
- **AXN CEE** — International — streak 61 — HTTP 503
- **FilmBox** — International — streak 8 — Timeout
- **HBO** — International — streak 154 — HTTP 403
- **Music Box Classic** — International — streak 61 — HTTP 503
- **Music Box Dance** — International — streak 61 — HTTP 503
- **Music Box Hits** — International — streak 61 — HTTP 503
- **Music Box Sexy** — International — streak 61 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 358 — Timeout
- **Minimax** — Kids — streak 61 — HTTP 503
- **Teen Nick** — Kids — streak 32 — HTTP 403
- **Islamic TV** — Religious — streak 3 — Timeout
- **Makkah Live** — Religious — streak 2 — Timeout
- **FOX Cricket 501** — Sports — streak 2 — Timeout
- **Sony Sports Ten 3** — Sports — streak 2 — Timeout
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
