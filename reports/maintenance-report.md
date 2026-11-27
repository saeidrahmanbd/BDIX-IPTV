# IPTV Maintenance Report

_Generated: **2026-11-27 01:37 UTC**_

Source playlist SHA-256: **6f303c4001f29d41036d95e093d9bcb4c4098c8db08b80360c05c5f2081d8103**

| Item | Result |
|---|---:|
| Current playlist streams | **1183** |
| Active channel identities | **708** |
| Backup stream entries | **434** |
| EPG IDs audited | **708** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **60.5%** |
| EPG programme coverage | **53%** |
| Health failures | **57** |
| Persistent health failures | **0** |
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
