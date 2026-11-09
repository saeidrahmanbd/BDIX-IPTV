# IPTV Maintenance Report

_Generated: **2026-11-09 07:00 UTC**_

Source playlist SHA-256: **a905c8a79fc9167d61323692f4a7b8df541e7e086f76552bc5632544ac4f00d7**

| Item | Result |
|---|---:|
| Current playlist streams | **996** |
| Active channel identities | **580** |
| Backup stream entries | **327** |
| EPG IDs audited | **580** |
| Logo exceptions | **1** |
| EPG mapping | **61.4%** |
| EPG programme coverage | **46%** |
| Health failures | **159** |
| Persistent health failures | **127** |
| Audit blockers | **16** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
