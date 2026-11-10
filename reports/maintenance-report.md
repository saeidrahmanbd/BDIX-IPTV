# IPTV Maintenance Report

_Generated: **2026-11-10 03:46 UTC**_

Source playlist SHA-256: **3a82bd3bb723138e3d18d13e4a394f6fe0c1e806e1159349bd3bcf4611413c78**

| Item | Result |
|---|---:|
| Current playlist streams | **1074** |
| Active channel identities | **591** |
| Backup stream entries | **329** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **194** |
| Persistent health failures | **185** |
| Audit blockers | **0** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
