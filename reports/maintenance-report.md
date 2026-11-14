# IPTV Maintenance Report

_Generated: **2026-11-14 11:51 UTC**_

Source playlist SHA-256: **d47607e2306ca0561e6181336ea25952f4f93a6f56d47b33abbb2b7d221b6c6b**

| Item | Result |
|---|---:|
| Current playlist streams | **1284** |
| Active channel identities | **646** |
| Backup stream entries | **424** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **2** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **178** |
| Persistent health failures | **175** |
| Audit blockers | **113** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
