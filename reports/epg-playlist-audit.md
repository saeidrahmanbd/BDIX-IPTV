# EPG Audit — Published Playlists

Generated: **2026-11-10T01:43:36+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1068 | 599 | 364 | 323 | 364 | 309 | 235 | OK |
| International-Playlist.m3u | 3054 | 1700 | 581 | 536 | 570 | 498 | 1119 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 352 | 11 | 11 | 341 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 64 | 4 | 2 | 60 |
| Brazil | 9 | 3 | 3 | 6 |
| Bulgaria | 21 | 6 | 5 | 15 |
| Canada | 30 | 23 | 17 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 1 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 17 | 5 |
| DO | 10 | 1 | 0 | 9 |
| Documentary & Wildlife | 55 | 43 | 31 | 12 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 14 | 25 |
| Germany | 73 | 18 | 17 | 55 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 7 | 8 |
| Indian Bangla | 39 | 28 | 26 | 11 |
| Indian Entertainment | 197 | 161 | 154 | 36 |
| Indian Movies | 83 | 62 | 55 | 21 |
| Indian Music | 66 | 57 | 54 | 9 |
| International | 174 | 34 | 26 | 140 |
| Iran | 11 | 1 | 0 | 10 |
| Italy | 27 | 11 | 11 | 16 |
| Kids | 38 | 20 | 18 | 18 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 16 | 7 | 6 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 20 | 1 | 1 | 19 |
| Panama | 5 | 0 | 0 | 5 |
| Peru | 8 | 0 | 0 | 8 |
| Poland | 25 | 13 | 12 | 12 |
| Religious | 26 | 5 | 5 | 21 |
| Romania | 28 | 9 | 9 | 19 |
| Russia | 56 | 15 | 15 | 41 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 1 | 4 |
| Spain | 22 | 4 | 4 | 18 |
| Sports | 48 | 27 | 25 | 21 |
| Sweden | 43 | 12 | 12 | 31 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 20 | 6 | 6 | 14 |
| United Kingdom | 17 | 4 | 3 | 13 |
| United States | 188 | 92 | 91 | 96 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **1cdf6fb9b301583e715aaa78826992aa3bb5ef9ef2de94b2d35437d2bfcc3676**
- International-Playlist.m3u SHA-256: **55590260231b80063a9d2c1e065a8f89ae36dccd133fc2229846dfd3c32e16f6**
