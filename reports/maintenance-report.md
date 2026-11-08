# IPTV Maintenance Report

_Generated: **2026-11-08 05:32 UTC**_

Source playlist SHA-256: **a5c0d5cbdb7c6b01393b624290f84e0e0b5b5df4437d63e967fd8228383264fd**

| Item | Result |
|---|---:|
| Current playlist streams | **1038** |
| Active channel identities | **698** |
| Backup stream entries | **339** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **16** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **65** |
| Persistent health failures | **60** |
| Audit blockers | **18** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
