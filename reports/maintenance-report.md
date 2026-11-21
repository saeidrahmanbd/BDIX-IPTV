# IPTV Maintenance Report

_Generated: **2026-11-21 00:57 UTC**_

Source playlist SHA-256: **9bbdc0608673318c3fc970a8904a67dc47387c4068ee8bc6dc3bab1594a1def7**

| Item | Result |
|---|---:|
| Current playlist streams | **1394** |
| Active channel identities | **694** |
| Backup stream entries | **443** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **227** |
| Persistent health failures | **51** |
| Audit findings (review warnings included) | **1** |
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
