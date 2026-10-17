# Stream Health Report

Generated: **2026-10-17T06:08:43+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1074**
- Reachable: **1030**
- Failed this check: **44**
- Persistent failures (3+ consecutive): **19**
- Intermittent failures: **25**
- Primary tested: **669**
- Backup tested: **405**

## Failure Classification

- HTTP 401/403 (auth): **10**
- HTTP 404 (not found): **20**
- HTTP 5xx (server): **1**
- Timeout: **13**
## Persistent Failures

- **Channel 52** — Backup — consecutive failures: **9** — HTTP 404
- **Channel S** — Backup — consecutive failures: **10** — Timeout
- **Channel S** — Backup — consecutive failures: **9** — HTTP 404
- **Channel S** — Backup — consecutive failures: **9** — HTTP 404
- **Channel S** — Backup — consecutive failures: **10** — Timeout
- **Green TV** — Backup — consecutive failures: **10** — Timeout
- **Green TV** — Backup — consecutive failures: **9** — HTTP 404
- **Green TV** — Backup — consecutive failures: **9** — HTTP 404
- **Green TV** — Backup — consecutive failures: **9** — HTTP 404
- **Green TV** — Backup — consecutive failures: **9** — HTTP 404
- **Ananda TV** — Bangladesh — consecutive failures: **10** — Timeout
- **Channel 16** — Bangladesh — consecutive failures: **22** — Timeout
- **Assam Talks** — Indian Entertainment — consecutive failures: **220** — HTTP 403
- **Oli TV** — Indian Entertainment — consecutive failures: **14** — HTTP 404
- **Cook & Bake** — International — consecutive failures: **26** — HTTP 504
- **HBO** — International — consecutive failures: **208** — HTTP 403
- **Teleritmo** — International — consecutive failures: **26** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **86** — HTTP 403
- **Makkah Live** — Religious — consecutive failures: **10** — Timeout

## Failed This Check

- **7X Punjabi** — Backup — streak 2 — HTTP 404
- **ATN Bangla** — Backup — streak 2 — Timeout
- **Aakaash Aath** — Backup — streak 2 — Timeout
- **Bahrain Sports 2** — Backup — streak 2 — HTTP 404
- **CBN TV USA** — Backup — streak 2 — HTTP 404
- **Channel 24** — Backup — streak 1 — HTTP 404
- **Channel 52** — Backup — streak 9 — HTTP 404
- **Channel S** — Backup — streak 10 — Timeout
- **Channel S** — Backup — streak 9 — HTTP 404
- **Channel S** — Backup — streak 9 — HTTP 404
- **Channel S** — Backup — streak 10 — Timeout
- **ESPN** — Backup — streak 2 — HTTP 403
- **Goldmines Movies** — Backup — streak 2 — HTTP 404
- **Green TV** — Backup — streak 10 — Timeout
- **Green TV** — Backup — streak 9 — HTTP 404
- **Green TV** — Backup — streak 9 — HTTP 404
- **Green TV** — Backup — streak 9 — HTTP 404
- **Green TV** — Backup — streak 9 — HTTP 404
- **Independent TV** — Backup — streak 2 — HTTP 404
- **Maasranga TV** — Backup — streak 2 — Timeout
- **Maasranga TV** — Backup — streak 2 — Timeout
- **NTV (Malayalam)** — Backup — streak 2 — HTTP 404
- **RTV** — Backup — streak 2 — Timeout
- **Somoy TV** — Backup — streak 2 — Timeout
- **Sony Aath** — Backup — streak 1 — HTTP 404
- **Sony SAB** — Backup — streak 2 — HTTP 404
- **Zee TV** — Backup — streak 2 — HTTP 404
- **Ananda TV** — Bangladesh — streak 10 — Timeout
- **Channel 16** — Bangladesh — streak 22 — Timeout
- **Jalsha Movies HD** — Indian Bangla — streak 2 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 220 — HTTP 403
- **Colors Infinity** — Indian Entertainment — streak 2 — HTTP 404
- **Oli TV** — Indian Entertainment — streak 14 — HTTP 404
- **CMAC TV** — International — streak 2 — HTTP 403
- **Cook & Bake** — International — streak 26 — HTTP 504
- **HBO** — International — streak 208 — HTTP 403
- **Lifetime** — International — streak 2 — HTTP 403
- **Teleritmo** — International — streak 26 — HTTP 403
- **Teen Nick** — Kids — streak 86 — HTTP 403
- **Makkah Live** — Religious — streak 10 — Timeout
- **PTV** — Sports — streak 2 — Timeout
- **Star Sports 2** — Sports — streak 2 — HTTP 403
- **T Sports** — Sports — streak 2 — HTTP 403
- **Willow TV** — Sports — streak 2 — HTTP 403

## Near-Duplicate URL Families

None.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
