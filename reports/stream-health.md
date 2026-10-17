# Stream Health Report

Generated: **2026-10-17T06:19:05+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1061**
- Reachable: **1032**
- Failed this check: **29**
- Persistent failures (3+ consecutive): **27**
- Intermittent failures: **2**
- Primary tested: **669**
- Backup tested: **392**

## Failure Classification

- HTTP 401/403 (auth): **10**
- HTTP 404 (not found): **11**
- HTTP 5xx (server): **1**
- Timeout: **7**
## Persistent Failures

- **7X Punjabi** — Backup — consecutive failures: **4** — HTTP 404
- **CBN TV USA** — Backup — consecutive failures: **4** — HTTP 404
- **Channel 52** — Backup — consecutive failures: **11** — HTTP 404
- **Channel S** — Backup — consecutive failures: **12** — Timeout
- **Channel S** — Backup — consecutive failures: **11** — HTTP 404
- **Channel S** — Backup — consecutive failures: **11** — HTTP 404
- **Channel S** — Backup — consecutive failures: **12** — Timeout
- **Green TV** — Backup — consecutive failures: **12** — Timeout
- **Green TV** — Backup — consecutive failures: **11** — HTTP 404
- **Green TV** — Backup — consecutive failures: **11** — HTTP 404
- **Green TV** — Backup — consecutive failures: **11** — HTTP 404
- **Green TV** — Backup — consecutive failures: **11** — HTTP 404
- **Ananda TV** — Bangladesh — consecutive failures: **12** — Timeout
- **Channel 16** — Bangladesh — consecutive failures: **24** — Timeout
- **Assam Talks** — Indian Entertainment — consecutive failures: **222** — HTTP 403
- **Oli TV** — Indian Entertainment — consecutive failures: **16** — HTTP 404
- **CMAC TV** — International — consecutive failures: **4** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **28** — HTTP 504
- **HBO** — International — consecutive failures: **210** — HTTP 403
- **Lifetime** — International — consecutive failures: **4** — HTTP 403
- **Teleritmo** — International — consecutive failures: **28** — HTTP 403
- **Teen Nick** — Kids — consecutive failures: **88** — HTTP 403
- **Makkah Live** — Religious — consecutive failures: **12** — Timeout
- **PTV** — Sports — consecutive failures: **4** — Timeout
- **Star Sports 2** — Sports — consecutive failures: **4** — HTTP 403
- **T Sports** — Sports — consecutive failures: **4** — HTTP 403
- **Willow TV** — Sports — consecutive failures: **4** — HTTP 403

## Failed This Check

- **7X Punjabi** — Backup — streak 4 — HTTP 404
- **CBN TV USA** — Backup — streak 4 — HTTP 404
- **Channel 52** — Backup — streak 11 — HTTP 404
- **Channel S** — Backup — streak 12 — Timeout
- **Channel S** — Backup — streak 11 — HTTP 404
- **Channel S** — Backup — streak 11 — HTTP 404
- **Channel S** — Backup — streak 12 — Timeout
- **Green TV** — Backup — streak 12 — Timeout
- **Green TV** — Backup — streak 11 — HTTP 404
- **Green TV** — Backup — streak 11 — HTTP 404
- **Green TV** — Backup — streak 11 — HTTP 404
- **Green TV** — Backup — streak 11 — HTTP 404
- **Jalwa TV** — Backup — streak 1 — HTTP 404
- **Shanson TV** — Backup — streak 2 — HTTP 403
- **Ananda TV** — Bangladesh — streak 12 — Timeout
- **Channel 16** — Bangladesh — streak 24 — Timeout
- **Assam Talks** — Indian Entertainment — streak 222 — HTTP 403
- **Oli TV** — Indian Entertainment — streak 16 — HTTP 404
- **CMAC TV** — International — streak 4 — HTTP 403
- **Cook & Bake** — International — streak 28 — HTTP 504
- **HBO** — International — streak 210 — HTTP 403
- **Lifetime** — International — streak 4 — HTTP 403
- **Teleritmo** — International — streak 28 — HTTP 403
- **Teen Nick** — Kids — streak 88 — HTTP 403
- **Makkah Live** — Religious — streak 12 — Timeout
- **PTV** — Sports — streak 4 — Timeout
- **Star Sports 2** — Sports — streak 4 — HTTP 403
- **T Sports** — Sports — streak 4 — HTTP 403
- **Willow TV** — Sports — streak 4 — HTTP 403

## Near-Duplicate URL Families

None.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
