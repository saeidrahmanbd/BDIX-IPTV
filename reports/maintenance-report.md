# IPTV Maintenance Report

_Generated: **2026-11-25 01:35 UTC**_

Source playlist SHA-256: **a2ef9bb3e7d03dbfffd4f78e796027e4f5e46374fe9717d89785190c04f23e6a**

| Item | Result |
|---|---:|
| Current playlist streams | **1354** |
| Active channel identities | **695** |
| Backup stream entries | **396** |
| EPG IDs audited | **695** |
| Logo exceptions | **0** |
| EPG mapping | **62.2%** |
| EPG programme coverage | **54%** |
| Health failures | **293** |
| Persistent health failures | **57** |
| Audit findings (review warnings included) | **19** |
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
