# IPTV Maintenance Report

_Generated: **2026-11-08 02:50 UTC**_

Source playlist SHA-256: **6da7347dcf4d355f3469116aea87f011f70e2699cfc38f2c08ff136138f1680e**

| Item | Result |
|---|---:|
| Current playlist streams | **1004** |
| Active channel identities | **674** |
| Backup stream entries | **330** |
| EPG IDs audited | **674** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **63.5%** |
| EPG programme coverage | **56%** |
| Health failures | **58** |
| Persistent health failures | **47** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
