# IPTV Maintenance Report

_Generated: **2026-10-31 01:07 UTC**_

Source playlist SHA-256: **2007da9d83805d6114936a5ea3b25f3bd16f4685fb4869fabca9f3da8a4712d4**

| Item | Result |
|---|---:|
| Current playlist streams | **1161** |
| Active channel identities | **655** |
| Backup stream entries | **366** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **167** |
| Persistent health failures | **131** |
| Audit blockers | **0** |
| Pre-publish gate | **UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current three-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
