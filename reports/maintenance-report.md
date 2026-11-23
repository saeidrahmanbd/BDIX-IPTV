# IPTV Maintenance Report

_Generated: **2026-11-23 01:31 UTC**_

Source playlist SHA-256: **edc2e1edbb195131dceb66cfedc7a3d7d3fcf9901d4a7c41066b9f052a4e3e0b**

| Item | Result |
|---|---:|
| Current playlist streams | **1346** |
| Active channel identities | **716** |
| Backup stream entries | **410** |
| EPG IDs audited | **716** |
| Logo exceptions | **0** |
| EPG mapping | **63.8%** |
| EPG programme coverage | **56%** |
| Health failures | **262** |
| Persistent health failures | **55** |
| Audit findings (review warnings included) | **8** |
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
