# EPG Audit — Published Playlists

Generated: **2026-11-12T08:55:48+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1242 | 650 | 383 | 337 | 383 | 333 | 267 | OK |
| International-Playlist.m3u | 3107 | 1712 | 584 | 501 | 574 | 508 | 1128 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 339 | 10 | 10 | 329 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 75 | 5 | 3 | 70 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 0 | 15 |
| Canada | 30 | 23 | 15 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 7 | 0 | 0 | 7 |
| Costa Rica | 8 | 0 | 0 | 8 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 10 | 1 | 0 | 9 |
| Documentary & Wildlife | 52 | 40 | 26 | 12 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 14 | 25 |
| Germany | 73 | 18 | 11 | 55 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 41 | 31 | 29 | 10 |
| Indian Entertainment | 199 | 164 | 157 | 35 |
| Indian Movies | 89 | 66 | 60 | 23 |
| Indian Music | 71 | 61 | 57 | 10 |
| International | 160 | 33 | 23 | 127 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 27 | 12 | 12 | 15 |
| Kids | 33 | 19 | 17 | 14 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 16 | 7 | 2 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 29 | 1 | 1 | 28 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 25 | 13 | 10 | 12 |
| Religious | 25 | 5 | 5 | 20 |
| Romania | 28 | 9 | 7 | 19 |
| Russia | 61 | 14 | 10 | 47 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 20 | 4 | 3 | 16 |
| Sports | 102 | 51 | 47 | 51 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 18 | 4 | 4 | 14 |
| United Kingdom | 16 | 3 | 2 | 13 |
| United States | 202 | 93 | 84 | 109 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 5 | 0 | 0 | 5 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **c4dece2f2bf4cd4b4b2d6b11c052f7a7f46d338791823e770a8ff3f38d53f646**
- International-Playlist.m3u SHA-256: **e2e9d5abca13f4ea9053057d21d4725713d3e7407fc4a0d5d8bcdd5347d789fa**
