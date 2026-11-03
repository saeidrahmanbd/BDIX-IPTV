# IPTV Maintenance Report

_Generated: **2026-11-03 02:20 UTC**_

Source playlist SHA-256: **0effbae25904525535b8b1cccb3c1c4a955b5785b5476d006857db7be5f26a1f**

| Item | Result |
|---|---:|
| Current playlist streams | **1090** |
| Active channel identities | **680** |
| Backup stream entries | **346** |
| EPG IDs audited | **741** |
| Logo exceptions | **7** |
| EPG mapping | **65.9%** |
| EPG programme coverage | **59%** |
| Health failures | **95** |
| Persistent health failures | **60** |
| Audit blockers | **7** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
