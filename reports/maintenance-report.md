# IPTV Maintenance Report

_Generated: **2026-11-13 07:17 UTC**_

Source playlist SHA-256: **c5e166a3a86ed6ff4a74ad8d55217cba0064d516238eb6a6c0223469b8ab878f**

| Item | Result |
|---|---:|
| Current playlist streams | **1280** |
| Active channel identities | **646** |
| Backup stream entries | **424** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **1** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **203** |
| Persistent health failures | **196** |
| Audit blockers | **104** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
