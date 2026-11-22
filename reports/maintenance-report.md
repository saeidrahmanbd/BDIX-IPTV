# IPTV Maintenance Report

_Generated: **2026-11-22 02:40 UTC**_

Source playlist SHA-256: **7535ac5bcd4eac4cc0fd8d5d4f13254a73b76d8c1b366adaca9a6c4571ad83b1**

| Item | Result |
|---|---:|
| Current playlist streams | **1389** |
| Active channel identities | **694** |
| Backup stream entries | **443** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **217** |
| Persistent health failures | **55** |
| Audit findings (review warnings included) | **5** |
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
