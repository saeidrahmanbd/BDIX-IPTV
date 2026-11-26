# IPTV Maintenance Report

_Generated: **2026-11-26 10:37 UTC**_

Source playlist SHA-256: **8360de3894d65813a1852f915a24ce62d26f2b69e04af590da5ae31538270ea7**

| Item | Result |
|---|---:|
| Current playlist streams | **1143** |
| Active channel identities | **708** |
| Backup stream entries | **434** |
| EPG IDs audited | **708** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **60.3%** |
| EPG programme coverage | **54%** |
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
