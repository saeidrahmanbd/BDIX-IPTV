# IPTV Maintenance Report

_Generated: **2026-11-10 09:58 UTC**_

Source playlist SHA-256: **963a30fd1d7f8b62a5c75208c6fa67adc11d24316ad9d3ff6b7ad3927000737d**

| Item | Result |
|---|---:|
| Current playlist streams | **1121** |
| Active channel identities | **580** |
| Backup stream entries | **379** |
| EPG IDs audited | **580** |
| Logo exceptions | **1** |
| EPG mapping | **60.9%** |
| EPG programme coverage | **52%** |
| Health failures | **199** |
| Persistent health failures | **166** |
| Audit blockers | **13** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
