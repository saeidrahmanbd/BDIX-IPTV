# EPG Audit — Published Playlists

Generated: **2026-11-07T09:30:51+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1005 | 674 | 428 | 397 | 428 | 384 | 246 | OK |
| International-Playlist.m3u | 3098 | 2281 | 940 | 896 | 929 | 842 | 1341 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 351 | 11 | 11 | 340 |
| Argentina | 17 | 1 | 1 | 16 |
| Aruba | 6 | 0 | 0 | 6 |
| Austria | 3 | 0 | 0 | 3 |
| Bangladesh | 78 | 5 | 3 | 73 |
| Brazil | 11 | 3 | 3 | 8 |
| Bulgaria | 20 | 6 | 6 | 14 |
| Canada | 33 | 25 | 25 | 8 |
| Chile | 23 | 1 | 1 | 22 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 14 | 1 | 0 | 13 |
| Costa Rica | 12 | 0 | 0 | 12 |
| Czech Republic | 24 | 17 | 17 | 7 |
| Documentary & Wildlife | 196 | 145 | 137 | 51 |
| Dominican Republic | 11 | 1 | 0 | 10 |
| Ecuador | 7 | 0 | 0 | 7 |
| Estonia | 6 | 1 | 1 | 5 |
| France | 43 | 16 | 15 | 27 |
| Germany | 39 | 29 | 29 | 10 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 17 | 8 | 8 | 9 |
| Indian Bangla | 42 | 34 | 31 | 8 |
| Indian Entertainment | 216 | 179 | 171 | 37 |
| Indian Movies | 84 | 62 | 58 | 22 |
| Indian Music | 71 | 59 | 56 | 12 |
| International | 183 | 60 | 55 | 123 |
| Iran | 16 | 3 | 3 | 13 |
| Italy | 30 | 12 | 12 | 18 |
| Kids | 196 | 103 | 98 | 93 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 15 | 6 | 5 | 9 |
| Netherlands | 18 | 9 | 9 | 9 |
| Pakistani | 16 | 2 | 2 | 14 |
| Panama | 6 | 0 | 0 | 6 |
| Paraguay | 9 | 0 | 0 | 9 |
| Peru | 12 | 0 | 0 | 12 |
| Poland | 29 | 18 | 18 | 11 |
| Portugal | 4 | 1 | 1 | 3 |
| Religious | 35 | 10 | 9 | 25 |
| Romania | 31 | 9 | 9 | 22 |
| Russia | 63 | 21 | 18 | 42 |
| Saudi Arabia | 10 | 0 | 0 | 10 |
| Serbia | 6 | 1 | 1 | 5 |
| Singapore | 6 | 1 | 1 | 5 |
| Spain | 16 | 4 | 4 | 12 |
| Sports | 244 | 117 | 114 | 127 |
| Sweden | 12 | 6 | 6 | 6 |
| Turkey | 12 | 0 | 0 | 12 |
| Ukraine | 20 | 6 | 6 | 14 |
| United Kingdom | 12 | 3 | 3 | 9 |
| United States | 171 | 85 | 84 | 86 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **84c02ef014377e5b6ba95a227f9783389650950895cfd82aece9c12b369a6a98**
- International-Playlist.m3u SHA-256: **c9542371251dc1172e23e2ae39d8c42e29a2df18a0ef4391efc4fdefcb49fff1**
