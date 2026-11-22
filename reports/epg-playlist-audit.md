# EPG Audit — Published Playlists

Generated: **2026-11-22T02:30:13+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1389 | 694 | 431 | 393 | 431 | 377 | 263 | OK |
| International-Playlist.m3u | 3304 | 1815 | 622 | 560 | 609 | 542 | 1193 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 366 | 13 | 13 | 353 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 82 | 5 | 3 | 77 |
| Brazil | 14 | 7 | 7 | 7 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 27 | 20 | 15 | 7 |
| Chile | 10 | 0 | 0 | 10 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 11 | 1 | 1 | 10 |
| Documentary & Wildlife | 58 | 44 | 35 | 14 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 44 | 19 | 18 | 25 |
| Germany | 72 | 18 | 12 | 54 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 14 | 6 | 5 | 8 |
| Indian Bangla | 42 | 32 | 29 | 10 |
| Indian Entertainment | 195 | 163 | 152 | 32 |
| Indian Movies | 89 | 67 | 60 | 22 |
| Indian Music | 71 | 59 | 55 | 12 |
| International | 182 | 49 | 41 | 133 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 23 | 12 | 12 | 11 |
| Kids | 44 | 24 | 22 | 20 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| News | 2 | 0 | 0 | 2 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 22 | 1 | 1 | 21 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 9 | 0 | 0 | 9 |
| Poland | 23 | 11 | 10 | 12 |
| Religious | 27 | 6 | 6 | 21 |
| Romania | 30 | 9 | 7 | 21 |
| Russia | 75 | 20 | 18 | 55 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 18 | 6 | 5 | 12 |
| Sports | 111 | 68 | 68 | 43 |
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

- IPTV-Playlist.m3u SHA-256: **0e135710f0964eb757aa03c22ce16c8b1d48cad03639d48f28903aadee255a73**
- International-Playlist.m3u SHA-256: **c5dab98657a86fd204721157eb66952ef1e8bda7f06c338d2f3ec73737802c71**
