# EPG Audit — Published Playlists

Generated: **2026-11-08T16:55:30+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 999 | 597 | 366 | 328 | 378 | 305 | 231 | OK |
| International-Playlist.m3u | 3030 | 2197 | 853 | 778 | 908 | 766 | 1344 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 351 | 11 | 11 | 340 |
| Argentina | 12 | 1 | 0 | 11 |
| Aruba | 1 | 0 | 0 | 1 |
| Austria | 2 | 0 | 0 | 2 |
| Bangladesh | 70 | 5 | 3 | 65 |
| Brazil | 9 | 2 | 2 | 7 |
| Bulgaria | 20 | 6 | 6 | 14 |
| Canada | 31 | 24 | 17 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 12 | 1 | 0 | 11 |
| Costa Rica | 12 | 0 | 0 | 12 |
| Czech Republic | 24 | 17 | 17 | 7 |
| Documentary & Wildlife | 195 | 139 | 117 | 56 |
| Dominican Republic | 11 | 1 | 0 | 10 |
| Ecuador | 4 | 0 | 0 | 4 |
| Estonia | 6 | 0 | 0 | 6 |
| Fashion TV | 1 | 1 | 0 | 0 |
| France | 44 | 17 | 16 | 27 |
| Germany | 39 | 12 | 12 | 27 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 17 | 7 | 7 | 10 |
| Indian Bangla | 44 | 33 | 30 | 11 |
| Indian Entertainment | 209 | 173 | 164 | 36 |
| Indian Movies | 84 | 62 | 59 | 22 |
| Indian Music | 69 | 56 | 53 | 13 |
| International | 146 | 31 | 23 | 115 |
| Iran | 16 | 1 | 0 | 15 |
| Italy | 24 | 11 | 11 | 13 |
| Kids | 198 | 98 | 91 | 100 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 15 | 6 | 5 | 9 |
| Netherlands | 16 | 9 | 6 | 7 |
| Pakistani | 18 | 1 | 1 | 17 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 4 | 0 | 0 | 4 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 29 | 14 | 13 | 15 |
| Portugal | 3 | 1 | 1 | 2 |
| Religious | 35 | 7 | 7 | 28 |
| Romania | 28 | 9 | 9 | 19 |
| Russia | 56 | 15 | 15 | 41 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Serbia | 2 | 0 | 0 | 2 |
| Singapore | 6 | 1 | 1 | 5 |
| Spain | 17 | 4 | 4 | 13 |
| Sports | 239 | 111 | 103 | 128 |
| Sweden | 12 | 2 | 2 | 10 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 19 | 4 | 4 | 15 |
| United Kingdom | 13 | 3 | 2 | 10 |
| United States | 169 | 71 | 70 | 98 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **dee4c0905162325bb433379bae254831ad1834640807c7670b213f343caec9f3**
- International-Playlist.m3u SHA-256: **be459b74430ed16017a820fe84a7d7fee7d861c0724f5a3698fd5397008da43f**
