# Stream Health Report

Generated: **2026-10-15T09:57:38+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1037**
- Reachable: **969**
- Failed this check: **68**
- Persistent failures (3+ consecutive): **15**
- Intermittent failures: **53**
- Primary tested: **652**
- Backup tested: **385**

## Failure Classification

- HTTP 401/403 (auth): **5**
- HTTP 404 (not found): **8**
- HTTP 5xx (server): **6**
- Timeout: **49**
## Persistent Failures

- **Ananda TV** — Backup — consecutive failures: **6** — Timeout
- **Disney Channel India** — Backup — consecutive failures: **78** — HTTP 403
- **G TV** — Backup — consecutive failures: **3** — Timeout
- **Goldmines** — Backup — consecutive failures: **3** — HTTP 404
- **Goldmines** — Backup — consecutive failures: **3** — HTTP 404
- **Channel 16** — Bangladesh — consecutive failures: **14** — Timeout
- **Assam Talks** — Indian Entertainment — consecutive failures: **212** — HTTP 403
- **Oli TV** — Indian Entertainment — consecutive failures: **6** — Timeout
- **Suriyan TV** — Indian Entertainment — consecutive failures: **6** — HTTP 523
- **K Cine** — Indian Movies — consecutive failures: **3** — Timeout
- **Afrobeats** — International — consecutive failures: **3** — HTTP 404
- **Cook & Bake** — International — consecutive failures: **18** — HTTP 504
- **HBO** — International — consecutive failures: **200** — HTTP 403
- **Teleritmo** — International — consecutive failures: **18** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **78** — HTTP 403

## Failed This Check

- **ATN Bangla UK** — Backup — streak 1 — HTTP 523
- **Amar Bangla Digital** — Backup — streak 1 — HTTP 523
- **Ananda TV** — Backup — streak 2 — Timeout
- **Ananda TV** — Backup — streak 6 — Timeout
- **Channel 1** — Backup — streak 2 — Timeout
- **Channel 1** — Backup — streak 2 — Timeout
- **Channel 52** — Backup — streak 1 — HTTP 404
- **Channel S** — Backup — streak 2 — Timeout
- **Channel S** — Backup — streak 1 — Timeout
- **Channel S** — Backup — streak 1 — Timeout
- **Channel S** — Backup — streak 2 — Timeout
- **Dangal** — Backup — streak 2 — HTTP 404
- **Deen TV** — Backup — streak 1 — Timeout
- **Desh TV** — Backup — streak 2 — Timeout
- **Discover Pakistan** — Backup — streak 1 — Timeout
- **Disney Channel India** — Backup — streak 78 — HTTP 403
- **Ekhon TV** — Backup — streak 2 — Timeout
- **Ekushey TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 1 — Timeout
- **G TV** — Backup — streak 3 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **Global TV** — Backup — streak 2 — Timeout
- **Goldmines** — Backup — streak 3 — HTTP 404
- **Goldmines** — Backup — streak 3 — HTTP 404
- **Green TV** — Backup — streak 1 — Timeout
- **Green TV** — Backup — streak 1 — Timeout
- **Green TV** — Backup — streak 1 — Timeout
- **Green TV** — Backup — streak 1 — HTTP 404
- **Jago News 24** — Backup — streak 1 — Timeout
- **Jago News 24** — Backup — streak 1 — Timeout
- **Medina Live** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 1 — Timeout
- **NTV Europe** — Backup — streak 1 — Timeout
- **RTV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **ATN Bangla UK** — Bangladesh — streak 1 — Timeout
- **Ananda TV** — Bangladesh — streak 2 — Timeout
- **Channel 16** — Bangladesh — streak 14 — Timeout
- **Channel S** — Bangladesh — streak 1 — HTTP 523
- **Channel S UK** — Bangladesh — streak 1 — Timeout
- **G TV** — Bangladesh — streak 1 — Timeout
- **Green TV** — Bangladesh — streak 2 — Timeout
- **Jago News 24** — Bangladesh — streak 1 — Timeout
- **Jonmobhumi TV** — Bangladesh — streak 1 — HTTP 404
- **NRB TV** — Bangladesh — streak 1 — Timeout
- **NTV Europe** — Bangladesh — streak 1 — HTTP 523
- **Time Television** — Bangladesh — streak 1 — Timeout
- **Amar Bangla** — Indian Bangla — streak 1 — Timeout
- **Channel 52** — Indian Bangla — streak 1 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 212 — HTTP 403
- **Oli TV** — Indian Entertainment — streak 6 — Timeout
- **Suriyan TV** — Indian Entertainment — streak 6 — HTTP 523
- **K Cine** — Indian Movies — streak 3 — Timeout
- **Afrobeats** — International — streak 3 — HTTP 404
- **Cook & Bake** — International — streak 18 — HTTP 504
- **HBO** — International — streak 200 — HTTP 403
- **Teleritmo** — International — streak 18 — HTTP 403
- **iON TV UK** — International — streak 1 — Timeout
- **Teen Nick** — Kids — streak 78 — HTTP 403
- **Iqra Bangla** — Religious — streak 1 — Timeout
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
