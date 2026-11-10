# IPTV Maintenance Report

_Generated: **2026-11-10 12:34 UTC**_

Source playlist SHA-256: **cad47ab906061198dde4b340ad8d12ae82144957cc14020cd84df15b093ce4ab**

| Item | Result |
|---|---:|
| Current playlist streams | **1150** |
| Active channel identities | **590** |
| Backup stream entries | **390** |
| EPG IDs audited | **590** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **61.0%** |
| EPG programme coverage | **53%** |
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
