# IPTV Maintenance Report

_Generated: **2026-11-09 15:25 UTC**_

Source playlist SHA-256: **8c1b3678eefb9c990ece2f8fcbd1fb1e5f2f3c8d7be6d1f4566fa0cf555b0267**

| Item | Result |
|---|---:|
| Current playlist streams | **1069** |
| Active channel identities | **585** |
| Backup stream entries | **331** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **3** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **227** |
| Persistent health failures | **176** |
| Audit blockers | **42** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
