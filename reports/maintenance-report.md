# IPTV Maintenance Report

_Generated: **2026-11-10 13:19 UTC**_

Source playlist SHA-256: **1fecff40e4b2f5a4a6e31805dc88b93179bdf2d752f56b8ae8cfc6aaacd8a6db**

| Item | Result |
|---|---:|
| Current playlist streams | **1169** |
| Active channel identities | **605** |
| Backup stream entries | **393** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **185** |
| Persistent health failures | **179** |
| Audit blockers | **0** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
