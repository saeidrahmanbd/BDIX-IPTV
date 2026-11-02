# EPG Audit — Published Playlists

Generated: **2026-11-02T11:53:38+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1090 | 741 | 485 | 441 | 485 | 424 | 256 | OK |
| International-Playlist.m3u | 2767 | 2350 | 808 | 666 | 800 | 625 | 1542 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 351 | 6 | 6 | 345 |
| Argentina | 18 | 1 | 1 | 17 |
| Aruba | 6 | 0 | 0 | 6 |
| Austria | 4 | 0 | 0 | 4 |
| Bangladesh | 74 | 3 | 2 | 71 |
| Brazil | 12 | 2 | 2 | 10 |
| Bulgaria | 18 | 6 | 6 | 12 |
| Canada | 31 | 23 | 19 | 8 |
| Chile | 24 | 1 | 0 | 23 |
| China | 10 | 0 | 0 | 10 |
| Colombia | 15 | 1 | 1 | 14 |
| Costa Rica | 13 | 0 | 0 | 13 |
| Czech Republic | 26 | 9 | 3 | 17 |
| Documentary & Wildlife | 204 | 135 | 103 | 69 |
| Dominican Republic | 11 | 1 | 0 | 10 |
| Ecuador | 8 | 0 | 0 | 8 |
| Estonia | 6 | 1 | 0 | 5 |
| France | 47 | 10 | 8 | 37 |
| Germany | 30 | 10 | 4 | 20 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 18 | 8 | 6 | 10 |
| Indian Bangla | 42 | 33 | 30 | 9 |
| Indian Entertainment | 218 | 180 | 171 | 38 |
| Indian Movies | 83 | 62 | 59 | 21 |
| Indian Music | 73 | 59 | 56 | 14 |
| International | 184 | 55 | 42 | 129 |
| Iran | 17 | 3 | 2 | 14 |
| Italy | 27 | 9 | 9 | 18 |
| Kids | 209 | 91 | 73 | 118 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 15 | 3 | 2 | 12 |
| Netherlands | 21 | 9 | 9 | 12 |
| New Backup | 6 | 4 | 4 | 2 |
| New Channels | 55 | 43 | 41 | 12 |
| Pakistani | 18 | 3 | 3 | 15 |
| Panama | 6 | 0 | 0 | 6 |
| Paraguay | 10 | 0 | 0 | 10 |
| Peru | 13 | 0 | 0 | 13 |
| Poland | 33 | 18 | 14 | 15 |
| Portugal | 5 | 1 | 1 | 4 |
| Religious | 35 | 10 | 6 | 25 |
| Romania | 33 | 10 | 9 | 23 |
| Russia | 74 | 14 | 10 | 60 |
| Saudi Arabia | 10 | 0 | 0 | 10 |
| Serbia | 6 | 1 | 0 | 5 |
| Singapore | 5 | 0 | 0 | 5 |
| Spain | 16 | 3 | 1 | 13 |
| Sports | 252 | 106 | 90 | 146 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 23 | 2 | 0 | 21 |
| United Kingdom | 12 | 1 | 0 | 11 |
| United States | 150 | 41 | 30 | 109 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **0effbae25904525535b8b1cccb3c1c4a955b5785b5476d006857db7be5f26a1f**
- International-Playlist.m3u SHA-256: **cc183f0ce5b4dc843eaf2a231b62e4c11f0fd4d48341ceb89a189d2374e5c021**
