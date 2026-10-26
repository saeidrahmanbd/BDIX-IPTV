# EPG Audit — Published Playlists

Generated: **2026-10-26T06:42:03+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1131 | 664 | 447 | 424 | 447 | 389 | 217 | OK |
| BDIX-Playlist.m3u | 139 | 131 | 76 | 72 | 76 | 68 | 55 | OK |
| International-Playlist.m3u | 1467 | 1373 | 330 | 306 | 330 | 282 | 1043 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 482 | 40 | 33 | 442 |
| Argentina | 13 | 0 | 0 | 13 |
| Backups | 24 | 16 | 16 | 8 |
| Bangladesh | 77 | 3 | 3 | 74 |
| Brazil | 5 | 0 | 0 | 5 |
| Canada | 2 | 2 | 2 | 0 |
| China | 10 | 0 | 0 | 10 |
| Documentary & Wildlife | 106 | 86 | 83 | 20 |
| France | 6 | 1 | 1 | 5 |
| Germany | 20 | 1 | 1 | 19 |
| Indian Bangla | 50 | 40 | 37 | 10 |
| Indian Entertainment | 224 | 179 | 166 | 45 |
| Indian Movies | 93 | 66 | 59 | 27 |
| Indian Music | 61 | 49 | 46 | 12 |
| International | 98 | 56 | 52 | 42 |
| International Movies | 165 | 14 | 14 | 151 |
| International Music | 90 | 5 | 5 | 85 |
| Kids | 51 | 33 | 32 | 18 |
| Pakistani | 41 | 6 | 6 | 35 |
| Poland | 5 | 1 | 1 | 4 |
| Religious | 32 | 10 | 9 | 22 |
| Romania | 5 | 3 | 3 | 2 |
| Russia | 10 | 0 | 0 | 10 |
| Spain | 5 | 2 | 1 | 3 |
| Sports | 38 | 29 | 27 | 9 |
| Sweden | 34 | 0 | 0 | 34 |
| United Kingdom | 13 | 4 | 4 | 9 |
| United States | 118 | 32 | 32 | 86 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **f61c38a3e13388833cf721031d0214366fb87b3a98a555d00da52100ddc58955**
- BDIX-Playlist.m3u SHA-256: **9cc2eaa4f9209e4d1a2576f9953f47240c176f15a929c41c94b9394f62323d81**
- International-Playlist.m3u SHA-256: **c816bf5276e62bc79a85429f23827cebe89bfd4f3fff34a67573ba9859f172aa**
