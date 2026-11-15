# EPG Audit — Published Playlists

Generated: **2026-11-15T10:02:40+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1274 | 647 | 380 | 336 | 380 | 330 | 267 | OK |
| International-Playlist.m3u | 3129 | 1752 | 599 | 514 | 588 | 520 | 1153 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 346 | 11 | 11 | 335 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 80 | 5 | 3 | 75 |
| Brazil | 13 | 7 | 7 | 6 |
| Bulgaria | 21 | 6 | 0 | 15 |
| Canada | 30 | 23 | 15 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 0 | 0 | 9 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 16 | 5 |
| DO | 10 | 1 | 0 | 9 |
| Documentary & Wildlife | 52 | 40 | 26 | 12 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 14 | 25 |
| Germany | 72 | 18 | 11 | 54 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 6 | 8 |
| Indian Bangla | 41 | 33 | 30 | 8 |
| Indian Entertainment | 200 | 163 | 152 | 37 |
| Indian Movies | 89 | 66 | 64 | 23 |
| Indian Music | 70 | 61 | 58 | 9 |
| International | 163 | 33 | 23 | 130 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 27 | 12 | 12 | 15 |
| Kids | 32 | 18 | 16 | 14 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 29 | 1 | 1 | 28 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 6 | 0 | 0 | 6 |
| Poland | 24 | 12 | 9 | 12 |
| Religious | 23 | 5 | 5 | 18 |
| Romania | 28 | 9 | 7 | 19 |
| Russia | 70 | 19 | 15 | 51 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 20 | 4 | 3 | 16 |
| Sports | 100 | 50 | 46 | 50 |
| Sweden | 49 | 12 | 12 | 37 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 25 | 5 | 5 | 20 |
| United Kingdom | 16 | 3 | 2 | 13 |
| United States | 208 | 98 | 89 | 110 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **1d0bc9ef3a01f48a9b0fc46677ab87c42774c9e1a1df080f3c47cc3d72bb1af7**
- International-Playlist.m3u SHA-256: **8acb8898c683fa633d4a1a86dfef767a1fb68f0a516ff9055f06d9a2fac6c38d**
