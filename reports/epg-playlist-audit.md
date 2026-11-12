# EPG Audit — Published Playlists

Generated: **2026-11-12T07:12:48+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1242 | 650 | 383 | 339 | 383 | 334 | 267 | OK |
| International-Playlist.m3u | 3107 | 1697 | 584 | 512 | 576 | 509 | 1113 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 329 | 8 | 8 | 321 |
| Argentina | 13 | 1 | 0 | 12 |
| Bangladesh | 77 | 5 | 3 | 72 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 0 | 15 |
| Canada | 29 | 22 | 16 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 1 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 10 | 1 | 0 | 9 |
| Documentary & Wildlife | 52 | 40 | 26 | 12 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 13 | 25 |
| Germany | 74 | 18 | 13 | 56 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 42 | 31 | 29 | 11 |
| Indian Entertainment | 201 | 164 | 158 | 37 |
| Indian Movies | 88 | 66 | 61 | 22 |
| Indian Music | 70 | 60 | 56 | 10 |
| International | 161 | 32 | 22 | 129 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 28 | 12 | 12 | 16 |
| Kids | 33 | 19 | 17 | 14 |
| Lebanon | 5 | 1 | 0 | 4 |
| Mexico | 16 | 7 | 2 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 28 | 1 | 0 | 27 |
| Panama | 5 | 0 | 0 | 5 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 25 | 13 | 11 | 12 |
| Religious | 25 | 5 | 5 | 20 |
| Romania | 28 | 9 | 7 | 19 |
| Russia | 65 | 18 | 16 | 47 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Spain | 19 | 4 | 3 | 15 |
| Sports | 102 | 51 | 48 | 51 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 24 | 7 | 7 | 17 |
| United Kingdom | 15 | 2 | 2 | 13 |
| United States | 193 | 90 | 84 | 103 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **b4bd82f1c2158f3f4cef5a6a16f9567e9db54d682a807b9dbc4ee64ccc0d59a4**
- International-Playlist.m3u SHA-256: **9b5feeea76c79307222ed7e33cfe4de550fab4feaf35331d8e39fa4f45c4fa5e**
