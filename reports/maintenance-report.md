# IPTV Maintenance Report

_Generated: **2026-11-10 01:43 UTC**_

Source playlist SHA-256: **1cdf6fb9b301583e715aaa78826992aa3bb5ef9ef2de94b2d35437d2bfcc3676**

| Item | Result |
|---|---:|
| Current playlist streams | **1068** |
| Active channel identities | **599** |
| Backup stream entries | **328** |
| EPG IDs audited | **599** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **60.8%** |
| EPG programme coverage | **52%** |
| Health failures | **187** |
| Persistent health failures | **187** |
| Audit blockers | **STALE / UNKNOWN** |
| Pre-publish gate | **STALE / UNKNOWN** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
