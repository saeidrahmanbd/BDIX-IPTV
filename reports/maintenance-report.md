# IPTV Maintenance Report

_Generated: **2026-11-23 03:41 UTC**_

Source playlist SHA-256: **b0f7fb7056bec0e61e50437f4ce8070b5c6a05169d030fc162bab5d1ca59f9da**

| Item | Result |
|---|---:|
| Current playlist streams | **1345** |
| Active channel identities | **715** |
| Backup stream entries | **410** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **253** |
| Persistent health failures | **55** |
| Audit findings (review warnings included) | **8** |
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
