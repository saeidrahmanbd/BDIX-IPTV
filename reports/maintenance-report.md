# IPTV Maintenance Report

_Generated: **2026-11-02 05:14 UTC**_

Source playlist SHA-256: **0e3ea858f8ba56c3cc8ce1d8d16e6bda7c758330612ecd4f76fb340b6e4ec783**

| Item | Result |
|---|---:|
| Current playlist streams | **1026** |
| Active channel identities | **680** |
| Backup stream entries | **346** |
| EPG IDs audited | **680** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **64.4%** |
| EPG programme coverage | **55%** |
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
