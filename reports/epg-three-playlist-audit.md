# EPG Audit — Published Playlists

Generated: **2026-11-01T02:17:12+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1161 | 690 | 464 | 408 | 464 | 394 | 226 | OK |
| BDIX-Playlist.m3u | 131 | 131 | 78 | 71 | 78 | 71 | 53 | OK |
| International-Playlist.m3u | 3305 | 2727 | 896 | 724 | 890 | 683 | 1831 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 354 | 6 | 6 | 348 |
| Argentina | 16 | 1 | 1 | 15 |
| Austria | 7 | 0 | 0 | 7 |
| Bangladesh | 87 | 3 | 0 | 84 |
| Brazil | 12 | 2 | 2 | 10 |
| Bulgaria | 22 | 7 | 6 | 15 |
| Canada | 26 | 21 | 17 | 5 |
| Chile | 16 | 1 | 0 | 15 |
| China | 12 | 0 | 0 | 12 |
| Colombia | 12 | 1 | 1 | 11 |
| Czech Republic | 27 | 9 | 3 | 18 |
| Documentary & Wildlife | 217 | 137 | 102 | 80 |
| Estonia | 9 | 1 | 0 | 8 |
| Finland | 9 | 0 | 0 | 9 |
| France | 50 | 13 | 11 | 37 |
| Germany | 87 | 11 | 5 | 76 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 16 | 9 | 7 | 7 |
| Indian Bangla | 51 | 41 | 37 | 10 |
| Indian Entertainment | 223 | 188 | 176 | 35 |
| Indian Movies | 92 | 70 | 64 | 22 |
| Indian Music | 74 | 59 | 55 | 15 |
| International | 98 | 56 | 44 | 42 |
| Iran | 16 | 3 | 2 | 13 |
| Italy | 26 | 7 | 7 | 19 |
| Kids | 226 | 97 | 75 | 129 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 20 | 6 | 4 | 14 |
| Netherlands | 19 | 8 | 8 | 11 |
| New Backup | 5 | 4 | 4 | 1 |
| New Channels | 179 | 33 | 27 | 146 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 21 | 4 | 4 | 17 |
| Peru | 10 | 0 | 0 | 10 |
| Poland | 29 | 18 | 14 | 11 |
| Portugal | 6 | 3 | 3 | 3 |
| Religious | 36 | 11 | 6 | 25 |
| Romania | 41 | 15 | 15 | 26 |
| Russia | 109 | 19 | 16 | 90 |
| Saudi Arabia | 14 | 3 | 1 | 11 |
| Serbia | 5 | 1 | 0 | 4 |
| Spain | 25 | 4 | 1 | 21 |
| Sports | 263 | 118 | 92 | 145 |
| Sweden | 55 | 0 | 0 | 55 |
| Turkey | 21 | 1 | 0 | 20 |
| Ukraine | 32 | 4 | 2 | 28 |
| United Kingdom | 15 | 4 | 2 | 11 |
| United States | 253 | 56 | 44 | 197 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **1fda9572c1802e8d9b965d28729654edc22a6b61e551f5349906bf174156f8dc**
- BDIX-Playlist.m3u SHA-256: **6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d**
- International-Playlist.m3u SHA-256: **127b96d96a025f2bef62a176e11f9dd146f9d2c9fed09badd7ee3a939472e74a**
