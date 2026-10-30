# IPTV Maintenance Report

_Generated: **2026-10-30 07:40 UTC**_

Source playlist SHA-256: **2f00cd81215b375e4776d6dd458f71acc5734daf86990b5c85061a1bec922a77**

| Item | Result |
|---|---:|
| Current playlist streams | **1160** |
| Active channel identities | **655** |
| Backup stream entries | **366** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **137** |
| Persistent health failures | **134** |
| Audit blockers | **0** |
| Pre-publish gate | **UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current three-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
