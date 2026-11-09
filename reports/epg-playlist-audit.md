# EPG Audit — Published Playlists

Generated: **2026-11-09T03:42:12+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 998 | 596 | 366 | 327 | 378 | 278 | 230 | OK |
| International-Playlist.m3u | 2983 | 1190 | 508 | 470 | 556 | 444 | 682 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 72 | 4 | 2 | 68 |
| Brazil | 10 | 4 | 4 | 6 |
| Bulgaria | 19 | 6 | 6 | 13 |
| Canada | 30 | 23 | 17 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 1 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 23 | 18 | 18 | 5 |
| DO | 10 | 1 | 0 | 9 |
| Documentary & Wildlife | 60 | 46 | 34 | 14 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 14 | 25 |
| Germany | 39 | 13 | 13 | 26 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 7 | 8 |
| Indian Bangla | 42 | 31 | 29 | 11 |
| Indian Entertainment | 174 | 147 | 142 | 27 |
| Indian Movies | 81 | 60 | 55 | 21 |
| Indian Music | 68 | 57 | 54 | 11 |
| International | 157 | 32 | 24 | 125 |
| Iran | 11 | 1 | 0 | 10 |
| Italy | 24 | 11 | 11 | 13 |
| Kids | 44 | 26 | 23 | 18 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 15 | 6 | 5 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 18 | 1 | 1 | 17 |
| Panama | 5 | 0 | 0 | 5 |
| Peru | 8 | 0 | 0 | 8 |
| Poland | 25 | 13 | 12 | 12 |
| Religious | 25 | 4 | 4 | 21 |
| Romania | 29 | 9 | 9 | 20 |
| Russia | 53 | 15 | 15 | 38 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 1 | 4 |
| Spain | 18 | 4 | 4 | 14 |
| Sports | 60 | 29 | 26 | 31 |
| Sweden | 12 | 2 | 2 | 10 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 20 | 6 | 6 | 14 |
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

- IPTV-Playlist.m3u SHA-256: **8675200ab8b37acc114ba0d5fc456d80611f2715c3226f08837681133391c6b5**
- International-Playlist.m3u SHA-256: **e82b876b16ceeb0ef3eaaf434c50d2d793b985a7e5fe1205230f2c14c620d6ff**
