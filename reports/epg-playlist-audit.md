# EPG Audit — Published Playlists

Generated: **2026-11-05T08:30:54+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1113 | 683 | 446 | 405 | 446 | 390 | 237 | OK |
| International-Playlist.m3u | 2960 | 2489 | 866 | 795 | 855 | 746 | 1623 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 351 | 11 | 11 | 340 |
| Argentina | 18 | 1 | 1 | 17 |
| Aruba | 6 | 0 | 0 | 6 |
| Austria | 4 | 0 | 0 | 4 |
| Bangladesh | 78 | 5 | 1 | 73 |
| Brazil | 12 | 2 | 2 | 10 |
| Bulgaria | 20 | 6 | 6 | 14 |
| Canada | 31 | 23 | 21 | 8 |
| Chile | 24 | 1 | 1 | 23 |
| China | 13 | 3 | 3 | 10 |
| Colombia | 15 | 1 | 0 | 14 |
| Costa Rica | 13 | 0 | 0 | 13 |
| Czech Republic | 26 | 10 | 10 | 16 |
| Documentary & Wildlife | 206 | 138 | 126 | 68 |
| Dominican Republic | 11 | 1 | 0 | 10 |
| Ecuador | 8 | 0 | 0 | 8 |
| Estonia | 6 | 1 | 1 | 5 |
| France | 48 | 11 | 10 | 37 |
| Germany | 38 | 10 | 10 | 28 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 18 | 8 | 8 | 10 |
| Indian Bangla | 42 | 34 | 31 | 8 |
| Indian Entertainment | 221 | 183 | 169 | 38 |
| Indian Movies | 86 | 63 | 56 | 23 |
| Indian Music | 75 | 60 | 56 | 15 |
| International | 191 | 60 | 52 | 131 |
| Iran | 18 | 3 | 3 | 15 |
| Italy | 27 | 9 | 7 | 18 |
| Kids | 209 | 94 | 86 | 115 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 17 | 5 | 4 | 12 |
| Netherlands | 21 | 9 | 9 | 12 |
| New Channels | 53 | 18 | 17 | 35 |
| Pakistani | 18 | 3 | 3 | 15 |
| Panama | 6 | 0 | 0 | 6 |
| Paraguay | 10 | 0 | 0 | 10 |
| Peru | 13 | 0 | 0 | 13 |
| Poland | 33 | 18 | 18 | 15 |
| Portugal | 5 | 1 | 1 | 4 |
| Religious | 34 | 10 | 9 | 24 |
| Romania | 33 | 10 | 10 | 23 |
| Russia | 84 | 15 | 11 | 69 |
| Saudi Arabia | 10 | 0 | 0 | 10 |
| Serbia | 6 | 1 | 1 | 5 |
| Singapore | 6 | 1 | 1 | 5 |
| Spain | 16 | 3 | 3 | 13 |
| Sports | 252 | 108 | 101 | 144 |
| Sweden | 12 | 0 | 0 | 12 |
| Turkey | 15 | 0 | 0 | 15 |
| Ukraine | 24 | 2 | 2 | 22 |
| United Kingdom | 13 | 2 | 2 | 11 |
| United States | 174 | 48 | 47 | 126 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **f5795953ab6e9474334bc1dc17149eaf70528a4602c0084f59ecbe44665f78ef**
- International-Playlist.m3u SHA-256: **4dab9731e1d877638d80c2962bb27b60f6ff064891788102a33d8a06f31f26d3**
