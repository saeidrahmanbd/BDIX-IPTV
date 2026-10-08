# IPTV Maintenance Report

_Generated: **2026-10-08 08:58 UTC**_

| Item | Result |
|---|---:|
| Current playlist streams | **1143** |
| Current channel IDs | **709** |
| Backup streams | **400** |
| New Channels | **0** |
| New Queue (legacy) | **0** |
| Logo exceptions | **0** |
| EPG mapping | **81.9%** |
| EPG programme coverage | **78.6%** |
| Health failures | **136** |
| Persistent health failures | **131** |
| Audit blockers | **117** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain separate user-controlled review queues.
- Dashboard and reports are generated from the current playlist.
