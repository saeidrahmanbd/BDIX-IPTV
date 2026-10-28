# IPTV Maintenance Report

_Generated: **2026-10-28 11:40 UTC**_

Source playlist SHA-256: **fabbd4dfb8fa0eca77679a7a872c21ef8813bb7f49556db6fe3ab18c4c07b697**

| Item | Result |
|---|---:|
| Current playlist streams | **1178** |
| Active channel identities | **656** |
| Backup stream entries | **366** |
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
