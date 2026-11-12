# IPTV Maintenance Report

_Generated: **2026-11-12 07:12 UTC**_

Source playlist SHA-256: **b4bd82f1c2158f3f4cef5a6a16f9567e9db54d682a807b9dbc4ee64ccc0d59a4**

| Item | Result |
|---|---:|
| Current playlist streams | **1242** |
| Active channel identities | **650** |
| Backup stream entries | **420** |
| EPG IDs audited | **650** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **58.9%** |
| EPG programme coverage | **51%** |
| Health failures | **STALE** |
| Persistent health failures | **STALE** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
