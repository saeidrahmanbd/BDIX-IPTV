# IPTV Maintenance Report

_Generated: **2026-11-09 18:27 UTC**_

Source playlist SHA-256: **fef2a109e2349dbd620cb09d4d8f529d164723c199fbdea3fff4527e4912b1c7**

| Item | Result |
|---|---:|
| Current playlist streams | **1068** |
| Active channel identities | **599** |
| Backup stream entries | **328** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **188** |
| Persistent health failures | **184** |
| Audit blockers | **0** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
