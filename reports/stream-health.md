# Stream Health Report

Generated: **2026-11-27T00:18:37+00:00**
Stream URL inventory SHA-256: **82c1d062d9ca6b483f623d691caf59058d6b130ea13a268b35459202d4349ec2**

Probe environment: **GitHub-hosted ubuntu-latest runner**.
A successful HTTP response confirms endpoint reachability, not guaranteed video/audio playback. HTTP 401/403 can reflect authentication, entitlement, or geographic restrictions; results from a GitHub-hosted runner should not be treated as proof of Bangladesh/India-local playback availability.

## Summary

- Streams tested: **1183**
- Reachable: **1126**
- Failed this check: **57**
- Persistent failures (3+ consecutive): **0**
- Intermittent failures: **57**
- Primary tested: **708**
- Backup tested: **434**
- Review-queue entries tested: **41**
- Near-duplicate URL families: **1**

## Failure Classification

- Only HTTP 404 and 410 count as definitive failures; all other HTTP statuses and network/authentication errors are inconclusive.
- Streaks count consecutive Bangladesh calendar days; repeated runs on one date count once, and a missed day resets the streak.

- HTTP 404/410 (definitive): **16**
- Inconclusive HTTP/network failure: **41**

## Persistent Failures

None.

## Failed This Check

- **7S Music** — Backup — streak 0 days — HTTP 403
- **9X Jalwa** — Backup — streak 0 days — HTTP 403
- **Aakaash Aath** — Backup — streak 0 days — HTTP 403
- **DD Bangla** — Backup — streak 1 days — HTTP 404
- **DD Girnar** — Backup — streak 1 days — HTTP 404
- **DD Goa** — Backup — streak 1 days — HTTP 404
- **DD Himachal Pradesh** — Backup — streak 1 days — HTTP 404
- **DD Malayalam** — Backup — streak 1 days — HTTP 404
- **DD Odia** — Backup — streak 1 days — HTTP 404
- **DD Sahyadri** — Backup — streak 1 days — HTTP 404
- **DD Tamil** — Backup — streak 1 days — HTTP 404
- **DD Yadagiri** — Backup — streak 1 days — HTTP 404
- **Dangal 2** — Backup — streak 0 days — HTTP 403
- **Goldmines Bollywood** — Backup — streak 0 days — HTTP 403
- **Kappa TV** — Backup — streak 0 days — HTTP 403
- **Kerala Vision** — Backup — streak 0 days — HTTP 403
- **Mahaa Max** — Backup — streak 0 days — HTTP 403
- **Mazhavil Manorama** — Backup — streak 0 days — HTTP 403
- **Shanson TV** — Backup — streak 0 days — HTTP 403
- **Shubh Cinema TV** — Backup — streak 0 days — HTTP 403
- **Zee Bangla** — Backup — streak 0 days — 200
- **Asianet Middle East** — Indian Entertainment — streak 0 days — HTTP 403
- **Kairali Arabia** — Indian Entertainment — streak 0 days — HTTP 403
- **N Vision** — Indian Entertainment — streak 1 days — HTTP 404
- **Periyar Vision** — Indian Entertainment — streak 0 days — HTTP 403
- **Siri Kannada** — Indian Entertainment — streak 0 days — HTTP 403
- **Sun Surya** — Indian Entertainment — streak 0 days — HTTP 403
- **Goldmines 2** — Indian Movies — streak 0 days — HTTP 403
- **Goldmines Action** — Indian Movies — streak 0 days — HTTP 403
- **MH One Movies** — Indian Movies — streak 0 days — HTTP 403
- **Thendral TV** — Indian Movies — streak 1 days — HTTP 404
- **Andy Haryana** — Indian Music — streak 0 days — HTTP 403
- **Dance TV** — International — streak 0 days — Timeout
- **Movies Now** — International — streak 2 days — HTTP 404
- **Teleritmo** — International — streak 0 days — HTTP 403
- **ATN Bangla (720p)** — New Backups — streak 0 days — Timeout
- **B4U Kadak (1080p)** — New Backups — streak 0 days — DNS
- **B4U Movies (1080p)** — New Backups — streak 0 days — DNS
- **DBC News (480p)** — New Backups — streak 0 days — Network
- **Duronto TV (720p)** — New Backups — streak 1 days — HTTP 404
- **Ekhon TV (1080p)** — New Backups — streak 0 days — TLS
- **Gazi TV (1080p)** — New Backups — streak 0 days — Network
- **Maasranga TV (720p)** — New Backups — streak 0 days — Timeout
- **RTV (Bangladesh) (720p)** — New Backups — streak 0 days — Timeout
- **AMN TV (576p)** — New Channels — streak 1 days — HTTP 404
- **News 21 Bangla TV (1080p)** — New Channels — streak 0 days — Other
- **Rupashi Bangla TV (720p)** — New Channels — streak 1 days — HTTP 404
- **Shemaroo Filmi Gaane (1080p)** — New Channels — streak 0 days — HTTP 403
- **Sooriyan TV (1080p)** — New Channels — streak 0 days — TLS
- **Zee Cine Classic (1080p)** — New Channels — streak 0 days — HTTP 403
- **Zee Comedy Nation (1080p)** — New Channels — streak 0 days — HTTP 403
- **Zee Dil Se (1080p)** — New Channels — streak 0 days — HTTP 403
- **Zee Horror Nights (1080p)** — New Channels — streak 0 days — HTTP 403
- **Zee South Flix (1080p)** — New Channels — streak 0 days — HTTP 403
- **Falak TV** — Pakistani — streak 1 days — HTTP 404
- **Star Sports 2** — Sports — streak 0 days — HTTP 403
- **Unite8 Sports 1** — Sports — streak 0 days — 200

## Near-Duplicate URL Families

- URL family fingerprint `e074fe47c468` — 2 URL variants; credentials and query values are not published.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- A URL family is not automatically counted as independent redundancy merely because its path, rendition, or query string differs.
