# IPTV Maintenance Report

_Generated: **2026-11-09 11:35 UTC**_

Source playlist SHA-256: **c0c115f5324a59094ecc502e03a3358f243ec4f6e74dc583e650e5009bf997b6**

| Item | Result |
|---|---:|
| Current playlist streams | **1069** |
| Active channel identities | **584** |
| Backup stream entries | **335** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **3** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **182** |
| Persistent health failures | **180** |
| Audit blockers | **18** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
