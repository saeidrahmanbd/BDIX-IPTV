# IPTV Maintenance Report

_Generated: **2026-11-02 10:02 UTC**_

Source playlist SHA-256: **c83a2db794504997f9441df2faae73c5ea42a78b7bf4e7bd8f4e3c1d397f5454**

| Item | Result |
|---|---:|
| Current playlist streams | **1066** |
| Active channel identities | **680** |
| Backup stream entries | **346** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **7** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **68** |
| Persistent health failures | **21** |
| Audit blockers | **7** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
