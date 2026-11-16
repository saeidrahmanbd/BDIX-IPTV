# EPG Audit — Published Playlists

Generated: **2026-11-16T09:54:07+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1307 | 673 | 416 | 383 | 416 | 371 | 257 | OK |
| International-Playlist.m3u | 3135 | 1764 | 612 | 548 | 600 | 541 | 1152 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 343 | 12 | 12 | 331 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 80 | 5 | 4 | 75 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 27 | 20 | 15 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 10 | 1 | 1 | 9 |
| Documentary & Wildlife | 54 | 39 | 31 | 15 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 14 | 25 |
| Germany | 72 | 18 | 11 | 54 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 41 | 33 | 29 | 8 |
| Indian Entertainment | 206 | 168 | 157 | 38 |
| Indian Movies | 88 | 66 | 65 | 22 |
| Indian Music | 68 | 59 | 56 | 9 |
| International | 178 | 44 | 37 | 134 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 27 | 12 | 12 | 15 |
| Kids | 33 | 19 | 17 | 14 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 22 | 1 | 1 | 21 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 23 | 11 | 9 | 12 |
| Religious | 26 | 5 | 5 | 21 |
| Romania | 28 | 9 | 7 | 19 |
| Russia | 73 | 20 | 16 | 53 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 20 | 5 | 3 | 15 |
| Sports | 103 | 64 | 61 | 39 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 12 | 0 | 0 | 12 |
| Ukraine | 27 | 7 | 7 | 20 |
| United Kingdom | 16 | 3 | 3 | 13 |
| United States | 207 | 99 | 95 | 108 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **9ca47f4a45ea83065516c4926ca22f771140f2d92005812e251417d5ca0843b0**
- International-Playlist.m3u SHA-256: **9599632e4e1a08863f6a6d91336ab49cb086cba1ddb79d5ee686591397a6cd3a**
