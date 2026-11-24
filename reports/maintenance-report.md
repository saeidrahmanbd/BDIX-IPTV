# IPTV Maintenance Report

_Generated: **2026-11-24 00:18 UTC**_

Source playlist SHA-256: **95ca9078eca1ae8371b7c211029a02bfed62a01de35303f09627ec12f3ba8bc7**

| Item | Result |
|---|---:|
| Current playlist streams | **1350** |
| Active channel identities | **716** |
| Backup stream entries | **410** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **250** |
| Persistent health failures | **56** |
| Audit findings (review warnings included) | **1** |
| Pre-publish gate | **PASS** |

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
