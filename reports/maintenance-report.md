# IPTV Maintenance Report

_Generated: **2026-10-31 10:56 UTC**_

Source playlist SHA-256: **6c693baea478e44539eac29fb99c0b3aa6e7109f06134b8b010d3449c259b49c**

| Item | Result |
|---|---:|
| Current playlist streams | **1160** |
| Active channel identities | **655** |
| Backup stream entries | **366** |
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
