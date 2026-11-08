# IPTV Maintenance Report

_Generated: **2026-11-08 18:06 UTC**_

Source playlist SHA-256: **dee4c0905162325bb433379bae254831ad1834640807c7670b213f343caec9f3**

| Item | Result |
|---|---:|
| Current playlist streams | **999** |
| Active channel identities | **597** |
| Backup stream entries | **324** |
| EPG IDs audited | **597** |
| Logo exceptions | **0** |
| EPG mapping | **61.3%** |
| EPG programme coverage | **51%** |
| Health failures | **130** |
| Persistent health failures | **126** |
| Audit blockers | **18** |
| Pre-publish gate | **BLOCK** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- Review, New Channels and New Backups remain hidden review queues.
- Backup counts do not imply independent CDN/origin redundancy.
- Report freshness is checked against current source hashes or the current two-playlist inventory; mismatched metrics are labelled stale instead of shown as current.
