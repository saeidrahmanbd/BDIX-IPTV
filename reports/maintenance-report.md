# IPTV Maintenance Report

_Generated: **2026-11-09 13:42 UTC**_

Source playlist SHA-256: **c05a91e4f6ff628f4f9416d8fbd7490004c83ce45cbd7913e415698c3c812421**

| Item | Result |
|---|---:|
| Current playlist streams | **1069** |
| Active channel identities | **584** |
| Backup stream entries | **334** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **3** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **198** |
| Persistent health failures | **176** |
| Audit blockers | **107** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
