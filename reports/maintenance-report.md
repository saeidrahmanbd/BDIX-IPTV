# IPTV Maintenance Report

_Generated: **2026-11-12 06:18 UTC**_

Source playlist SHA-256: **da00dcae1e57f4bf8f743e612c8c55bb19699c12744f59b6264957e7ee792387**

| Item | Result |
|---|---:|
| Current playlist streams | **1381** |
| Active channel identities | **685** |
| Backup stream entries | **463** |
| EPG IDs audited | **685** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **59.4%** |
| EPG programme coverage | **52%** |
| Health failures | **STALE** |
| Persistent health failures | **STALE** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
