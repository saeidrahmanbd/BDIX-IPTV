# IPTV Maintenance Report

_Generated: **2026-11-01 01:12 UTC**_

Source playlist SHA-256: **d9faa0bd18a7e337a947e992e486b256c8fc0eca1c451f59668ea256e0a0d5fd**

| Item | Result |
|---|---:|
| Current playlist streams | **1161** |
| Active channel identities | **655** |
| Backup stream entries | **366** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **157** |
| Persistent health failures | **139** |
| Audit blockers | **0** |
| Pre-publish gate | **UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current three-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
