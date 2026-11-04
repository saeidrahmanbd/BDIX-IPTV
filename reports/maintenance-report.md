# IPTV Maintenance Report

_Generated: **2026-11-04 01:49 UTC**_

Source playlist SHA-256: **f9899be34933deceb7b8eb79fc830c4bfbe7e6d1f902e499f09ddc54c9c0d315**

| Item | Result |
|---|---:|
| Current playlist streams | **1090** |
| Active channel identities | **680** |
| Backup stream entries | **346** |
| EPG IDs audited | **741** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **65.9%** |
| EPG programme coverage | **59%** |
| Health failures | **110** |
| Persistent health failures | **87** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
