# EPG Audit — Published Playlists

Generated: **2026-11-13T18:33:43+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1284 | 646 | 379 | 335 | 379 | 328 | 267 | OK |
| International-Playlist.m3u | 3236 | 1744 | 593 | 510 | 582 | 513 | 1151 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 351 | 11 | 11 | 340 |
| Argentina | 13 | 1 | 0 | 12 |
| Bangladesh | 78 | 5 | 3 | 73 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 0 | 15 |
| Canada | 30 | 23 | 15 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 8 | 0 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 9 | 1 | 0 | 8 |
| Documentary & Wildlife | 52 | 40 | 26 | 12 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 14 | 25 |
| Germany | 73 | 18 | 11 | 55 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| India | 3 | 2 | 2 | 1 |
| Indian Bangla | 41 | 33 | 31 | 8 |
| Indian Entertainment | 197 | 159 | 149 | 38 |
| Indian Movies | 89 | 66 | 65 | 23 |
| Indian Music | 70 | 61 | 58 | 9 |
| International | 163 | 33 | 23 | 130 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 27 | 12 | 12 | 15 |
| Kids | 33 | 19 | 17 | 14 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 29 | 1 | 1 | 28 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 24 | 12 | 9 | 12 |
| Religious | 25 | 5 | 5 | 20 |
| Romania | 28 | 9 | 7 | 19 |
| Russia | 64 | 14 | 10 | 50 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 20 | 4 | 3 | 16 |
| Sports | 101 | 50 | 45 | 51 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 23 | 4 | 4 | 19 |
| United Kingdom | 16 | 3 | 2 | 13 |
| United States | 207 | 97 | 88 | 110 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 4 | 0 | 0 | 4 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **18961862f7ba2836ff0f867724779b2bdd3afbba16d9882faf394eca6f55b469**
- International-Playlist.m3u SHA-256: **ff372fe52c2663dafb601e52f8558384e019331d01864dd8d370ab750b3548ac**
