# IPTV Maintenance Report

_Generated: **2026-11-27 05:26 UTC**_

Source playlist SHA-256: **9558746a36438c06848914c1906a5f2210f5c8e6c367af65c65a1529bbcf4c49**

| Item | Result |
|---|---:|
| Current playlist streams | **1196** |
| Active channel identities | **708** |
| Backup stream entries | **434** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **67** |
| Persistent health failures | **0** |
| Audit findings (review warnings included) | **2** |
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
