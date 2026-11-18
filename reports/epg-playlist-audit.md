# EPG Audit — Published Playlists

Generated: **2026-11-18T03:50:28+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1378 | 714 | 434 | 400 | 434 | 384 | 280 | OK |
| International-Playlist.m3u | 3251 | 1845 | 665 | 598 | 654 | 585 | 1180 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 300 | 11 | 11 | 289 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 85 | 5 | 4 | 80 |
| Brazil | 12 | 7 | 7 | 5 |
| Bulgaria | 21 | 6 | 4 | 15 |
| Canada | 27 | 20 | 16 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 8 | 0 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 10 | 1 | 1 | 9 |
| Documentary & Wildlife | 60 | 45 | 36 | 15 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 41 | 16 | 15 | 25 |
| Germany | 74 | 18 | 12 | 56 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 42 | 32 | 29 | 10 |
| Indian Entertainment | 204 | 168 | 157 | 36 |
| Indian Movies | 86 | 64 | 63 | 22 |
| Indian Music | 66 | 56 | 53 | 10 |
| International | 185 | 49 | 42 | 136 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 26 | 12 | 12 | 14 |
| Kids | 40 | 24 | 22 | 16 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 9 | 6 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 30 | 1 | 1 | 29 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 6 | 0 | 0 | 6 |
| Poland | 23 | 11 | 9 | 12 |
| Religious | 27 | 6 | 6 | 21 |
| Romania | 28 | 9 | 7 | 19 |
| Russia | 73 | 20 | 16 | 53 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 23 | 7 | 5 | 16 |
| Sports | 114 | 70 | 67 | 44 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 13 | 0 | 0 | 13 |
| Ukraine | 27 | 7 | 6 | 20 |
| United Kingdom | 16 | 3 | 3 | 13 |
| United States | 206 | 98 | 95 | 108 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **939b956ecb9712790c70bc6b900d94a994112871cbfc7376d86b5cd3cb87373e**
- International-Playlist.m3u SHA-256: **46877e223e5894ce198f2c89157cf2bd672513e198a046cd02612edb6f5e422a**
