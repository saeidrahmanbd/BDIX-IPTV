# EPG Audit — Published Playlists

Generated: **2026-10-30T07:40:05+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1160 | 690 | 464 | 409 | 464 | 398 | 226 | OK |
| BDIX-Playlist.m3u | 131 | 131 | 78 | 71 | 78 | 71 | 53 | OK |
| International-Playlist.m3u | 3205 | 2649 | 869 | 707 | 863 | 673 | 1780 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 359 | 6 | 6 | 353 |
| Argentina | 14 | 1 | 1 | 13 |
| Austria | 7 | 0 | 0 | 7 |
| Bangladesh | 87 | 3 | 1 | 84 |
| Brazil | 11 | 2 | 2 | 9 |
| Bulgaria | 19 | 7 | 6 | 12 |
| Canada | 25 | 20 | 16 | 5 |
| Chile | 18 | 1 | 0 | 17 |
| China | 12 | 0 | 0 | 12 |
| Colombia | 10 | 1 | 1 | 9 |
| Czech Republic | 27 | 9 | 3 | 18 |
| Documentary & Wildlife | 217 | 137 | 102 | 80 |
| Estonia | 6 | 1 | 0 | 5 |
| Finland | 9 | 0 | 0 | 9 |
| France | 45 | 10 | 8 | 35 |
| Germany | 84 | 11 | 9 | 73 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 15 | 8 | 6 | 7 |
| Indian Bangla | 51 | 41 | 35 | 10 |
| Indian Entertainment | 224 | 187 | 173 | 37 |
| Indian Movies | 92 | 69 | 66 | 23 |
| Indian Music | 72 | 59 | 56 | 13 |
| International | 98 | 56 | 45 | 42 |
| Iran | 16 | 3 | 2 | 13 |
| Italy | 26 | 5 | 5 | 21 |
| Kids | 226 | 96 | 75 | 130 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 19 | 6 | 4 | 13 |
| Netherlands | 17 | 8 | 8 | 9 |
| New Backup | 5 | 4 | 4 | 1 |
| New Channels | 180 | 33 | 27 | 147 |
| Pakistani | 21 | 4 | 4 | 17 |
| Peru | 8 | 0 | 0 | 8 |
| Poland | 29 | 18 | 14 | 11 |
| Portugal | 7 | 3 | 3 | 4 |
| Religious | 37 | 11 | 6 | 26 |
| Romania | 37 | 11 | 11 | 26 |
| Russia | 99 | 16 | 13 | 83 |
| Saudi Arabia | 13 | 3 | 1 | 10 |
| Spain | 21 | 4 | 1 | 17 |
| Sports | 263 | 118 | 95 | 145 |
| Sweden | 55 | 0 | 0 | 55 |
| Turkey | 20 | 1 | 0 | 19 |
| Ukraine | 31 | 4 | 2 | 27 |
| United Arab Emirates | 4 | 2 | 0 | 2 |
| United Kingdom | 12 | 2 | 1 | 10 |
| United States | 220 | 46 | 34 | 174 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 5 | 0 | 0 | 5 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **2f00cd81215b375e4776d6dd458f71acc5734daf86990b5c85061a1bec922a77**
- BDIX-Playlist.m3u SHA-256: **6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d**
- International-Playlist.m3u SHA-256: **359731d46ab6910e71335940aacfdeb1321d84c824fea6e120575031d128eff3**
