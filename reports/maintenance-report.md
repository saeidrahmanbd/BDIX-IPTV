# IPTV Maintenance Report

_Generated: **2026-11-06 14:12 UTC**_

Source playlist SHA-256: **9984e08ae9e3a60145c9376882c244a81d0f8526b9794a3978714b5dab6d9ed9**

| Item | Result |
|---|---:|
| Current playlist streams | **1121** |
| Active channel identities | **656** |
| Backup stream entries | **321** |
| EPG IDs audited | **672** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **63.8%** |
| EPG programme coverage | **57%** |
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
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
