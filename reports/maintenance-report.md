# IPTV Maintenance Report

_Generated: **2026-11-12 11:50 UTC**_

Source playlist SHA-256: **9035b8514990d9681dc96a8d7ea6999c2c0777762e2945cdaf2edbd8fdce224e**

| Item | Result |
|---|---:|
| Current playlist streams | **1242** |
| Active channel identities | **650** |
| Backup stream entries | **420** |
| EPG IDs audited | **650** |
| Logo exceptions | **1** |
| EPG mapping | **58.9%** |
| EPG programme coverage | **52%** |
| Health failures | **173** |
| Persistent health failures | **164** |
| Audit blockers | **35** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
