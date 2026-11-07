# IPTV Maintenance Report

_Generated: **2026-11-07 04:45 UTC**_

Source playlist SHA-256: **bca056bd163da5534c5919402db1640ccfae58240476c255e4cf422c46701346**

| Item | Result |
|---|---:|
| Current playlist streams | **1010** |
| Active channel identities | **664** |
| Backup stream entries | **324** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **70** |
| Persistent health failures | **46** |
| Audit blockers | **0** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
