# Stream Health Report

Generated: **2026-10-15T09:44:58+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1037**
- Reachable: **988**
- Failed this check: **49**
- Persistent failures (3+ consecutive): **11**
- Intermittent failures: **38**
- Primary tested: **652**
- Backup tested: **385**

## Failure Classification

- HTTP 401/403 (auth): **6**
- HTTP 404 (not found): **9**
- HTTP 5xx (server): **3**
- Timeout: **31**
## Persistent Failures

- **Ananda TV** — Backup — consecutive failures: **5** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **77** — HTTP 403
- **Shanson TV** — Backup — consecutive failures: **4** — HTTP 403
- **Channel 16** — Bangladesh — consecutive failures: **13** — Timeout
- **Assam Talks** — Indian Entertainment — consecutive failures: **211** — HTTP 403
- **Oli TV** — Indian Entertainment — consecutive failures: **5** — Timeout
- **Suriyan TV** — Indian Entertainment — consecutive failures: **5** — HTTP 523
- **Cook & Bake** — International — consecutive failures: **17** — HTTP 504
- **HBO** — International — consecutive failures: **199** — HTTP 403
- **Teleritmo** — International — consecutive failures: **17** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **77** — HTTP 403

## Failed This Check

- **Ananda TV** — Backup — streak 1 — Timeout
- **Ananda TV** — Backup — streak 5 — HTTP 404
- **Channel 1** — Backup — streak 1 — Timeout
- **Channel 1** — Backup — streak 1 — Timeout
- **Channel S** — Backup — streak 1 — Timeout
- **Channel S** — Backup — streak 1 — Timeout
- **Dangal** — Backup — streak 1 — HTTP 404
- **Desh TV** — Backup — streak 1 — Timeout
- **Disney Channel India** — Backup — streak 77 — HTTP 403
- **Duronto TV** — Backup — streak 2 — Timeout
- **Ekhon TV** — Backup — streak 1 — Timeout
- **Ekushey TV** — Backup — streak 1 — Timeout
- **G TV** — Backup — streak 1 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 1 — Timeout
- **Global TV** — Backup — streak 1 — Timeout
- **Goldmines** — Backup — streak 2 — HTTP 404
- **Goldmines** — Backup — streak 2 — HTTP 404
- **Manoranjan TV** — Backup — streak 1 — HTTP 404
- **Medina Live** — Backup — streak 1 — Timeout
- **Movie Bangla** — Backup — streak 1 — Timeout
- **Movie Bangla** — Backup — streak 1 — Timeout
- **My TV** — Backup — streak 1 — Timeout
- **My TV** — Backup — streak 1 — Timeout
- **RTV** — Backup — streak 1 — Timeout
- **SA TV** — Backup — streak 1 — Timeout
- **SA TV** — Backup — streak 1 — Timeout
- **Shanson TV** — Backup — streak 4 — HTTP 403
- **Ananda TV** — Bangladesh — streak 1 — Timeout
- **Bengali Beats** — Bangladesh — streak 1 — HTTP 502
- **Channel 16** — Bangladesh — streak 13 — Timeout
- **Channel 9** — Bangladesh — streak 2 — HTTP 404
- **Green TV** — Bangladesh — streak 1 — Timeout
- **Nagorik TV** — Bangladesh — streak 2 — HTTP 404
- **Jalsha Movies** — Indian Bangla — streak 2 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 211 — HTTP 403
- **Oli TV** — Indian Entertainment — streak 5 — Timeout
- **Suriyan TV** — Indian Entertainment — streak 5 — HTTP 523
- **K Cine** — Indian Movies — streak 2 — Timeout
- **Afrobeats** — International — streak 2 — HTTP 404
- **Cook & Bake** — International — streak 17 — HTTP 504
- **HBO** — International — streak 199 — HTTP 403
- **Teleritmo** — International — streak 17 — HTTP 403
- **Teen Nick** — Kids — streak 77 — HTTP 403
- **Islamic TV** — Religious — streak 1 — Timeout
- **Makkah Live** — Religious — streak 1 — Timeout
- **Astro Cricbuzz** — Sports — streak 1 — Timeout
- **FOX Cricket 501** — Sports — streak 2 — Timeout
- **Ten Sports** — Sports — streak 2 — Timeout

## Near-Duplicate URL Families

- **https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.
- **https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8** — 2 URL variants; query/token differences are preserved and require review.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
