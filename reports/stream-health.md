# Stream Health Report

Generated: **2026-10-14T06:17:15+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **940**
- Reachable: **914**
- Failed this check: **26**
- Persistent failures (3+ consecutive): **21**
- Intermittent failures: **5**
- Primary tested: **594**
- Backup tested: **346**

## Failure Classification

- HTTP 401/403 (auth): **4**
- HTTP 404 (not found): **7**
- HTTP 5xx (server): **9**
- Timeout: **6**
## Persistent Failures

- **Ananda TV** — Backup — consecutive failures: **4** — HTTP 404
- **Channel 16** — Backup — consecutive failures: **26** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **24** — HTTP 403
- **Duronto TV** — Backup — consecutive failures: **4** — Timeout
- **Goldmines Bollywood** — Backup — consecutive failures: **4** — HTTP 404
- **Shemaroo TV** — Backup — consecutive failures: **4** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **158** — HTTP 403
- **Star Gold Thrills** — Indian Movies — consecutive failures: **3** — Timeout
- **AXN Black Czech Republic** — International — consecutive failures: **53** — HTTP 503
- **AXN CEE** — International — consecutive failures: **53** — HTTP 503
- **HBO** — International — consecutive failures: **146** — HTTP 403
- **Music Box Classic** — International — consecutive failures: **53** — HTTP 503
- **Music Box Dance** — International — consecutive failures: **53** — HTTP 503
- **Music Box Hits** — International — consecutive failures: **53** — HTTP 503
- **Music Box Sexy** — International — consecutive failures: **53** — HTTP 503
- **ETV Bal Bharat** — Kids — consecutive failures: **350** — Timeout
- **Minimax** — Kids — consecutive failures: **53** — HTTP 503
- **Teen Nick** — Kids — consecutive failures: **24** — HTTP 403
- **Astro Cricbuzz** — Sports — consecutive failures: **3** — Timeout
- **FOX Cricket 501** — Sports — consecutive failures: **3** — Timeout
- **Ten Sports** — Sports — consecutive failures: **3** — Timeout

## Failed This Check

- **Ananda TV** — Backup — streak 4 — HTTP 404
- **Channel 16** — Backup — streak 26 — HTTP 404
- **Disney Channel India** — Backup — streak 24 — HTTP 403
- **Duronto TV** — Backup — streak 4 — Timeout
- **Goldmines Bollywood** — Backup — streak 4 — HTTP 404
- **Goldmines Movies** — Backup — streak 2 — HTTP 404
- **RTV** — Backup — streak 1 — HTTP 500
- **SA TV** — Backup — streak 1 — HTTP 500
- **Shemaroo TV** — Backup — streak 4 — HTTP 404
- **NRB TV** — Bangladesh — streak 1 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 158 — HTTP 403
- **Epic Parivar** — Indian Entertainment — streak 1 — HTTP 404
- **Star Gold Thrills** — Indian Movies — streak 3 — Timeout
- **AXN Black Czech Republic** — International — streak 53 — HTTP 503
- **AXN CEE** — International — streak 53 — HTTP 503
- **HBO** — International — streak 146 — HTTP 403
- **Music Box Classic** — International — streak 53 — HTTP 503
- **Music Box Dance** — International — streak 53 — HTTP 503
- **Music Box Hits** — International — streak 53 — HTTP 503
- **Music Box Sexy** — International — streak 53 — HTTP 503
- **ETV Bal Bharat** — Kids — streak 350 — Timeout
- **Minimax** — Kids — streak 53 — HTTP 503
- **Teen Nick** — Kids — streak 24 — HTTP 403
- **Astro Cricbuzz** — Sports — streak 3 — Timeout
- **FOX Cricket 501** — Sports — streak 3 — Timeout
- **Ten Sports** — Sports — streak 3 — Timeout

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
