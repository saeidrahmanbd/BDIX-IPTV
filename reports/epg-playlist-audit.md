# EPG Audit — Published Playlists

Generated: **2026-11-26T02:01:12+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1371 | 695 | 432 | 370 | 432 | 357 | 263 | OK |
| International-Playlist.m3u | 3322 | 2301 | 880 | 740 | 867 | 760 | 1421 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 366 | 13 | 13 | 353 |
| Argentina | 14 | 0 | 0 | 14 |
| Bangladesh | 82 | 5 | 4 | 77 |
| Brazil | 14 | 7 | 7 | 7 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 27 | 20 | 15 | 7 |
| Chile | 10 | 0 | 0 | 10 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 23 | 17 | 16 | 6 |
| DO | 11 | 1 | 1 | 10 |
| Documentary & Wildlife | 159 | 106 | 81 | 53 |
| Estonia | 6 | 0 | 0 | 6 |
| Fashion TV | 1 | 1 | 1 | 0 |
| France | 43 | 18 | 17 | 25 |
| Germany | 71 | 18 | 12 | 53 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 42 | 32 | 24 | 10 |
| Indian Entertainment | 197 | 164 | 140 | 33 |
| Indian Movies | 94 | 72 | 61 | 22 |
| Indian Music | 74 | 60 | 50 | 14 |
| International | 183 | 50 | 42 | 133 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 22 | 12 | 12 | 10 |
| Kids | 160 | 80 | 61 | 80 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| News | 2 | 0 | 0 | 2 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 20 | 1 | 1 | 19 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 9 | 0 | 0 | 9 |
| Poland | 24 | 11 | 10 | 13 |
| Religious | 37 | 7 | 6 | 30 |
| Romania | 30 | 9 | 7 | 21 |
| Russia | 75 | 20 | 18 | 55 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 17 | 6 | 5 | 11 |
| Sports | 225 | 126 | 114 | 99 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 28 | 8 | 7 | 20 |
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

- IPTV-Playlist.m3u SHA-256: **8167fe97fbf5e046ec9f27fdb6a89679c51ec7abda12ff14819dab25c02bb081**
- International-Playlist.m3u SHA-256: **aca22e32fbe473ee8505b996463c19709bc709420f345a316c8d9e7bcd3d4c08**
