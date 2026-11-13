# IPTV Maintenance Report

_Generated: **2026-11-13 06:29 UTC**_

Source playlist SHA-256: **4757dc831cd0ebeecd432ee55cb3d5529eaf7e11858aa6a72ac73eff4ad7e4eb**

| Item | Result |
|---|---:|
| Current playlist streams | **1242** |
| Active channel identities | **646** |
| Backup stream entries | **424** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **1** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **178** |
| Persistent health failures | **157** |
| Audit blockers | **104** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
