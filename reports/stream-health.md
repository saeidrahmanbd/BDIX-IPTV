# Stream Health Report

Generated: **2026-10-14T14:45:03+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **919**
- Failed this check: **21**
- Persistent failures (3+ consecutive): **15**
- Intermittent failures: **6**
- Primary tested: **593**
- Backup tested: **347**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **5**
- HTTP 5xx (server): **9**
- Other: **1**
- Timeout: **2**
## Persistent Failures

- **Disney Channel India** — Backup — consecutive failures: **54** — HTTP 403
- **Goldmines Movies** — Backup — consecutive failures: **6** — HTTP 404
- **Deepto TV** — Bangladesh — consecutive failures: **24** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **188** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **83** — HTTP 503
- **AXN CEE** — International — consecutive failures: **83** — HTTP 503
- **FilmBox** — International — consecutive failures: **18** — Timeout
- **HBO** — International — consecutive failures: **176** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **83** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **83** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **83** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **83** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **380** — Timeout
- **Minimax** — Kids — consecutive failures: **83** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **54** — HTTP 403

## Failed This Check

- **Disney Channel India** — Backup — streak 54 — HTTP 403
- **Ekattor TV** — Backup — streak 1 — HTTP 404
- **Goldmines Movies** — Backup — streak 6 — HTTP 404
- **Nan TV** — Backup — streak 2 — HTTP 404
- **Zee Cinema** — Backup — streak 1 — HTTP 404
- **Deepto TV** — Bangladesh — streak 24 — HTTP 404
- **NTV Europe** — Bangladesh — streak 1 — HTTP 500
- **Amar Bangla** — Indian Bangla — streak 1 — HTTP 500
- **Assam Talks** — Indian Entertainment — streak 188 — HTTP 403
- **Sony Max 2 [US]** — Indian Movies — streak 2 — Other
- **AXN Black Czech Republic** — International — streak 83 — HTTP 503
- **AXN CEE** — International — streak 83 — HTTP 503
- **FilmBox** — International — streak 18 — Timeout
- **HBO** — International — streak 176 — HTTP 403
- **Music Box Classic** — International — streak 83 — HTTP 503
- **Music Box Dance** — International — streak 83 — HTTP 503
- **Music Box Hits** — International — streak 83 — HTTP 503
- **Music Box Sexy** — International — streak 83 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 380 — Timeout
- **Minimax** — Kids — streak 83 — HTTP 503
- **Teen Nick** — Kids — streak 54 — HTTP 403

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
