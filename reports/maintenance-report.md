# IPTV Maintenance Report

_Generated: **2026-11-08 13:34 UTC**_

Source playlist SHA-256: **314c5dc9ebb651e864423c1f54c189ba2f39050b1ceaebca5615636237ec6dcf**

| Item | Result |
|---|---:|
| Current playlist streams | **934** |
| Active channel identities | **597** |
| Backup stream entries | **324** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **60** |
| Persistent health failures | **53** |
| Audit blockers | **1** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
