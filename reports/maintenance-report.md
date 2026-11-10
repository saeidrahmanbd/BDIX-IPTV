# IPTV Maintenance Report

_Generated: **2026-11-10 11:46 UTC**_

Source playlist SHA-256: **3abe47e2bd3ed160ca8a0b1dc4286ff2367d8255deb252abbe9531a654716a54**

| Item | Result |
|---|---:|
| Current playlist streams | **1121** |
| Active channel identities | **580** |
| Backup stream entries | **379** |
| EPG IDs audited | **580** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **60.9%** |
| EPG programme coverage | **52%** |
| Health failures | **199** |
| Persistent health failures | **166** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
