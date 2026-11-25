# IPTV Maintenance Report

_Generated: **2026-11-25 08:40 UTC**_

Source playlist SHA-256: **c4a95d4b9182121074a01e2863683a37f0b41db4242dba26b72ee7a1c25de3d5**

| Item | Result |
|---|---:|
| Current playlist streams | **1369** |
| Active channel identities | **695** |
| Backup stream entries | **405** |
| EPG IDs audited | **695** |
| Logo exceptions | **0** |
| EPG mapping | **62.2%** |
| EPG programme coverage | **54%** |
| Health failures | **257** |
| Persistent health failures | **57** |
| Audit findings (review warnings included) | **4** |
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
