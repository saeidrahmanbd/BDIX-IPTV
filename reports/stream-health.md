# Stream Health Report

Generated: **2026-10-14T14:14:39+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **892**
- Failed this check: **48**
- Persistent failures (3+ consecutive): **16**
- Intermittent failures: **32**
- Primary tested: **593**
- Backup tested: **347**

## Failure Classification

- Connection: **13**
- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **2**
- HTTP 5xx (server): **10**
- Timeout: **19**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **52** — Timeout
- **Channel S** — Backup — consecutive failures: **3** — Timeout
- **Disney Channel India** — Backup — consecutive failures: **50** — HTTP 403
- **Deepto TV** — Bangladesh — consecutive failures: **20** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **184** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **79** — HTTP 503
- **AXN CEE** — International — consecutive failures: **79** — HTTP 503
- **FilmBox** — International — consecutive failures: **14** — Timeout
- **HBO** — International — consecutive failures: **172** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **79** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **79** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **79** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **79** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **376** — Timeout
- **Minimax** — Kids — consecutive failures: **79** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **50** — HTTP 403

## Failed This Check

- **Channel 1** — Backup — streak 2 — Timeout
- **Channel 16** — Backup — streak 52 — Timeout
- **Channel S** — Backup — streak 2 — Timeout
- **Channel S** — Backup — streak 3 — Timeout
- **Disney Channel India** — Backup — streak 50 — HTTP 403
- **Ekhon TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **Goldmines Movies** — Backup — streak 2 — HTTP 404
- **Movie Bangla** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **Movies Now** — Backup — streak 1 — Connection
- **My TV** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 1 — HTTP 500
- **RTV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **Sony Entertainment TV** — Backup — streak 1 — Connection
- **Sony Entertainment TV** — Backup — streak 1 — Connection
- **Sony SAB** — Backup — streak 1 — Connection
- **Sony SAB** — Backup — streak 1 — Connection
- **Star Jalsha** — Backup — streak 1 — Connection
- **Star Jalsha** — Backup — streak 1 — Connection
- **Star Movies Select** — Backup — streak 1 — Connection
- **Zee Bangla** — Backup — streak 1 — Connection
- **Zee Cinema** — Backup — streak 1 — Connection
- **Zee Cinema** — Backup — streak 1 — Connection
- **Zee TV** — Backup — streak 1 — Connection
- **Zee TV** — Backup — streak 1 — Connection
- **Ananda TV** — Bangladesh — streak 2 — Timeout
- **Deepto TV** — Bangladesh — streak 20 — HTTP 404
- **G TV** — Bangladesh — streak 1 — HTTP 500
- **Green TV** — Bangladesh — streak 2 — Timeout
- **Assam Talks** — Indian Entertainment — streak 184 — HTTP 403
- **AXN Black Czech Republic** — International — streak 79 — HTTP 503
- **AXN CEE** — International — streak 79 — HTTP 503
- **FilmBox** — International — streak 14 — Timeout
- **HBO** — International — streak 172 — HTTP 403
- **Music Box Classic** — International — streak 79 — HTTP 503
- **Music Box Dance** — International — streak 79 — HTTP 503
- **Music Box Hits** — International — streak 79 — HTTP 503
- **Music Box Sexy** — International — streak 79 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 376 — Timeout
- **Minimax** — Kids — streak 79 — HTTP 503
- **Teen Nick** — Kids — streak 50 — HTTP 403
- **Iqra Bangla** — Religious — streak 1 — HTTP 500
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
