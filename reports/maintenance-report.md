# IPTV Maintenance Report

_Generated: **2026-10-08 03:46 UTC**_

| Item | Result |
|---|---:|
| Current playlist streams | **1143** |
| Current channel IDs | **707** |
| Backup streams | **400** |
| New Channels | **0** |
| New Queue (legacy) | **0** |
| Logo exceptions | **1** |
| EPG mapping | **82.2%** |
| EPG programme coverage | **79.0%** |
| Health failures | **142** |
| Persistent health failures | **113** |
| Audit blockers | **15** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain separate user-controlled review queues.
- Dashboard and reports are generated from the current playlist.
