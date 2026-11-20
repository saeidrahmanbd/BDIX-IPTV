# IPTV Maintenance Report

_Generated: **2026-11-20 01:35 UTC**_

Source playlist SHA-256: **046c235b4d1b57347bf03c7a8a29c35616b825dd2f5ee23a4c3674089ecbb8b9**

| Item | Result |
|---|---:|
| Current playlist streams | **1379** |
| Active channel identities | **694** |
| Backup stream entries | **443** |
| EPG IDs audited | **694** |
| Logo exceptions | **0** |
| EPG mapping | **62.1%** |
| EPG programme coverage | **55%** |
| Health failures | **215** |
| Persistent health failures | **48** |
| Audit findings (review warnings included) | **1** |
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
