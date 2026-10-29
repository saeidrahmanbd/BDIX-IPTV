# IPTV Maintenance Report

_Generated: **2026-10-29 02:06 UTC**_

Source playlist SHA-256: **8ff6e086dbbf08eaf0c2a77c43fa9df102e13fdb58c46f1bc4126ed60d8c6a68**

| Item | Result |
|---|---:|
| Current playlist streams | **1159** |
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
