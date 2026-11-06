# IPTV Maintenance Report

_Generated: **2026-11-06 16:20 UTC**_

Source playlist SHA-256: **d8ac07ce135cde8d024e6a4945c377175132e290d02e275bcd0e376fdddc692e**

| Item | Result |
|---|---:|
| Current playlist streams | **1121** |
| Active channel identities | **656** |
| Backup stream entries | **321** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **1** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **142** |
| Persistent health failures | **121** |
| Audit blockers | **1** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
