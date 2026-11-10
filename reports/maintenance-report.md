# IPTV Maintenance Report

_Generated: **2026-11-10 08:57 UTC**_

Source playlist SHA-256: **b9788f72fccc6068192664229352aba60bf534028a8d2362a740cf7623425e9c**

| Item | Result |
|---|---:|
| Current playlist streams | **1066** |
| Active channel identities | **577** |
| Backup stream entries | **327** |
| EPG IDs audited | **577** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **60.8%** |
| EPG programme coverage | **52%** |
| Health failures | **STALE** |
| Persistent health failures | **STALE** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
