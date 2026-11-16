# IPTV Maintenance Report

_Generated: **2026-11-16 09:54 UTC**_

Source playlist SHA-256: **9ca47f4a45ea83065516c4926ca22f771140f2d92005812e251417d5ca0843b0**

| Item | Result |
|---|---:|
| Current playlist streams | **1307** |
| Active channel identities | **673** |
| Backup stream entries | **469** |
| EPG IDs audited | **673** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **61.8%** |
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
