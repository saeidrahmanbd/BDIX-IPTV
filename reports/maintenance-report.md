# IPTV Maintenance Report

_Generated: **2026-11-12 08:13 UTC**_

Source playlist SHA-256: **c4dece2f2bf4cd4b4b2d6b11c052f7a7f46d338791823e770a8ff3f38d53f646**

| Item | Result |
|---|---:|
| Current playlist streams | **1242** |
| Active channel identities | **650** |
| Backup stream entries | **420** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **3** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **210** |
| Persistent health failures | **165** |
| Audit blockers | **28** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
