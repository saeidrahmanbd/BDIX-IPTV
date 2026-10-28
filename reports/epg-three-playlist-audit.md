# EPG Audit — Published Playlists

Generated: **2026-10-28T11:40:28+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1178 | 707 | 476 | 426 | 476 | 183 | 231 | OK |
| BDIX-Playlist.m3u | 131 | 131 | 75 | 70 | 75 | 15 | 56 | OK |
| International-Playlist.m3u | 3221 | 2672 | 864 | 707 | 858 | 396 | 1808 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 359 | 6 | 6 | 353 |
| Argentina | 17 | 1 | 1 | 16 |
| Aruba | 6 | 0 | 0 | 6 |
| Bangladesh | 87 | 1 | 0 | 86 |
| Brazil | 12 | 2 | 2 | 10 |
| Bulgaria | 15 | 7 | 5 | 8 |
| Canada | 26 | 20 | 16 | 6 |
| Chile | 27 | 1 | 0 | 26 |
| China | 14 | 0 | 0 | 14 |
| Colombia | 13 | 1 | 1 | 12 |
| Czech Republic | 26 | 9 | 3 | 17 |
| Documentary & Wildlife | 217 | 137 | 103 | 80 |
| Dominican Republic | 7 | 0 | 0 | 7 |
| Egypt | 5 | 2 | 0 | 3 |
| Estonia | 6 | 1 | 0 | 5 |
| France | 45 | 9 | 7 | 36 |
| Germany | 74 | 11 | 9 | 63 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 16 | 8 | 6 | 8 |
| Indian Bangla | 50 | 40 | 34 | 10 |
| Indian Entertainment | 227 | 190 | 177 | 37 |
| Indian Movies | 92 | 69 | 66 | 23 |
| Indian Music | 72 | 59 | 56 | 13 |
| International | 98 | 56 | 46 | 42 |
| Iran | 15 | 3 | 2 | 12 |
| Italy | 26 | 6 | 6 | 20 |
| Kids | 226 | 96 | 76 | 130 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 19 | 6 | 5 | 13 |
| Netherlands | 21 | 8 | 8 | 13 |
| New Backup | 20 | 17 | 17 | 3 |
| New Channels | 177 | 29 | 26 | 148 |
| Pakistani | 21 | 3 | 3 | 18 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 14 | 0 | 0 | 14 |
| Poland | 33 | 17 | 13 | 16 |
| Portugal | 7 | 3 | 3 | 4 |
| Religious | 36 | 11 | 6 | 25 |
| Romania | 40 | 12 | 12 | 28 |
| Russia | 90 | 16 | 13 | 74 |
| Saudi Arabia | 15 | 3 | 1 | 12 |
| Serbia | 5 | 1 | 0 | 4 |
| Spain | 41 | 4 | 1 | 37 |
| Sports | 258 | 113 | 92 | 145 |
| Sweden | 43 | 0 | 0 | 43 |
| Turkey | 20 | 1 | 0 | 19 |
| Ukraine | 30 | 3 | 0 | 27 |
| United Arab Emirates | 4 | 2 | 1 | 2 |
| United Kingdom | 12 | 2 | 1 | 10 |
| United States | 208 | 41 | 29 | 167 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 5 | 0 | 0 | 5 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **fabbd4dfb8fa0eca77679a7a872c21ef8813bb7f49556db6fe3ab18c4c07b697**
- BDIX-Playlist.m3u SHA-256: **596c7c069bed399dc8e5029090b788b7421ac82a315c5ac55b8caf1b82ff529d**
- International-Playlist.m3u SHA-256: **a300f65b5f0b5568475a09e5dd3a68eb749d22812aaa9a09034ebee9a7a2d1ce**
