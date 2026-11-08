# IPTV Maintenance Report

_Generated: **2026-11-08 05:16 UTC**_

Source playlist SHA-256: **90a62dd358fda44303cd601078218e4d569d8c342a838ebda275b59cd0025a6b**

| Item | Result |
|---|---:|
| Current playlist streams | **1007** |
| Active channel identities | **676** |
| Backup stream entries | **330** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **1** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **87** |
| Persistent health failures | **59** |
| Audit blockers | **2** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
