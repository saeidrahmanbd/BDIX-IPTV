# IPTV Maintenance Report

_Generated: **2026-11-09 00:03 UTC**_

Source playlist SHA-256: **a02d892fda4e692ec37814a8206c4ff6c6ab200d77b7592a17da1d7c01fd070b**

| Item | Result |
|---|---:|
| Current playlist streams | **998** |
| Active channel identities | **596** |
| Backup stream entries | **324** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **157** |
| Persistent health failures | **121** |
| Audit blockers | **0** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
