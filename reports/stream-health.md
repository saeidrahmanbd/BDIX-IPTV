# Stream Health Report

Generated: **2026-10-14T14:24:19+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **924**
- Failed this check: **16**
- Persistent failures (3+ consecutive): **16**
- Intermittent failures: **0**
- Primary tested: **593**
- Backup tested: **347**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **3**
- HTTP 5xx (server): **7**
- Timeout: **2**
## Persistent Failures

- **Channel 16** — Backup — consecutive failures: **54** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **52** — HTTP 403
- **Goldmines Movies** — Backup — consecutive failures: **4** — HTTP 404
- **Deepto TV** — Bangladesh — consecutive failures: **22** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **186** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **81** — HTTP 503
- **AXN CEE** — International — consecutive failures: **81** — HTTP 503
- **FilmBox** — International — consecutive failures: **16** — Timeout
- **HBO** — International — consecutive failures: **174** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **81** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **81** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **81** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **81** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **378** — Timeout
- **Minimax** — Kids — consecutive failures: **81** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **52** — HTTP 403

## Failed This Check

- **Channel 16** — Backup — streak 54 — HTTP 404
- **Disney Channel India** — Backup — streak 52 — HTTP 403
- **Goldmines Movies** — Backup — streak 4 — HTTP 404
- **Deepto TV** — Bangladesh — streak 22 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 186 — HTTP 403
- **AXN Black Czech Republic** — International — streak 81 — HTTP 503
- **AXN CEE** — International — streak 81 — HTTP 503
- **FilmBox** — International — streak 16 — Timeout
- **HBO** — International — streak 174 — HTTP 403
- **Music Box Classic** — International — streak 81 — HTTP 503
- **Music Box Dance** — International — streak 81 — HTTP 503
- **Music Box Hits** — International — streak 81 — HTTP 503
- **Music Box Sexy** — International — streak 81 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 378 — Timeout
- **Minimax** — Kids — streak 81 — HTTP 503
- **Teen Nick** — Kids — streak 52 — HTTP 403

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
