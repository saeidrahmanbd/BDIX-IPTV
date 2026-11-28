# EPG Audit — Published Playlists

Generated: **2026-11-28T18:15:37+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1373 | 780 | 453 | 422 | 453 | 404 | 327 | OK |
| International-Playlist.m3u | 3332 | 2064 | 766 | 664 | 753 | 678 | 1298 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 366 | 13 | 13 | 353 |
| Argentina | 11 | 0 | 0 | 11 |
| Bangladesh | 77 | 5 | 4 | 72 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 25 | 18 | 13 | 7 |
| Chile | 10 | 0 | 0 | 10 |
| China | 7 | 3 | 3 | 4 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 8 | 0 | 0 | 8 |
| Czech Republic | 23 | 17 | 16 | 6 |
| DO | 11 | 1 | 1 | 10 |
| Documentary & Wildlife | 157 | 103 | 79 | 54 |
| Estonia | 6 | 0 | 0 | 6 |
| Fashion TV | 2 | 1 | 0 | 1 |
| France | 24 | 13 | 11 | 11 |
| Germany | 70 | 18 | 12 | 52 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 43 | 33 | 29 | 10 |
| Indian Entertainment | 206 | 157 | 146 | 49 |
| Indian Movies | 84 | 63 | 61 | 21 |
| Indian Music | 71 | 59 | 56 | 12 |
| International | 180 | 54 | 45 | 126 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 20 | 10 | 10 | 10 |
| Kids | 157 | 79 | 64 | 78 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 14 | 6 | 2 | 8 |
| Netherlands | 11 | 5 | 5 | 6 |
| News | 1 | 0 | 0 | 1 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 22 | 1 | 1 | 21 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 20 | 11 | 10 | 9 |
| Religious | 38 | 6 | 6 | 32 |
| Romania | 28 | 8 | 7 | 20 |
| Russia | 50 | 7 | 7 | 43 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Spain | 14 | 4 | 3 | 10 |
| Sports | 264 | 133 | 121 | 131 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 12 | 0 | 0 | 12 |
| Ukraine | 12 | 4 | 4 | 8 |
| United Kingdom | 12 | 2 | 2 | 10 |
| United States | 132 | 51 | 48 | 81 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **25206445454790f8cf1e4f60acef3d030b563cba93de4c0d68c3603eee1a077c**
- International-Playlist.m3u SHA-256: **9733b1940dfab714e8f54460b870ffa7b37748ece1c9526ac8f90f9a734ca299**
