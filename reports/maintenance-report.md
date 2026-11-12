# IPTV Maintenance Report

_Generated: **2026-11-12 16:02 UTC**_

Source playlist SHA-256: **d6e1529751e08b7398130851537c569ab346feb702af65937d14753d6f1146f1**

| Item | Result |
|---|---:|
| Current playlist streams | **1242** |
| Active channel identities | **646** |
| Backup stream entries | **424** |
| EPG IDs audited | **646** |
| Logo exceptions | **1** |
| EPG mapping | **58.7%** |
| EPG programme coverage | **51%** |
| Health failures | **181** |
| Persistent health failures | **161** |
| Audit blockers | **104** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
