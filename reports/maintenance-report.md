# IPTV Maintenance Report

_Corrected: **2026-10-10 — stream count checked against live IPTV-Playlist.m3u**_

| Item | Result |
|---|---:|
| Current playlist streams | **1061** |
| Current channel IDs | **Not refreshed in this correction** |
| Backup streams | **Not refreshed in this correction** |
| New Channels | **Not refreshed in this correction** |
| New Queue (legacy) | **Not refreshed in this correction** |
| Logo exceptions | **0** |
| EPG mapping | **Not refreshed in this correction** |
| EPG programme coverage | **Not refreshed in this correction** |
| Health failures | **Not refreshed in this correction** |
| Persistent health failures | **Not refreshed in this correction** |
| Audit blockers | **Not refreshed in this correction** |
| Pre-publish gate | **Not rerun in this correction** |

## Data freshness note
- The stream total was verified directly against the live playlist (1,061 entries).
- Other operational metrics are marked unrefreshed rather than presented as current. Run the IPTV Playlist Update workflow to regenerate the complete report set.

## Protection
- Duplicate stream URLs are blocking.
- Primary streams are protected from silent removal.
- Backup streams are never deleted because of health failures.
- New Channels and New Backup remain separate user-controlled review queues.
- Dashboard and reports are generated from the current playlist.
