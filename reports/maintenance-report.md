# IPTV Maintenance Report

_Generated: **2026-11-07 21:51 UTC**_

Source playlist SHA-256: **630592a6da287492f2f8b41b94028eeed5610cf41d3aac44054b2cf6c3bc5e29**

| Item | Result |
|---|---:|
| Current playlist streams | **1004** |
| Active channel identities | **674** |
| Backup stream entries | **330** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **58** |
| Persistent health failures | **47** |
| Audit blockers | **1** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
