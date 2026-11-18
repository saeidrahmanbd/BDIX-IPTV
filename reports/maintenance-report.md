# IPTV Maintenance Report

_Generated: **2026-11-18 03:11 UTC**_

Source playlist SHA-256: **939b956ecb9712790c70bc6b900d94a994112871cbfc7376d86b5cd3cb87373e**

| Item | Result |
|---|---:|
| Current playlist streams | **1378** |
| Active channel identities | **714** |
| Backup stream entries | **463** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **1** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **215** |
| Persistent health failures | **49** |
| Audit findings (review warnings included) | **18** |
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
