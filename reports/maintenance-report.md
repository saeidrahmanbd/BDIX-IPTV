# IPTV Maintenance Report

_Generated: **2026-11-09 10:43 UTC**_

Source playlist SHA-256: **0680bfb8102b091d27c93ed5c2b58c175616473b7d81543b8dfdfcb0f1fa6b54**

| Item | Result |
|---|---:|
| Current playlist streams | **1069** |
| Active channel identities | **578** |
| Backup stream entries | **335** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **3** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **179** |
| Persistent health failures | **171** |
| Audit blockers | **18** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
