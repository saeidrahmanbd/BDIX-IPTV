# IPTV Maintenance Report

_Generated: **2026-11-18 12:49 UTC**_

Source playlist SHA-256: **002e4acc43c2210fe25ceb35ed68582b869af2706f3754964d43a274d3618baf**

| Item | Result |
|---|---:|
| Current playlist streams | **1378** |
| Active channel identities | **714** |
| Backup stream entries | **463** |
| EPG IDs audited | **714** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **60.8%** |
| EPG programme coverage | **54%** |
| Health failures | **264** |
| Persistent health failures | **49** |
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
