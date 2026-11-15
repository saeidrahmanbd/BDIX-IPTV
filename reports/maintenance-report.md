# IPTV Maintenance Report

_Generated: **2026-11-15 08:14 UTC**_

Source playlist SHA-256: **80cee209bddaaed878591d9fb195a8619ba2663a375dd834edd7e8c70c2c1518**

| Item | Result |
|---|---:|
| Current playlist streams | **1276** |
| Active channel identities | **645** |
| Backup stream entries | **423** |
| EPG IDs audited | **645** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **58.9%** |
| EPG programme coverage | **50%** |
| Health failures | **STALE** |
| Persistent health failures | **STALE** |
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
