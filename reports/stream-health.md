# Stream Health Report

Generated: **2026-10-17T06:32:10+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1060**
- Reachable: **1025**
- Failed this check: **35**
- Persistent failures (3+ consecutive): **23**
- Intermittent failures: **12**
- Primary tested: **669**
- Backup tested: **391**

## Failure Classification

- HTTP 401/403 (auth): **11**
- HTTP 404 (not found): **22**
- HTTP 5xx (server): **1**
- Timeout: **1**
## Persistent Failures

- **7X Punjabi** — Backup — consecutive failures: **6** — HTTP 404
- **CBN TV USA** — Backup — consecutive failures: **6** — HTTP 404
- **Channel 52** — Backup — consecutive failures: **13** — HTTP 404
- **Channel S** — Backup — consecutive failures: **14** — HTTP 404
- **Channel S** — Backup — consecutive failures: **13** — HTTP 404
- **Channel S** — Backup — consecutive failures: **13** — HTTP 404
- **Channel S** — Backup — consecutive failures: **14** — HTTP 404
- **Green TV** — Backup — consecutive failures: **14** — HTTP 404
- **Green TV** — Backup — consecutive failures: **13** — HTTP 404
- **Green TV** — Backup — consecutive failures: **13** — HTTP 404
- **Green TV** — Backup — consecutive failures: **13** — HTTP 404
- **Green TV** — Backup — consecutive failures: **13** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **224** — HTTP 403
- **Oli TV** — Indian Entertainment — consecutive failures: **18** — HTTP 404
- **CMAC TV** — International — consecutive failures: **6** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **30** — HTTP 504
- **HBO** — International — consecutive failures: **212** — HTTP 403
- **Lifetime** — International — consecutive failures: **6** — HTTP 403
- **Teleritmo** — International — consecutive failures: **30** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **90** — HTTP 403
- **Star Sports 2** — Sports — consecutive failures: **6** — HTTP 403
- **T Sports** — Sports — consecutive failures: **6** — HTTP 403
- **Willow TV** — Sports — consecutive failures: **6** — HTTP 403

## Failed This Check

- **7X Punjabi** — Backup — streak 6 — HTTP 404
- **Balle Balle** — Backup — streak 1 — HTTP 404
- **CBN TV USA** — Backup — streak 6 — HTTP 404
- **Channel 52** — Backup — streak 13 — HTTP 404
- **Channel S** — Backup — streak 14 — HTTP 404
- **Channel S** — Backup — streak 13 — HTTP 404
- **Channel S** — Backup — streak 13 — HTTP 404
- **Channel S** — Backup — streak 14 — HTTP 404
- **Dangal 2** — Backup — streak 2 — HTTP 404
- **Dangal 2** — Backup — streak 2 — HTTP 404
- **Desh TV** — Backup — streak 1 — HTTP 403
- **Green TV** — Backup — streak 14 — HTTP 404
- **Green TV** — Backup — streak 13 — HTTP 404
- **Green TV** — Backup — streak 13 — HTTP 404
- **Green TV** — Backup — streak 13 — HTTP 404
- **Green TV** — Backup — streak 13 — HTTP 404
- **Jalwa TV** — Backup — streak 1 — HTTP 404
- **Zee Bangla** — Backup — streak 1 — HTTP 404
- **Zee Cinema** — Backup — streak 1 — HTTP 404
- **Channel S UK** — Bangladesh — streak 1 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 224 — HTTP 403
- **Oli TV** — Indian Entertainment — streak 18 — HTTP 404
- **Star Gold** — Indian Movies — streak 2 — HTTP 403
- **CMAC TV** — International — streak 6 — HTTP 403
- **Cook & Bake** — International — streak 30 — HTTP 504
- **HBO** — International — streak 212 — HTTP 403
- **HBO 2** — International — streak 1 — HTTP 404
- **Lifetime** — International — streak 6 — HTTP 403
- **Teleritmo** — International — streak 30 — HTTP 403
- **Nick** — Kids — streak 2 — Timeout
- **Teen Nick** — Kids — streak 90 — HTTP 403
- **Jalwa TV** — Pakistani — streak 1 — HTTP 404
- **Star Sports 2** — Sports — streak 6 — HTTP 403
- **T Sports** — Sports — streak 6 — HTTP 403
- **Willow TV** — Sports — streak 6 — HTTP 403

## Near-Duplicate URL Families

None.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
