# IPTV Maintenance Report

_Generated: **2026-11-10 08:03 UTC**_

Source playlist SHA-256: **0c1edb1d00f703b7c5176236b251a547670551d4be1f47619cfb735b64cfaa5b**

| Item | Result |
|---|---:|
| Current playlist streams | **1066** |
| Active channel identities | **577** |
| Backup stream entries | **327** |
| EPG IDs audited | **577** |
| Logo exceptions | **0** |
| EPG mapping | **60.8%** |
| EPG programme coverage | **52%** |
| Health failures | **195** |
| Persistent health failures | **182** |
| Audit blockers | **7** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
