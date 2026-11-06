# IPTV Maintenance Report

_Generated: **2026-11-06 21:42 UTC**_

Source playlist SHA-256: **92a045f671165942d728082edaac08bdaa83c0320afde042d00ed9b6ea1da67a**

| Item | Result |
|---|---:|
| Current playlist streams | **1121** |
| Active channel identities | **655** |
| Backup stream entries | **322** |
| EPG IDs audited | **671** |
| Logo exceptions | **1** |
| EPG mapping | **63.8%** |
| EPG programme coverage | **57%** |
| Health failures | **162** |
| Persistent health failures | **135** |
| Audit blockers | **13** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
