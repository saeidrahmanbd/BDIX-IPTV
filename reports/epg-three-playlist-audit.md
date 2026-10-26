# EPG Audit — Published Playlists

Generated: **2026-10-26T12:59:47+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1178 | 709 | 480 | 455 | 480 | 435 | 229 | OK |
| BDIX-Playlist.m3u | 139 | 131 | 76 | 71 | 76 | 70 | 55 | OK |
| International-Playlist.m3u | 2917 | 2348 | 802 | 756 | 802 | 715 | 1546 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 359 | 13 | 9 | 346 |
| Argentina | 15 | 0 | 0 | 15 |
| Aruba | 6 | 0 | 0 | 6 |
| Bangladesh | 82 | 3 | 3 | 79 |
| Brazil | 11 | 2 | 2 | 9 |
| Bulgaria | 11 | 1 | 1 | 10 |
| Canada | 26 | 20 | 20 | 6 |
| Chile | 26 | 1 | 1 | 25 |
| China | 9 | 0 | 0 | 9 |
| Colombia | 13 | 0 | 0 | 13 |
| Czech Republic | 26 | 9 | 6 | 17 |
| Documentary & Wildlife | 216 | 130 | 126 | 86 |
| Dominican Republic | 7 | 0 | 0 | 7 |
| Egypt | 5 | 2 | 2 | 3 |
| Estonia | 6 | 1 | 1 | 5 |
| France | 44 | 8 | 8 | 36 |
| Germany | 27 | 9 | 8 | 18 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 14 | 6 | 6 | 8 |
| Indian Bangla | 50 | 40 | 34 | 10 |
| Indian Entertainment | 227 | 192 | 182 | 35 |
| Indian Movies | 94 | 71 | 66 | 23 |
| Indian Music | 71 | 58 | 55 | 13 |
| International | 98 | 56 | 52 | 42 |
| Iran | 13 | 3 | 3 | 10 |
| Italy | 26 | 6 | 6 | 20 |
| Kids | 224 | 91 | 87 | 133 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 14 | 1 | 1 | 13 |
| Netherlands | 17 | 4 | 4 | 13 |
| New Backup | 15 | 12 | 12 | 3 |
| New Channels | 161 | 29 | 29 | 132 |
| Pakistani | 19 | 3 | 3 | 16 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 14 | 0 | 0 | 14 |
| Poland | 24 | 17 | 17 | 7 |
| Portugal | 6 | 0 | 0 | 6 |
| Religious | 37 | 11 | 10 | 26 |
| Romania | 38 | 10 | 9 | 28 |
| Russia | 62 | 7 | 4 | 55 |
| Saudi Arabia | 15 | 3 | 3 | 12 |
| Serbia | 5 | 1 | 1 | 4 |
| Spain | 17 | 3 | 3 | 14 |
| Sports | 257 | 104 | 99 | 153 |
| Turkey | 18 | 0 | 0 | 18 |
| Ukraine | 23 | 3 | 2 | 20 |
| United Kingdom | 11 | 1 | 1 | 10 |
| United States | 119 | 35 | 35 | 84 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 5 | 0 | 0 | 5 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **b2748fe0fdbdefef8146fa5f13df0be984517adb4b9a8d871bdff22573b2cb9f**
- BDIX-Playlist.m3u SHA-256: **2c5d5d89f98d92eb6a2f7439b3fe3edaabe13c6fb4f8c6f438f7bdc7c7dbf9d0**
- International-Playlist.m3u SHA-256: **356abeb35a533e7b6fa4b66c99a6ff781d83911e707ffd899676d3e16da33272**
