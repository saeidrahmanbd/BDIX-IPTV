# EPG Audit — Published Playlists

Generated: **2026-11-27T08:40:23+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1196 | 708 | 428 | 397 | 428 | 380 | 280 | OK |
| International-Playlist.m3u | 3343 | 2092 | 777 | 670 | 764 | 689 | 1315 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 366 | 13 | 13 | 353 |
| Argentina | 11 | 0 | 0 | 11 |
| Bangladesh | 78 | 5 | 4 | 73 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 26 | 19 | 14 | 7 |
| Chile | 10 | 0 | 0 | 10 |
| China | 7 | 3 | 3 | 4 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 23 | 17 | 16 | 6 |
| DO | 11 | 1 | 1 | 10 |
| Documentary & Wildlife | 159 | 105 | 78 | 54 |
| Estonia | 6 | 0 | 0 | 6 |
| Fashion TV | 2 | 1 | 0 | 1 |
| France | 24 | 13 | 11 | 11 |
| Germany | 70 | 18 | 12 | 52 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 43 | 33 | 30 | 10 |
| Indian Entertainment | 209 | 158 | 147 | 51 |
| Indian Movies | 84 | 63 | 60 | 21 |
| Indian Music | 72 | 60 | 57 | 12 |
| International | 178 | 51 | 42 | 127 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 20 | 10 | 10 | 10 |
| Kids | 159 | 80 | 64 | 79 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 15 | 6 | 2 | 9 |
| Netherlands | 11 | 5 | 5 | 6 |
| News | 1 | 0 | 0 | 1 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 20 | 1 | 1 | 19 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 8 | 0 | 0 | 8 |
| Poland | 20 | 11 | 10 | 9 |
| Religious | 36 | 7 | 7 | 29 |
| Romania | 29 | 9 | 7 | 20 |
| Russia | 57 | 8 | 8 | 49 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Spain | 14 | 4 | 3 | 10 |
| Sports | 227 | 127 | 115 | 100 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 13 | 0 | 0 | 13 |
| Ukraine | 12 | 4 | 4 | 8 |
| United Kingdom | 12 | 2 | 2 | 10 |
| United States | 134 | 53 | 50 | 81 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **5b13ee8b1e9ac748bcf7e274638d42ee60f078298acbc6b550712521b064b71d**
- International-Playlist.m3u SHA-256: **ac590fd34726acfe479ba48aca0ea1d4da3ca5262f97fc21a0963c54d27d8fd6**
