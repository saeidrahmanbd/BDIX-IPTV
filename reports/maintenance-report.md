# IPTV Maintenance Report

_Generated: **2026-11-13 08:51 UTC**_

Source playlist SHA-256: **006cd670ecdde84fe0481c6405214f3fb618e234a7abe12f8bce3f1553bb6c8d**

| Item | Result |
|---|---:|
| Current playlist streams | **1280** |
| Active channel identities | **646** |
| Backup stream entries | **424** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **4** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **207** |
| Persistent health failures | **196** |
| Audit blockers | **107** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
