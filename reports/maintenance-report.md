# IPTV Maintenance Report

_Generated: **2026-11-24 07:09 UTC**_

Source playlist SHA-256: **ff15c8ceffaa71c72e6b9f2c387ff941dc227454cb482bb4a2943966640ec13c**

| Item | Result |
|---|---:|
| Current playlist streams | **1339** |
| Active channel identities | **695** |
| Backup stream entries | **396** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **271** |
| Persistent health failures | **56** |
| Audit findings (review warnings included) | **35** |
| Pre-publish gate | **BLOCK** |

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
