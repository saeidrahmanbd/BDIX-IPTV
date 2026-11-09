# IPTV Maintenance Report

_Generated: **2026-11-09 17:17 UTC**_

Source playlist SHA-256: **f50a8a1a719081af7d1e77ccd1457ce89c860ec875ed99a5f933958bfdedae39**

| Item | Result |
|---|---:|
| Current playlist streams | **1069** |
| Active channel identities | **599** |
| Backup stream entries | **334** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **3** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **184** |
| Persistent health failures | **180** |
| Audit blockers | **42** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
