# IPTV Maintenance Report

_Generated: **2026-11-08 09:40 UTC**_

Source playlist SHA-256: **6a28ea1a0563866ab751af2be458465788011ee1f8c39e3adfba9c629b15ff2d**

| Item | Result |
|---|---:|
| Current playlist streams | **952** |
| Active channel identities | **618** |
| Backup stream entries | **333** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **10** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **54** |
| Persistent health failures | **46** |
| Audit blockers | **10** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
