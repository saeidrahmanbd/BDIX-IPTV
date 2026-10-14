# Stream Health Report

Generated: **2026-10-14T05:08:50+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **905**
- Failed this check: **35**
- Persistent failures (3+ consecutive): **30**
- Intermittent failures: **5**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **5**
- HTTP 5xx (server): **7**
- TLS: **1**
- Timeout: **18**
## Persistent Failures

- **Channel 1** — Backup — consecutive failures: **12** — Timeout
- **Channel 16** — Backup — consecutive failures: **18** — Timeout
- **Channel S** — Backup — consecutive failures: **12** — Timeout
- **Channel S** — Backup — consecutive failures: **12** — Timeout
- **Disney Channel India** — Backup — consecutive failures: **16** — HTTP 403
- **Ekhon TV** — Backup — consecutive failures: **12** — Timeout
- **G TV** — Backup — consecutive failures: **12** — Timeout
- **G TV** — Backup — consecutive failures: **12** — Timeout
- **Goldmines Bollywood** — Backup — consecutive failures: **14** — HTTP 404
- **Movie Bangla** — Backup — consecutive failures: **12** — Timeout
- **Movie Bangla** — Backup — consecutive failures: **12** — Timeout
- **My TV** — Backup — consecutive failures: **12** — Timeout
- **RTV** — Backup — consecutive failures: **12** — Timeout
- **SA TV** — Backup — consecutive failures: **12** — Timeout
- **SA TV** — Backup — consecutive failures: **12** — Timeout
- **Ananda TV** — Bangladesh — consecutive failures: **13** — Timeout
- **Green TV** — Bangladesh — consecutive failures: **12** — Timeout
- **Assam Talks** — Indian Entertainment — consecutive failures: **150** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **45** — HTTP 503
- **AXN CEE** — International — consecutive failures: **45** — HTTP 503
- **HBO** — International — consecutive failures: **138** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **45** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **45** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **45** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **45** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **342** — Timeout
- **Minimax** — Kids — consecutive failures: **45** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **16** — HTTP 403
- **Islamic TV** — Religious — consecutive failures: **12** — Timeout
- **Makkah Live** — Religious — consecutive failures: **12** — Timeout

## Failed This Check

- **Balle Balle** — Backup — streak 1 — HTTP 404
- **Channel 1** — Backup — streak 12 — Timeout
- **Channel 16** — Backup — streak 18 — Timeout
- **Channel S** — Backup — streak 12 — Timeout
- **Channel S** — Backup — streak 12 — Timeout
- **Disney Channel India** — Backup — streak 16 — HTTP 403
- **Ekhon TV** — Backup — streak 12 — Timeout
- **G TV** — Backup — streak 12 — Timeout
- **G TV** — Backup — streak 12 — Timeout
- **Goldmines Bollywood** — Backup — streak 14 — HTTP 404
- **ME TV** — Backup — streak 1 — HTTP 404
- **ME TV** — Backup — streak 1 — HTTP 404
- **ME TV** — Backup — streak 1 — HTTP 404
- **Movie Bangla** — Backup — streak 12 — Timeout
- **Movie Bangla** — Backup — streak 12 — Timeout
- **My TV** — Backup — streak 12 — Timeout
- **RTV** — Backup — streak 12 — Timeout
- **SA TV** — Backup — streak 12 — Timeout
- **SA TV** — Backup — streak 12 — Timeout
- **Ananda TV** — Bangladesh — streak 13 — Timeout
- **Green TV** — Bangladesh — streak 12 — Timeout
- **Assam Talks** — Indian Entertainment — streak 150 — HTTP 403
- **AXN Black Czech Republic** — International — streak 45 — HTTP 503
- **AXN CEE** — International — streak 45 — HTTP 503
- **FON Music** — International — streak 1 — TLS
- **HBO** — International — streak 138 — HTTP 403
- **Music Box Classic** — International — streak 45 — HTTP 503
- **Music Box Dance** — International — streak 45 — HTTP 503
- **Music Box Hits** — International — streak 45 — HTTP 503
- **Music Box Sexy** — International — streak 45 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 342 — Timeout
- **Minimax** — Kids — streak 45 — HTTP 503
- **Teen Nick** — Kids — streak 16 — HTTP 403
- **Islamic TV** — Religious — streak 12 — Timeout
- **Makkah Live** — Religious — streak 12 — Timeout

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
