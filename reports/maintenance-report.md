# IPTV Maintenance Report

_Generated: **2026-11-11 15:01 UTC**_

Source playlist SHA-256: **0923016ca9694c93b3ec171f3ceb07b921cbf2187a7858070c4154aaeb354cb7**

| Item | Result |
|---|---:|
| Current playlist streams | **1391** |
| Active channel identities | **733** |
| Backup stream entries | **463** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **46** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **237** |
| Persistent health failures | **178** |
| Audit blockers | **177** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
