# IPTV Maintenance Report

_Generated: **2026-11-19 11:27 UTC**_

Source playlist SHA-256: **04218b088615b9350bffc495ff7f758deb67a7f4a7fc10cc0bbcbefcdf532cf5**

| Item | Result |
|---|---:|
| Current playlist streams | **1333** |
| Active channel identities | **694** |
| Backup stream entries | **443** |
| EPG IDs audited | **694** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **62.1%** |
| EPG programme coverage | **56%** |
| Health failures | **STALE** |
| Persistent health failures | **STALE** |
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
