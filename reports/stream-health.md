# Stream Health Report

Generated: **2026-10-15T06:06:33+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1043**
- Reachable: **990**
- Failed this check: **53**
- Persistent failures (3+ consecutive): **4**
- Intermittent failures: **49**
- Primary tested: **636**
- Backup tested: **407**

## Failure Classification

- HTTP 401/403 (auth): **6**
- HTTP 404 (not found): **11**
- HTTP 5xx (server): **2**
- Timeout: **34**
## Persistent Failures

- **Disney Channel India** — Backup — consecutive failures: **62** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **196** — HTTP 403
- **HBO** — International — consecutive failures: **184** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **62** — HTTP 403

## Failed This Check

- **Ananda TV** — Backup — streak 2 — Timeout
- **Balle Balle** — Backup — streak 1 — HTTP 404
- **Channel 1** — Backup — streak 2 — Timeout
- **Channel 1** — Backup — streak 2 — Timeout
- **Channel 16** — Backup — streak 2 — Timeout
- **Channel S** — Backup — streak 2 — Timeout
- **Channel S** — Backup — streak 2 — Timeout
- **Dangal** — Backup — streak 2 — HTTP 404
- **Dangal 2** — Backup — streak 2 — HTTP 404
- **Dangal 2** — Backup — streak 2 — HTTP 404
- **Desh TV** — Backup — streak 2 — Timeout
- **Disney Channel India** — Backup — streak 62 — HTTP 403
- **Ekhon TV** — Backup — streak 2 — Timeout
- **Ekushey TV** — Backup — streak 1 — Timeout
- **Ekushey TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **Global TV** — Backup — streak 2 — Timeout
- **Goldmines** — Backup — streak 2 — HTTP 404
- **Goldmines** — Backup — streak 2 — HTTP 404
- **Hum TV** — Backup — streak 1 — Timeout
- **MH One Dil Se** — Backup — streak 1 — HTTP 404
- **MH One Movies** — Backup — streak 2 — HTTP 404
- **MH One Prime** — Backup — streak 1 — HTTP 404
- **Manoranjan TV** — Backup — streak 2 — HTTP 404
- **Medina Live** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 2 — Timeout
- **RTV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **Shanson TV** — Backup — streak 2 — HTTP 403
- **Suriyan TV** — Backup — streak 2 — Timeout
- **Ananda TV** — Bangladesh — streak 2 — Timeout
- **Green TV** — Bangladesh — streak 2 — Timeout
- **Aaryaa TV** — Indian Entertainment — streak 1 — Timeout
- **Assam Talks** — Indian Entertainment — streak 196 — HTTP 403
- **NKR TV Kannada** — Indian Entertainment — streak 1 — Timeout
- **Sana TV** — Indian Entertainment — streak 2 — HTTP 504
- **Suriya TV** — Indian Entertainment — streak 1 — Timeout
- **Vaanavil TV** — Indian Entertainment — streak 1 — Timeout
- **MH One Movies** — Indian Movies — streak 2 — HTTP 404
- **Punjabi Hits** — Indian Music — streak 2 — Timeout
- **Ultimate TV** — Indian Music — streak 1 — Timeout
- **Cook & Bake** — International — streak 2 — HTTP 504
- **HBO** — International — streak 184 — HTTP 403
- **Teleritmo** — International — streak 2 — HTTP 403
- **Teen Nick** — Kids — streak 62 — HTTP 403
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
