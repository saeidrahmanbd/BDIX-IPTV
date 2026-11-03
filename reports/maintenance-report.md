# IPTV Maintenance Report

_Generated: **2026-11-03 09:06 UTC**_

Source playlist SHA-256: **31cc18da8c3736dbd854affb71d2b1de66eed37dc02a1417286f4068adf1ae5e**

| Item | Result |
|---|---:|
| Current playlist streams | **1090** |
| Active channel identities | **680** |
| Backup stream entries | **346** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **7** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **89** |
| Persistent health failures | **59** |
| Audit blockers | **7** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
