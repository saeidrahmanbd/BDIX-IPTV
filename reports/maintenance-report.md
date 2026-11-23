# IPTV Maintenance Report

_Generated: **2026-11-23 04:15 UTC**_

Source playlist SHA-256: **fdf0515a52d6545ef6c4b5f1a5f9bbc0e87e46dcb7adc948b5457b356e8a5279**

| Item | Result |
|---|---:|
| Current playlist streams | **1355** |
| Active channel identities | **721** |
| Backup stream entries | **410** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **253** |
| Persistent health failures | **55** |
| Audit findings (review warnings included) | **14** |
| Pre-publish gate | **BLOCK** |

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
