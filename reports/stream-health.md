# Stream Health Report

Generated: **2026-11-26T10:39:38+00:00**
Stream URL inventory SHA-256: **b0f88876a679327c38cf3ef0831d246e6f126ac1e97eadfab59c9f8a68292d8e**

Probe environment: **GitHub-hosted ubuntu-latest runner**.
A successful HTTP response confirms endpoint reachability, not guaranteed video/audio playback. HTTP 401/403 can reflect authentication, entitlement, or geographic restrictions; results from a GitHub-hosted runner should not be treated as proof of Bangladesh/India-local playback availability.

## Summary

- Streams tested: **1143**
- Reachable: **1070**
- Failed this check: **73**
- Persistent failures (3+ consecutive): **1**
- Intermittent failures: **73**
- Primary tested: **708**
- Backup tested: **434**
- Review-queue entries tested: **1**
- Near-duplicate URL families: **1**

## Failure Classification

- Only HTTP 404 and 410 count as definitive failures; all other HTTP statuses and network/authentication errors are inconclusive.
- Streaks count consecutive Bangladesh calendar days; repeated runs on one date count once, and a missed day resets the streak.

- HTTP 404/410 (definitive): **5**
- Inconclusive HTTP/network failure: **68**

## Persistent Failures

- **Bol Entertainment** — Pakistani — consecutive failed days: **7** — 206

## Failed This Check

- **7S Music** — Backup — streak 0 days — HTTP 403
- **9X Jalwa** — Backup — streak 0 days — HTTP 403
- **ATN Bangla** — Backup — streak 0 days — Timeout
- **ATN Bangla UK** — Backup — streak 0 days — Timeout
- **ATN News** — Backup — streak 0 days — Timeout
- **Aakaash Aath** — Backup — streak 0 days — HTTP 403
- **Ananda TV** — Backup — streak 0 days — Timeout
- **Bangla Vision** — Backup — streak 0 days — Timeout
- **Channel 52** — Backup — streak 0 days — Timeout
- **Channel 9** — Backup — streak 0 days — Timeout
- **Channel I** — Backup — streak 0 days — Timeout
- **Channel S** — Backup — streak 0 days — Timeout
- **Channel S** — Backup — streak 0 days — Timeout
- **Channel S UK** — Backup — streak 0 days — HTTP 404
- **Dangal 2** — Backup — streak 0 days — HTTP 403
- **Ekhon TV** — Backup — streak 0 days — Timeout
- **Ekushey TV** — Backup — streak 0 days — Timeout
- **G TV** — Backup — streak 0 days — HTTP 500
- **G TV** — Backup — streak 0 days — Timeout
- **Global TV** — Backup — streak 0 days — Timeout
- **Goldmines Bollywood** — Backup — streak 0 days — HTTP 403
- **Islam Channel Bangla** — Backup — streak 0 days — Timeout
- **Kappa TV** — Backup — streak 0 days — HTTP 403
- **Kerala Vision** — Backup — streak 0 days — HTTP 403
- **Mahaa Max** — Backup — streak 0 days — HTTP 403
- **Makkah TV** — Backup — streak 0 days — Timeout
- **Mazhavil Manorama** — Backup — streak 0 days — HTTP 403
- **Medina Live** — Backup — streak 0 days — Timeout
- **Movie Bangla** — Backup — streak 0 days — Timeout
- **Movie Bangla** — Backup — streak 0 days — Timeout
- **My TV** — Backup — streak 0 days — Timeout
- **NRB TV** — Backup — streak 0 days — Timeout
- **RTV** — Backup — streak 0 days — Timeout
- **SA TV** — Backup — streak 0 days — Timeout
- **Shanson TV** — Backup — streak 0 days — HTTP 403
- **Shubh Cinema TV** — Backup — streak 0 days — HTTP 403
- **Thikana TV** — Backup — streak 0 days — Timeout
- **Ultimate TV** — Backup — streak 0 days — HTTP 404
- **Banglar Kontho 24** — Bangladesh — streak 0 days — Timeout
- **Biswa Bangla 24** — Bangladesh — streak 0 days — Timeout
- **Channel 1** — Bangladesh — streak 0 days — Timeout
- **Channel 16** — Bangladesh — streak 0 days — Timeout
- **Channel S UK** — Bangladesh — streak 0 days — HTTP 404
- **DBC News** — Bangladesh — streak 0 days — Timeout
- **Desh Bangla TV** — Bangladesh — streak 1 days — Timeout
- **Desh TV** — Bangladesh — streak 0 days — Timeout
- **Deshe Bideshe** — Bangladesh — streak 0 days — Timeout
- **Matribhumi TV** — Bangladesh — streak 0 days — Timeout
- **Music Bangla** — Bangladesh — streak 0 days — Timeout
- **SA TV** — Bangladesh — streak 0 days — Timeout
- **Shikor TV Canada** — Bangladesh — streak 0 days — Timeout
- **Vision 24** — Bangladesh — streak 0 days — Timeout
- **Ten TV Prime** — Indian Bangla — streak 0 days — Timeout
- **Asianet Middle East** — Indian Entertainment — streak 0 days — HTTP 403
- **Drisya TV** — Indian Entertainment — streak 0 days — HTTP 404
- **Gangaur TV** — Indian Entertainment — streak 0 days — Timeout
- **Kairali Arabia** — Indian Entertainment — streak 0 days — HTTP 403
- **Periyar Vision** — Indian Entertainment — streak 0 days — HTTP 403
- **Siri Kannada** — Indian Entertainment — streak 0 days — HTTP 403
- **Sun Surya** — Indian Entertainment — streak 0 days — HTTP 403
- **Goldmines 2** — Indian Movies — streak 0 days — HTTP 403
- **Goldmines Action** — Indian Movies — streak 0 days — HTTP 403
- **MH One Movies** — Indian Movies — streak 0 days — HTTP 403
- **Andy Haryana** — Indian Music — streak 0 days — HTTP 403
- **Movies Now** — International — streak 1 days — HTTP 404
- **Teleritmo** — International — streak 0 days — HTTP 403
- **Al Sunnah Al Nabawiyah** — Religious — streak 0 days — Timeout
- **Azan TV** — Religious — streak 0 days — Timeout
- **Islamic TV** — Religious — streak 0 days — Timeout
- **Makkah Live** — Religious — streak 0 days — Timeout
- **Peace TV Bangla** — Religious — streak 0 days — Timeout
- **TV One UK** — Religious — streak 0 days — Timeout
- **Star Sports 2** — Sports — streak 0 days — HTTP 403

## Near-Duplicate URL Families

- URL family fingerprint `e074fe47c468` — 2 URL variants; credentials and query values are not published.

## Policy

- Health failures never delete or reclassify streams automatically.
- Backup streams remain protected even after repeated failures.
- Persistent failures are reported for review; they are never automatic deletion candidates.
- A URL family is not automatically counted as independent redundancy merely because its path, rendition, or query string differs.
