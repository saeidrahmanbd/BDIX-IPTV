# IPTV Maintenance Report

_Generated: **2026-10-30 02:20 UTC**_

Source playlist SHA-256: **7f2fa0e3b0ff34ceb5823b465b75dc99e6fb3fc8f1fac5a8c5f88b0ed52663ab**

| Item | Result |
|---|---:|
| Current playlist streams | **1159** |
| Active channel identities | **655** |
| Backup stream entries | **366** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **161** |
| Persistent health failures | **58** |
| Audit blockers | **0** |
| Pre-publish gate | **UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current three-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
