# IPTV Maintenance Report

_Generated: **2026-11-11 19:26 UTC**_

Source playlist SHA-256: **a98bfb7e890a2d639d238b957b98d47678e6aef0a035b526716557990ef5c04f**

| Item | Result |
|---|---:|
| Current playlist streams | **1331** |
| Active channel identities | **685** |
| Backup stream entries | **463** |
| EPG IDs audited | **685** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **59.1%** |
| EPG programme coverage | **52%** |
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
