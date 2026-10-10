# IPTV Maintenance Report

_Generated: **2026-10-10 08:31 UTC**_

| Item | Result |
|---|---:|
| Current playlist streams | **1152** |
| Current channel IDs | **713** |
| Backup streams | **398** |
| New Channels | **0** |
| New Queue (legacy) | **0** |
| Logo exceptions | **1** |
| EPG mapping | **81.9%** |
| EPG programme coverage | **79.0%** |
| Health failures | **188** |
| Persistent health failures | **137** |
| Audit blockers | **16** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain separate user-controlled review queues.
- Dashboard and reports are generated from the current playlist.
