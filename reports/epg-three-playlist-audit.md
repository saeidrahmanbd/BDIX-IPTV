# EPG Audit — Published Playlists

Generated: **2026-10-27T02:48:46+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1168 | 700 | 473 | 446 | 473 | 425 | 227 | OK |
| BDIX-Playlist.m3u | 139 | 131 | 76 | 73 | 76 | 71 | 55 | OK |
| International-Playlist.m3u | 2967 | 2398 | 810 | 765 | 810 | 721 | 1588 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 359 | 13 | 10 | 346 |
| Argentina | 17 | 1 | 1 | 16 |
| Aruba | 6 | 0 | 0 | 6 |
| Bangladesh | 82 | 3 | 3 | 79 |
| Brazil | 11 | 2 | 2 | 9 |
| Bulgaria | 13 | 1 | 1 | 12 |
| Canada | 26 | 20 | 20 | 6 |
| Chile | 26 | 1 | 1 | 25 |
| China | 10 | 0 | 0 | 10 |
| Colombia | 13 | 0 | 0 | 13 |
| Czech Republic | 26 | 9 | 9 | 17 |
| Documentary & Wildlife | 216 | 130 | 125 | 86 |
| Dominican Republic | 7 | 0 | 0 | 7 |
| Egypt | 5 | 2 | 2 | 3 |
| Estonia | 6 | 1 | 1 | 5 |
| France | 44 | 8 | 8 | 36 |
| Germany | 27 | 9 | 8 | 18 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 15 | 6 | 6 | 9 |
| Indian Bangla | 50 | 40 | 36 | 10 |
| Indian Entertainment | 226 | 191 | 181 | 35 |
| Indian Movies | 93 | 70 | 64 | 23 |
| Indian Music | 72 | 59 | 54 | 13 |
| International | 98 | 56 | 51 | 42 |
| Iran | 13 | 3 | 3 | 10 |
| Italy | 26 | 6 | 6 | 20 |
| Kids | 224 | 91 | 87 | 133 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 17 | 1 | 1 | 16 |
| Netherlands | 21 | 8 | 8 | 13 |
| New Backup | 15 | 14 | 14 | 1 |
| New Channels | 165 | 29 | 28 | 136 |
| Pakistani | 21 | 3 | 3 | 18 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 14 | 0 | 0 | 14 |
| Poland | 33 | 17 | 17 | 16 |
| Portugal | 6 | 0 | 0 | 6 |
| Religious | 37 | 11 | 10 | 26 |
| Romania | 40 | 12 | 12 | 28 |
| Russia | 70 | 7 | 4 | 63 |
| Saudi Arabia | 15 | 3 | 3 | 12 |
| Serbia | 5 | 1 | 1 | 4 |
| Spain | 17 | 3 | 3 | 14 |
| Sports | 257 | 104 | 98 | 153 |
| Turkey | 18 | 0 | 0 | 18 |
| Ukraine | 24 | 3 | 3 | 21 |
| United Kingdom | 11 | 1 | 1 | 10 |
| United States | 130 | 36 | 36 | 94 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 5 | 0 | 0 | 5 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **8c318ad6772c4cf7df97c81157fdd9d8064a9aec32fb5e8414bfd9f529167568**
- BDIX-Playlist.m3u SHA-256: **2c5d5d89f98d92eb6a2f7439b3fe3edaabe13c6fb4f8c6f438f7bdc7c7dbf9d0**
- International-Playlist.m3u SHA-256: **27fa6f0fb5ff3a26df4a11f9fd6421c9629b5982d02763e455740a48b1dfd2c7**
