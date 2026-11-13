# IPTV Maintenance Report

_Generated: **2026-11-13 18:33 UTC**_

Source playlist SHA-256: **18961862f7ba2836ff0f867724779b2bdd3afbba16d9882faf394eca6f55b469**

| Item | Result |
|---|---:|
| Current playlist streams | **1284** |
| Active channel identities | **646** |
| Backup stream entries | **424** |
| EPG IDs audited | **646** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **58.7%** |
| EPG programme coverage | **51%** |
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
