# Stream Health Report

Generated: **2026-10-15T04:30:30+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **910**
- Failed this check: **30**
- Persistent failures (3+ consecutive): **29**
- Intermittent failures: **1**
- Primary tested: **593**
- Backup tested: **347**

## Failure Classification

- HTTP 401/403 (auth): **16**
- HTTP 404 (not found): **4**
- HTTP 4xx (other): **1**
- HTTP 5xx (server): **7**
- Timeout: **2**
## Persistent Failures

- **Desh TV** — Backup — consecutive failures: **5** — HTTP 403
- **Discovery** — Backup — consecutive failures: **4** — HTTP 403
- **Discovery Kids** — Backup — consecutive failures: **4** — HTTP 403
- **Discovery Science** — Backup — consecutive failures: **4** — HTTP 403
- **Discovery Turbo** — Backup — consecutive failures: **4** — HTTP 403
- **Disney Channel India** — Backup — consecutive failures: **60** — HTTP 403
- **Investigation Discovery** — Backup — consecutive failures: **4** — HTTP 403
- **Nan TV** — Backup — consecutive failures: **8** — HTTP 404
- **Nexus TV** — Backup — consecutive failures: **5** — HTTP 403
- **Shemaroo Josh** — Backup — consecutive failures: **6** — HTTP 404
- **Shemaroo TV** — Backup — consecutive failures: **6** — HTTP 404
- **Sony Max** — Backup — consecutive failures: **5** — HTTP 403
- **Zee Action** — Backup — consecutive failures: **5** — HTTP 403
- **Zee Bangla Cinema** — Backup — consecutive failures: **5** — HTTP 403
- **Zee Bollywood** — Backup — consecutive failures: **5** — HTTP 403
- **Deepto TV** — Bangladesh — consecutive failures: **4** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **194** — HTTP 403
- **Zee Anmol** — Indian Entertainment — consecutive failures: **4** — HTTP 403
- **AXN Black Czech Republic** — International — consecutive failures: **89** — HTTP 503
- **AXN CEE** — International — consecutive failures: **89** — HTTP 503
- **FilmBox** — International — consecutive failures: **24** — Timeout
- **HBO** — International — consecutive failures: **182** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **89** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **89** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **89** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **89** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **386** — Timeout
- **Minimax** — Kids — consecutive failures: **89** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **60** — HTTP 403

## Failed This Check

- **Desh TV** — Backup — streak 5 — HTTP 403
- **Discovery** — Backup — streak 4 — HTTP 403
- **Discovery Kids** — Backup — streak 4 — HTTP 403
- **Discovery Science** — Backup — streak 4 — HTTP 403
- **Discovery Turbo** — Backup — streak 4 — HTTP 403
- **Disney Channel India** — Backup — streak 60 — HTTP 403
- **Investigation Discovery** — Backup — streak 4 — HTTP 403
- **Nan TV** — Backup — streak 8 — HTTP 404
- **Nexus TV** — Backup — streak 5 — HTTP 403
- **Shemaroo Josh** — Backup — streak 6 — HTTP 404
- **Shemaroo TV** — Backup — streak 6 — HTTP 404
- **Sony Max** — Backup — streak 5 — HTTP 403
- **Zee Action** — Backup — streak 5 — HTTP 403
- **Zee Bangla Cinema** — Backup — streak 5 — HTTP 403
- **Zee Bollywood** — Backup — streak 5 — HTTP 403
- **Deepto TV** — Bangladesh — streak 4 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 194 — HTTP 403
- **Zee Anmol** — Indian Entertainment — streak 4 — HTTP 403
- **AXN Black Czech Republic** — International — streak 89 — HTTP 503
- **AXN CEE** — International — streak 89 — HTTP 503
- **FilmBox** — International — streak 24 — Timeout
- **HBO** — International — streak 182 — HTTP 403
- **Music Box Classic** — International — streak 89 — HTTP 503
- **Music Box Dance** — International — streak 89 — HTTP 503
- **Music Box Hits** — International — streak 89 — HTTP 503
- **Music Box Sexy** — International — streak 89 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 386 — Timeout
- **Minimax** — Kids — streak 89 — HTTP 503
- **Sonic Bangla** — Kids — streak 1 — HTTP 429
- **Teen Nick** — Kids — streak 60 — HTTP 403

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
