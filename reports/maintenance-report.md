# IPTV Maintenance Report

_Generated: **2026-11-28 00:18 UTC**_

Source playlist SHA-256: **bc20e905e2a4c4935f2a0ce061b61ef523f9a4a5a2e11e8e632cfc87b79fc57c**

| Item | Result |
|---|---:|
| Current playlist streams | **1197** |
| Active channel identities | **708** |
| Backup stream entries | **434** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **55** |
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
