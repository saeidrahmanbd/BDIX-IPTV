# IPTV Maintenance Report

_Generated: **2026-10-06 06:30 UTC**_

| Item | Result |
|---|---:|
| Current playlist streams | **1085** |
| Current channel IDs | **698** |
| Backup streams | **360** |
| New Channels | **0** |
| New Queue (legacy) | **0** |
| Logo exceptions | **1** |
| EPG mapping | **83.2%** |
| EPG programme coverage | **78.8%** |
| Health failures | **135** |
| Persistent health failures | **130** |
| Audit blockers | **28** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain separate user-controlled review queues.
- Dashboard and reports are generated from the current playlist.
