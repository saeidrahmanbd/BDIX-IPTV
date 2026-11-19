# EPG Audit — Published Playlists

Generated: **2026-11-19T11:27:25+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1333 | 694 | 431 | 398 | 431 | 388 | 263 | OK |
| International-Playlist.m3u | 3290 | 1819 | 623 | 561 | 610 | 550 | 1196 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 366 | 13 | 13 | 353 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 82 | 5 | 4 | 77 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 27 | 20 | 16 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 8 | 0 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 10 | 1 | 1 | 9 |
| Documentary & Wildlife | 58 | 44 | 35 | 14 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 44 | 19 | 18 | 25 |
| Germany | 73 | 18 | 12 | 55 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 42 | 32 | 29 | 10 |
| Indian Entertainment | 196 | 164 | 153 | 32 |
| Indian Movies | 87 | 64 | 63 | 23 |
| Indian Music | 71 | 59 | 56 | 12 |
| International | 184 | 48 | 41 | 136 |
| Iran | 9 | 1 | 0 | 8 |
| Italy | 23 | 12 | 12 | 11 |
| Kids | 44 | 24 | 22 | 20 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| News | 2 | 0 | 0 | 2 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 23 | 1 | 1 | 22 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 8 | 0 | 0 | 8 |
| Poland | 23 | 11 | 9 | 12 |
| Religious | 27 | 6 | 6 | 21 |
| Romania | 28 | 9 | 7 | 19 |
| Russia | 74 | 20 | 16 | 54 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 19 | 6 | 3 | 13 |
| Sports | 111 | 68 | 65 | 43 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 28 | 8 | 8 | 20 |
| United Kingdom | 16 | 3 | 3 | 13 |
| United States | 216 | 99 | 96 | 117 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **04218b088615b9350bffc495ff7f758deb67a7f4a7fc10cc0bbcbefcdf532cf5**
- International-Playlist.m3u SHA-256: **4c283c9a61fb02f85335597e47c961077b99dd9155594a84ef1dc2fbd453fadd**
