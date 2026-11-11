# IPTV Maintenance Report

_Generated: **2026-11-11 07:02 UTC**_

Source playlist SHA-256: **de1b7f58ac232ec72d734c2aca3bb35070d31536fda83b52f4e4ac1cc39dde5a**

| Item | Result |
|---|---:|
| Current playlist streams | **1184** |
| Active channel identities | **592** |
| Backup stream entries | **406** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **202** |
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
