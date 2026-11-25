# EPG Audit — Published Playlists

Generated: **2026-11-25T01:29:32+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1354 | 695 | 432 | 384 | 432 | 376 | 263 | OK |
| International-Playlist.m3u | 3321 | 2307 | 890 | 764 | 877 | 791 | 1417 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 366 | 13 | 13 | 353 |
| Argentina | 14 | 0 | 0 | 14 |
| Bangladesh | 81 | 5 | 4 | 76 |
| Brazil | 14 | 7 | 7 | 7 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 27 | 20 | 15 | 7 |
| Chile | 10 | 0 | 0 | 10 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 11 | 1 | 1 | 10 |
| Documentary & Wildlife | 157 | 104 | 79 | 53 |
| Estonia | 6 | 0 | 0 | 6 |
| Fashion TV | 2 | 1 | 1 | 1 |
| France | 43 | 18 | 17 | 25 |
| Germany | 72 | 18 | 12 | 54 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 42 | 32 | 24 | 10 |
| Indian Entertainment | 197 | 164 | 145 | 33 |
| Indian Movies | 95 | 72 | 67 | 23 |
| Indian Music | 76 | 62 | 55 | 14 |
| International | 184 | 50 | 42 | 134 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 23 | 12 | 12 | 11 |
| Kids | 157 | 78 | 61 | 79 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| News | 2 | 0 | 0 | 2 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 19 | 1 | 1 | 18 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 8 | 0 | 0 | 8 |
| Poland | 23 | 11 | 10 | 12 |
| Religious | 36 | 7 | 7 | 29 |
| Romania | 30 | 9 | 7 | 21 |
| Russia | 75 | 20 | 18 | 55 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 18 | 6 | 5 | 12 |
| Sports | 225 | 128 | 118 | 97 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 28 | 8 | 7 | 20 |
| United Kingdom | 16 | 3 | 3 | 13 |
| United States | 220 | 103 | 99 | 117 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **a2ef9bb3e7d03dbfffd4f78e796027e4f5e46374fe9717d89785190c04f23e6a**
- International-Playlist.m3u SHA-256: **ac46370e5f6aa0b95c2c56df06a0d9b8eadf35f94c85e7044e9cec3f316f7619**
