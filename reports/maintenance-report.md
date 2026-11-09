# IPTV Maintenance Report

_Generated: **2026-11-09 09:22 UTC**_

Source playlist SHA-256: **d4bab23c700d8a1cfd18c45af6ffafabb6fcc5dece8fef83fa4f96629a9580eb**

| Item | Result |
|---|---:|
| Current playlist streams | **1061** |
| Active channel identities | **592** |
| Backup stream entries | **376** |
| EPG IDs audited | **592** |
| Logo exceptions | **5** |
| EPG mapping | **61.7%** |
| EPG programme coverage | **53%** |
| Health failures | **166** |
| Persistent health failures | **127** |
| Audit blockers | **24** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
