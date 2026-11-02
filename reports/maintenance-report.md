# IPTV Maintenance Report

_Generated: **2026-11-02 04:01 UTC**_

Source playlist SHA-256: **0c31f4d953ef07e39cd11c10526f6dab9ffe77d5ee69b5030d2c4ae744f6811e**

| Item | Result |
|---|---:|
| Current playlist streams | **1186** |
| Active channel identities | **685** |
| Backup stream entries | **340** |
| EPG IDs audited | **705** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **65.5%** |
| EPG programme coverage | **56%** |
| Health failures | **STALE** |
| Persistent health failures | **STALE** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current three-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
