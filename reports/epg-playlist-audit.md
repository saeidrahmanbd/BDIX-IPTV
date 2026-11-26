# EPG Audit — Published Playlists

Generated: **2026-11-26T10:37:30+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1143 | 708 | 427 | 397 | 427 | 379 | 281 | OK |
| International-Playlist.m3u | 3318 | 2306 | 882 | 775 | 869 | 792 | 1424 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 366 | 13 | 13 | 353 |
| Argentina | 14 | 0 | 0 | 14 |
| Bangladesh | 79 | 5 | 4 | 74 |
| Brazil | 14 | 7 | 7 | 7 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 27 | 20 | 15 | 7 |
| Chile | 10 | 0 | 0 | 10 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 23 | 17 | 16 | 6 |
| DO | 11 | 1 | 1 | 10 |
| Documentary & Wildlife | 159 | 105 | 81 | 54 |
| Estonia | 6 | 0 | 0 | 6 |
| Fashion TV | 2 | 1 | 1 | 1 |
| France | 43 | 18 | 17 | 25 |
| Germany | 71 | 18 | 12 | 53 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 43 | 33 | 30 | 10 |
| Indian Entertainment | 215 | 163 | 154 | 52 |
| Indian Movies | 92 | 70 | 65 | 22 |
| Indian Music | 73 | 61 | 58 | 12 |
| International | 183 | 51 | 43 | 132 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 22 | 12 | 12 | 10 |
| Kids | 161 | 81 | 65 | 80 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| News | 2 | 0 | 0 | 2 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 22 | 1 | 1 | 21 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 9 | 0 | 0 | 9 |
| Poland | 24 | 11 | 10 | 13 |
| Religious | 36 | 7 | 7 | 29 |
| Romania | 30 | 9 | 7 | 21 |
| Russia | 75 | 20 | 18 | 55 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 17 | 6 | 5 | 11 |
| Sports | 227 | 124 | 113 | 103 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 28 | 8 | 8 | 20 |
| United Kingdom | 15 | 3 | 3 | 12 |
| United States | 221 | 103 | 99 | 118 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **8360de3894d65813a1852f915a24ce62d26f2b69e04af590da5ae31538270ea7**
- International-Playlist.m3u SHA-256: **3615fbfe99b6cc86d5c469f9e152f1d11c60b81f76765fc7353857b2de59e155**
