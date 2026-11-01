# IPTV Maintenance Report

_Generated: **2026-11-01 11:44 UTC**_

Source playlist SHA-256: **97a7b8af8401226343356911e2ff5b275c8fef45eb1f955ef28d38f2301583b6**

| Item | Result |
|---|---:|
| Current playlist streams | **1178** |
| Active channel identities | **643** |
| Backup stream entries | **315** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **STALE** |
| Persistent health failures | **STALE** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current three-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
