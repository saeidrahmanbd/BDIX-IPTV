# IPTV Maintenance Report

_Generated: **2026-11-11 06:35 UTC**_

Source playlist SHA-256: **8ef94f81f3cac966cc88b0eac2b173686e44c385802f6d1a02e6e42227e97ae8**

| Item | Result |
|---|---:|
| Current playlist streams | **1184** |
| Active channel identities | **592** |
| Backup stream entries | **406** |
| EPG IDs audited | **592** |
| Logo exceptions | **0** |
| EPG mapping | **61.1%** |
| EPG programme coverage | **52%** |
| Health failures | **204** |
| Persistent health failures | **183** |
| Audit blockers | **0** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
