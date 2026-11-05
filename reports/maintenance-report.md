# IPTV Maintenance Report

_Generated: **2026-11-05 01:45 UTC**_

Source playlist SHA-256: **f5795953ab6e9474334bc1dc17149eaf70528a4602c0084f59ecbe44665f78ef**

| Item | Result |
|---|---:|
| Current playlist streams | **1113** |
| Active channel identities | **683** |
| Backup stream entries | **335** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **1** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **127** |
| Persistent health failures | **90** |
| Audit blockers | **1** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
