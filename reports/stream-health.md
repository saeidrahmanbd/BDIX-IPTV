# Stream Health Report

Generated: **2026-10-14T03:58:34+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **888**
- Failed this check: **52**
- Persistent failures (3+ consecutive): **16**
- Intermittent failures: **36**
- Primary tested: **578**
- Backup tested: **362**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **1**
- HTTP 5xx (server): **9**
- Timeout: **38**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **4** — Timeout
- **Channel S** — Backup — consecutive failures: **3** — Timeout
- **Goldmines Movies** — Backup — consecutive failures: **4** — Timeout
- **RTV** — Backup — consecutive failures: **3** — Timeout
- **SA TV** — Backup — consecutive failures: **3** — Timeout
- **Assam Talks** — Indian Entertainment — consecutive failures: **136** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **31** — HTTP 503
- **AXN CEE** — International — consecutive failures: **31** — HTTP 503
- **FilmBox** — International — consecutive failures: **4** — Timeout
- **HBO** — International — consecutive failures: **124** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **31** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **31** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **31** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **31** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **328** — Timeout
- **Minimax** — Kids — consecutive failures: **31** — HTTP 503

## Failed This Check

- **Animal Planet** — Backup — streak 2 — Timeout
- **Channel 1** — Backup — streak 2 — Timeout
- **Channel 16** — Backup — streak 4 — Timeout
- **Channel I** — Backup — streak 2 — HTTP 504
- **Channel S** — Backup — streak 2 — Timeout
- **Channel S** — Backup — streak 1 — HTTP 500
- **Channel S** — Backup — streak 3 — Timeout
- **Dangal 2** — Backup — streak 2 — Timeout
- **Deen TV** — Backup — streak 2 — Timeout
- **Disney Channel India** — Backup — streak 2 — HTTP 403
- **Ekhon TV** — Backup — streak 2 — Timeout
- **Food Food** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **Goldmines Movies** — Backup — streak 4 — Timeout
- **MNTV (Tamil)** — Backup — streak 1 — HTTP 404
- **Movie Bangla** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 2 — Timeout
- **RTV** — Backup — streak 3 — Timeout
- **SA TV** — Backup — streak 3 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **Shemaroo TV** — Backup — streak 2 — Timeout
- **TLC** — Backup — streak 2 — Timeout
- **Ananda TV** — Bangladesh — streak 2 — Timeout
- **Green TV** — Bangladesh — streak 2 — Timeout
- **Discovery Science** — Documentary & Wildlife — streak 2 — Timeout
- **Discovery Turbo** — Documentary & Wildlife — streak 2 — Timeout
- **Food Network** — Documentary & Wildlife — streak 2 — Timeout
- **HGTV** — Documentary & Wildlife — streak 2 — Timeout
- **HISTORY TV** — Documentary & Wildlife — streak 2 — Timeout
- **Nat Geo TV** — Documentary & Wildlife — streak 2 — Timeout
- **Travel Channel** — Documentary & Wildlife — streak 2 — Timeout
- **Assam Talks** — Indian Entertainment — streak 136 — HTTP 403
- **AXN Black Czech Republic** — International — streak 31 — HTTP 503
- **AXN CEE** — International — streak 31 — HTTP 503
- **AXS** — International — streak 2 — Timeout
- **EPIX TV** — International — streak 2 — Timeout
- **FilmBox** — International — streak 4 — Timeout
- **HBO** — International — streak 124 — HTTP 403
- **HBO 2** — International — streak 2 — Timeout
- **Music Box Classic** — International — streak 31 — HTTP 503
- **Music Box Dance** — International — streak 31 — HTTP 503
- **Music Box Hits** — International — streak 31 — HTTP 503
- **Music Box Sexy** — International — streak 31 — HTTP 503
- **YTV** — International — streak 2 — Timeout
- **ETV Bal Bharat** — Kids — streak 328 — Timeout
- **Minimax** — Kids — streak 31 — HTTP 503
- **Teen Nick** — Kids — streak 2 — HTTP 403
- **Islamic TV** — Religious — streak 2 — Timeout
- **Madani TV** — Religious — streak 2 — Timeout
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
