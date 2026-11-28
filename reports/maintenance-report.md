# IPTV Maintenance Report

_Generated: **2026-11-28 10:58 UTC**_

Source playlist SHA-256: **1430770e8c02dd64d1d03bab2f1809e4251e771e5737759c2ec945d0525e162c**

| Item | Result |
|---|---:|
| Current playlist streams | **1373** |
| Active channel identities | **702** |
| Backup stream entries | **489** |
| EPG IDs audited | **702** |
| Logo exceptions | **14** |
| EPG mapping | **60.5%** |
| EPG programme coverage | **54%** |
| Health failures | **68** |
| Persistent health failures | **0** |
| Audit findings (review warnings included) | **154** |
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
