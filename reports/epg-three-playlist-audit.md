# EPG Audit — Published Playlists

Generated: **2026-10-31T10:56:50+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1160 | 690 | 464 | 416 | 464 | 403 | 226 | OK |
| BDIX-Playlist.m3u | 131 | 131 | 78 | 71 | 78 | 71 | 53 | OK |
| International-Playlist.m3u | 3312 | 2752 | 887 | 727 | 881 | 690 | 1865 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 359 | 6 | 6 | 353 |
| Argentina | 18 | 1 | 1 | 17 |
| Austria | 7 | 0 | 0 | 7 |
| Bangladesh | 87 | 3 | 0 | 84 |
| Brazil | 12 | 2 | 2 | 10 |
| Bulgaria | 22 | 7 | 6 | 15 |
| Canada | 27 | 20 | 16 | 7 |
| Chile | 19 | 1 | 0 | 18 |
| China | 12 | 0 | 0 | 12 |
| Colombia | 13 | 1 | 1 | 12 |
| Czech Republic | 27 | 9 | 3 | 18 |
| Documentary & Wildlife | 217 | 137 | 103 | 80 |
| Estonia | 7 | 1 | 0 | 6 |
| Finland | 9 | 0 | 0 | 9 |
| France | 51 | 13 | 11 | 38 |
| Germany | 88 | 12 | 6 | 76 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 16 | 9 | 7 | 7 |
| Indian Bangla | 51 | 41 | 37 | 10 |
| Indian Entertainment | 224 | 188 | 180 | 36 |
| Indian Movies | 92 | 70 | 66 | 22 |
| Indian Music | 73 | 59 | 56 | 14 |
| International | 98 | 56 | 46 | 42 |
| Iran | 16 | 3 | 2 | 13 |
| Italy | 26 | 7 | 7 | 19 |
| Kids | 226 | 97 | 75 | 129 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 20 | 6 | 5 | 14 |
| Netherlands | 18 | 8 | 8 | 10 |
| New Backup | 5 | 4 | 4 | 1 |
| New Channels | 192 | 32 | 27 | 160 |
| North Macedonia | 5 | 0 | 0 | 5 |
| Pakistani | 22 | 4 | 4 | 18 |
| Peru | 11 | 0 | 0 | 11 |
| Poland | 29 | 18 | 14 | 11 |
| Portugal | 8 | 3 | 3 | 5 |
| Religious | 37 | 11 | 6 | 26 |
| Romania | 40 | 14 | 14 | 26 |
| Russia | 110 | 19 | 16 | 91 |
| Saudi Arabia | 15 | 3 | 1 | 12 |
| Serbia | 5 | 1 | 0 | 4 |
| Spain | 25 | 4 | 1 | 21 |
| Sports | 263 | 118 | 95 | 145 |
| Sweden | 55 | 0 | 0 | 55 |
| Turkey | 21 | 1 | 0 | 20 |
| Ukraine | 32 | 4 | 2 | 28 |
| United Arab Emirates | 4 | 2 | 1 | 2 |
| United Kingdom | 15 | 2 | 0 | 13 |
| United States | 241 | 48 | 36 | 193 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **6c693baea478e44539eac29fb99c0b3aa6e7109f06134b8b010d3449c259b49c**
- BDIX-Playlist.m3u SHA-256: **6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d**
- International-Playlist.m3u SHA-256: **cc8be6868a2a963163405b70c670b252cc015d8cf305467ed941abae02b6be93**
