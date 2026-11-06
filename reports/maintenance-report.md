# IPTV Maintenance Report

_Generated: **2026-11-06 13:31 UTC**_

Source playlist SHA-256: **e1dc8920d2906ee16fcf71ce8cf0bf16900c231cf306ea6874bae398dbd6e29a**

| Item | Result |
|---|---:|
| Current playlist streams | **1120** |
| Active channel identities | **656** |
| Backup stream entries | **321** |
| EPG IDs audited | **PENDING — guide not current** |
| Logo exceptions | **2** |
| EPG mapping | **PENDING — guide not current** |
| EPG programme coverage | **PENDING** |
| Health failures | **139** |
| Persistent health failures | **128** |
| Audit blockers | **2** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain active discovery/review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
