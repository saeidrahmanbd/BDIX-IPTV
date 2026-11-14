# IPTV Maintenance Report

_Generated: **2026-11-14 10:51 UTC**_

Source playlist SHA-256: **6d59d90055cc32036f9aeee9d86ad878fbced2364308b6f3ef53228686c91771**

| Item | Result |
|---|---:|
| Current playlist streams | **1284** |
| Active channel identities | **646** |
| Backup stream entries | **424** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **3** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **189** |
| Persistent health failures | **174** |
| Audit blockers | **107** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
