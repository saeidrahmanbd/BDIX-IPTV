# IPTV Maintenance Report

_Generated: **2026-11-01 12:26 UTC**_

Source playlist SHA-256: **d3085d33a0d6e95f27d2d1bbe6acd87a18d55ee5ff1da89ecea62cffbe62bccd**

| Item | Result |
|---|---:|
| Current playlist streams | **1167** |
| Active channel identities | **641** |
| Backup stream entries | **340** |
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
