# IPTV Maintenance Report

_Generated: **2026-11-10 02:34 UTC**_

Source playlist SHA-256: **fd5245ea3bdc1231dd6a4cdc22f82db1b887c7ca4c7d3f028ee6c831c7ba927a**

| Item | Result |
|---|---:|
| Current playlist streams | **1074** |
| Active channel identities | **591** |
| Backup stream entries | **329** |
| EPG IDs audited | **591** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **61.1%** |
| EPG programme coverage | **52%** |
| Health failures | **STALE** |
| Persistent health failures | **STALE** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
