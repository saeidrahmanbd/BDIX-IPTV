# EPG Audit — Published Playlists

Generated: **2026-10-26T03:33:11+00:00**

This report measures the three core M3U playlists included in the automated EPG pipeline. The repository also contains BD.IN-Playlist.m3u, which is outside this report's scope. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1234 | 694 | 466 | 442 | 466 | 437 | 228 | OK |
| BDIX-Playlist.m3u | 139 | 131 | 76 | 72 | 76 | 72 | 55 | OK |
| International-Playlist.m3u | 1467 | 1373 | 329 | 305 | 329 | 300 | 1044 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 482 | 40 | 33 | 442 |
| Argentina | 13 | 0 | 0 | 13 |
| Backups | 24 | 16 | 16 | 8 |
| Bangladesh | 76 | 3 | 3 | 73 |
| Brazil | 5 | 0 | 0 | 5 |
| Canada | 2 | 2 | 2 | 0 |
| China | 10 | 0 | 0 | 10 |
| Documentary & Wildlife | 106 | 86 | 83 | 20 |
| France | 6 | 1 | 1 | 5 |
| Germany | 20 | 1 | 1 | 19 |
| Indian Bangla | 49 | 38 | 35 | 11 |
| Indian Entertainment | 208 | 163 | 150 | 45 |
| Indian Movies | 91 | 65 | 58 | 26 |
| Indian Music | 58 | 47 | 44 | 11 |
| International | 109 | 68 | 64 | 41 |
| International Movies | 165 | 13 | 13 | 152 |
| International Music | 90 | 5 | 5 | 85 |
| Kids | 52 | 34 | 33 | 18 |
| New Backup | 9 | 5 | 5 | 4 |
| New Channels | 16 | 10 | 10 | 6 |
| Pakistani | 41 | 6 | 6 | 35 |
| Poland | 5 | 1 | 1 | 4 |
| Religious | 31 | 9 | 8 | 22 |
| Romania | 5 | 3 | 3 | 2 |
| Russia | 10 | 0 | 0 | 10 |
| Spain | 5 | 2 | 1 | 3 |
| Sports | 41 | 31 | 29 | 10 |
| Sweden | 34 | 0 | 0 | 34 |
| United Kingdom | 13 | 4 | 4 | 9 |
| United States | 110 | 25 | 25 | 85 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **fdaef8ff41c34e946df4c34a7e1b999b4ebc216a613c0003f7bc2563791654bb**
- BDIX-Playlist.m3u SHA-256: **9cc2eaa4f9209e4d1a2576f9953f47240c176f15a929c41c94b9394f62323d81**
- International-Playlist.m3u SHA-256: **17446f6124c8c2e5cbbfbae4bea0306774a8772949c684c2d53292e7e367fc25**
