# EPG Audit — Published Playlists

Generated: **2026-10-26T09:09:57+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1131 | 664 | 447 | 424 | 447 | 386 | 217 | OK |
| BDIX-Playlist.m3u | 139 | 131 | 76 | 72 | 76 | 67 | 55 | OK |
| International-Playlist.m3u | 2966 | 2405 | 848 | 800 | 848 | 737 | 1557 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 359 | 13 | 9 | 346 |
| Argentina | 15 | 0 | 0 | 15 |
| Austria | 4 | 0 | 0 | 4 |
| BANGLA MUSIC | 1 | 0 | 0 | 1 |
| Backups | 55 | 27 | 26 | 28 |
| Bangladesh | 83 | 3 | 3 | 80 |
| Brazil | 11 | 2 | 2 | 9 |
| Bulgaria | 8 | 1 | 1 | 7 |
| Canada | 26 | 20 | 20 | 6 |
| Chile | 27 | 1 | 1 | 26 |
| China | 7 | 0 | 0 | 7 |
| Colombia | 15 | 0 | 0 | 15 |
| Czech Republic | 27 | 10 | 7 | 17 |
| Documentary & Wildlife | 217 | 131 | 127 | 86 |
| Egypt | 6 | 3 | 3 | 3 |
| Estonia | 6 | 1 | 1 | 5 |
| France | 45 | 8 | 8 | 37 |
| Germany | 16 | 9 | 8 | 7 |
| Greece | 10 | 2 | 2 | 8 |
| HINDI | 1 | 0 | 0 | 1 |
| Hungary | 14 | 6 | 6 | 8 |
| ISLAMIC | 1 | 0 | 0 | 1 |
| Indian Bangla | 50 | 40 | 37 | 10 |
| Indian Entertainment | 230 | 191 | 180 | 39 |
| Indian Movies | 93 | 70 | 65 | 23 |
| Indian Music | 71 | 57 | 54 | 14 |
| International | 98 | 56 | 52 | 42 |
| Iran | 12 | 3 | 3 | 9 |
| Italy | 24 | 4 | 4 | 20 |
| Kids | 226 | 93 | 88 | 133 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 14 | 1 | 1 | 13 |
| Netherlands | 14 | 4 | 4 | 10 |
| New Channels | 153 | 11 | 11 | 142 |
| Pakistani | 18 | 3 | 3 | 15 |
| Peru | 14 | 0 | 0 | 14 |
| Poland | 24 | 17 | 17 | 7 |
| Portugal | 6 | 0 | 0 | 6 |
| Religious | 36 | 11 | 10 | 25 |
| Romania | 36 | 9 | 8 | 27 |
| Russia | 60 | 7 | 4 | 53 |
| Saudi Arabia | 15 | 3 | 3 | 12 |
| Serbia | 5 | 1 | 1 | 4 |
| Spain | 17 | 3 | 3 | 14 |
| Sports | 267 | 112 | 107 | 155 |
| Turkey | 13 | 0 | 0 | 13 |
| Ukraine | 23 | 3 | 2 | 20 |
| United Kingdom | 7 | 1 | 1 | 6 |
| United States | 106 | 35 | 35 | 71 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 5 | 0 | 0 | 5 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **f61c38a3e13388833cf721031d0214366fb87b3a98a555d00da52100ddc58955**
- BDIX-Playlist.m3u SHA-256: **9cc2eaa4f9209e4d1a2576f9953f47240c176f15a929c41c94b9394f62323d81**
- International-Playlist.m3u SHA-256: **7f4f4d837228541697cf071df5eeb86f09eee09e003135c506e6b0eb75b90973**
