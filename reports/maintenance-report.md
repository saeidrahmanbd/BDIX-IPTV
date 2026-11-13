# IPTV Maintenance Report

_Generated: **2026-11-13 07:26 UTC**_

Source playlist SHA-256: **b2d641cfb05c47f5ab58b602feac8b88d5daaa6c520470b8609f5d59b6ea8d5c**

| Item | Result |
|---|---:|
| Current playlist streams | **1280** |
| Active channel identities | **646** |
| Backup stream entries | **424** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **4** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **198** |
| Persistent health failures | **196** |
| Audit blockers | **107** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
