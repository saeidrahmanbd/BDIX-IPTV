# IPTV Maintenance Report

_Generated: **2026-11-08 14:23 UTC**_

Source playlist SHA-256: **ad7ab0110569ca3f9aa02be4d0caf0af3b61d0255bae43ee04fee6bbcac4b3bf**

| Item | Result |
|---|---:|
| Current playlist streams | **990** |
| Active channel identities | **597** |
| Backup stream entries | **324** |
| EPG IDs audited | **597** |
| Logo exceptions | **STALE / UNKNOWN** |
| EPG mapping | **60.8%** |
| EPG programme coverage | **51%** |
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
