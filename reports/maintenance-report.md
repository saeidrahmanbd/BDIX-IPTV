# IPTV Maintenance Report

_Generated: **2026-11-28 17:46 UTC**_

Source playlist SHA-256: **25206445454790f8cf1e4f60acef3d030b563cba93de4c0d68c3603eee1a077c**

| Item | Result |
|---|---:|
| Current playlist streams | **1373** |
| Active channel identities | **780** |
| Backup stream entries | **489** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **7** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **68** |
| Persistent health failures | **0** |
| Audit findings (review warnings included) | **33** |
| Pre-publish gate | **BLOCK** |

## Audit metric scope
- Audit findings combine blocking defects with non-blocking review warnings, including preserved row-order/category-order and channel-number sequence observations.
- The Pre-Publish Gate is the authoritative hard-safety-blocker decision; PASS means no hard blockers were detected for this source revision.

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
