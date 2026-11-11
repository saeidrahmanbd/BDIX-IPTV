# IPTV Maintenance Report

_Generated: **2026-11-11 09:20 UTC**_

Source playlist SHA-256: **81708ed765570d9c3d509cd9a471595b621b5f2145e4decc0d8bed1cea81d3ce**

| Item | Result |
|---|---:|
| Current playlist streams | **1143** |
| Active channel identities | **579** |
| Backup stream entries | **385** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **189** |
| Persistent health failures | **184** |
| Audit blockers | **24** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
