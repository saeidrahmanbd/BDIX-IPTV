# IPTV Maintenance Report

_Generated: **2026-11-09 04:58 UTC**_

Source playlist SHA-256: **0971846e84de0e04e79a2d27a11b6d8df7a8def644acead8f3facd9ecf556bf3**

| Item | Result |
|---|---:|
| Current playlist streams | **989** |
| Active channel identities | **576** |
| Backup stream entries | **324** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **135** |
| Persistent health failures | **130** |
| Audit blockers | **13** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
