# IPTV Maintenance Report

_Generated: **2026-11-11 01:39 UTC**_

Source playlist SHA-256: **068d75f7a328a5a3f6bf9de04769dad2e798b2a5a5c361da81644581f8485993**

| Item | Result |
|---|---:|
| Current playlist streams | **1188** |
| Active channel identities | **609** |
| Backup stream entries | **408** |
| EPG IDs audited | **609** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **61.4%** |
| EPG programme coverage | **53%** |
| Health failures | **194** |
| Persistent health failures | **180** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
