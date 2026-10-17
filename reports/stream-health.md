# Stream Health Report

Generated: **2026-10-17T07:32:21+00:00**

Non-destructive connectivity check. A successful HTTP response confirms reachability of the stream endpoint, not guaranteed video/audio playback.

## Summary

- Streams tested: **1094**
- Reachable: **1033**
- Failed this check: **61**
- Persistent failures (3+ consecutive): **26**
- Intermittent failures: **35**
- Primary tested: **667**
- Backup tested: **427**

## Failure Classification

- HTTP 401/403 (auth): **12**
- HTTP 404 (not found): **20**
- HTTP 5xx (server): **3**
- Timeout: **26**
## Persistent Failures

- **7X Punjabi** — Backup — consecutive failures: **10** — HTTP 404
- **CBN TV USA** — Backup — consecutive failures: **10** — HTTP 404
- **Channel 52** — Backup — consecutive failures: **17** — HTTP 404
- **Channel S** — Backup — consecutive failures: **18** — Timeout
- **Channel S** — Backup — consecutive failures: **17** — HTTP 404
- **Channel S** — Backup — consecutive failures: **17** — HTTP 404
- **Channel S** — Backup — consecutive failures: **18** — Timeout
- **Desh TV** — Backup — consecutive failures: **5** — HTTP 404
- **Green TV** — Backup — consecutive failures: **18** — Timeout
- **Green TV** — Backup — consecutive failures: **17** — HTTP 404
- **Green TV** — Backup — consecutive failures: **17** — HTTP 404
- **Green TV** — Backup — consecutive failures: **17** — HTTP 404
- **Green TV** — Backup — consecutive failures: **17** — HTTP 404
- **Assam Talks** — Indian Entertainment — consecutive failures: **228** — HTTP 403
- **Star Gold** — Indian Movies — consecutive failures: **6** — HTTP 404
- **CMAC TV** — International — consecutive failures: **10** — HTTP 403
- **Cook & Bake** — International — consecutive failures: **34** — HTTP 504
- **HBO** — International — consecutive failures: **216** — HTTP 403
- **Lifetime** — International — consecutive failures: **10** — HTTP 403
- **Teleritmo** — International — consecutive failures: **34** — HTTP 403
- **Nick** — Kids — consecutive failures: **6** — Timeout
- **Teen Nick** — Kids — consecutive failures: **94** — HTTP 403
- **Jalwa TV** — Pakistani — consecutive failures: **5** — HTTP 404
- **Star Sports 2** — Sports — consecutive failures: **10** — HTTP 403
- **T Sports** — Sports — consecutive failures: **10** — HTTP 403
- **Willow TV** — Sports — consecutive failures: **10** — HTTP 403

## Failed This Check

- **7X Punjabi** — Backup — streak 10 — HTTP 404
- **Amar Bangla Digital** — Backup — streak 1 — HTTP 500
- **Ananda TV** — Backup — streak 2 — Timeout
- **Ananda TV** — Backup — streak 1 — HTTP 500
- **Bahrain Sports 2** — Backup — streak 2 — HTTP 404
- **CBN TV USA** — Backup — streak 10 — HTTP 404
- **Channel 1** — Backup — streak 2 — Timeout
- **Channel 1** — Backup — streak 2 — Timeout
- **Channel 52** — Backup — streak 17 — HTTP 404
- **Channel S** — Backup — streak 18 — Timeout
- **Channel S** — Backup — streak 17 — HTTP 404
- **Channel S** — Backup — streak 17 — HTTP 404
- **Channel S** — Backup — streak 18 — Timeout
- **Desh TV** — Backup — streak 2 — Timeout
- **Desh TV** — Backup — streak 5 — HTTP 404
- **Disney Channel India** — Backup — streak 2 — HTTP 403
- **ESPN** — Backup — streak 2 — HTTP 403
- **Ekhon TV** — Backup — streak 2 — Timeout
- **Ekushey TV** — Backup — streak 2 — Timeout
- **Ekushey TV** — Backup — streak 1 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — HTTP 404
- **G TV** — Backup — streak 2 — Timeout
- **G TV** — Backup — streak 2 — Timeout
- **Global TV** — Backup — streak 2 — Timeout
- **Goldmines Movies** — Backup — streak 2 — HTTP 404
- **Green TV** — Backup — streak 18 — Timeout
- **Green TV** — Backup — streak 17 — HTTP 404
- **Green TV** — Backup — streak 17 — HTTP 404
- **Green TV** — Backup — streak 17 — HTTP 404
- **Green TV** — Backup — streak 17 — HTTP 404
- **Independent TV** — Backup — streak 2 — HTTP 404
- **Jalwa TV** — Backup — streak 2 — HTTP 404
- **Medina Live** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **Movie Bangla** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 2 — Timeout
- **My TV** — Backup — streak 2 — Timeout
- **NTV** — Backup — streak 2 — HTTP 404
- **RTV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **SA TV** — Backup — streak 2 — Timeout
- **Shanson TV** — Backup — streak 2 — HTTP 403
- **Star Jalsha** — Backup — streak 2 — HTTP 404
- **Ananda TV** — Bangladesh — streak 2 — Timeout
- **Channel 16** — Bangladesh — streak 2 — Timeout
- **Assam Talks** — Indian Entertainment — streak 228 — HTTP 403
- **Star Gold** — Indian Movies — streak 6 — HTTP 404
- **CMAC TV** — International — streak 10 — HTTP 403
- **Cook & Bake** — International — streak 34 — HTTP 504
- **HBO** — International — streak 216 — HTTP 403
- **Lifetime** — International — streak 10 — HTTP 403
- **NASHE Music** — International — streak 1 — HTTP 404
- **Teleritmo** — International — streak 34 — HTTP 403
- **Nick** — Kids — streak 6 — Timeout
- **Teen Nick** — Kids — streak 94 — HTTP 403
- **Jalwa TV** — Pakistani — streak 5 — HTTP 404
- **Makkah Live** — Religious — streak 2 — Timeout
- **Star Sports 2** — Sports — streak 10 — HTTP 403
- **T Sports** — Sports — streak 10 — HTTP 403
- **Willow TV** — Sports — streak 10 — HTTP 403

## Near-Duplicate URL Families

None.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- Persistent failures are reported for review; they are never automatic deletion candidates.
