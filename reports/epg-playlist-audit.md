# EPG Audit — Published Playlists

Generated: **2026-11-17T08:07:50+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1405 | 711 | 435 | 399 | 435 | 384 | 276 | OK |
| International-Playlist.m3u | 3138 | 1732 | 618 | 554 | 607 | 542 | 1114 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 300 | 11 | 11 | 289 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 88 | 5 | 4 | 83 |
| Brazil | 12 | 7 | 7 | 5 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 27 | 20 | 15 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 8 | 0 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 10 | 1 | 1 | 9 |
| Documentary & Wildlife | 59 | 44 | 35 | 15 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 41 | 16 | 15 | 25 |
| Germany | 74 | 18 | 12 | 56 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 41 | 32 | 28 | 9 |
| Indian Entertainment | 204 | 166 | 155 | 38 |
| Indian Movies | 88 | 67 | 63 | 21 |
| Indian Music | 67 | 58 | 54 | 9 |
| International | 185 | 49 | 42 | 136 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 26 | 12 | 12 | 14 |
| Kids | 40 | 24 | 22 | 16 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 24 | 1 | 1 | 23 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 6 | 0 | 0 | 6 |
| Poland | 23 | 11 | 10 | 12 |
| Religious | 25 | 5 | 5 | 20 |
| Romania | 28 | 9 | 7 | 19 |
| Russia | 73 | 20 | 18 | 53 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 23 | 7 | 5 | 16 |
| Sports | 114 | 70 | 68 | 44 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 13 | 0 | 0 | 13 |
| Ukraine | 27 | 7 | 6 | 20 |
| United Kingdom | 16 | 3 | 3 | 13 |
| United States | 206 | 98 | 94 | 108 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **24f3fdfaa0d8f3c191c12b8824130d2b5f6bdde45f9cd0c4b3118a93265fb384**
- International-Playlist.m3u SHA-256: **f4b5bb596ec1d62617daa3ea05290116bdc297fbbb7c58b23ba171de3296ae8f**
