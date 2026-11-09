# IPTV Maintenance Report

_Generated: **2026-11-09 16:16 UTC**_

Source playlist SHA-256: **1238de7a6f4d50b9fefee2a4e2d3d675e879522d6eaf0e88a8799ac94e2261bc**

| Item | Result |
|---|---:|
| Current playlist streams | **1069** |
| Active channel identities | **601** |
| Backup stream entries | **395** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **3** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **184** |
| Persistent health failures | **181** |
| Audit blockers | **45** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
