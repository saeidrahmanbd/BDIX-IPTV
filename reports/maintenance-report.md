# IPTV Maintenance Report

_Generated: **2026-10-30 02:46 UTC**_

Source playlist SHA-256: **1f7aba9c86bea57673b8b0cbe71a3d71e4842a2b1155aeffb6b9d6ea2fe59d07**

| Item | Result |
|---|---:|
| Current playlist streams | **1159** |
| Active channel identities | **655** |
| Backup stream entries | **366** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **142** |
| Persistent health failures | **56** |
| Audit blockers | **0** |
| Pre-publish gate | **UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current three-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
