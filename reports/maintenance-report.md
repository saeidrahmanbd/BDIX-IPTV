# IPTV Maintenance Report

_Generated: **2026-10-31 01:45 UTC**_

Source playlist SHA-256: **e599bef5f4e795d2d1a1071c388c11140bad5f611843a573340ee3b35dc29293**

| Item | Result |
|---|---:|
| Current playlist streams | **1159** |
| Active channel identities | **655** |
| Backup stream entries | **366** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **161** |
| Persistent health failures | **131** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current three-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
