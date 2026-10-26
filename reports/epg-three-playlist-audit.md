# EPG Audit — Published Playlists

Generated: **2026-10-26T11:05:15+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1154 | 686 | 459 | 433 | 459 | 412 | 227 | OK |
| BDIX-Playlist.m3u | 139 | 131 | 76 | 71 | 76 | 70 | 55 | OK |
| International-Playlist.m3u | 2907 | 2342 | 817 | 769 | 817 | 727 | 1525 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 359 | 13 | 9 | 346 |
| Argentina | 15 | 0 | 0 | 15 |
| Aruba | 6 | 0 | 0 | 6 |
| Austria | 4 | 0 | 0 | 4 |
| Bangladesh | 82 | 3 | 3 | 79 |
| Brazil | 14 | 2 | 2 | 12 |
| Bulgaria | 9 | 1 | 1 | 8 |
| Canada | 27 | 20 | 20 | 7 |
| Chile | 27 | 1 | 1 | 26 |
| China | 9 | 0 | 0 | 9 |
| Colombia | 16 | 0 | 0 | 16 |
| Czech Republic | 27 | 10 | 7 | 17 |
| Documentary & Wildlife | 216 | 130 | 126 | 86 |
| Dominican Republic | 7 | 0 | 0 | 7 |
| Egypt | 6 | 3 | 3 | 3 |
| Estonia | 6 | 1 | 1 | 5 |
| France | 46 | 8 | 8 | 38 |
| Germany | 16 | 9 | 8 | 7 |
| Greece | 10 | 2 | 2 | 8 |
| Hungary | 14 | 6 | 6 | 8 |
| Indian Bangla | 50 | 40 | 34 | 10 |
| Indian Entertainment | 227 | 190 | 179 | 37 |
| Indian Movies | 94 | 71 | 66 | 23 |
| Indian Music | 71 | 57 | 54 | 14 |
| International | 98 | 56 | 52 | 42 |
| Iran | 15 | 4 | 4 | 11 |
| Italy | 24 | 4 | 4 | 20 |
| Kids | 226 | 93 | 89 | 133 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 15 | 1 | 1 | 14 |
| Netherlands | 14 | 4 | 4 | 10 |
| New Backup | 8 | 5 | 5 | 3 |
| New Channels | 123 | 16 | 16 | 107 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 19 | 3 | 3 | 16 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 14 | 0 | 0 | 14 |
| Poland | 24 | 17 | 17 | 7 |
| Portugal | 6 | 0 | 0 | 6 |
| Religious | 37 | 11 | 10 | 26 |
| Romania | 37 | 9 | 8 | 28 |
| Russia | 60 | 7 | 4 | 53 |
| Saudi Arabia | 15 | 3 | 3 | 12 |
| Serbia | 5 | 1 | 1 | 4 |
| Spain | 18 | 3 | 3 | 15 |
| Sports | 267 | 112 | 107 | 155 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 24 | 3 | 2 | 21 |
| United Kingdom | 8 | 1 | 1 | 7 |
| United States | 106 | 35 | 35 | 71 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 5 | 0 | 0 | 5 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **9e51d792eecc6487488c43225623eacfa0d69b2710bd021063f29ddaa3ce573d**
- BDIX-Playlist.m3u SHA-256: **9cc2eaa4f9209e4d1a2576f9953f47240c176f15a929c41c94b9394f62323d81**
- International-Playlist.m3u SHA-256: **4cc466ddf574c583a96113075f09ddd6d1dafa5d17da26bcd619c9624e239d7c**
