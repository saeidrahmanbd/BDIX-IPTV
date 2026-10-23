# EPG Audit — Published Playlists

Generated: **2026-10-23T08:52:50+00:00**

This report measures the two M3U files currently published at the repository root. The historic filename epg-three-playlist-audit.md is retained for link compatibility; it does not mean a third playlist file exists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1265 | 815 | 559 | 530 | 321 | 172 | 256 | OK |
| BDIX-Playlist.m3u | 139 | 131 | 76 | 74 | 76 | 30 | 55 | OK |
| International-Playlist.m3u | 1155 | 928 | 301 | 283 | 126 | 61 | 627 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 519 | 49 | 39 | 470 |
| Bangladesh | 71 | 3 | 3 | 68 |
| Documentary & Wildlife | 107 | 87 | 86 | 20 |
| Indian Bangla | 48 | 38 | 37 | 10 |
| Indian Entertainment | 166 | 146 | 138 | 20 |
| Indian Movies | 72 | 61 | 59 | 11 |
| Indian Music | 56 | 49 | 46 | 7 |
| International | 166 | 97 | 93 | 69 |
| Kids | 47 | 31 | 30 | 16 |
| New Backup | 59 | 44 | 43 | 15 |
| New Channels | 120 | 85 | 80 | 35 |
| Pakistani | 46 | 8 | 7 | 38 |
| Religious | 51 | 17 | 12 | 34 |
| Sports | 40 | 31 | 28 | 9 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **0ce6e1a9799733fae3febaa075d00c8c19a71f5ec225525a6559bbdcdc7ad3d5**
- BDIX-Playlist.m3u SHA-256: **9cc2eaa4f9209e4d1a2576f9953f47240c176f15a929c41c94b9394f62323d81**
- International-Playlist.m3u SHA-256: **dedc725ba5eccdb5619232a12750cd1b3397122ca4627d5c7a1da58c18c3537c**
