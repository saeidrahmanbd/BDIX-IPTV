# IPTV Maintenance Report

_Generated: **2026-11-08 04:23 UTC**_

Source playlist SHA-256: **e63f25d17d0eee6f63243d8402bf18380bcc58ecf2f2eca7918d8bd79f09e318**

| Item | Result |
|---|---:|
| Current playlist streams | **1004** |
| Active channel identities | **674** |
| Backup stream entries | **330** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **65** |
| Persistent health failures | **47** |
| Audit blockers | **1** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
