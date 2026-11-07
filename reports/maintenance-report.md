# IPTV Maintenance Report

_Generated: **2026-11-07 04:22 UTC**_

Source playlist SHA-256: **cd6377419d8ca65d3d25ee56f45c93652662f387ef32bc1175d99e268aa6d935**

| Item | Result |
|---|---:|
| Current playlist streams | **1007** |
| Active channel identities | **658** |
| Backup stream entries | **349** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **1** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **48** |
| Persistent health failures | **45** |
| Audit blockers | **14** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
