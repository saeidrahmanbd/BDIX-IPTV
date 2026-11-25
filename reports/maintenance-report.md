# IPTV Maintenance Report

_Generated: **2026-11-25 09:23 UTC**_

Source playlist SHA-256: **72b27febe9a11669f9351b81beac6ff23b82b10f241a4052af20783e38fde0cf**

| Item | Result |
|---|---:|
| Current playlist streams | **1369** |
| Active channel identities | **695** |
| Backup stream entries | **405** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **256** |
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
