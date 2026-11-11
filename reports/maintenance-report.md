# IPTV Maintenance Report

_Generated: **2026-11-11 08:36 UTC**_

Source playlist SHA-256: **34f9bc33c915a05f01807e768ede043d93d7e59798afa56826f95acd3cf0fbde**

| Item | Result |
|---|---:|
| Current playlist streams | **1143** |
| Active channel identities | **588** |
| Backup stream entries | **385** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **189** |
| Persistent health failures | **181** |
| Audit blockers | **23** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
