# Stream Health Report

Generated: **2026-11-28T11:14:01+00:00**
Stream URL inventory SHA-256: **41255b51e075d36b980d74ed53109f117baf7b47284eca5bf84960fa9127e2b8**

Probe environment: **GitHub-hosted ubuntu-latest runner**.
A successful HTTP response confirms endpoint reachability, not guaranteed video/audio playback. HTTP 401/403 can reflect authentication, entitlement, or geographic restrictions; results from a GitHub-hosted runner should not be treated as proof of Bangladesh/India-local playback availability.

## Summary

- Streams tested: **1373**
- Reachable: **1297**
- Failed this check: **76**
- Persistent failures (3+ consecutive): **0**
- Intermittent failures: **76**
- Primary tested: **824**
- Backup tested: **489**
- Review-queue entries tested: **60**
- Near-duplicate URL families: **3**

## Failure Classification

- Only HTTP 404 and 410 count as definitive failures; all other HTTP statuses and network/authentication errors are inconclusive.
- Streaks count consecutive Bangladesh calendar days; repeated runs on one date count once, and a missed day resets the streak.

- HTTP 404/410 (definitive): **20**
- Inconclusive HTTP/network failure: **56**

## Persistent Failures

None.

## Failed This Check

- **7S Music** — Backup — streak 0 days — HTTP 403
- **9X Jalwa** — Backup — streak 0 days — HTTP 403
- **9X Tashan** — Backup — streak 0 days — HTTP 404
- **A Sports** — Backup — streak 0 days — HTTP 403
- **Aakaash Aath** — Backup — streak 0 days — HTTP 403
- **Dangal 2** — Backup — streak 0 days — HTTP 403
- **ESPN** — Backup — streak 0 days — HTTP 403
- **Goldmines Bollywood** — Backup — streak 0 days — HTTP 403
- **Kappa TV** — Backup — streak 0 days — HTTP 403
- **Kerala Vision** — Backup — streak 0 days — HTTP 403
- **Mahaa Max** — Backup — streak 0 days — HTTP 403
- **Mazhavil Manorama** — Backup — streak 0 days — HTTP 403
- **NRB TV** — Backup — streak 0 days — HTTP 500
- **PTV Sports** — Backup — streak 0 days — HTTP 403
- **Shanson TV** — Backup — streak 0 days — HTTP 403
- **Shubh Cinema TV** — Backup — streak 0 days — HTTP 403
- **Star Sports 2** — Backup — streak 0 days — HTTP 403
- **Zee TV** — Backup — streak 0 days — HTTP 404
- **Desh TV** — Bangladesh — streak 0 days — HTTP 500
- **Colors Bangla Cinema** — Indian Bangla — streak 0 days — Timeout
- **Asianet Middle East** — Indian Entertainment — streak 0 days — HTTP 403
- **City Channel** — Indian Entertainment — streak 0 days — HTTP 404
- **Drishya TV** — Indian Entertainment — streak 0 days — HTTP 404
- **Kairali Arabia** — Indian Entertainment — streak 0 days — HTTP 403
- **Periyar Vision** — Indian Entertainment — streak 0 days — HTTP 503
- **Siri Kannada** — Indian Entertainment — streak 0 days — HTTP 403
- **Goldmines 2** — Indian Movies — streak 0 days — HTTP 403
- **Goldmines Action** — Indian Movies — streak 0 days — HTTP 403
- **MH One Movies** — Indian Movies — streak 0 days — HTTP 403
- **Andy Haryana** — Indian Music — streak 0 days — HTTP 403
- **Teleritmo** — International — streak 0 days — HTTP 403
- **Disney Channel** — Kids — streak 0 days — HTTP 403
- **AMN TV** — Review — streak 2 days — HTTP 404
- **ATN Bangla** — Review — streak 0 days — Timeout
- **Animal Planet** — Review — streak 1 days — HTTP 404
- **B4U Kadak** — Review — streak 0 days — DNS
- **B4U Movies** — Review — streak 0 days — DNS
- **CCTV Kunnamkulam** — Review — streak 0 days — TLS
- **Colors Bangla** — Review — streak 0 days — HTTP 404
- **DBC News** — Review — streak 0 days — Network
- **Dangal** — Review — streak 1 days — HTTP 404
- **Duronto TV** — Review — streak 2 days — HTTP 404
- **Ekhon TV** — Review — streak 0 days — TLS
- **Enter TV** — Review — streak 0 days — HTTP 530
- **Enter TV** — Review — streak 0 days — HTTP 530
- **Gazi TV** — Review — streak 0 days — Network
- **Goldmines Bollywood** — Review — streak 0 days — HTTP 404
- **Kerala Today TV** — Review — streak 1 days — HTTP 404
- **Maasranga TV** — Review — streak 0 days — Timeout
- **RTV** — Review — streak 0 days — HTTP 404
- **RTV** — Review — streak 0 days — HTTP 404
- **RTV** — Review — streak 0 days — HTTP 404
- **RTV** — Review — streak 1 days — HTTP 404
- **RTV (Bangladesh)** — Review — streak 0 days — Timeout
- **Rupashi Bangla TV** — Review — streak 2 days — HTTP 404
- **Shemaroo Filmi Gaane** — Review — streak 0 days — HTTP 403
- **Sony Sports Ten 2** — Review — streak 0 days — HTTP 404
- **Sooriyan TV** — Review — streak 0 days — TLS
- **Star Movies** — Review — streak 0 days — 200
- **Vision (India)** — Review — streak 0 days — HTTP 404
- **ZB Cinema** — Review — streak 0 days — HTTP 404
- **Zee Bangla** — Review — streak 0 days — HTTP 404
- **Zee Cine Classic** — Review — streak 0 days — HTTP 403
- **Zee Comedy Nation** — Review — streak 0 days — HTTP 403
- **Zee Dil Se** — Review — streak 0 days — HTTP 403
- **Zee Horror Nights** — Review — streak 0 days — HTTP 403
- **Zee South Flix** — Review — streak 0 days — HTTP 403
- **Max Sport 1** — Sports — streak 0 days — Timeout
- **Max Sport 2** — Sports — streak 0 days — Timeout
- **Max Sport 3** — Sports — streak 0 days — Timeout
- **Max Sport 4** — Sports — streak 0 days — Timeout
- **Sportivnyy** — Sports — streak 0 days — HTTP 503
- **Star Sports 1** — Sports — streak 0 days — Timeout
- **Star Sports 2** — Sports — streak 0 days — HTTP 403
- **Star Sports Select 1** — Sports — streak 0 days — Timeout
- **Star Sports Select 2** — Sports — streak 0 days — Timeout

## Near-Duplicate URL Families

- URL family fingerprint `d8eee792b099` — 2 URL variants; credentials and query values are not published.
- URL family fingerprint `e074fe47c468` — 2 URL variants; credentials and query values are not published.
- URL family fingerprint `cf1c51b3c1bf` — 3 URL variants; credentials and query values are not published.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- A URL family is not automatically counted as independent redundancy merely because its path, rendition, or query string differs.
