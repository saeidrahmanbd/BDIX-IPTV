# IPTV Maintenance Report

_Generated: **2026-10-31 01:17 UTC**_

Source playlist SHA-256: **3602101f00a9ad15e65a0892743076a3c8fb52f5c135f1b288b318691497b8e4**

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
