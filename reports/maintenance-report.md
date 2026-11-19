# IPTV Maintenance Report

_Generated: **2026-11-19 05:04 UTC**_

Source playlist SHA-256: **8611340c6b07807062028b490d6f6cd925bf5fb18ac79bb174f637872523e81e**

| Item | Result |
|---|---:|
| Current playlist streams | **1390** |
| Active channel identities | **714** |
| Backup stream entries | **463** |
| EPG IDs audited | **714** |
| Logo exceptions | **1** |
| EPG mapping | **60.8%** |
| EPG programme coverage | **54%** |
| Health failures | **240** |
| Persistent health failures | **50** |
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
