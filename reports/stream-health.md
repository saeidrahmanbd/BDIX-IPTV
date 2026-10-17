# Stream Health Report

Generated: **2026-10-17T07:52:34+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1094**
- Reachable: **1053**
- Failed this check: **41**
- Persistent failures (3+ consecutive): **30**
- Intermittent failures: **11**
- Primary tested: **667**
- Backup tested: **427**

## Failure Classification

- HTTP 401/403 (auth): **12**
- HTTP 404 (not found): **23**
- HTTP 5xx (server): **4**
- TLS: **1**
- Timeout: **1**
## Persistent Failures

- **CBN TV USA** — Backup — consecutive failures: **14** — HTTP 404
- **Channel 52** — Backup — consecutive failures: **21** — HTTP 404
- **Channel S** — Backup — consecutive failures: **22** — HTTP 404
- **Channel S** — Backup — consecutive failures: **21** — HTTP 404
- **Channel S** — Backup — consecutive failures: **21** — HTTP 404
- **Channel S** — Backup — consecutive failures: **22** — HTTP 404
- **Desh TV** — Backup — consecutive failures: **9** — HTTP 404
- **Disney Channel India** — Backup — consecutive failures: **6** — HTTP 403
- **ESPN** — Backup — consecutive failures: **6** — HTTP 403
- **G TV** — Backup — consecutive failures: **6** — HTTP 500
- **G TV** — Backup — consecutive failures: **6** — HTTP 404
- **G TV** — Backup — consecutive failures: **6** — TLS
- **G TV** — Backup — consecutive failures: **6** — HTTP 500
- **Green TV** — Backup — consecutive failures: **22** — HTTP 404
- **Green TV** — Backup — consecutive failures: **21** — HTTP 404
- **Green TV** — Backup — consecutive failures: **21** — HTTP 404
- **Green TV** — Backup — consecutive failures: **21** — HTTP 404
- **Green TV** — Backup — consecutive failures: **21** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **232** — HTTP 403
- **Star Gold** — Indian Movies — consecutive failures: **10** — HTTP 404
- **CMAC TV** — International — consecutive failures: **14** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **38** — HTTP 504
- **HBO** — International — consecutive failures: **220** — HTTP 403
- **Lifetime** — International — consecutive failures: **14** — HTTP 403
- **Teleritmo** — International — consecutive failures: **38** — HTTP 403
- **Nick** — Kids — consecutive failures: **10** — Timeout
- **Teen Nick** — Kids — consecutive failures: **98** — HTTP 403
- **Star Sports 2** — Sports — consecutive failures: **14** — HTTP 403
- **T Sports** — Sports — consecutive failures: **14** — HTTP 403
- **Willow TV** — Sports — consecutive failures: **14** — HTTP 403

## Failed This Check

- **CBN TV USA** — Backup — streak 14 — HTTP 404
- **Channel 52** — Backup — streak 21 — HTTP 404
- **Channel S** — Backup — streak 22 — HTTP 404
- **Channel S** — Backup — streak 21 — HTTP 404
- **Channel S** — Backup — streak 21 — HTTP 404
- **Channel S** — Backup — streak 22 — HTTP 404
- **Dangal** — Backup — streak 1 — HTTP 404
- **Desh TV** — Backup — streak 9 — HTTP 404
- **Disney Channel India** — Backup — streak 6 — HTTP 403
- **ESPN** — Backup — streak 6 — HTTP 403
- **G TV** — Backup — streak 6 — HTTP 500
- **G TV** — Backup — streak 6 — HTTP 404
- **G TV** — Backup — streak 6 — TLS
- **G TV** — Backup — streak 6 — HTTP 500
- **Goldmines Movies** — Backup — streak 1 — HTTP 404
- **Green TV** — Backup — streak 22 — HTTP 404
- **Green TV** — Backup — streak 21 — HTTP 404
- **Green TV** — Backup — streak 21 — HTTP 404
- **Green TV** — Backup — streak 21 — HTTP 404
- **Green TV** — Backup — streak 21 — HTTP 404
- **Independent TV** — Backup — streak 2 — HTTP 404
- **Manoranjan TV** — Backup — streak 1 — HTTP 404
- **Shanson TV** — Backup — streak 2 — HTTP 403
- **Sony Entertainment TV** — Backup — streak 1 — HTTP 404
- **Sony SAB** — Backup — streak 1 — HTTP 404
- **Zee TV** — Backup — streak 1 — HTTP 404
- **Channel S UK** — Bangladesh — streak 1 — HTTP 500
- **Jalsha Movies HD** — Indian Bangla — streak 2 — HTTP 404
- **Assam Talks** — Indian Entertainment — streak 232 — HTTP 403
- **Colors Infinity** — Indian Entertainment — streak 1 — HTTP 404
- **Star Gold** — Indian Movies — streak 10 — HTTP 404
- **CMAC TV** — International — streak 14 — HTTP 403
- **Cook & Bake** — International — streak 38 — HTTP 504
- **HBO** — International — streak 220 — HTTP 403
- **Lifetime** — International — streak 14 — HTTP 403
- **Teleritmo** — International — streak 38 — HTTP 403
- **Nick** — Kids — streak 10 — Timeout
- **Teen Nick** — Kids — streak 98 — HTTP 403
- **Star Sports 2** — Sports — streak 14 — HTTP 403
- **T Sports** — Sports — streak 14 — HTTP 403
- **Willow TV** — Sports — streak 14 — HTTP 403

## Near-Duplicate URL Families

None.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
