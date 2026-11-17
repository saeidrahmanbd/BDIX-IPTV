# IPTV Maintenance Report

_Generated: **2026-11-17 04:59 UTC**_

Source playlist SHA-256: **037d30711009a5d40bb284fd4e55a73f8669cc19e5fb36f8d85f86181f377561**

| Item | Result |
|---|---:|
| Current playlist streams | **1318** |
| Active channel identities | **660** |
| Backup stream entries | **462** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **2** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **183** |
| Persistent health failures | **45** |
| Audit findings (review warnings included) | **3** |
| Pre-publish gate | **PASS** |

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
