# EPG Audit — Published Playlists

Generated: **2026-11-09T00:38:59+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 998 | 596 | 366 | 327 | 378 | 278 | 230 | OK |
| International-Playlist.m3u | 3071 | 1209 | 516 | 477 | 564 | 459 | 693 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Argentina | 12 | 1 | 0 | 11 |
| Bangladesh | 71 | 5 | 2 | 66 |
| Brazil | 10 | 3 | 3 | 7 |
| Bulgaria | 19 | 6 | 6 | 13 |
| Canada | 30 | 23 | 17 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 10 | 1 | 0 | 9 |
| Costa Rica | 11 | 0 | 0 | 11 |
| Czech Republic | 24 | 18 | 18 | 6 |
| DO | 11 | 1 | 0 | 10 |
| Documentary & Wildlife | 58 | 46 | 34 | 12 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 41 | 16 | 15 | 25 |
| Germany | 39 | 13 | 13 | 26 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 7 | 8 |
| Indian Bangla | 42 | 31 | 29 | 11 |
| Indian Entertainment | 174 | 147 | 142 | 27 |
| Indian Movies | 82 | 60 | 54 | 22 |
| Indian Music | 69 | 57 | 54 | 12 |
| International | 162 | 32 | 24 | 130 |
| Iran | 12 | 1 | 0 | 11 |
| Italy | 24 | 11 | 11 | 13 |
| Kids | 41 | 25 | 22 | 16 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 15 | 6 | 5 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 18 | 1 | 1 | 17 |
| Panama | 5 | 0 | 0 | 5 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 26 | 13 | 12 | 13 |
| Religious | 24 | 4 | 4 | 20 |
| Romania | 28 | 9 | 9 | 19 |
| Russia | 54 | 15 | 15 | 39 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 1 | 4 |
| Spain | 18 | 4 | 4 | 14 |
| Sports | 52 | 28 | 26 | 24 |
| Sweden | 12 | 2 | 2 | 10 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 19 | 4 | 4 | 15 |
| United Kingdom | 14 | 3 | 2 | 11 |
| United States | 159 | 71 | 70 | 88 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **a02d892fda4e692ec37814a8206c4ff6c6ab200d77b7592a17da1d7c01fd070b**
- International-Playlist.m3u SHA-256: **78f1aa33f238b6584576ea03b006d78132bd54bbafb7f665f62da461309aa5e0**
