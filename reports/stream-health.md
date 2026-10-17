# Stream Health Report

Generated: **2026-10-17T07:41:53+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1094**
- Reachable: **1058**
- Failed this check: **36**
- Persistent failures (3+ consecutive): **33**
- Intermittent failures: **3**
- Primary tested: **667**
- Backup tested: **427**

## Failure Classification

- HTTP 401/403 (auth): **11**
- HTTP 404 (not found): **18**
- HTTP 5xx (server): **5**
- TLS: **1**
- Timeout: **1**
## Persistent Failures

- **7X Punjabi** — Backup — consecutive failures: **12** — HTTP 404
- **CBN TV USA** — Backup — consecutive failures: **12** — HTTP 404
- **Channel 52** — Backup — consecutive failures: **19** — HTTP 404
- **Channel S** — Backup — consecutive failures: **20** — HTTP 500
- **Channel S** — Backup — consecutive failures: **19** — HTTP 404
- **Channel S** — Backup — consecutive failures: **19** — HTTP 404
- **Channel S** — Backup — consecutive failures: **20** — HTTP 404
- **Desh TV** — Backup — consecutive failures: **7** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **4** — HTTP 403
- **ESPN** — Backup — consecutive failures: **4** — HTTP 403
- **G TV** — Backup — consecutive failures: **4** — HTTP 500
- **G TV** — Backup — consecutive failures: **4** — HTTP 404
- **G TV** — Backup — consecutive failures: **4** — TLS
- **G TV** — Backup — consecutive failures: **4** — HTTP 500
- **Goldmines Movies** — Backup — consecutive failures: **4** — HTTP 404
- **Green TV** — Backup — consecutive failures: **20** — HTTP 404
- **Green TV** — Backup — consecutive failures: **19** — HTTP 404
- **Green TV** — Backup — consecutive failures: **19** — HTTP 404
- **Green TV** — Backup — consecutive failures: **19** — HTTP 404
- **Green TV** — Backup — consecutive failures: **19** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **230** — HTTP 403
- **Star Gold** — Indian Movies — consecutive failures: **8** — HTTP 404
- **CMAC TV** — International — consecutive failures: **12** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **36** — HTTP 504
- **HBO** — International — consecutive failures: **218** — HTTP 403
- **Lifetime** — International — consecutive failures: **12** — HTTP 403
- **NASHE Music** — International — consecutive failures: **3** — HTTP 404
- **Teleritmo** — International — consecutive failures: **36** — HTTP 403
- **Nick** — Kids — consecutive failures: **8** — Timeout
- **Teen Nick** — Kids — consecutive failures: **96** — HTTP 403
- **Star Sports 2** — Sports — consecutive failures: **12** — HTTP 403
- **T Sports** — Sports — consecutive failures: **12** — HTTP 403
- **Willow TV** — Sports — consecutive failures: **12** — HTTP 403

## Failed This Check

- **7X Punjabi** — Backup — streak 12 — HTTP 404
- **CBN TV USA** — Backup — streak 12 — HTTP 404
- **Channel 52** — Backup — streak 19 — HTTP 404
- **Channel S** — Backup — streak 20 — HTTP 500
- **Channel S** — Backup — streak 19 — HTTP 404
- **Channel S** — Backup — streak 19 — HTTP 404
- **Channel S** — Backup — streak 20 — HTTP 404
- **Desh TV** — Backup — streak 7 — HTTP 404
- **Disney Channel India** — Backup — streak 4 — HTTP 403
- **ESPN** — Backup — streak 4 — HTTP 403
- **G TV** — Backup — streak 4 — HTTP 500
- **G TV** — Backup — streak 1 — HTTP 404
- **G TV** — Backup — streak 4 — HTTP 404
- **G TV** — Backup — streak 4 — TLS
- **G TV** — Backup — streak 4 — HTTP 500
- **Goldmines Movies** — Backup — streak 4 — HTTP 404
- **Green TV** — Backup — streak 20 — HTTP 404
- **Green TV** — Backup — streak 19 — HTTP 404
- **Green TV** — Backup — streak 19 — HTTP 404
- **Green TV** — Backup — streak 19 — HTTP 404
- **Green TV** — Backup — streak 19 — HTTP 404
- **Movie Bangla** — Backup — streak 1 — HTTP 500
- **Sony Entertainment TV** — Backup — streak 1 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 230 — HTTP 403
- **Star Gold** — Indian Movies — streak 8 — HTTP 404
- **CMAC TV** — International — streak 12 — HTTP 403
- **Cook & Bake** — International — streak 36 — HTTP 504
- **HBO** — International — streak 218 — HTTP 403
- **Lifetime** — International — streak 12 — HTTP 403
- **NASHE Music** — International — streak 3 — HTTP 404
- **Teleritmo** — International — streak 36 — HTTP 403
- **Nick** — Kids — streak 8 — Timeout
- **Teen Nick** — Kids — streak 96 — HTTP 403
- **Star Sports 2** — Sports — streak 12 — HTTP 403
- **T Sports** — Sports — streak 12 — HTTP 403
- **Willow TV** — Sports — streak 12 — HTTP 403

## Near-Duplicate URL Families

None.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
