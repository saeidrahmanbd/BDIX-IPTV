# IPTV Maintenance Report

_Generated: **2026-11-03 09:13 UTC**_

Source playlist SHA-256: **9066c575b7ec57f8cecc46f47ef89584a8b2398c1023122866e72e480bd571ee**

| Item | Result |
|---|---:|
| Current playlist streams | **1090** |
| Active channel identities | **680** |
| Backup stream entries | **346** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **7** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **94** |
| Persistent health failures | **86** |
| Audit blockers | **7** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
