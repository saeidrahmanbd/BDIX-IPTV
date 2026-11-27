# IPTV Maintenance Report

_Generated: **2026-11-27 08:40 UTC**_

Source playlist SHA-256: **5b13ee8b1e9ac748bcf7e274638d42ee60f078298acbc6b550712521b064b71d**

| Item | Result |
|---|---:|
| Current playlist streams | **1196** |
| Active channel identities | **708** |
| Backup stream entries | **434** |
| EPG IDs audited | **708** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **60.5%** |
| EPG programme coverage | **54%** |
| Health failures | **67** |
| Persistent health failures | **0** |
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
