# IPTV Maintenance Report

_Generated: **2026-11-13 01:32 UTC**_

Source playlist SHA-256: **4757dc831cd0ebeecd432ee55cb3d5529eaf7e11858aa6a72ac73eff4ad7e4eb**

| Item | Result |
|---|---:|
| Current playlist streams | **1242** |
| Active channel identities | **646** |
| Backup stream entries | **424** |
| EPG IDs audited | **646** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **58.7%** |
| EPG programme coverage | **50%** |
| Health failures | **181** |
| Persistent health failures | **161** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
