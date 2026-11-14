# IPTV Maintenance Report

_Generated: **2026-11-14 18:27 UTC**_

Source playlist SHA-256: **7a602ff4a6fe777cc812dcedb118b638ab62913c0987dff0a6ac7d674a974d65**

| Item | Result |
|---|---:|
| Current playlist streams | **1284** |
| Active channel identities | **645** |
| Backup stream entries | **425** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **191** |
| Persistent health failures | **155** |
| Audit findings (review warnings included) | **91** |
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
