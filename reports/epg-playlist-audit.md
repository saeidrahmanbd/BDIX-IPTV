# EPG Audit — Published Playlists

Generated: **2026-11-28T10:57:01+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1373 | 702 | 425 | 394 | 425 | 379 | 277 | OK |
| International-Playlist.m3u | 3332 | 2064 | 768 | 651 | 755 | 682 | 1296 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 366 | 13 | 13 | 353 |
| Argentina | 11 | 0 | 0 | 11 |
| Bangladesh | 76 | 5 | 4 | 71 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 25 | 18 | 14 | 7 |
| Chile | 10 | 0 | 0 | 10 |
| China | 7 | 3 | 3 | 4 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 8 | 0 | 0 | 8 |
| Czech Republic | 23 | 17 | 16 | 6 |
| DO | 11 | 1 | 1 | 10 |
| Documentary & Wildlife | 157 | 103 | 76 | 54 |
| Estonia | 6 | 0 | 0 | 6 |
| Fashion TV | 2 | 1 | 0 | 1 |
| France | 24 | 13 | 11 | 11 |
| Germany | 70 | 18 | 12 | 52 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 43 | 33 | 30 | 10 |
| Indian Entertainment | 206 | 157 | 146 | 49 |
| Indian Movies | 84 | 63 | 61 | 21 |
| Indian Music | 71 | 59 | 56 | 12 |
| International | 174 | 51 | 42 | 123 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 20 | 10 | 10 | 10 |
| Kids | 157 | 79 | 58 | 78 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 14 | 6 | 2 | 8 |
| Netherlands | 11 | 5 | 5 | 6 |
| News | 1 | 0 | 0 | 1 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 20 | 1 | 1 | 19 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 20 | 11 | 9 | 9 |
| Religious | 36 | 7 | 7 | 29 |
| Romania | 29 | 9 | 7 | 20 |
| Russia | 50 | 7 | 6 | 43 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Spain | 14 | 4 | 3 | 10 |
| Sports | 223 | 124 | 108 | 99 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 12 | 0 | 0 | 12 |
| Ukraine | 12 | 4 | 4 | 8 |
| United Kingdom | 12 | 2 | 2 | 10 |
| United States | 132 | 51 | 47 | 81 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **1430770e8c02dd64d1d03bab2f1809e4251e771e5737759c2ec945d0525e162c**
- International-Playlist.m3u SHA-256: **248ff78f7e53dc302880e5cb413bfd2f727021f7d7d92a3f3c6f5222618bbe7b**
