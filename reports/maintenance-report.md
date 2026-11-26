# IPTV Maintenance Report

_Generated: **2026-11-26 08:27 UTC**_

Source playlist SHA-256: **fb2881b5951519aa648850f8de2cf82826a551cfd6bb983b4084fdb73eb639bc**

| Item | Result |
|---|---:|
| Current playlist streams | **1442** |
| Active channel identities | **695** |
| Backup stream entries | **465** |
| EPG IDs audited | **695** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **62.2%** |
| EPG programme coverage | **55%** |
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
