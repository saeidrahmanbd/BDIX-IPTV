# IPTV Maintenance Report

_Generated: **2026-11-15 06:17 UTC**_

Source playlist SHA-256: **dca221fc5c3faa47dc7849d90cfeecc8207f30dbe9fb9c72d6259717ae63693d**

| Item | Result |
|---|---:|
| Current playlist streams | **1276** |
| Active channel identities | **644** |
| Backup stream entries | **424** |
| EPG IDs audited | **644** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **58.9%** |
| EPG programme coverage | **51%** |
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
