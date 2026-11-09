# IPTV Maintenance Report

_Generated: **2026-11-09 18:14 UTC**_

Source playlist SHA-256: **7f2e81547740b18d20fa6f73e80fac1aa4b99bf7321468f0467d55b7e6d74a42**

| Item | Result |
|---|---:|
| Current playlist streams | **1068** |
| Active channel identities | **598** |
| Backup stream entries | **329** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **193** |
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
