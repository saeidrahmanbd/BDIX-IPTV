# IPTV Maintenance Report

_Generated: **2026-11-09 04:17 UTC**_

Source playlist SHA-256: **e55dc8cf1536db3e5db4794947ea664c267179f08882d87e89517b0eacd5e286**

| Item | Result |
|---|---:|
| Current playlist streams | **1000** |
| Active channel identities | **596** |
| Backup stream entries | **324** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **136** |
| Persistent health failures | **133** |
| Audit blockers | **0** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
