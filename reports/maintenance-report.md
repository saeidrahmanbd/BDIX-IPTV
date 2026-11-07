# IPTV Maintenance Report

_Generated: **2026-11-07 14:23 UTC**_

Source playlist SHA-256: **84c02ef014377e5b6ba95a227f9783389650950895cfd82aece9c12b369a6a98**

| Item | Result |
|---|---:|
| Current playlist streams | **1005** |
| Active channel identities | **674** |
| Backup stream entries | **331** |
| EPG IDs audited | **674** |
| Logo exceptions | **0** |
| EPG mapping | **63.5%** |
| EPG programme coverage | **57%** |
| Health failures | **54** |
| Persistent health failures | **47** |
| Audit blockers | **0** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
