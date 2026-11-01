# IPTV Maintenance Report

_Generated: **2026-11-01 10:21 UTC**_

Source playlist SHA-256: **32b6dd7241c3541e314d58e49c077cb0e7eb9384141e5419f6d03376ec98769e**

| Item | Result |
|---|---:|
| Current playlist streams | **1119** |
| Active channel identities | **643** |
| Backup stream entries | **315** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
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
