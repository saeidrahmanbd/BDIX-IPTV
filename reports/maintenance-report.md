# IPTV Maintenance Report

_Generated: **2026-11-19 08:34 UTC**_

Source playlist SHA-256: **8d12d8dcbca54e61e1834b12fd6a4e2d0cfb255be6f085d06dd6c2c2a0791983**

| Item | Result |
|---|---:|
| Current playlist streams | **1375** |
| Active channel identities | **714** |
| Backup stream entries | **463** |
| EPG IDs audited | **714** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **60.8%** |
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
