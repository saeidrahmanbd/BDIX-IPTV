# IPTV Maintenance Report

_Generated: **2026-10-09 09:05 UTC**_

| Item | Result |
|---|---:|
| Current playlist streams | **1151** |
| Current channel IDs | **712** |
| Backup streams | **398** |
| New Channels | **0** |
| New Queue (legacy) | **0** |
| Logo exceptions | **1** |
| EPG mapping | **81.9%** |
| EPG programme coverage | **77.9%** |
| Health failures | **168** |
| Persistent health failures | **121** |
| Audit blockers | **16** |
| Pre-publish gate | **PASS** |

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain separate user-controlled review queues.
- Dashboard and reports are generated from the current playlist.
