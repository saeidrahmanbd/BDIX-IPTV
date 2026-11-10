# IPTV Maintenance Report

_Generated: **2026-11-10 15:12 UTC**_

Source playlist SHA-256: **a7fce54b25229033af7ba06f82a1ef694995f79680b58cbc8abcaa1932353a04**

| Item | Result |
|---|---:|
| Current playlist streams | **1188** |
| Active channel identities | **609** |
| Backup stream entries | **408** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **194** |
| Persistent health failures | **180** |
| Audit blockers | **6** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
