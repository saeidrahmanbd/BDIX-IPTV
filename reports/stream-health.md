# Stream Health Report

Generated: **2026-10-14T04:49:22+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **901**
- Failed this check: **39**
- Persistent failures (3+ consecutive): **35**
- Intermittent failures: **4**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- Connection: **3**
- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **6**
- HTTP 5xx (server): **7**
- Timeout: **19**
## Persistent Failures

- **Channel 1** — Backup — consecutive failures: **8** — Timeout
- **Channel 16** — Backup — consecutive failures: **14** — Timeout
- **Channel S** — Backup — consecutive failures: **8** — Timeout
- **Channel S** — Backup — consecutive failures: **8** — Timeout
- **Colors Bangla** — Backup — consecutive failures: **6** — Connection
- **Disney Channel India** — Backup — consecutive failures: **12** — HTTP 403
- **Ekhon TV** — Backup — consecutive failures: **8** — Timeout
- **G TV** — Backup — consecutive failures: **8** — Timeout
- **G TV** — Backup — consecutive failures: **8** — Timeout
- **Goldmines Bollywood** — Backup — consecutive failures: **10** — HTTP 404
- **Goldmines Movies** — Backup — consecutive failures: **14** — HTTP 404
- **Movie Bangla** — Backup — consecutive failures: **8** — Timeout
- **Movie Bangla** — Backup — consecutive failures: **8** — Timeout
- **My TV** — Backup — consecutive failures: **8** — Timeout
- **RTV** — Backup — consecutive failures: **8** — Timeout
- **SA TV** — Backup — consecutive failures: **8** — Timeout
- **SA TV** — Backup — consecutive failures: **8** — Timeout
- **Ananda TV** — Bangladesh — consecutive failures: **9** — Timeout
- **Green TV** — Bangladesh — consecutive failures: **8** — Timeout
- **Colors Bangla Cinema** — Indian Bangla — consecutive failures: **6** — Connection
- **Assam Talks** — Indian Entertainment — consecutive failures: **146** — HTTP 403
- **Star Plus** — Indian Entertainment — consecutive failures: **6** — Connection
- **AXN Black Czech Republic** — International — consecutive failures: **41** — HTTP 503
- **AXN CEE** — International — consecutive failures: **41** — HTTP 503
- **FilmBox** — International — consecutive failures: **14** — Timeout
- **HBO** — International — consecutive failures: **134** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **41** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **41** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **41** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **41** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **338** — Timeout
- **Minimax** — Kids — consecutive failures: **41** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **12** — HTTP 403
- **Islamic TV** — Religious — consecutive failures: **8** — Timeout
- **Makkah Live** — Religious — consecutive failures: **8** — Timeout

## Failed This Check

- **Balle Balle** — Backup — streak 1 — HTTP 404
- **Channel 1** — Backup — streak 8 — Timeout
- **Channel 16** — Backup — streak 14 — Timeout
- **Channel S** — Backup — streak 8 — Timeout
- **Channel S** — Backup — streak 8 — Timeout
- **Colors Bangla** — Backup — streak 6 — Connection
- **Disney Channel India** — Backup — streak 12 — HTTP 403
- **Ekhon TV** — Backup — streak 8 — Timeout
- **G TV** — Backup — streak 8 — Timeout
- **G TV** — Backup — streak 8 — Timeout
- **Goldmines Bollywood** — Backup — streak 10 — HTTP 404
- **Goldmines Movies** — Backup — streak 14 — HTTP 404
- **Movie Bangla** — Backup — streak 8 — Timeout
- **Movie Bangla** — Backup — streak 8 — Timeout
- **My TV** — Backup — streak 8 — Timeout
- **RTV** — Backup — streak 8 — Timeout
- **SA TV** — Backup — streak 8 — Timeout
- **SA TV** — Backup — streak 8 — Timeout
- **Ananda TV** — Bangladesh — streak 9 — Timeout
- **Green TV** — Bangladesh — streak 8 — Timeout
- **Colors Bangla Cinema** — Indian Bangla — streak 6 — Connection
- **Zee Bangla** — Indian Bangla — streak 1 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 146 — HTTP 403
- **Star Plus** — Indian Entertainment — streak 6 — Connection
- **Movies Now** — Indian Movies — streak 1 — HTTP 404
- **Star Movies Select** — Indian Movies — streak 1 — HTTP 404
- **AXN Black Czech Republic** — International — streak 41 — HTTP 503
- **AXN CEE** — International — streak 41 — HTTP 503
- **FilmBox** — International — streak 14 — Timeout
- **HBO** — International — streak 134 — HTTP 403
- **Music Box Classic** — International — streak 41 — HTTP 503
- **Music Box Dance** — International — streak 41 — HTTP 503
- **Music Box Hits** — International — streak 41 — HTTP 503
- **Music Box Sexy** — International — streak 41 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 338 — Timeout
- **Minimax** — Kids — streak 41 — HTTP 503
- **Teen Nick** — Kids — streak 12 — HTTP 403
- **Islamic TV** — Religious — streak 8 — Timeout
- **Makkah Live** — Religious — streak 8 — Timeout

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
