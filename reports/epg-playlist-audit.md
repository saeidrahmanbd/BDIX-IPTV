# EPG Audit — Published Playlists

Generated: **2026-11-08T02:50:41+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1004 | 674 | 428 | 392 | 428 | 380 | 246 | OK |
| International-Playlist.m3u | 3030 | 2211 | 937 | 883 | 926 | 829 | 1274 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 351 | 11 | 11 | 340 |
| Argentina | 14 | 1 | 1 | 13 |
| Aruba | 1 | 0 | 0 | 1 |
| Austria | 2 | 0 | 0 | 2 |
| Bangladesh | 77 | 5 | 3 | 72 |
| Brazil | 10 | 3 | 3 | 7 |
| Bulgaria | 20 | 6 | 5 | 14 |
| Canada | 31 | 25 | 25 | 6 |
| Chile | 12 | 1 | 1 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 11 | 1 | 0 | 10 |
| Costa Rica | 11 | 0 | 0 | 11 |
| Czech Republic | 24 | 17 | 17 | 7 |
| Documentary & Wildlife | 196 | 145 | 136 | 51 |
| Dominican Republic | 11 | 1 | 0 | 10 |
| Ecuador | 3 | 0 | 0 | 3 |
| Estonia | 6 | 1 | 1 | 5 |
| France | 43 | 16 | 15 | 27 |
| Germany | 39 | 29 | 29 | 10 |
| Greece | 7 | 2 | 2 | 5 |
| Hungary | 17 | 8 | 8 | 9 |
| Indian Bangla | 42 | 34 | 31 | 8 |
| Indian Entertainment | 215 | 178 | 169 | 37 |
| Indian Movies | 84 | 62 | 54 | 22 |
| Indian Music | 69 | 57 | 54 | 12 |
| International | 183 | 60 | 52 | 123 |
| Iran | 16 | 3 | 3 | 13 |
| Italy | 24 | 11 | 11 | 13 |
| Kids | 196 | 103 | 97 | 93 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 15 | 6 | 5 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| Pakistani | 16 | 2 | 2 | 14 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 4 | 0 | 0 | 4 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 28 | 18 | 18 | 10 |
| Portugal | 3 | 1 | 1 | 2 |
| Religious | 35 | 10 | 9 | 25 |
| Romania | 28 | 9 | 9 | 19 |
| Russia | 62 | 21 | 19 | 41 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Serbia | 2 | 1 | 1 | 1 |
| Singapore | 6 | 1 | 1 | 5 |
| Spain | 16 | 4 | 4 | 12 |
| Sports | 244 | 117 | 112 | 127 |
| Sweden | 12 | 6 | 6 | 6 |
| Turkey | 12 | 0 | 0 | 12 |
| Ukraine | 19 | 6 | 6 | 13 |
| United Kingdom | 12 | 3 | 3 | 9 |
| United States | 169 | 85 | 84 | 84 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **6da7347dcf4d355f3469116aea87f011f70e2699cfc38f2c08ff136138f1680e**
- International-Playlist.m3u SHA-256: **7cc909e5c9d9086ae1f28f720653c7bdd68a1bb1b5e64a61e3280074253069a5**
