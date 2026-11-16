# IPTV Maintenance Report

_Generated: **2026-11-16 03:33 UTC**_

Source playlist SHA-256: **910e85f0a79f101b8afe550c781126fb156b183e4c678472f2fe3f1699777d73**

| Item | Result |
|---|---:|
| Current playlist streams | **1298** |
| Active channel identities | **657** |
| Backup stream entries | **438** |
| EPG IDs audited | **657** |
| Logo exceptions | **0** |
| EPG mapping | **58.8%** |
| EPG programme coverage | **50%** |
| Health failures | **200** |
| Persistent health failures | **0** |
| Audit findings (review warnings included) | **128** |
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
