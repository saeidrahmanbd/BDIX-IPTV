# IPTV Maintenance Report

_Generated: **2026-11-10 15:04 UTC**_

Source playlist SHA-256: **8b798099a5a4fd789da0456a308e8091c7d2c5da6795cd227c44c1e6258a7ef7**

| Item | Result |
|---|---:|
| Current playlist streams | **1171** |
| Active channel identities | **606** |
| Backup stream entries | **394** |
| EPG IDs audited | **606** |
| Logo exceptions | **0** |
| EPG mapping | **61.2%** |
| EPG programme coverage | **53%** |
| Health failures | **188** |
| Persistent health failures | **180** |
| Audit blockers | **2** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
