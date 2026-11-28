# Stream Health Report

Generated: **2026-11-28T00:18:22+00:00**
Stream URL inventory SHA-256: **33b10a8be11d4ae2a878bb68b993688a627b4367e585da093cc4588d2cb6cf91**

Probe environment: **GitHub-hosted ubuntu-latest runner**.
A successful HTTP response confirms endpoint reachability, not guaranteed video/audio playback. HTTP 401/403 can reflect authentication, entitlement, or geographic restrictions; results from a GitHub-hosted runner should not be treated as proof of Bangladesh/India-local playback availability.

## Summary

- Streams tested: **1197**
- Reachable: **1142**
- Failed this check: **55**
- Persistent failures (3+ consecutive): **0**
- Intermittent failures: **55**
- Primary tested: **708**
- Backup tested: **434**
- Review-queue entries tested: **55**
- Near-duplicate URL families: **1**

## Failure Classification

- Only HTTP 404 and 410 count as definitive failures; all other HTTP statuses and network/authentication errors are inconclusive.
- Streaks count consecutive Bangladesh calendar days; repeated runs on one date count once, and a missed day resets the streak.

- HTTP 404/410 (definitive): **9**
- Inconclusive HTTP/network failure: **46**

## Persistent Failures

None.

## Failed This Check

- **7S Music** — Backup — streak 0 days — HTTP 403
- **9X Jalwa** — Backup — streak 0 days — HTTP 403
- **Aakaash Aath** — Backup — streak 0 days — HTTP 403
- **Balle Balle** — Backup — streak 1 days — HTTP 404
- **Dangal 2** — Backup — streak 0 days — HTTP 403
- **Deepto TV** — Backup — streak 1 days — HTTP 404
- **Deepto TV** — Backup — streak 1 days — HTTP 404
- **ESPN** — Backup — streak 0 days — HTTP 403
- **Goldmines Bollywood** — Backup — streak 0 days — HTTP 403
- **Kappa TV** — Backup — streak 0 days — HTTP 403
- **Kerala Vision** — Backup — streak 0 days — HTTP 403
- **Mahaa Max** — Backup — streak 0 days — HTTP 403
- **Mazhavil Manorama** — Backup — streak 0 days — HTTP 403
- **Shanson TV** — Backup — streak 0 days — HTTP 403
- **Shubh Cinema TV** — Backup — streak 0 days — HTTP 403
- **beIN SPORTS 2** — Backup — streak 0 days — 200
- **Banglar Kontho 24** — Bangladesh — streak 0 days — HTTP 500
- **Jago News 24** — Bangladesh — streak 0 days — HTTP 500
- **Animal Planet** — Documentary & Wildlife — streak 1 days — HTTP 404
- **Colors Bangla Cinema** — Indian Bangla — streak 0 days — Timeout
- **Asianet Middle East** — Indian Entertainment — streak 0 days — HTTP 403
- **Kairali Arabia** — Indian Entertainment — streak 0 days — HTTP 403
- **Kerala Today TV** — Indian Entertainment — streak 1 days — HTTP 404
- **Siri Kannada** — Indian Entertainment — streak 0 days — HTTP 403
- **Goldmines 2** — Indian Movies — streak 0 days — HTTP 403
- **Goldmines Action** — Indian Movies — streak 0 days — HTTP 403
- **MH One Movies** — Indian Movies — streak 0 days — HTTP 403
- **Andy Haryana** — Indian Music — streak 0 days — HTTP 403
- **Kalika TV** — Indian Music — streak 1 days — HTTP 404
- **Star Movies** — International — streak 0 days — 200
- **Teleritmo** — International — streak 0 days — HTTP 403
- **Disney Channel** — Kids — streak 0 days — HTTP 403
- **ATN Bangla (720p)** — New Backups — streak 0 days — Timeout
- **B4U Kadak (1080p)** — New Backups — streak 0 days — DNS
- **B4U Movies (1080p)** — New Backups — streak 0 days — DNS
- **DBC News (480p)** — New Backups — streak 0 days — Network
- **Duronto TV (720p)** — New Backups — streak 2 days — HTTP 404
- **Ekhon TV (1080p)** — New Backups — streak 0 days — TLS
- **Gazi TV (1080p)** — New Backups — streak 0 days — Network
- **Maasranga TV (720p)** — New Backups — streak 0 days — Timeout
- **RTV (Bangladesh) (720p)** — New Backups — streak 0 days — Timeout
- **AMN TV (576p)** — New Channels — streak 2 days — HTTP 404
- **Rupashi Bangla TV (720p)** — New Channels — streak 2 days — HTTP 404
- **Shemaroo Filmi Gaane (1080p)** — New Channels — streak 0 days — HTTP 403
- **Sooriyan TV (1080p)** — New Channels — streak 0 days — TLS
- **Zee Cine Classic (1080p)** — New Channels — streak 0 days — HTTP 403
- **Zee Comedy Nation (1080p)** — New Channels — streak 0 days — HTTP 403
- **Zee Dil Se (1080p)** — New Channels — streak 0 days — HTTP 403
- **Zee Horror Nights (1080p)** — New Channels — streak 0 days — HTTP 403
- **Zee South Flix (1080p)** — New Channels — streak 0 days — HTTP 403
- **Sky Sports Cricket** — Sports — streak 0 days — 200
- **Star Sports 1 HD** — Sports — streak 0 days — Timeout
- **Star Sports 2** — Sports — streak 0 days — HTTP 403
- **Star Sports Select 1** — Sports — streak 0 days — Timeout
- **Star Sports Select 2** — Sports — streak 0 days — Timeout

## Near-Duplicate URL Families

- URL family fingerprint `e074fe47c468` — 2 URL variants; credentials and query values are not published.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- A URL family is not automatically counted as independent redundancy merely because its path, rendition, or query string differs.
