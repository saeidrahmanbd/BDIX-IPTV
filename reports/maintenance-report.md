# IPTV Maintenance Report

_Generated: **2026-11-17 08:07 UTC**_

Source playlist SHA-256: **24f3fdfaa0d8f3c191c12b8824130d2b5f6bdde45f9cd0c4b3118a93265fb384**

| Item | Result |
|---|---:|
| Current playlist streams | **1405** |
| Active channel identities | **711** |
| Backup stream entries | **496** |
| EPG IDs audited | **711** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **61.2%** |
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
