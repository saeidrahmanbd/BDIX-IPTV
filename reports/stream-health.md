# Stream Health Report

Generated: **2026-10-17T07:02:19+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1060**
- Reachable: **1029**
- Failed this check: **31**
- Persistent failures (3+ consecutive): **28**
- Intermittent failures: **3**
- Primary tested: **667**
- Backup tested: **393**

## Failure Classification

- HTTP 401/403 (auth): **10**
- HTTP 404 (not found): **18**
- HTTP 5xx (server): **2**
- Timeout: **1**
## Persistent Failures

- **7X Punjabi** — Backup — consecutive failures: **8** — HTTP 404
- **CBN TV USA** — Backup — consecutive failures: **8** — HTTP 404
- **Channel 52** — Backup — consecutive failures: **15** — HTTP 404
- **Channel S** — Backup — consecutive failures: **16** — HTTP 404
- **Channel S** — Backup — consecutive failures: **15** — HTTP 404
- **Channel S** — Backup — consecutive failures: **15** — HTTP 404
- **Channel S** — Backup — consecutive failures: **16** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **4** — HTTP 404
- **Dangal 2** — Backup — consecutive failures: **4** — HTTP 404
- **Desh TV** — Backup — consecutive failures: **3** — HTTP 404
- **Green TV** — Backup — consecutive failures: **16** — HTTP 404
- **Green TV** — Backup — consecutive failures: **15** — HTTP 404
- **Green TV** — Backup — consecutive failures: **15** — HTTP 404
- **Green TV** — Backup — consecutive failures: **15** — HTTP 404
- **Green TV** — Backup — consecutive failures: **15** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **226** — HTTP 403
- **Star Gold** — Indian Movies — consecutive failures: **4** — HTTP 404
- **CMAC TV** — International — consecutive failures: **8** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **32** — HTTP 504
- **HBO** — International — consecutive failures: **214** — HTTP 403
- **Lifetime** — International — consecutive failures: **8** — HTTP 403
- **Teleritmo** — International — consecutive failures: **32** — HTTP 403
- **Nick** — Kids — consecutive failures: **4** — Timeout
- **Teen Nick** — Kids — consecutive failures: **92** — HTTP 403
- **Jalwa TV** — Pakistani — consecutive failures: **3** — HTTP 404
- **Star Sports 2** — Sports — consecutive failures: **8** — HTTP 403
- **T Sports** — Sports — consecutive failures: **8** — HTTP 403
- **Willow TV** — Sports — consecutive failures: **8** — HTTP 403

## Failed This Check

- **7X Punjabi** — Backup — streak 8 — HTTP 404
- **CBN TV USA** — Backup — streak 8 — HTTP 404
- **Channel 52** — Backup — streak 15 — HTTP 404
- **Channel S** — Backup — streak 16 — HTTP 404
- **Channel S** — Backup — streak 15 — HTTP 404
- **Channel S** — Backup — streak 15 — HTTP 404
- **Channel S** — Backup — streak 16 — HTTP 404
- **Dangal 2** — Backup — streak 4 — HTTP 404
- **Dangal 2** — Backup — streak 4 — HTTP 404
- **Desh TV** — Backup — streak 3 — HTTP 404
- **G TV** — Backup — streak 1 — HTTP 404
- **Green TV** — Backup — streak 16 — HTTP 404
- **Green TV** — Backup — streak 15 — HTTP 404
- **Green TV** — Backup — streak 15 — HTTP 404
- **Green TV** — Backup — streak 15 — HTTP 404
- **Green TV** — Backup — streak 15 — HTTP 404
- **Investigation Discovery** — Backup — streak 1 — HTTP 403
- **Assam Talks** — Indian Entertainment — streak 226 — HTTP 403
- **Star Gold** — Indian Movies — streak 4 — HTTP 404
- **CMAC TV** — International — streak 8 — HTTP 403
- **Cook & Bake** — International — streak 32 — HTTP 504
- **HBO** — International — streak 214 — HTTP 403
- **Lifetime** — International — streak 8 — HTTP 403
- **Teleritmo** — International — streak 32 — HTTP 403
- **Bantul the Great** — Kids — streak 1 — HTTP 502
- **Nick** — Kids — streak 4 — Timeout
- **Teen Nick** — Kids — streak 92 — HTTP 403
- **Jalwa TV** — Pakistani — streak 3 — HTTP 404
- **Star Sports 2** — Sports — streak 8 — HTTP 403
- **T Sports** — Sports — streak 8 — HTTP 403
- **Willow TV** — Sports — streak 8 — HTTP 403

## Near-Duplicate URL Families

None.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
