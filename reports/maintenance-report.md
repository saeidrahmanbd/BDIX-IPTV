# IPTV Maintenance Report

_Generated: **2026-11-26 02:01 UTC**_

Source playlist SHA-256: **8167fe97fbf5e046ec9f27fdb6a89679c51ec7abda12ff14819dab25c02bb081**

| Item | Result |
|---|---:|
| Current playlist streams | **1371** |
| Active channel identities | **695** |
| Backup stream entries | **405** |
| EPG IDs audited | **695** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **62.2%** |
| EPG programme coverage | **51%** |
| Health failures | **266** |
| Persistent health failures | **56** |
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
