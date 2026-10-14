# Stream Health Report

Generated: **2026-10-14T04:16:44+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **913**
- Failed this check: **27**
- Persistent failures (3+ consecutive): **17**
- Intermittent failures: **10**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **11**
- HTTP 5xx (server): **10**
- Timeout: **2**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **6** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **4** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **4** — HTTP 403
- **Goldmines Movies** — Backup — consecutive failures: **6** — HTTP 404
- **Shemaroo TV** — Backup — consecutive failures: **4** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **138** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **33** — HTTP 503
- **AXN CEE** — International — consecutive failures: **33** — HTTP 503
- **FilmBox** — International — consecutive failures: **6** — Timeout
- **HBO** — International — consecutive failures: **126** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **33** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **33** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **33** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **33** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **330** — Timeout
- **Minimax** — Kids — consecutive failures: **33** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **4** — HTTP 403

## Failed This Check

- **Channel 16** — Backup — streak 6 — HTTP 404
- **Channel S** — Backup — streak 1 — HTTP 500
- **Dangal 2** — Backup — streak 4 — HTTP 404
- **Deewana** — Backup — streak 1 — HTTP 502
- **Disney Channel India** — Backup — streak 4 — HTTP 403
- **Goldmines Bollywood** — Backup — streak 2 — HTTP 404
- **Goldmines Movies** — Backup — streak 6 — HTTP 404
- **Shemaroo TV** — Backup — streak 4 — HTTP 404
- **Ananda TV** — Bangladesh — streak 1 — HTTP 500
- **Jalsha Movies HD** — Indian Bangla — streak 1 — HTTP 404
- **Zee Bangla** — Indian Bangla — streak 1 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 138 — HTTP 403
- **Colors Infinity** — Indian Entertainment — streak 1 — HTTP 404
- **Epic Parivar** — Indian Entertainment — streak 1 — HTTP 404
- **Star Movies Select** — Indian Movies — streak 1 — HTTP 404
- **Sana Plus** — Indian Music — streak 2 — HTTP 404
- **AXN Black Czech Republic** — International — streak 33 — HTTP 503
- **AXN CEE** — International — streak 33 — HTTP 503
- **FilmBox** — International — streak 6 — Timeout
- **HBO** — International — streak 126 — HTTP 403
- **Music Box Classic** — International — streak 33 — HTTP 503
- **Music Box Dance** — International — streak 33 — HTTP 503
- **Music Box Hits** — International — streak 33 — HTTP 503
- **Music Box Sexy** — International — streak 33 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 330 — Timeout
- **Minimax** — Kids — streak 33 — HTTP 503
- **Teen Nick** — Kids — streak 4 — HTTP 403

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
