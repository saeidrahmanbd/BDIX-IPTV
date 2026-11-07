# IPTV Maintenance Report

_Generated: **2026-11-07 04:55 UTC**_

Source playlist SHA-256: **6e44e22bfc055b60ad16371a15e76724955d2779304f30257697067d7c545b46**

| Item | Result |
|---|---:|
| Current playlist streams | **1002** |
| Active channel identities | **672** |
| Backup stream entries | **330** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **0** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **67** |
| Persistent health failures | **44** |
| Audit blockers | **0** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
