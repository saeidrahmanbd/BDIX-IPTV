# IPTV Maintenance Report

_Generated: **2026-11-07 03:32 UTC**_

Source playlist SHA-256: **cdb8200954f20b0f2542239d830d95dddcb4582bc659b8225fd0ab2a794fa468**

| Item | Result |
|---|---:|
| Current playlist streams | **1135** |
| Active channel identities | **655** |
| Backup stream entries | **322** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **2** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **157** |
| Persistent health failures | **134** |
| Audit blockers | **2** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
