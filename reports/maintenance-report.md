# IPTV Maintenance Report

_Generated: **2026-11-12 03:26 UTC**_

Source playlist SHA-256: **ebabf8e5d80fa4c1524209e86de1022f0c7195719266f81eccbad13b250bca95**

| Item | Result |
|---|---:|
| Current playlist streams | **1331** |
| Active channel identities | **685** |
| Backup stream entries | **463** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **7** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **183** |
| Persistent health failures | **165** |
| Audit blockers | **19** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
