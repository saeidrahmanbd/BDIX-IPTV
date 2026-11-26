# EPG Audit — Published Playlists

Generated: **2026-11-26T14:36:27+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1143 | 708 | 428 | 398 | 428 | 381 | 280 | OK |
| International-Playlist.m3u | 3318 | 2306 | 881 | 775 | 868 | 792 | 1425 | OK |

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
| Indian Entertainment | 213 | 161 | 152 | 52 |
| Indian Movies | 92 | 70 | 66 | 22 |
| Indian Music | 73 | 61 | 58 | 12 |
| International | 184 | 52 | 43 | 132 |
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

- IPTV-Playlist.m3u SHA-256: **00129460214a9ee239552d01b1bc22ffd907140b7e55a60236d9cf77d46ba935**
- International-Playlist.m3u SHA-256: **0f07449134d36264a75c856d7f9a04c968349687a62008481b0e025e80290d70**
