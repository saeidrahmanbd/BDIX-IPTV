# IPTV Maintenance Report

_Generated: **2026-11-14 14:32 UTC**_

Source playlist SHA-256: **d47607e2306ca0561e6181336ea25952f4f93a6f56d47b33abbb2b7d221b6c6b**

| Item | Result |
|---|---:|
| Current playlist streams | **1284** |
| Active channel identities | **646** |
| Backup stream entries | **424** |
| EPG IDs audited | **646** |
| Logo exceptions | **2** |
| EPG mapping | **58.7%** |
| EPG programme coverage | **51%** |
| Health failures | **196** |
| Persistent health failures | **185** |
| Audit findings (review warnings included) | **113** |
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
