# IPTV Maintenance Report

_Generated: **2026-10-06 11:10 UTC**_

| Item | Result |
|---|---:|
| Current playlist streams | **1095** |
| Current channel IDs | **699** |
| Backup streams | **352** |
| New Channels | **0** |
| New Queue (legacy) | **0** |
| Logo exceptions | **0** |
| EPG mapping | **83.5%** |
| EPG programme coverage | **79.4%** |
| Health failures | **139** |
| Persistent health failures | **120** |
| Audit blockers | **29** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain separate user-controlled review queues.
- Dashboard and reports are generated from the current playlist.
