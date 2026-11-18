# IPTV Maintenance Report

_Generated: **2026-11-18 10:47 UTC**_

Source playlist SHA-256: **a43b9174e373427cdfb91993bb9814e7ce7f3a1f12a95189d62e964e6ee5ad44**

| Item | Result |
|---|---:|
| Current playlist streams | **1378** |
| Active channel identities | **714** |
| Backup stream entries | **463** |
| EPG IDs audited | **714** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **60.8%** |
| EPG programme coverage | **54%** |
| Health failures | **264** |
| Persistent health failures | **49** |
| Audit findings (review warnings included) | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

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
