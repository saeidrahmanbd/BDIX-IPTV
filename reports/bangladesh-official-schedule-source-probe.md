# Bangladesh official schedule source probe

Generated: **2026-11-09T06:17:38+00:00**

## Safety and scope

- Read-only. This probe does not change playlists, EPG mappings, source lists or epg/epg.xml.
- It runs only the repository's existing public HTML schedule adapters and fetches public navigation pages.
- Exact tvg-id identity is required. Similar names are not treated as matches.
- No subscriber login, app token, private endpoint, session cookie or API key is used.
- Backup, Review, New Channels and New Backups are counted as inactive groups for the active-match column.

- Bangladesh-scope unique IDs in both playlists (group-title Bangladesh or .bd ID): **89**
- IDs currently in active groups: **74**
- Schedule window: **-6 hours to +7 days**

## Existing official schedule adapters

| Source | XMLTV channel ID | Result | Usable rows | Unique titles | Exact playlist status | Group | First start (UTC) | Last stop (UTC) | Error |
|---|---|---|---:|---:|---|---|---|---|---|
| RTV official weekly/daily schedule | RTV.bd | FAILED | 0 | 0 | EXACT_ACTIVE | Backup, Bangladesh, Review | - | - | RuntimeError: Could not obtain a current official RTV schedule over verified HTTPS (rtvonline: no daily schedule article link on homepage; www.rtvbd.tv: URLError after retry; rtvbd.tv: URLError after retry) |
| BTV official programme guide (legacy endpoint) | BTVNational.bd | OK | 74 | 38 | EXACT_INACTIVE_ONLY | Review | 2026-11-09T01:00+00:00 | 2026-11-15T12:00+00:00 |  |
| Maasranga official weekly schedule | MaasrangaTV.bd | FAILED | 0 | 0 | EXACT_ACTIVE | Backup, Bangladesh, Review | - | - | HTTPError: HTTP Error 403: Forbidden |

## Public schedule-navigation pages

| Page | Fetch result | HTTP | Page URL | Bytes | Candidate schedule links | Note |
|---|---|---:|---|---:|---|---|
| BTV official homepage | FAILED | - | https://btv.gov.bd/ | 0 | - | URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1011)> |
| BTV legacy live programme guide | OK | 200 | https://migrate.btvlive.gov.bd/channel/BTV | 209388 | - | Public page fetch only; links are candidates, not schedule rows. |
| Prothom Alo TV section | OK | 200 | https://www.prothomalo.com/entertainment/tv | 2981400 | - | Public page fetch only; links are candidates, not schedule rows. |
| Prothom Alo entertainment section | OK | 200 | https://www.prothomalo.com/entertainment | 3136586 | - | Public page fetch only; links are candidates, not schedule rows. |

## Summary

- Usable programme rows from tested official adapters: **74**
- Rows attached to exact active playlist IDs: **0**
- Rows attached only to exact inactive playlist IDs: **74**
- A successfully fetched schedule for a Backup/Review-only channel does not count as active-playlist coverage.
- A public navigation page without a current dated schedule is not treated as an EPG source.
- Public pages and adapters require separate data-redistribution review before any schedule data can be added to the public XMLTV guide.
