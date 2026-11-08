# IPTV Maintenance Report

_Generated: **2026-11-08 10:56 UTC**_

Source playlist SHA-256: **42d6d2b01b52c16d2c9a8f0d0593b6df532bef90c37667e755cfc1b085f5540c**

| Item | Result |
|---|---:|
| Current playlist streams | **943** |
| Active channel identities | **609** |
| Backup stream entries | **333** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **1** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **56** |
| Persistent health failures | **49** |
| Audit blockers | **1** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
