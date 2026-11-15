# IPTV Maintenance Report

_Generated: **2026-11-15 10:02 UTC**_

Source playlist SHA-256: **1d0bc9ef3a01f48a9b0fc46677ab87c42774c9e1a1df080f3c47cc3d72bb1af7**

| Item | Result |
|---|---:|
| Current playlist streams | **1274** |
| Active channel identities | **647** |
| Backup stream entries | **423** |
| EPG IDs audited | **647** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **58.7%** |
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
