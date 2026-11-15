# EPG Audit — Published Playlists

Generated: **2026-11-15T16:12:49+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1298 | 657 | 386 | 341 | 386 | 334 | 271 | OK |
| International-Playlist.m3u | 3129 | 1752 | 599 | 514 | 588 | 520 | 1153 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 346 | 11 | 11 | 335 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 81 | 5 | 3 | 76 |
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
| Indian Entertainment | 203 | 166 | 155 | 37 |
| Indian Movies | 89 | 66 | 64 | 23 |
| Indian Music | 70 | 61 | 58 | 9 |
| International | 165 | 33 | 23 | 132 |
| Iran | 13 | 1 | 0 | 12 |
| Italy | 27 | 12 | 12 | 15 |
| Kids | 33 | 19 | 17 | 14 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 17 | 8 | 2 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 29 | 1 | 1 | 28 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 6 | 0 | 0 | 6 |
| Poland | 24 | 12 | 9 | 12 |
| Religious | 24 | 5 | 5 | 19 |
| Romania | 28 | 9 | 7 | 19 |
| Russia | 70 | 19 | 15 | 51 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 0 | 4 |
| Spain | 20 | 4 | 3 | 16 |
| Sports | 100 | 50 | 45 | 50 |
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

- IPTV-Playlist.m3u SHA-256: **571a66b5526fe77da17afbe18e249ec092484806765e8cf0a5f4265518ebad24**
- International-Playlist.m3u SHA-256: **8acb8898c683fa633d4a1a86dfef767a1fb68f0a516ff9055f06d9a2fac6c38d**
