# EPG Audit — Published Playlists

Generated: **2026-10-31T10:05:42+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1161 | 691 | 464 | 416 | 464 | 403 | 227 | OK |
| BDIX-Playlist.m3u | 131 | 131 | 78 | 71 | 78 | 71 | 53 | OK |
| International-Playlist.m3u | 6540 | 2710 | 885 | 726 | 879 | 689 | 1825 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 359 | 6 | 6 | 353 |
| Argentina | 16 | 1 | 1 | 15 |
| Austria | 7 | 0 | 0 | 7 |
| Bangladesh | 87 | 3 | 0 | 84 |
| Brazil | 12 | 2 | 2 | 10 |
| Bulgaria | 21 | 7 | 6 | 14 |
| Canada | 25 | 20 | 16 | 5 |
| Chile | 19 | 1 | 0 | 18 |
| China | 12 | 0 | 0 | 12 |
| Colombia | 11 | 1 | 1 | 10 |
| Czech Republic | 27 | 9 | 3 | 18 |
| Documentary & Wildlife | 217 | 137 | 103 | 80 |
| Estonia | 6 | 1 | 0 | 5 |
| Finland | 9 | 0 | 0 | 9 |
| France | 49 | 12 | 10 | 37 |
| Germany | 87 | 12 | 6 | 75 |
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
| Mexico | 19 | 6 | 5 | 13 |
| Netherlands | 17 | 8 | 8 | 9 |
| New Backup | 5 | 4 | 4 | 1 |
| New Channels | 191 | 33 | 27 | 158 |
| Pakistani | 22 | 4 | 4 | 18 |
| Peru | 10 | 0 | 0 | 10 |
| Poland | 29 | 18 | 14 | 11 |
| Portugal | 8 | 3 | 3 | 5 |
| Religious | 37 | 11 | 6 | 26 |
| Romania | 40 | 14 | 14 | 26 |
| Russia | 105 | 19 | 16 | 86 |
| Saudi Arabia | 14 | 3 | 1 | 11 |
| Spain | 23 | 4 | 1 | 19 |
| Sports | 263 | 118 | 95 | 145 |
| Sweden | 55 | 0 | 0 | 55 |
| Turkey | 21 | 1 | 0 | 20 |
| Ukraine | 32 | 4 | 2 | 28 |
| United Arab Emirates | 4 | 2 | 1 | 2 |
| United Kingdom | 13 | 2 | 1 | 11 |
| United States | 236 | 47 | 35 | 189 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 5 | 0 | 0 | 5 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **4bd6baeed0589da3c3a464d09c746a3eef1ac64eb99a39714b257814633bdf73**
- BDIX-Playlist.m3u SHA-256: **6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d**
- International-Playlist.m3u SHA-256: **e2fcb233e0c34c12830d9faf3936d9ff3982f6c90bd31e8b30b2a7486e0e6a1f**
