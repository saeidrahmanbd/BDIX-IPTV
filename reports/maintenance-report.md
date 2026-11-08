# IPTV Maintenance Report

_Generated: **2026-11-08 08:48 UTC**_

Source playlist SHA-256: **f1ecd6bd351968ef79708f50c7251d6967d4aaf442066e439f621b0a600240ec**

| Item | Result |
|---|---:|
| Current playlist streams | **952** |
| Active channel identities | **618** |
| Backup stream entries | **333** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **10** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **58** |
| Persistent health failures | **49** |
| Audit blockers | **13** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
