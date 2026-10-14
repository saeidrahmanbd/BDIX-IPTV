# Stream Health Report

Generated: **2026-10-14T04:59:22+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **907**
- Failed this check: **33**
- Persistent failures (3+ consecutive): **32**
- Intermittent failures: **1**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **2**
- HTTP 5xx (server): **7**
- Timeout: **20**
## Persistent Failures

- **Channel 1** — Backup — consecutive failures: **10** — Timeout
- **Channel 16** — Backup — consecutive failures: **16** — Timeout
- **Channel S** — Backup — consecutive failures: **10** — Timeout
- **Channel S** — Backup — consecutive failures: **10** — Timeout
- **Disney Channel India** — Backup — consecutive failures: **14** — HTTP 403
- **Ekhon TV** — Backup — consecutive failures: **10** — Timeout
- **G TV** — Backup — consecutive failures: **10** — Timeout
- **G TV** — Backup — consecutive failures: **10** — Timeout
- **Goldmines Bollywood** — Backup — consecutive failures: **12** — HTTP 404
- **Goldmines Movies** — Backup — consecutive failures: **16** — HTTP 404
- **Movie Bangla** — Backup — consecutive failures: **10** — Timeout
- **Movie Bangla** — Backup — consecutive failures: **10** — Timeout
- **My TV** — Backup — consecutive failures: **10** — Timeout
- **RTV** — Backup — consecutive failures: **10** — Timeout
- **SA TV** — Backup — consecutive failures: **10** — Timeout
- **SA TV** — Backup — consecutive failures: **10** — Timeout
- **Ananda TV** — Bangladesh — consecutive failures: **11** — Timeout
- **Green TV** — Bangladesh — consecutive failures: **10** — Timeout
- **Assam Talks** — Indian Entertainment — consecutive failures: **148** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **43** — HTTP 503
- **AXN CEE** — International — consecutive failures: **43** — HTTP 503
- **FilmBox** — International — consecutive failures: **16** — Timeout
- **HBO** — International — consecutive failures: **136** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **43** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **43** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **43** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **43** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **340** — Timeout
- **Minimax** — Kids — consecutive failures: **43** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **14** — HTTP 403
- **Islamic TV** — Religious — consecutive failures: **10** — Timeout
- **Makkah Live** — Religious — consecutive failures: **10** — Timeout

## Failed This Check

- **Channel 1** — Backup — streak 10 — Timeout
- **Channel 16** — Backup — streak 16 — Timeout
- **Channel S** — Backup — streak 10 — Timeout
- **Channel S** — Backup — streak 10 — Timeout
- **Disney Channel India** — Backup — streak 14 — HTTP 403
- **Ekhon TV** — Backup — streak 10 — Timeout
- **G TV** — Backup — streak 10 — Timeout
- **G TV** — Backup — streak 10 — Timeout
- **Goldmines Bollywood** — Backup — streak 12 — HTTP 404
- **Goldmines Movies** — Backup — streak 16 — HTTP 404
- **Movie Bangla** — Backup — streak 10 — Timeout
- **Movie Bangla** — Backup — streak 10 — Timeout
- **My TV** — Backup — streak 10 — Timeout
- **RTV** — Backup — streak 10 — Timeout
- **SA TV** — Backup — streak 10 — Timeout
- **SA TV** — Backup — streak 10 — Timeout
- **Ananda TV** — Bangladesh — streak 11 — Timeout
- **Green TV** — Bangladesh — streak 10 — Timeout
- **Assam Talks** — Indian Entertainment — streak 148 — HTTP 403
- **AXN Black Czech Republic** — International — streak 43 — HTTP 503
- **AXN CEE** — International — streak 43 — HTTP 503
- **FilmBox** — International — streak 16 — Timeout
- **HBO** — International — streak 136 — HTTP 403
- **Music Box Classic** — International — streak 43 — HTTP 503
- **Music Box Dance** — International — streak 43 — HTTP 503
- **Music Box Hits** — International — streak 43 — HTTP 503
- **Music Box Sexy** — International — streak 43 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 340 — Timeout
- **Minimax** — Kids — streak 43 — HTTP 503
- **Teen Nick** — Kids — streak 14 — HTTP 403
- **Islamic TV** — Religious — streak 10 — Timeout
- **Makkah Live** — Religious — streak 10 — Timeout
- **Sony Sports Ten 3** — Sports — streak 1 — Timeout

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
