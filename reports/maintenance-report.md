# IPTV Maintenance Report

_Generated: **2026-10-06 07:33 UTC**_

| Item | Result |
|---|---:|
| Current playlist streams | **1082** |
| Current channel IDs | **696** |
| Backup streams | **352** |
| New Channels | **0** |
| New Queue (legacy) | **0** |
| Logo exceptions | **0** |
| EPG mapping | **83.5%** |
| EPG programme coverage | **79.4%** |
| Health failures | **117** |
| Persistent health failures | **110** |
| Audit blockers | **13** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain separate user-controlled review queues.
- Dashboard and reports are generated from the current playlist.
