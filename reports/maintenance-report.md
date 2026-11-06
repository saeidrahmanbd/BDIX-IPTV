# IPTV Maintenance Report

_Generated: **2026-11-06 13:12 UTC**_

Source playlist SHA-256: **a65adeae4aa920ad86e8a064f0dd20df5045382598268d2a201c99d0f238ef31**

| Item | Result |
|---|---:|
| Current playlist streams | **1120** |
| Active channel identities | **658** |
| Backup stream entries | **322** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **2** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **135** |
| Persistent health failures | **129** |
| Audit blockers | **2** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
