# IPTV Maintenance Report

_Generated: **2026-11-07 04:32 UTC**_

Source playlist SHA-256: **b21a4dad6ee749428f415bb044c876dc88c6e8cada2c5e50c155b3c9397a16ff**

| Item | Result |
|---|---:|
| Current playlist streams | **1010** |
| Active channel identities | **659** |
| Backup stream entries | **351** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **1** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **47** |
| Persistent health failures | **46** |
| Audit blockers | **16** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
