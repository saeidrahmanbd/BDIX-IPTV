# IPTV Maintenance Report

_Generated: **2026-11-08 10:08 UTC**_

Source playlist SHA-256: **56bfb01abfd601e1a1971134720650745d4d799bb6c0a74683e24f375f1f22f6**

| Item | Result |
|---|---:|
| Current playlist streams | **942** |
| Active channel identities | **608** |
| Backup stream entries | **333** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
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
