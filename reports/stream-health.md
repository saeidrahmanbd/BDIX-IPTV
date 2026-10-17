# Stream Health Report

Generated: **2026-10-17T08:12:07+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1094**
- Reachable: **1053**
- Failed this check: **41**
- Persistent failures (3+ consecutive): **31**
- Intermittent failures: **10**
- Primary tested: **667**
- Backup tested: **427**

## Failure Classification

- HTTP 401/403 (auth): **12**
- HTTP 404 (not found): **14**
- HTTP 5xx (server): **5**
- TLS: **1**
- Timeout: **9**
## Persistent Failures

- **CBN TV USA** — Backup — consecutive failures: **16** — HTTP 404
- **Channel 52** — Backup — consecutive failures: **23** — HTTP 404
- **Channel S** — Backup — consecutive failures: **24** — HTTP 404
- **Channel S** — Backup — consecutive failures: **23** — HTTP 404
- **Channel S** — Backup — consecutive failures: **23** — HTTP 404
- **Channel S** — Backup — consecutive failures: **24** — HTTP 404
- **Desh TV** — Backup — consecutive failures: **11** — Timeout
- **Disney Channel India** — Backup — consecutive failures: **8** — HTTP 403
- **ESPN** — Backup — consecutive failures: **8** — HTTP 403
- **G TV** — Backup — consecutive failures: **8** — HTTP 500
- **G TV** — Backup — consecutive failures: **8** — HTTP 404
- **G TV** — Backup — consecutive failures: **8** — TLS
- **G TV** — Backup — consecutive failures: **8** — HTTP 500
- **Green TV** — Backup — consecutive failures: **24** — HTTP 404
- **Green TV** — Backup — consecutive failures: **23** — HTTP 404
- **Green TV** — Backup — consecutive failures: **23** — HTTP 404
- **Green TV** — Backup — consecutive failures: **23** — HTTP 404
- **Green TV** — Backup — consecutive failures: **23** — HTTP 404
- **Shanson TV** — Backup — consecutive failures: **4** — HTTP 403
- **Assam Talks** — Indian Entertainment — consecutive failures: **234** — HTTP 403
- **Star Gold** — Indian Movies — consecutive failures: **12** — HTTP 404
- **CMAC TV** — International — consecutive failures: **16** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **40** — HTTP 504
- **HBO** — International — consecutive failures: **222** — HTTP 403
- **Lifetime** — International — consecutive failures: **16** — HTTP 403
- **Teleritmo** — International — consecutive failures: **40** — HTTP 403
- **Nick** — Kids — consecutive failures: **12** — Timeout
- **Teen Nick** — Kids — consecutive failures: **100** — HTTP 403
- **Star Sports 2** — Sports — consecutive failures: **16** — HTTP 403
- **T Sports** — Sports — consecutive failures: **16** — HTTP 403
- **Willow TV** — Sports — consecutive failures: **16** — HTTP 403

## Failed This Check

- **ATN Bangla** — Backup — streak 1 — Timeout
- **Aakaash Aath** — Backup — streak 1 — Timeout
- **CBN TV USA** — Backup — streak 16 — HTTP 404
- **Channel 52** — Backup — streak 23 — HTTP 404
- **Channel S** — Backup — streak 24 — HTTP 404
- **Channel S** — Backup — streak 23 — HTTP 404
- **Channel S** — Backup — streak 23 — HTTP 404
- **Channel S** — Backup — streak 24 — HTTP 404
- **Desh TV** — Backup — streak 11 — Timeout
- **Disney Channel India** — Backup — streak 8 — HTTP 403
- **ESPN** — Backup — streak 8 — HTTP 403
- **G TV** — Backup — streak 8 — HTTP 500
- **G TV** — Backup — streak 1 — HTTP 404
- **G TV** — Backup — streak 8 — HTTP 404
- **G TV** — Backup — streak 8 — TLS
- **G TV** — Backup — streak 8 — HTTP 500
- **Green TV** — Backup — streak 24 — HTTP 404
- **Green TV** — Backup — streak 23 — HTTP 404
- **Green TV** — Backup — streak 23 — HTTP 404
- **Green TV** — Backup — streak 23 — HTTP 404
- **Green TV** — Backup — streak 23 — HTTP 404
- **Maasranga TV** — Backup — streak 1 — Timeout
- **Maasranga TV** — Backup — streak 1 — Timeout
- **RTV** — Backup — streak 1 — Timeout
- **Shanson TV** — Backup — streak 4 — HTTP 403
- **Somoy TV** — Backup — streak 1 — Timeout
- **Ananda TV** — Bangladesh — streak 1 — HTTP 500
- **Channel S UK** — Bangladesh — streak 1 — HTTP 500
- **Assam Talks** — Indian Entertainment — streak 234 — HTTP 403
- **Star Gold** — Indian Movies — streak 12 — HTTP 404
- **CMAC TV** — International — streak 16 — HTTP 403
- **Cook & Bake** — International — streak 40 — HTTP 504
- **HBO** — International — streak 222 — HTTP 403
- **Lifetime** — International — streak 16 — HTTP 403
- **Teleritmo** — International — streak 40 — HTTP 403
- **Nick** — Kids — streak 12 — Timeout
- **Teen Nick** — Kids — streak 100 — HTTP 403
- **PTV** — Sports — streak 1 — Timeout
- **Star Sports 2** — Sports — streak 16 — HTTP 403
- **T Sports** — Sports — streak 16 — HTTP 403
- **Willow TV** — Sports — streak 16 — HTTP 403

## Near-Duplicate URL Families

None.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
