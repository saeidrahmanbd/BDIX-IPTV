# EPG Audit — Published Playlists

Generated: **2026-11-24T10:06:29+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1339 | 695 | 433 | 403 | 433 | 387 | 262 | OK |
| International-Playlist.m3u | 3319 | 2307 | 890 | 767 | 877 | 806 | 1417 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 366 | 13 | 13 | 353 |
| Argentina | 14 | 0 | 0 | 14 |
| Bangladesh | 81 | 5 | 4 | 76 |
| Brazil | 14 | 7 | 7 | 7 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 27 | 20 | 16 | 7 |
| Chile | 10 | 0 | 0 | 10 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 11 | 1 | 1 | 10 |
| Documentary & Wildlife | 157 | 104 | 74 | 53 |
| Estonia | 6 | 0 | 0 | 6 |
| Fashion TV | 2 | 1 | 0 | 1 |
| France | 43 | 18 | 17 | 25 |
| Germany | 72 | 18 | 12 | 54 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 42 | 32 | 29 | 10 |
| Indian Entertainment | 198 | 165 | 155 | 33 |
| Indian Movies | 95 | 72 | 69 | 23 |
| Indian Music | 76 | 62 | 59 | 14 |
| International | 183 | 50 | 42 | 133 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 23 | 12 | 12 | 11 |
| Kids | 157 | 78 | 56 | 79 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| News | 2 | 0 | 0 | 2 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 19 | 1 | 1 | 18 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 8 | 0 | 0 | 8 |
| Poland | 23 | 11 | 9 | 12 |
| Religious | 36 | 7 | 7 | 29 |
| Romania | 30 | 9 | 7 | 21 |
| Russia | 75 | 20 | 16 | 55 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 18 | 6 | 5 | 12 |
| Sports | 225 | 128 | 115 | 97 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 28 | 8 | 8 | 20 |
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

- IPTV-Playlist.m3u SHA-256: **ff15c8ceffaa71c72e6b9f2c387ff941dc227454cb482bb4a2943966640ec13c**
- International-Playlist.m3u SHA-256: **1e8a9d34987a0e4fa2c626dc68216f38db8d562a2a26d12945d6138a2d6e7585**
