# IPTV Maintenance Report

_Generated: **2026-11-26 14:36 UTC**_

Source playlist SHA-256: **00129460214a9ee239552d01b1bc22ffd907140b7e55a60236d9cf77d46ba935**

| Item | Result |
|---|---:|
| Current playlist streams | **1143** |
| Active channel identities | **708** |
| Backup stream entries | **434** |
| EPG IDs audited | **708** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **60.5%** |
| EPG programme coverage | **54%** |
| Health failures | **73** |
| Persistent health failures | **1** |
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
