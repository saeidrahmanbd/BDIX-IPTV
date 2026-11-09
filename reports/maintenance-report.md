# IPTV Maintenance Report

_Generated: **2026-11-09 03:00 UTC**_

Source playlist SHA-256: **8675200ab8b37acc114ba0d5fc456d80611f2715c3226f08837681133391c6b5**

| Item | Result |
|---|---:|
| Current playlist streams | **998** |
| Active channel identities | **596** |
| Backup stream entries | **324** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **161** |
| Persistent health failures | **132** |
| Audit blockers | **0** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
