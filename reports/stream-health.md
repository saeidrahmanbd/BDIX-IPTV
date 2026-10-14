# Stream Health Report

Generated: **2026-10-14T11:08:38+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **905**
- Failed this check: **35**
- Persistent failures (3+ consecutive): **18**
- Intermittent failures: **17**
- Primary tested: **593**
- Backup tested: **347**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **4**
- HTTP 5xx (server): **7**
- Timeout: **20**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **48** — Timeout
- **Channel S** — Backup — consecutive failures: **3** — Timeout
- **Disney Channel India** — Backup — consecutive failures: **46** — HTTP 403
- **Deepto TV** — Bangladesh — consecutive failures: **16** — HTTP 404
- **Green TV** — Bangladesh — consecutive failures: **3** — Timeout
- **Assam Talks** — Indian Entertainment — consecutive failures: **180** — HTTP 403
- **Raj Music Telugu** — Indian Music — consecutive failures: **4** — HTTP 404
- **AXN Black Czech Republic** — International — consecutive failures: **75** — HTTP 503
- **AXN CEE** — International — consecutive failures: **75** — HTTP 503
- **FilmBox** — International — consecutive failures: **10** — Timeout
- **HBO** — International — consecutive failures: **168** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **75** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **75** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **75** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **75** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **372** — Timeout
- **Minimax** — Kids — consecutive failures: **75** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **46** — HTTP 403

## Failed This Check

- **Channel 1** — Backup — streak 2 — Timeout
- **Channel 16** — Backup — streak 48 — Timeout
- **Channel S** — Backup — streak 2 — Timeout
- **Channel S** — Backup — streak 3 — Timeout
- **Disney Channel India** — Backup — streak 46 — HTTP 403
- **Ekhon TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 2 — Timeout
- **RTV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **Thikana** — Backup — streak 1 — Timeout
- **Ananda TV** — Bangladesh — streak 2 — Timeout
- **Deepto TV** — Bangladesh — streak 16 — HTTP 404
- **Green TV** — Bangladesh — streak 3 — Timeout
- **Nat Geo TV** — Documentary & Wildlife — streak 2 — HTTP 404
- **Jalsha Movies HD** — Indian Bangla — streak 1 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 180 — HTTP 403
- **Raj Music Telugu** — Indian Music — streak 4 — HTTP 404
- **AXN Black Czech Republic** — International — streak 75 — HTTP 503
- **AXN CEE** — International — streak 75 — HTTP 503
- **FilmBox** — International — streak 10 — Timeout
- **HBO** — International — streak 168 — HTTP 403
- **Music Box Classic** — International — streak 75 — HTTP 503
- **Music Box Dance** — International — streak 75 — HTTP 503
- **Music Box Hits** — International — streak 75 — HTTP 503
- **Music Box Sexy** — International — streak 75 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 372 — Timeout
- **Minimax** — Kids — streak 75 — HTTP 503
- **Teen Nick** — Kids — streak 46 — HTTP 403
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
