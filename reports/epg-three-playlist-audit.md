# EPG Audit — Published Playlists

Generated: **2026-11-01T13:28:45+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1186 | 705 | 462 | 418 | 462 | 403 | 243 | OK |
| BDIX-Playlist.m3u | 131 | 131 | 78 | 74 | 78 | 74 | 53 | OK |
| International-Playlist.m3u | 2514 | 2065 | 761 | 620 | 755 | 585 | 1304 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 350 | 6 | 6 | 344 |
| Argentina | 13 | 1 | 1 | 12 |
| Australia | 3 | 1 | 1 | 2 |
| Austria | 2 | 0 | 0 | 2 |
| Bangladesh | 84 | 3 | 2 | 81 |
| Brazil | 9 | 2 | 2 | 7 |
| Bulgaria | 17 | 6 | 6 | 11 |
| Canada | 23 | 20 | 16 | 3 |
| Chile | 12 | 1 | 0 | 11 |
| China | 7 | 0 | 0 | 7 |
| Colombia | 9 | 1 | 1 | 8 |
| Costa Rica | 8 | 0 | 0 | 8 |
| Czech Republic | 26 | 9 | 3 | 17 |
| Documentary & Wildlife | 207 | 138 | 106 | 69 |
| Dominican Republic | 11 | 1 | 0 | 10 |
| Estonia | 6 | 1 | 0 | 5 |
| Finland | 2 | 0 | 0 | 2 |
| France | 40 | 9 | 7 | 31 |
| Germany | 19 | 10 | 4 | 9 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 8 | 6 | 7 |
| Indian Bangla | 48 | 39 | 35 | 9 |
| Indian Entertainment | 226 | 188 | 178 | 38 |
| Indian Movies | 79 | 58 | 55 | 21 |
| Indian Music | 72 | 60 | 57 | 12 |
| International | 163 | 58 | 45 | 105 |
| Iran | 9 | 3 | 2 | 6 |
| Italy | 17 | 6 | 6 | 11 |
| Kids | 213 | 95 | 77 | 118 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 12 | 2 | 1 | 10 |
| Netherlands | 8 | 4 | 4 | 4 |
| New Backup | 1 | 1 | 1 | 0 |
| New Channels | 19 | 15 | 15 | 4 |
| North Macedonia | 4 | 0 | 0 | 4 |
| Pakistani | 16 | 3 | 3 | 13 |
| Panama | 5 | 0 | 0 | 5 |
| Paraguay | 5 | 0 | 0 | 5 |
| Peru | 7 | 0 | 0 | 7 |
| Poland | 23 | 17 | 13 | 6 |
| Portugal | 3 | 1 | 1 | 2 |
| Religious | 35 | 10 | 6 | 25 |
| Romania | 27 | 9 | 9 | 18 |
| Russia | 53 | 10 | 8 | 43 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Serbia | 1 | 1 | 0 | 0 |
| Singapore | 3 | 0 | 0 | 3 |
| Spain | 15 | 3 | 1 | 12 |
| Sports | 269 | 117 | 98 | 152 |
| Turkey | 13 | 0 | 0 | 13 |
| Ukraine | 18 | 2 | 0 | 16 |
| United Arab Emirates | 2 | 1 | 1 | 1 |
| United Kingdom | 9 | 1 | 0 | 8 |
| United States | 101 | 35 | 24 | 66 |
| Uzbekistan | 3 | 0 | 0 | 3 |
| Venezuela | 2 | 0 | 0 | 2 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **1f4142a28a97b4c13ad28a295ea7d931db654c6726fa6608b3f4e8e327217811**
- BDIX-Playlist.m3u SHA-256: **6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d**
- International-Playlist.m3u SHA-256: **1fe061be22b2f0ba30e3af4533d431a3a11eb482f36d0b01d39474f87b116106**
