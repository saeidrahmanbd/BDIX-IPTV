# IPTV Maintenance Report

_Generated: **2026-11-06 01:38 UTC**_

Source playlist SHA-256: **c1e170f5553fb67bfd7966dc803db253fd14b6e20a94375f13cf7f6b50710bc0**

| Item | Result |
|---|---:|
| Current playlist streams | **1065** |
| Active channel identities | **676** |
| Backup stream entries | **304** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **1** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **103** |
| Persistent health failures | **94** |
| Audit blockers | **42** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
