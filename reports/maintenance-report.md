# IPTV Maintenance Report

_Generated: **2026-11-22 06:56 UTC**_

Source playlist SHA-256: **0e135710f0964eb757aa03c22ce16c8b1d48cad03639d48f28903aadee255a73**

| Item | Result |
|---|---:|
| Current playlist streams | **1389** |
| Active channel identities | **694** |
| Backup stream entries | **443** |
| EPG IDs audited | **694** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **62.1%** |
| EPG programme coverage | **55%** |
| Health failures | **216** |
| Persistent health failures | **55** |
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
