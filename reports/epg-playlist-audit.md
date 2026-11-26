# EPG Audit — Published Playlists

Generated: **2026-11-26T08:27:28+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1442 | 695 | 432 | 397 | 432 | 382 | 263 | OK |
| International-Playlist.m3u | 3318 | 2306 | 882 | 753 | 869 | 791 | 1424 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 366 | 13 | 13 | 353 |
| Argentina | 14 | 0 | 0 | 14 |
| Bangladesh | 82 | 5 | 4 | 77 |
| Brazil | 14 | 7 | 7 | 7 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 27 | 20 | 16 | 7 |
| Chile | 10 | 0 | 0 | 10 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 23 | 17 | 16 | 6 |
| DO | 11 | 1 | 1 | 10 |
| Documentary & Wildlife | 159 | 106 | 76 | 53 |
| Estonia | 6 | 0 | 0 | 6 |
| Fashion TV | 2 | 1 | 0 | 1 |
| France | 43 | 18 | 17 | 25 |
| Germany | 71 | 18 | 12 | 53 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 42 | 32 | 28 | 10 |
| Indian Entertainment | 197 | 164 | 154 | 33 |
| Indian Movies | 94 | 72 | 65 | 22 |
| Indian Music | 75 | 61 | 57 | 14 |
| International | 184 | 50 | 42 | 134 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 22 | 12 | 12 | 10 |
| Kids | 160 | 80 | 58 | 80 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| News | 2 | 0 | 0 | 2 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 20 | 1 | 1 | 19 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 9 | 0 | 0 | 9 |
| Poland | 24 | 11 | 9 | 13 |
| Religious | 37 | 7 | 7 | 30 |
| Romania | 30 | 9 | 7 | 21 |
| Russia | 75 | 20 | 16 | 55 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 17 | 6 | 5 | 11 |
| Sports | 225 | 126 | 111 | 99 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 28 | 8 | 8 | 20 |
| United Kingdom | 15 | 3 | 3 | 12 |
| United States | 219 | 102 | 98 | 117 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **fb2881b5951519aa648850f8de2cf82826a551cfd6bb983b4084fdb73eb639bc**
- International-Playlist.m3u SHA-256: **3615fbfe99b6cc86d5c469f9e152f1d11c60b81f76765fc7353857b2de59e155**
