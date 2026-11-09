# EPG Audit — Published Playlists

Generated: **2026-11-09T06:57:42+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 996 | 580 | 356 | 317 | 367 | 268 | 224 | OK |
| International-Playlist.m3u | 3017 | 1523 | 515 | 476 | 552 | 439 | 1008 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 351 | 11 | 11 | 340 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 70 | 4 | 2 | 66 |
| Brazil | 9 | 3 | 3 | 6 |
| Bulgaria | 19 | 6 | 6 | 13 |
| Canada | 30 | 23 | 17 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 1 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 17 | 5 |
| DO | 10 | 1 | 0 | 9 |
| Documentary & Wildlife | 58 | 46 | 34 | 12 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 14 | 25 |
| Germany | 39 | 13 | 13 | 26 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 7 | 8 |
| Indian Bangla | 41 | 30 | 28 | 11 |
| Indian Entertainment | 173 | 146 | 141 | 27 |
| Indian Movies | 76 | 55 | 50 | 21 |
| Indian Music | 68 | 56 | 53 | 12 |
| International | 156 | 32 | 24 | 124 |
| Iran | 11 | 1 | 0 | 10 |
| Italy | 24 | 11 | 11 | 13 |
| Kids | 37 | 23 | 20 | 14 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 15 | 6 | 5 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 17 | 1 | 1 | 16 |
| Panama | 5 | 0 | 0 | 5 |
| Peru | 8 | 0 | 0 | 8 |
| Poland | 25 | 13 | 12 | 12 |
| Religious | 24 | 4 | 4 | 20 |
| Romania | 28 | 9 | 9 | 19 |
| Russia | 53 | 15 | 15 | 38 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 1 | 4 |
| Spain | 18 | 4 | 4 | 14 |
| Sports | 48 | 27 | 24 | 21 |
| Sweden | 12 | 2 | 2 | 10 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 20 | 6 | 5 | 14 |
| United Kingdom | 14 | 3 | 2 | 11 |
| United States | 147 | 69 | 68 | 78 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **a905c8a79fc9167d61323692f4a7b8df541e7e086f76552bc5632544ac4f00d7**
- International-Playlist.m3u SHA-256: **7b5b134e3388d23a567590234d6be11b4ef78731aae7228a473c7a3ace143c3e**
