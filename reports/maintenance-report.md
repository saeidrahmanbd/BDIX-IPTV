# IPTV Maintenance Report

_Generated: **2026-10-07 10:52 UTC**_

| Item | Result |
|---|---:|
| Current playlist streams | **1142** |
| Current channel IDs | **706** |
| Backup streams | **400** |
| New Channels | **0** |
| New Queue (legacy) | **0** |
| Logo exceptions | **1** |
| EPG mapping | **82.2%** |
| EPG programme coverage | **77.9%** |
| Health failures | **114** |
| Persistent health failures | **112** |
| Audit blockers | **15** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain separate user-controlled review queues.
- Dashboard and reports are generated from the current playlist.
