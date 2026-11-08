# IPTV Maintenance Report

_Generated: **2026-11-08 05:27 UTC**_

Source playlist SHA-256: **ba3d0054b73cb0318a5c4696368ca7c81842e955420369aab9dd0af0b697e941**

| Item | Result |
|---|---:|
| Current playlist streams | **1018** |
| Active channel identities | **679** |
| Backup stream entries | **338** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **1** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **68** |
| Persistent health failures | **60** |
| Audit blockers | **3** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
