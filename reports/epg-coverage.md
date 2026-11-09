# EPG Coverage & Mapping Report

Generated: **2026-11-09T12:15:32+00:00**

This report audits active unique channel identities across the two maintained playlists configured in the automated EPG pipeline. A source mapping is not counted as usable current/future coverage unless it has a valid programme interval and valid non-empty multilingual title data within the generator's -6-hour/+7-day window; English titles rank first, then Bengali, then other valid languages.
The XMLTV guide is published at **epg/epg.xml**. The published guide uses the playlist's tvg-id as the XMLTV channel ID, not the upstream provider's source ID.

## Overall Coverage

- Active unique playlist channel IDs audited: **1966**
- IDs with an EPG source mapping: **733/1966 (37.3%)**
- IDs with usable current/future source schedules (nonblank multilingual titles (English preferred, then Bengali, then other valid languages)): **673/1966 (34.2%)**
- IDs with no EPG source mapping: **1233**

## Coverage by Playlist Group

| Group | Active IDs | Mapped IDs | Current/future | No mapping |
|---|---:|---:|---:|---:|
| Adult | 352 | 11 | 11 | 341 |
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 71 | 5 | 3 | 66 |
| Brazil | 9 | 3 | 3 | 6 |
| Bulgaria | 21 | 6 | 6 | 15 |
| Canada | 30 | 23 | 17 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 1 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 22 | 17 | 17 | 5 |
| DO | 10 | 1 | 0 | 9 |
| Documentary & Wildlife | 53 | 41 | 29 | 12 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 14 | 25 |
| Germany | 73 | 18 | 18 | 55 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 7 | 8 |
| Indian Bangla | 39 | 28 | 26 | 11 |
| Indian Entertainment | 197 | 162 | 156 | 35 |
| Indian Movies | 85 | 63 | 61 | 22 |
| Indian Music | 66 | 57 | 54 | 9 |
| International | 164 | 33 | 25 | 131 |
| Iran | 11 | 1 | 0 | 10 |
| Italy | 27 | 11 | 11 | 16 |
| Kids | 38 | 20 | 17 | 18 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 16 | 7 | 6 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 20 | 1 | 1 | 19 |
| Panama | 5 | 0 | 0 | 5 |
| Peru | 8 | 0 | 0 | 8 |
| Poland | 25 | 13 | 12 | 12 |
| Religious | 23 | 4 | 4 | 19 |
| Romania | 28 | 9 | 9 | 19 |
| Russia | 56 | 15 | 15 | 41 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 1 | 4 |
| Spain | 22 | 4 | 4 | 18 |
| Sports | 47 | 26 | 23 | 21 |
| Sweden | 43 | 12 | 12 | 31 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 20 | 6 | 6 | 14 |
| United Kingdom | 17 | 4 | 3 | 13 |
| United States | 188 | 92 | 91 | 96 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Source Status

- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz — 946 channel IDs; 700 IDs with usable current/future programmes; 89188 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz — 54 channel IDs; 5 IDs with usable current/future programmes; 47 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz — 557 channel IDs; 523 IDs with usable current/future programmes; 19517 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — https://www.free-epg.de/api/epg/pk.xml.gz — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 503: Service Unavailable
- **OK** — https://iptv-epg.org/files/epg-in.xml.gz — 419 channel IDs; 269 IDs with usable current/future programmes; 53666 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://epg.lat/files/in.xml.gz — 1166 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://epg.lat/files/us.xml.gz — 4456 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.free-epg.de/api/epg/in.xml.gz — 947 channel IDs; 773 IDs with usable current/future programmes; 63669 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.free-epg.de/api/epg/us.xml.gz — 5546 channel IDs; 5541 IDs with usable current/future programmes; 173911 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.open-epg.com/files/india.xml.gz — 1178 channel IDs; 745 IDs with usable current/future programmes; 38954 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ar.xml.gz — 185 channel IDs; 132 IDs with usable current/future programmes; 2845 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-bg.xml.gz — 116 channel IDs; 96 IDs with usable current/future programmes; 16193 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-br.xml.gz — 182 channel IDs; 133 IDs with usable current/future programmes; 24669 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ca.xml.gz — 808 channel IDs; 803 IDs with usable current/future programmes; 113686 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://iptv-epg.org/files/epg-cl.xml.gz — 184 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://iptv-epg.org/files/epg-co.xml.gz — 180 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-cz.xml.gz — 261 channel IDs; 222 IDs with usable current/future programmes; 50420 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-de.xml.gz — 438 channel IDs; 371 IDs with usable current/future programmes; 65892 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-es.xml.gz — 300 channel IDs; 276 IDs with usable current/future programmes; 31746 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-fr.xml.gz — 485 channel IDs; 376 IDs with usable current/future programmes; 39064 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-gr.xml.gz — 177 channel IDs; 163 IDs with usable current/future programmes; 14337 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-hk.xml.gz — 176 channel IDs; 127 IDs with usable current/future programmes; 21171 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-hu.xml.gz — 152 channel IDs; 131 IDs with usable current/future programmes; 29063 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-it.xml.gz — 306 channel IDs; 262 IDs with usable current/future programmes; 33304 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-mx.xml.gz — 175 channel IDs; 137 IDs with usable current/future programmes; 16645 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-nl.xml.gz — 184 channel IDs; 154 IDs with usable current/future programmes; 37186 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://iptv-epg.org/files/epg-pe.xml.gz — 128 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-pl.xml.gz — 447 channel IDs; 402 IDs with usable current/future programmes; 87023 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-pt.xml.gz — 195 channel IDs; 147 IDs with usable current/future programmes; 30129 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ro.xml.gz — 282 channel IDs; 254 IDs with usable current/future programmes; 51864 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ru.xml.gz — 223 channel IDs; 198 IDs with usable current/future programmes; 46345 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-rs.xml.gz — 265 channel IDs; 240 IDs with usable current/future programmes; 24962 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-se.xml.gz — 95 channel IDs; 80 IDs with usable current/future programmes; 15349 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-tr.xml.gz — 108 channel IDs; 81 IDs with usable current/future programmes; 17211 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-gb.xml.gz — 932 channel IDs; 875 IDs with usable current/future programmes; 88088 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-at.xml.gz — 286 channel IDs; 262 IDs with usable current/future programmes; 42618 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-au.xml.gz — 490 channel IDs; 486 IDs with usable current/future programmes; 47145 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-cr.xml.gz — 84 channel IDs; 74 IDs with usable current/future programmes; 8799 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-pa.xml.gz — 121 channel IDs; 112 IDs with usable current/future programmes; 11493 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-py.xml.gz — 79 channel IDs; 70 IDs with usable current/future programmes; 8732 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-sg.xml.gz — 209 channel IDs; 153 IDs with usable current/future programmes; 27085 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/at.xml.gz — 286 channel IDs; 262 IDs with usable current/future programmes; 42618 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/cn.xml.gz — 711 channel IDs; 533 IDs with usable current/future programmes; 35404 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/cr.xml.gz — 84 channel IDs; 74 IDs with usable current/future programmes; 8799 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://free-epg.de/api/epg/ec.xml.gz — 104 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — https://free-epg.de/api/epg/ee.xml.gz — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 503: Service Unavailable
- **OK** — https://free-epg.de/api/epg/pa.xml.gz — 121 channel IDs; 112 IDs with usable current/future programmes; 11485 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/sa.xml.gz — 138 channel IDs; 18 IDs with usable current/future programmes; 792 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://free-epg.de/api/epg/ua.xml.gz — 231 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/in.xml — 206 channel IDs; 202 IDs with usable current/future programmes; 2087 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/us.xml — 593 channel IDs; 582 IDs with usable current/future programmes; 4912 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml — 698 channel IDs; 642 IDs with usable current/future programmes; 55792 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz — 717 channel IDs; 675 IDs with usable current/future programmes; 27691 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=IN1.xml.gz — 946 channel IDs; 699 IDs with usable current/future programmes; 63829 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=IN4.xml.gz — 557 channel IDs; 505 IDs with usable current/future programmes; 10059 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://m3u-edit.com/epg-source.php?file=india_dishtv.in.xml — 394 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml — 762 channel IDs; 755 IDs with usable current/future programmes; 76084 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml — 1496 channel IDs; 1320 IDs with usable current/future programmes; 66988 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml — 286 channel IDs; 243 IDs with usable current/future programmes; 6886 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml — 120 channel IDs; 106 IDs with usable current/future programmes; 22270 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/slingtv.xml — 6 channel IDs; 6 IDs with usable current/future programmes; 69 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/epg.xml.gz — 2233 channel IDs; 883 IDs with usable current/future programmes; 16317 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/jioepg.xml.gz — 1173 channel IDs; 262 IDs with usable current/future programmes; 4777 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/tsepg.xml.gz — 717 channel IDs; 675 IDs with usable current/future programmes; 27691 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz — 487 channel IDs; 385 IDs with usable current/future programmes; 30314 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.open-epg.com/files/unitedkingdom.xml.gz — 566 channel IDs; 540 IDs with usable current/future programmes; 28146 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz — 792 channel IDs; 773 IDs with usable current/future programmes; 61980 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-us.xml.gz — 12843 channel IDs; 12234 IDs with usable current/future programmes; 945866 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz — 912 channel IDs; 824 IDs with usable current/future programmes; 87415 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz — 345 channel IDs; 282 IDs with usable current/future programmes; 42056 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz — 696 channel IDs; 695 IDs with usable current/future programmes; 69357 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CH1.xml.gz — 751 channel IDs; 730 IDs with usable current/future programmes; 62644 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CZ1.xml.gz — 1087 channel IDs; 513 IDs with usable current/future programmes; 40437 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DE1.xml.gz — 266 channel IDs; 250 IDs with usable current/future programmes; 21718 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DO1.xml.gz — 56 channel IDs; 55 IDs with usable current/future programmes; 4733 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_ES1.xml.gz — 256 channel IDs; 237 IDs with usable current/future programmes; 4640 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_FR1.xml.gz — 574 channel IDs; 529 IDs with usable current/future programmes; 54708 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_GR1.xml.gz — 321 channel IDs; 301 IDs with usable current/future programmes; 20048 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz — 143 channel IDs; 132 IDs with usable current/future programmes; 13355 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HU1.xml.gz — 193 channel IDs; 166 IDs with usable current/future programmes; 17189 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IT1.xml.gz — 195 channel IDs; 151 IDs with usable current/future programmes; 15152 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz — 163 channel IDs; 129 IDs with usable current/future programmes; 10800 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MX1.xml.gz — 178 channel IDs; 164 IDs with usable current/future programmes; 12842 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_NL1.xml.gz — 159 channel IDs; 156 IDs with usable current/future programmes; 21940 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_PL1.xml.gz — 636 channel IDs; 581 IDs with usable current/future programmes; 87278 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_RO1.xml.gz — 370 channel IDs; 353 IDs with usable current/future programmes; 35067 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_SA2.xml.gz — 31 channel IDs; 31 IDs with usable current/future programmes; 4081 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_TR1.xml.gz — 178 channel IDs; 139 IDs with usable current/future programmes; 13320 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR1.xml.gz — 266 channel IDs; 98 IDs with usable current/future programmes; 16074 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR2.xml.gz — 97 channel IDs; 92 IDs with usable current/future programmes; 8372 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://hum.tv/schedule/ — 1 channel IDs; 1 IDs with usable current/future programmes; 21 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — RTV official daily schedule (Bangladesh) — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; Could not obtain a current official RTV schedule over verified HTTPS (rtvonline: no daily schedule article link on homepage; www.rtvbd.tv: URLError after retry; rtvbd.tv: URLError after retry)
- **OK** — https://migrate.btvlive.gov.bd/channel/BTV — 1 channel IDs; 1 IDs with usable current/future programmes; 68 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — Maasranga official weekly grid (undated) — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 403: Forbidden
- **NO_PROGRAMMES** — M3U4U XMLTV (private Actions secret) — 229 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — iptv-org/epg (targeted build-time guide) — 244 channel IDs; 217 IDs with usable current/future programmes; 7623 eligible programme rows with valid non-empty titles in any language in the guide window

## Channels Requiring Attention

The table includes every active channel identity without usable current/future guide data, not only Indian channels. NO_GUIDE_HIT means no configured source could be matched; MAPPED_ID_ONLY means an identity was found but no usable schedule was available; MAPPED_NOT_CURRENTLY_FOUND means a retained mapping was not found in the currently configured feeds.

| Group | Channel | Playlist ID | EPG source ID | Status |
|---|---|---|---|---|
| Adult | Abella Danger | custom.24-7-xxx-abella-danger | - | NO_GUIDE_HIT |
| Adult | AJ Applegate | custom.24-7-xxx-aj-applegate | - | NO_GUIDE_HIT |
| Adult | Alba 2 | custom.alba-2 | - | NO_GUIDE_HIT |
| Adult | Alba 3 | custom.alba-3 | - | NO_GUIDE_HIT |
| Adult | Alba 4 | custom.alba-4 | - | NO_GUIDE_HIT |
| Adult | Alexis Texas | custom.24-7-xxx-alexis-texas | - | NO_GUIDE_HIT |
| Adult | Alura Jenson | custom.24-7-xxx-alura-jenson | - | NO_GUIDE_HIT |
| Adult | Amateur | custom.24-7-xxx-amateur | - | NO_GUIDE_HIT |
| Adult | Anal | custom.xxx-anal | - | NO_GUIDE_HIT |
| Adult | Anal Mom | custom.xxx-anal-mom | - | NO_GUIDE_HIT |
| Adult | Anal Teen Angels | custom.xxx-anal-teen-angels | - | NO_GUIDE_HIT |
| Adult | Angel Smalls | custom.24-7-xxx-angel-smalls | - | NO_GUIDE_HIT |
| Adult | Angela White | custom.24-7-xxx-angela-white | - | NO_GUIDE_HIT |
| Adult | AsiaN | AsiaN.kr | - | NO_GUIDE_HIT |
| Adult | Ass Parade | custom.24-7-xxx-ass-parade | - | NO_GUIDE_HIT |
| Adult | Ava Devine | custom.24-7-xxx-ava-devine | - | NO_GUIDE_HIT |
| Adult | Babes TV | BabesTV.us | - | NO_GUIDE_HIT |
| Adult | Babes TV Russia | custom.babes-tv-russia | - | NO_GUIDE_HIT |
| Adult | Bangbus | custom.24-7-xxx-bangbus | - | NO_GUIDE_HIT |
| Adult | BBC Big Ass | custom.24-7-xxx-bbc-big-ass | - | NO_GUIDE_HIT |
| Adult | BBW | custom.24-7-xxx-bbw | - | NO_GUIDE_HIT |
| Adult | BDSM | custom.24-7-xxx-bdsm | - | NO_GUIDE_HIT |
| Adult | Big Ass | custom.24-7-xxx-big-ass | - | NO_GUIDE_HIT |
| Adult | Big Dick | custom.xxx-big-dick | - | NO_GUIDE_HIT |
| Adult | Big Tits | custom.24-7-xxx-big-tits | - | NO_GUIDE_HIT |
| Adult | Blonde | custom.blonde | - | NO_GUIDE_HIT |
| Adult | Blowjob | custom.xxx-blowjob | - | NO_GUIDE_HIT |
| Adult | Brand New Amateurs | custom.xxx-brand-new-amateurs | - | NO_GUIDE_HIT |
| Adult | Brazzers Extra | custom.xxx-brazzers-extra | - | NO_GUIDE_HIT |
| Adult | Brazzers Rated | custom.24-7-xxx-brazzers-rated | - | NO_GUIDE_HIT |
| Adult | Brazzers Rated 2 | custom.24-7-xxx-brazzers-rated-2 | - | NO_GUIDE_HIT |
| Adult | Brazzzers 1 | custom.24-7-xxx-brazzzers-1 | - | NO_GUIDE_HIT |
| Adult | Brazzzers 2 | custom.24-7-xxx-brazzzers-2 | - | NO_GUIDE_HIT |
| Adult | Brazzzers 3 | custom.24-7-xxx-brazzzers-3 | - | NO_GUIDE_HIT |
| Adult | Bridgette B | custom.24-7-xxx-bridgette-b | - | NO_GUIDE_HIT |
| Adult | Brunette | custom.brunette | - | NO_GUIDE_HIT |
| Adult | Casting Couch | custom.24-7-xxx-casting-couch | - | NO_GUIDE_HIT |
| Adult | Cathy Heaven | custom.24-7-xxx-cathy-heaven | - | NO_GUIDE_HIT |
| Adult | Cherie Deville | custom.24-7-xxx-cherie-deville | - | NO_GUIDE_HIT |
| Adult | Compilation | custom.xxx-compilation | - | NO_GUIDE_HIT |
| Adult | Cuckold | custom.cuckold | - | NO_GUIDE_HIT |
| Adult | Cum Perfection | custom.xxx-cum-perfection | - | NO_GUIDE_HIT |
| Adult | Day With A Pornstar | custom.xxx-day-with-a-pornstar | - | NO_GUIDE_HIT |
| Adult | Dee Williams | custom.24-7-xxx-dee-williams | - | NO_GUIDE_HIT |
| Adult | Dorcel Club | custom.xxx-dorcel-club | - | NO_GUIDE_HIT |
| Adult | Ebony | custom.24-7-xxx-ebony | - | NO_GUIDE_HIT |
| Adult | Elsa Jean | custom.24-7-xxx-elsa-jean | - | NO_GUIDE_HIT |
| Adult | Erox XXX | custom.xxx-erox-xxx-hd | - | NO_GUIDE_HIT |
| Adult | Euro Girls On Girls | custom.xxx-euro-girls-on-girls | - | NO_GUIDE_HIT |
| Adult | Evil Angel | custom.24-7-xxx-evil-angel | - | NO_GUIDE_HIT |
| Adult | Evolved Fights | custom.xxx-evolved-fights | - | NO_GUIDE_HIT |
| Adult | Exxxotica TV | custom.exxxotica-tv | - | NO_GUIDE_HIT |
| Adult | Fake Taxi 1 | custom.24-7-xxx-fake-taxi-1 | - | NO_GUIDE_HIT |
| Adult | Fake Taxi 3 | custom.24-7-xxx-fake-taxi-3 | - | NO_GUIDE_HIT |
| Adult | Fap TV 6 | custom.fap-tv-6 | - | NO_GUIDE_HIT |
| Adult | Fetish | custom.xxx-fetish | - | NO_GUIDE_HIT |
| Adult | Gangbang | custom.xxx-gangbang | - | NO_GUIDE_HIT |
| Adult | Gay 2 | custom.24-7-xxx-gay-2 | - | NO_GUIDE_HIT |
| Adult | Gay 3 | custom.24-7-xxx-gay-3 | - | NO_GUIDE_HIT |
| Adult | Gay Latin | custom.24-7-xxx-gay-latin | - | NO_GUIDE_HIT |
| Adult | Gloryhole | custom.24-7-xxx-gloryhole | - | NO_GUIDE_HIT |
| Adult | Group | custom.24-7-xxx-group | - | NO_GUIDE_HIT |
| Adult | Group 2 | custom.24-7-xxx-group-2 | - | NO_GUIDE_HIT |
| Adult | Hardcore | custom.24-7-xxx-hardcore | - | NO_GUIDE_HIT |
| Adult | Hilary Scott | custom.24-7-xxx-hilary-scott | - | NO_GUIDE_HIT |
| Adult | Holly Hendrix | custom.24-7-xxx-holly-hendrix | - | NO_GUIDE_HIT |
| Adult | Hookup Hotshot | custom.xxx-hookup-hotshot | - | NO_GUIDE_HIT |
| Adult | Hot Guys Fuck | custom.xxx-hot-guys-fuck | - | NO_GUIDE_HIT |
| Adult | Interracial | custom.xxx-interracial | - | NO_GUIDE_HIT |
| Adult | Jada Stevens | custom.24-7-xxx-jada-stevens | - | NO_GUIDE_HIT |
| Adult | Jasmine Jae | custom.24-7-xxx-jasmine-jae | - | NO_GUIDE_HIT |
| Adult | Karma RX | custom.24-7-xxx-karma-rx | - | NO_GUIDE_HIT |
| Adult | Kelly Divine | custom.24-7-xxx-kelly-divine | - | NO_GUIDE_HIT |
| Adult | Kelsie Monroe | custom.24-7-xxx-kelsie-monroe | - | NO_GUIDE_HIT |
| Adult | Kenzie Reeves | custom.24-7-xxx-kenzie-reeves | - | NO_GUIDE_HIT |
| Adult | Latina | Latina.pe | - | NO_GUIDE_HIT |
| Adult | Latina | custom.xxx-latina | - | NO_GUIDE_HIT |
| Adult | Lesbian | custom.xxx-lesbian | - | NO_GUIDE_HIT |
| Adult | Lisa Ann | custom.24-7-xxx-lisa-ann | - | NO_GUIDE_HIT |
| Adult | Live Cams | custom.live-cams | - | NO_GUIDE_HIT |
| Adult | London Keyes | custom.24-7-xxx-london-keyes | - | NO_GUIDE_HIT |
| Adult | Luna Star | custom.24-7-xxx-luna-star | - | NO_GUIDE_HIT |
| Adult | m3u.Com Anal | custom.adultm3u-com-anal | - | NO_GUIDE_HIT |
| Adult | m3u.Com Asian | custom.adultm3u-com-asian | - | NO_GUIDE_HIT |
| Adult | m3u.Com Big Ass | custom.adultm3u-com-big-ass | - | NO_GUIDE_HIT |
| Adult | m3u.Com Big Dick | custom.adultm3u-com-big-dick | - | NO_GUIDE_HIT |
| Adult | m3u.Com Big Tits | custom.adultm3u-com-big-tits | - | NO_GUIDE_HIT |
| Adult | m3u.Com Blonde | custom.adultm3u-com-blonde | - | NO_GUIDE_HIT |
| Adult | m3u.Com Blowjob | custom.adultm3u-com-blowjob | - | NO_GUIDE_HIT |
| Adult | m3u.Com Brunette | custom.adultm3u-com-brunette | - | NO_GUIDE_HIT |
| Adult | m3u.Com Compilation | custom.adultm3u-com-compilation | - | NO_GUIDE_HIT |
| Adult | m3u.Com Cuckold | custom.adultm3u-com-cuckold | - | NO_GUIDE_HIT |
| Adult | m3u.Com Fetish | custom.adultm3u-com-fetish | - | NO_GUIDE_HIT |
| Adult | m3u.Com Gangbang | custom.adultm3u-com-gangbang | - | NO_GUIDE_HIT |
| Adult | m3u.Com Hardcore | custom.adultm3u-com-hardcore | - | NO_GUIDE_HIT |
| Adult | m3u.Com Interracial | custom.adultm3u-com-interracial | - | NO_GUIDE_HIT |
| Adult | m3u.Com Latina | custom.adultm3u-com-latina | - | NO_GUIDE_HIT |
| Adult | m3u.Com Lesbian | custom.adultm3u-com-lesbian | - | NO_GUIDE_HIT |
| Adult | m3u.Com Live Cams | custom.adultm3u-com-live-cams | - | NO_GUIDE_HIT |
| Adult | m3u.Com Pornstar | custom.adultm3u-com-pornstar | - | NO_GUIDE_HIT |
| Adult | m3u.Com Pov | custom.adultm3u-com-pov | - | NO_GUIDE_HIT |
| Adult | m3u.Com Rough | custom.adultm3u-com-rough | - | NO_GUIDE_HIT |
| Adult | m3u.Com Russian | custom.adultm3u-com-russian | - | NO_GUIDE_HIT |
| Adult | m3u.Com Threesome | custom.adultm3u-com-threesome | - | NO_GUIDE_HIT |
| Adult | Mature | custom.24-7-xxx-mature | - | NO_GUIDE_HIT |
| Adult | Mctv Big Dick | custom.xxx-mctv-big-dick | - | NO_GUIDE_HIT |
| Adult | Mctv Big Tits | custom.xxx-mctv-big-tits | - | NO_GUIDE_HIT |
| Adult | Mctv Pornstar | custom.xxx-mctv-pornstar | - | NO_GUIDE_HIT |
| Adult | Mctv Rough | custom.xxx-mctv-rough | - | NO_GUIDE_HIT |
| Adult | Mia Khalifa | custom.24-7-xxx-mia-khalifa | - | NO_GUIDE_HIT |
| Adult | Milf | custom.adultm3u-com-milf | - | NO_GUIDE_HIT |
| Adult | Milfs | custom.24-7-xxx-milfs | - | NO_GUIDE_HIT |
| Adult | Milfs Stepmom | custom.24-7-xxx-milfs-stepmom | - | NO_GUIDE_HIT |
| Adult | Mom Lovers | custom.24-7-xxx-mom-lovers | - | NO_GUIDE_HIT |
| Adult | My Daughter's Hot Friend | custom.xxx-my-daughter-s-hot-friend | - | NO_GUIDE_HIT |
| Adult | My Dirty Maid | custom.24-7-xxx-my-dirty-maid | - | NO_GUIDE_HIT |
| Adult | My FIrst Sex Teacher | custom.24-7-xxx-my-first-sex-teacher | - | NO_GUIDE_HIT |
| Adult | My Friends Hot Mom | custom.24-7-xxx-my-friends-hot-mom | - | NO_GUIDE_HIT |
| Adult | MyCam TV Anal | MyCamTVAnal.cy | - | NO_GUIDE_HIT |
| Adult | MyCam TV Blowjob | MyCamTVBlowjob.cy | - | NO_GUIDE_HIT |
| Adult | MyCam TV MILF | MyCamTVMILF.cy | - | NO_GUIDE_HIT |
| Adult | Mycamtv Arab Girls | custom.mycamtv-arab-girls | - | NO_GUIDE_HIT |
| Adult | Mycamtv Asian Girls | custom.mycamtv-asian-girls | - | NO_GUIDE_HIT |
| Adult | Mycamtv Big Ass Girls | custom.mycamtv-big-ass-girls | - | NO_GUIDE_HIT |
| Adult | Mycamtv Blonde Girls | custom.mycamtv-blonde-girls | - | NO_GUIDE_HIT |
| Adult | Mycamtv Brunette Girls | custom.mycamtv-brunette-girls | - | NO_GUIDE_HIT |
| Adult | Mycamtv Ebony Girls | custom.mycamtv-ebony-girls | - | NO_GUIDE_HIT |
| Adult | Mycamtv Girls Squirt | custom.mycamtv-girls-squirt | - | NO_GUIDE_HIT |
| Adult | Mycamtv Latina Girls | custom.mycamtv-latina-girls | - | NO_GUIDE_HIT |
| Adult | Mycamtv Mature | custom.mycamtv-mature | - | NO_GUIDE_HIT |
| Adult | Mycamtv Medium Girls | custom.mycamtv-medium-girls | - | NO_GUIDE_HIT |
| Adult | Mycamtv Skinny Girls | custom.mycamtv-skinny-girls | - | NO_GUIDE_HIT |
| Adult | Mycamtv White Girls | custom.mycamtv-white-girls | - | NO_GUIDE_HIT |
| Adult | Naughty America | custom.xxx-naughty-america | - | NO_GUIDE_HIT |
| Adult | Nicole Doshi | custom.24-7-xxx-nicole-doshi | - | NO_GUIDE_HIT |
| Adult | Nicolette Shea | custom.24-7-xxx-nicolette-shea | - | NO_GUIDE_HIT |
| Adult | Nina Elle | custom.24-7-xxx-nina-elle | - | NO_GUIDE_HIT |
| Adult | O LA LA | custom.xxx-o-la-la | - | NO_GUIDE_HIT |
| Adult | Only Fans Jade Bunny | custom.24-7-xxx-only-fans-jade-bunny | - | NO_GUIDE_HIT |
| Adult | Penthouse After Midnight | PenthouseAfterMidnight.us | - | NO_GUIDE_HIT |
| Adult | Penthouse Black | PenthouseBlack.us | - | NO_GUIDE_HIT |
| Adult | Penthouse Naughty Nights | PenthouseNaughtyNights.us | - | NO_GUIDE_HIT |
| Adult | Penthouse Passion | PenthousePassion.us | - | NO_GUIDE_HIT |
| Adult | Penthouse Reality TV | PenthouseRealityTV.us | - | NO_GUIDE_HIT |
| Adult | Penthouse TV | custom.penthouse-tv | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 1 | custom.pink-erotic-1 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 2 | custom.xxx-pink-erotic-2 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 3 | custom.xxx-pink-erotic-3 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 4 | custom.xxx-pink-erotic-4 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 5 | custom.xxx-pink-erotic-5 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 6 | custom.xxx-pink-erotic-6 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 7 | custom.xxx-pink-erotic-7 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 8 | custom.xxx-pink-erotic-8 | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: BAEB | custom.pornbox-4k-baeb | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: BBC PIE | custom.pornbox-4k-bbc-pie | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: CUM | custom.pornbox-4k-cum-4k | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: GIRL CUM | custom.pornbox-4k-girl-cum | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: JAYS POV | custom.pornbox-4k-jays-pov | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: LUBED PORN | custom.pornbox-4k-lubed-porn | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: NANNY SPY | custom.pornbox-4k-nanny-spy | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: SPANK MONSTER | custom.pornbox-4k-spank-monster | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: SPY FAM | custom.pornbox-4k-spy-fam | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: TINY | custom.pornbox-4k-tiny-4k | - | NO_GUIDE_HIT |
| Adult | PORNBOX GAY: BEEFCAKE HUNTER | custom.pornbox-gay-beefcake-hunter | - | NO_GUIDE_HIT |
| Adult | PORNBOX GAY: BOY FUN | custom.pornbox-gay-boy-fun | - | NO_GUIDE_HIT |
| Adult | PORNBOX GAY: MAN | custom.pornbox-gay-man | - | NO_GUIDE_HIT |
| Adult | PORNBOX: 1111 CUSTOMS | custom.pornbox-1111-customs | - | NO_GUIDE_HIT |
| Adult | PORNBOX: ADULT TIME | custom.pornbox-adult-time | - | NO_GUIDE_HIT |
| Adult | PORNBOX: ALEX LEGEND | custom.pornbox-alex-legend | - | NO_GUIDE_HIT |
| Adult | PORNBOX: ALL GROUP SEX | custom.pornbox-all-group-sex | - | NO_GUIDE_HIT |
| Adult | PORNBOX: AMATEUR EURO | custom.pornbox-amateur-euro | - | NO_GUIDE_HIT |
| Adult | PORNBOX: ASIAN FOOTJOB | custom.pornbox-asian-footjob | - | NO_GUIDE_HIT |
| Adult | PORNBOX: ATK GIRLFRIENDS | custom.pornbox-atk-girlfriends | - | NO_GUIDE_HIT |
| Adult | PORNBOX: AV TAXI | custom.pornbox-av-taxi | - | NO_GUIDE_HIT |
| Adult | PORNBOX: BABES | custom.pornbox-babes | - | NO_GUIDE_HIT |
| Adult | PORNBOX: BANG BROS NETWORK | custom.pornbox-bang-bros-network | - | NO_GUIDE_HIT |
| Adult | PORNBOX: BIG BOOTY CITY | custom.pornbox-big-booty-city | - | NO_GUIDE_HIT |
| Adult | PORNBOX: BLACKED | custom.pornbox-blacked | - | NO_GUIDE_HIT |
| Adult | PORNBOX: BLOW ME POV | custom.pornbox-blow-me-pov | - | NO_GUIDE_HIT |
| Adult | PORNBOX: BOX OF PORN | custom.pornbox-box-of-porn | - | NO_GUIDE_HIT |
| Adult | PORNBOX: BRATTY SIS | custom.pornbox-bratty-sis | - | NO_GUIDE_HIT |
| Adult | PORNBOX: BRAZZERS | custom.pornbox-brazzers | - | NO_GUIDE_HIT |
| Adult | PORNBOX: BUMS BUS | custom.pornbox-bums-bus | - | NO_GUIDE_HIT |
| Adult | PORNBOX: CASTING COUCH | custom.pornbox-casting-couch | - | NO_GUIDE_HIT |
| Adult | PORNBOX: DAGFS | custom.pornbox-dagfs | - | NO_GUIDE_HIT |
| Adult | PORNBOX: DDF BUSTY | custom.pornbox-ddf-busty | - | NO_GUIDE_HIT |
| Adult | PORNBOX: DEEPER | custom.pornbox-deeper | - | NO_GUIDE_HIT |
| Adult | PORNBOX: DIGITAL PLAYGROUND | custom.pornbox-digital-playground | - | NO_GUIDE_HIT |
| Adult | PORNBOX: DOG HOUSE | custom.pornbox-dog-house | - | NO_GUIDE_HIT |
| Adult | PORNBOX: DOGFART NETWORK | custom.pornbox-dogfart-network | - | NO_GUIDE_HIT |
| Adult | PORNBOX: DORCEL CLUB | custom.pornbox-dorcel-club | - | NO_GUIDE_HIT |
| Adult | PORNBOX: DREAMROOM | custom.pornbox-dreamroom | - | NO_GUIDE_HIT |
| Adult | PORNBOX: EXOTIC | custom.pornbox-exotic | - | NO_GUIDE_HIT |
| Adult | PORNBOX: FAKE HOSTEL | custom.pornbox-fake-hostel | - | NO_GUIDE_HIT |
| Adult | PORNBOX: FAKE TAXI | custom.pornbox-fake-taxi | - | NO_GUIDE_HIT |
| Adult | PORNBOX: FAMILY STROKES | custom.pornbox-family-strokes | - | NO_GUIDE_HIT |
| Adult | PORNBOX: FAMILY SWAP XXX | custom.pornbox-family-swap-xxx | - | NO_GUIDE_HIT |
| Adult | PORNBOX: FAPADOO | custom.pornbox-fapadoo | - | NO_GUIDE_HIT |
| Adult | PORNBOX: FILTHY KINGS | custom.pornbox-filthy-kings | - | NO_GUIDE_HIT |
| Adult | PORNBOX: FIRST ANAL QUEST | custom.pornbox-first-anal-quest | - | NO_GUIDE_HIT |
| Adult | PORNBOX: FIRST CLASS POV | custom.pornbox-first-class-pov | - | NO_GUIDE_HIT |
| Adult | PORNBOX: FIT 18 | custom.pornbox-fit-18 | - | NO_GUIDE_HIT |
| Adult | PORNBOX: GANGBANG CREAMPIE | custom.pornbox-gangbang-creampie | - | NO_GUIDE_HIT |
| Adult | PORNBOX: GOTMYLF | custom.pornbox-gotmylf | - | NO_GUIDE_HIT |
| Adult | PORNBOX: HENTAINED | custom.pornbox-hentained | - | NO_GUIDE_HIT |
| Adult | PORNBOX: HER LIMIT | custom.pornbox-her-limit | - | NO_GUIDE_HIT |
| Adult | PORNBOX: HOLED | custom.pornbox-holed | - | NO_GUIDE_HIT |
| Adult | PORNBOX: HORNY DREAM BABEZ | custom.pornbox-horny-dream-babez | - | NO_GUIDE_HIT |
| Adult | PORNBOX: HORNY HOSTEL | custom.pornbox-horny-hostel | - | NO_GUIDE_HIT |
| Adult | PORNBOX: HOT WIFE XXX | custom.pornbox-hot-wife-xxx | - | NO_GUIDE_HIT |
| Adult | PORNBOX: HUSSIE PASS | custom.pornbox-hussie-pass | - | NO_GUIDE_HIT |
| Adult | PORNBOX: INTERRACIAL PASS | custom.pornbox-interracial-pass | - | NO_GUIDE_HIT |
| Adult | PORNBOX: JOI BABES | custom.pornbox-joi-babes | - | NO_GUIDE_HIT |
| Adult | PORNBOX: KINKY FAMILY | custom.pornbox-kinky-family | - | NO_GUIDE_HIT |
| Adult | PORNBOX: KINKY INLAWS | custom.pornbox-kinky-inlaws | - | NO_GUIDE_HIT |
| Adult | PORNBOX: KINKY SPA | custom.pornbox-kinky-spa | - | NO_GUIDE_HIT |
| Adult | PORNBOX: LETHAL TEENS | custom.pornbox-lethal-teens | - | NO_GUIDE_HIT |
| Adult | PORNBOX: LETS DOE IT | custom.pornbox-lets-doe-it | - | NO_GUIDE_HIT |
| Adult | PORNBOX: LIFE SELECTOR | custom.pornbox-life-selector | - | NO_GUIDE_HIT |
| Adult | PORNBOX: LOVE HER FEET | custom.pornbox-love-her-feet | - | NO_GUIDE_HIT |
| Adult | PORNBOX: LOVE HOME PORN | custom.pornbox-love-home-porn | - | NO_GUIDE_HIT |
| Adult | PORNBOX: LUBED | custom.pornbox-lubed | - | NO_GUIDE_HIT |
| Adult | PORNBOX: LW PRODUCTIONS | custom.pornbox-lw-productions | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MAMACITAZ | custom.pornbox-mamacitaz | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MANO JOB | custom.pornbox-mano-job | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MASSAGE ROOMS | custom.pornbox-massage-rooms | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MAX J | custom.pornbox-max-j | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MOFOS | custom.pornbox-mofos | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MOM TEACH SEX | custom.pornbox-mom-teach-sex | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MOM XXX | custom.pornbox-mom-xxx | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MY 18 TEENS | custom.pornbox-my-18-teens | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MY DIRTY HOBBY | custom.pornbox-my-dirty-hobby | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MY FAMILY PIES | custom.pornbox-my-family-pies | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MY LIFE IN MIAMI | custom.pornbox-my-life-in-miami | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MY PERVY FAMILY | custom.pornbox-my-pervy-family | - | NO_GUIDE_HIT |
| Adult | PORNBOX: MYLF | custom.pornbox-mylf | - | NO_GUIDE_HIT |
| Adult | PORNBOX: NEW SENSATIONS | custom.pornbox-new-sensations | - | NO_GUIDE_HIT |
| Adult | PORNBOX: NF BUSTY | custom.pornbox-nf-busty | - | NO_GUIDE_HIT |
| Adult | PORNBOX: NUBILE FILMS | custom.pornbox-nubile-films | - | NO_GUIDE_HIT |
| Adult | PORNBOX: PASSION | custom.pornbox-passion | - | NO_GUIDE_HIT |
| Adult | PORNBOX: PERV CITY | custom.pornbox-perv-city | - | NO_GUIDE_HIT |
| Adult | PORNBOX: PERV MOM | custom.pornbox-perv-mom | - | NO_GUIDE_HIT |
| Adult | PORNBOX: POOKSI | custom.pornbox-pooksi | - | NO_GUIDE_HIT |
| Adult | PORNBOX: PORN WORLD HARDCORE | custom.pornbox-porn-world-hardcore | - | NO_GUIDE_HIT |
| Adult | PORNBOX: PORNHOCHIC | custom.pornbox-pornhochic | - | NO_GUIDE_HIT |
| Adult | PORNBOX: POV MASTERS | custom.pornbox-pov-masters | - | NO_GUIDE_HIT |
| Adult | PORNBOX: PRIVATE | custom.pornbox-private | - | NO_GUIDE_HIT |
| Adult | PORNBOX: PRIVATE SOCIETY | custom.pornbox-private-society | - | NO_GUIDE_HIT |
| Adult | PORNBOX: PUBA | custom.pornbox-puba | - | NO_GUIDE_HIT |
| Adult | PORNBOX: PUBLIC AGENT | custom.pornbox-public-agent | - | NO_GUIDE_HIT |
| Adult | PORNBOX: PURE MATURE | custom.pornbox-pure-mature | - | NO_GUIDE_HIT |
| Adult | PORNBOX: RAW ATTACK | custom.pornbox-raw-attack | - | NO_GUIDE_HIT |
| Adult | PORNBOX: REALITY JUNKIES | custom.pornbox-reality-junkies | - | NO_GUIDE_HIT |
| Adult | PORNBOX: REALITY KINGS | custom.pornbox-reality-kings | - | NO_GUIDE_HIT |
| Adult | PORNBOX: SHAGGING MOMS | custom.pornbox-shagging-moms | - | NO_GUIDE_HIT |
| Adult | PORNBOX: SHE IS NERDY | custom.pornbox-she-is-nerdy | - | NO_GUIDE_HIT |
| Adult | PORNBOX: SLIM | custom.pornbox-slim | - | NO_GUIDE_HIT |
| Adult | PORNBOX: SOFIE MARIE XXX | custom.pornbox-sofie-marie-xxx | - | NO_GUIDE_HIT |
| Adult | PORNBOX: STROKIES | custom.pornbox-strokies | - | NO_GUIDE_HIT |
| Adult | PORNBOX: SUGAR BABES TV | custom.pornbox-sugar-babes-tv | - | NO_GUIDE_HIT |
| Adult | PORNBOX: SWEET SINNER | custom.pornbox-sweet-sinner | - | NO_GUIDE_HIT |
| Adult | PORNBOX: SWEETHEART PORN | custom.pornbox-sweetheart-porn | - | NO_GUIDE_HIT |
| Adult | PORNBOX: THE WHITE BOXXX | custom.pornbox-the-white-boxxx | - | NO_GUIDE_HIT |
| Adult | PORNBOX: TRUE AMATEURS | custom.pornbox-true-amateurs | - | NO_GUIDE_HIT |
| Adult | PORNBOX: TWISTY | custom.pornbox-twisty | - | NO_GUIDE_HIT |
| Adult | Pornstar | custom.xxx-pornstar | - | NO_GUIDE_HIT |
| Adult | POV | custom.xxx-pov | - | NO_GUIDE_HIT |
| Adult | Princess Cum | custom.xxx-princess-cum | - | NO_GUIDE_HIT |
| Adult | Pure Babes | PureBabes.us | - | NO_GUIDE_HIT |
| Adult | Pure Taboo | custom.24-7-xxx-pure-taboo | - | NO_GUIDE_HIT |
| Adult | Rated | custom.24-7-xxx-rated | - | NO_GUIDE_HIT |
| Adult | Rated 3 | custom.24-7-xxx-rated-3 | - | NO_GUIDE_HIT |
| Adult | Real Wife Stories | custom.xxx-real-wife-stories | - | NO_GUIDE_HIT |
| Adult | Riley Reid | custom.24-7-xxx-riley-reid | - | NO_GUIDE_HIT |
| Adult | Rough | custom.xxx-rough | - | NO_GUIDE_HIT |
| Adult | Russian | custom.xxx-russian | - | NO_GUIDE_HIT |
| Adult | Russian Night | custom.xxx-russian-night | - | NO_GUIDE_HIT |
| Adult | Sexto Sento | custom.xxx-sexto-sento | - | NO_GUIDE_HIT |
| Adult | ShopLyfter | custom.24-7-xxx-shoplyfter | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: ABELLA DANGER | custom.stars-exclusive-abella-danger | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: ADRIANA CHECHIK | custom.stars-exclusive-adriana-chechik | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: ALINA LOPEZ | custom.stars-exclusive-alina-lopez | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: ANGELA WHITE | custom.stars-exclusive-angela-white | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: ARIANA MARIE | custom.stars-exclusive-ariana-marie | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: AUGUST AMES | custom.stars-exclusive-august-ames | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: AUTUMN FALLS | custom.stars-exclusive-autumn-falls | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: BLAKE BLOSSOM | custom.stars-exclusive-blake-blossom | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: BRANDI LOVE | custom.stars-exclusive-brandi-love | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: DANI DANIELS | custom.stars-exclusive-dani-daniels | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: ELSA JEAN | custom.stars-exclusive-elsa-jean | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: EMILY WILLIS | custom.stars-exclusive-emily-willis | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: EVA LOVIA | custom.stars-exclusive-eva-lovia | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: GINA VALENTINA | custom.stars-exclusive-gina-valentina | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: JESSA RHODES | custom.stars-exclusive-jessa-rhodes | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: LANA RHOADES | custom.stars-exclusive-lana-rhoades | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: LENA PAUL | custom.stars-exclusive-lena-paul | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: LISA ANN | custom.stars-exclusive-lisa-ann | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: MADISON IVY | custom.stars-exclusive-madison-ivy | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: MIA MALKOVA | custom.stars-exclusive-mia-malkova | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: NICOLE ANISTON | custom.stars-exclusive-nicole-aniston | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: RILEY REID | custom.stars-exclusive-riley-reid | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: UMA JOLIE | custom.stars-exclusive-uma-jolie | - | NO_GUIDE_HIT |
| Adult | STARS EXCLUSIVE: VALENTINA NAPPI | custom.stars-exclusive-valentina-nappi | - | NO_GUIDE_HIT |
| Adult | Strap on | custom.24-7-xxx-strap-on | - | NO_GUIDE_HIT |
| Adult | Swallowed | custom.24-7-xxx-swallowed | - | NO_GUIDE_HIT |
| Adult | Teen Red TV | custom.xxx-teen-red-tv | - | NO_GUIDE_HIT |
| Adult | Threesome | custom.xxx-threesome | - | NO_GUIDE_HIT |
| Adult | Tiny | custom.xxx-tiny-4k | - | NO_GUIDE_HIT |
| Adult | Trans | custom.24-7-xxx-trans | - | NO_GUIDE_HIT |
| Adult | True Anal | custom.24-7-xxx-true-anal | - | NO_GUIDE_HIT |
| Adult | Uniform | custom.24-7-xxx-uniform | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: BIGTITTYGOTHEGG | custom.verified-amateurs-bigtittygothegg | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: CARLACUTE | custom.verified-amateurs-carlacute | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: CHERRY GRACE | custom.verified-amateurs-cherry-grace | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: CHESSIE RAE | custom.verified-amateurs-chessie-rae | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: DIANA DANIELS | custom.verified-amateurs-diana-daniels | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: ELLA KOJIRO | custom.verified-amateurs-ella-kojiro | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: KRISS KISS | custom.verified-amateurs-kriss-kiss | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: LEAH MEOW | custom.verified-amateurs-leah-meow | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: LUXURYGIRL | custom.verified-amateurs-luxurygirl | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: MIKANIKA69 | custom.verified-amateurs-mikanika69 | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: MINI DIVA | custom.verified-amateurs-mini-diva | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: MOLLYREDWOLF | custom.verified-amateurs-mollyredwolf | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: NOFACEGIRL | custom.verified-amateurs-nofacegirl | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: NOTSOAMATEUR | custom.verified-amateurs-notsoamateur | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: NYNA FERRAGNI | custom.verified-amateurs-nyna-ferragni | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: PAMSNUSNU | custom.verified-amateurs-pamsnusnu | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: PURPLE BITCH | custom.verified-amateurs-purple-bitch | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: REISLIN | custom.verified-amateurs-reislin | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: SECRETCRUSH | custom.verified-amateurs-secretcrush | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: SHAIDEN ROUGE | custom.verified-amateurs-shaiden-rouge | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: SOLAZOLA | custom.verified-amateurs-solazola | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: TESSA WINTERS | custom.verified-amateurs-tessa-winters | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: TINNA ANGEL | custom.verified-amateurs-tinna-angel | - | NO_GUIDE_HIT |
| Adult | VERIFIED AMATEURS: YINYLEON | custom.verified-amateurs-yinyleon | - | NO_GUIDE_HIT |
| Adult | Veronica Avluv | custom.24-7-xxx-veronica-avluv | - | NO_GUIDE_HIT |
| Adult | Violet Myers | custom.24-7-xxx-violet-myers | - | NO_GUIDE_HIT |
| Adult | Vivid TV Europe | VividTVEurope.uk | - | NO_GUIDE_HIT |
| Adult | Vixen | custom.vixen | - | NO_GUIDE_HIT |
| Adult | Wank It Now | custom.xxx-wank-it-now | - | NO_GUIDE_HIT |
| Adult | Xy Max | custom.xxx-xy-max | - | NO_GUIDE_HIT |
| Argentina | Cosmos Tv | CosmosTv.ar@HD | US2900025U8 | MAPPED_NOT_CURRENTLY_FOUND |
| Argentina | Allegro | AllegroHD.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Azahares Radiovisual Multimedia | AzaharesRadiovisualMultimedia.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Chamame TV | ChamameTV.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Cumbia Mix | CumbiaMix.ar@HD | - | NO_GUIDE_HIT |
| Argentina | HTV Argentina | HTV.us@Argentina | - | NO_GUIDE_HIT |
| Argentina | La 100 | La100.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Quiero Musica en mi Idioma | QuieroMusicaenmiIdioma.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Retroclub | custom.retroclub-ar-music | - | NO_GUIDE_HIT |
| Argentina | Rock & Pop | RockPop.ar@SD | - | NO_GUIDE_HIT |
| Argentina | X Level Media | XLevelMedia.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Xtrema Accion | XtremaAccion.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Xtrema Cine Clasico | XtremaCineClasico.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Xtrema Terror | XtremaTerror.ar@SD | - | NO_GUIDE_HIT |
| Bangladesh | Maasranga TV | MaasrangaTV.bd | MaasrangaTV.bd | MAPPED_NOT_CURRENTLY_FOUND |
| Bangladesh | RTV | RTV.bd | RTV.bd | MAPPED_NOT_CURRENTLY_FOUND |
| Bangladesh | Ananda TV | AnandaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Asian TV | AsianTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | ATN Bangla | ATNBangla.bd | - | NO_GUIDE_HIT |
| Bangladesh | ATN News | ATNNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ayna TV | custom.bdix.ayna-tv | - | NO_GUIDE_HIT |
| Bangladesh | Bangla TV | BanglaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bangla Vision | BanglaVision.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bijoy TV | BijoyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Boishakhi TV | BoishakhiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV Chattogram | BTVChattogram.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 1 | Channel1.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 16 | Channel16.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 24 | Channel24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 52 | Channel52.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 9 | Channel9.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel Europe | ChannelEurope.uk | - | NO_GUIDE_HIT |
| Bangladesh | Channel I | ChannelI.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel S | ChannelS.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | Channel S | ChannelS.uk | - | NO_GUIDE_HIT |
| Bangladesh | Channel S UK | ChannelS.uk@679aa9 | - | NO_GUIDE_HIT |
| Bangladesh | DBC News | DBCNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Deepto TV | DeeptoTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Desh TV | DeshTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Deshe Bideshe | DesheBideshe.ca | - | NO_GUIDE_HIT |
| Bangladesh | Deshi TV | DeshiTV.ca@SD | - | NO_GUIDE_HIT |
| Bangladesh | Doyel TV | DoyelTV.ca@SD | - | NO_GUIDE_HIT |
| Bangladesh | Duronto TV | DurontoTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | Ekattor TV | EkattorTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekhon TV | EkhonTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekushey TV | EkusheyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Enter TV | EnterTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | G Series Drama | GSeriesDrama.bd | - | NO_GUIDE_HIT |
| Bangladesh | G TV | GaziTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | GAZI TV | GaziTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | Global TV | GlobalTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jago News 24 | JagoNews24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jalsha Bangla BD | JalshaBanglaBD.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jamuna TV | JamunaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jonmobhumi TV | JonmobhumiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Matribhumi TV | MatribhumiTV.bd@HD | - | NO_GUIDE_HIT |
| Bangladesh | ME TV | METV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Mohona TV | MohonaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Movie Bangla | MovieBangla.bd | - | NO_GUIDE_HIT |
| Bangladesh | Movie Bangla | MovieBangla.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | MUSIC BANGLA | MUSICBANGLA | - | NO_GUIDE_HIT |
| Bangladesh | My TV | MyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Nagorik TV | NagorikTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | NAN TV | NANTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | NEWS 21 BANGLA | custom.bdix.news21-bangla | - | NO_GUIDE_HIT |
| Bangladesh | News 24 | News24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Nexus TV | NexusTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Nexus TV | NexusTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | NRB | custom.bdix.nrb-hd | - | NO_GUIDE_HIT |
| Bangladesh | NRB TV | NRBTV.ca | - | NO_GUIDE_HIT |
| Bangladesh | NTV | NTV-IN | - | NO_GUIDE_HIT |
| Bangladesh | NTV | NTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Probashi TV | ProbashiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Rajdhani TV | RajdhaniTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Rajdhani TV | custom.rajdhani | - | NO_GUIDE_HIT |
| Bangladesh | Rupashi Bangla TV | RupashiBanglaTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | SA TV | SATV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Somoy TV | SomoyNewsTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | SRK | SRK.bd | - | NO_GUIDE_HIT |
| Bangladesh | TBN24 | TBN24.us | - | NO_GUIDE_HIT |
| Bangladesh | Thikana | ThikanaTV.us | - | NO_GUIDE_HIT |
| Bangladesh | Time Television | TimeTelevision.us | - | NO_GUIDE_HIT |
| Brazil | +MaisUm | PlusMaisUm.br@HD | - | NO_GUIDE_HIT |
| Brazil | AMC Latin America Brazil | AMCLatinAmerica.us@Brazil | - | NO_GUIDE_HIT |
| Brazil | CINDIE TV | CINDIETV.br@HD | - | NO_GUIDE_HIT |
| Brazil | Classique TV | ClassiqueTV.br@SD | - | NO_GUIDE_HIT |
| Brazil | Lamore Rock Show WebTV | LamoreRockShowWebTV.br@SD | - | NO_GUIDE_HIT |
| Brazil | Rádio Temas de Novelas | custom.radio-temas-de-novelas-br-music | - | NO_GUIDE_HIT |
| Bulgaria | BOX TV | BOXTV.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | bTV Lady | bTVLady.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | cine.box | cinebox.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | CineStar 1 Bulgaria | CineStar1Bulgaria.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | CineStar Action Bulgaria | CineStarActionBulgaria.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | City TV (Bulgaria) | CityTV.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | DSTV (Bulgaria) | DSTV.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | FILMBOX+ Emotion Bulgaria | FILMBOXPlusEmotion.pl@Bulgaria | - | NO_GUIDE_HIT |
| Bulgaria | FILMBOX+ Love & Crime Bulgaria | FILMBOXPlusLoveCrime.pl@Bulgaria | - | NO_GUIDE_HIT |
| Bulgaria | FILMBOX+ One Bulgaria | FILMBOXPlusOne.pl@Bulgaria | - | NO_GUIDE_HIT |
| Bulgaria | Hit Mix Music | HitMixMusic.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | Movie Star | MovieStar.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | Tiankov Folk | TiankovFolk.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | Tiankov Orient Folk | TiankovOrientFolk.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | TV1000 | TV1000.bg@SD | - | NO_GUIDE_HIT |
| Canada | Stingray Cozy Cafe | custom.stingray-cozy-cafe-ca-music | jtv3481 | MAPPED_NOT_CURRENTLY_FOUND |
| Canada | Stingray Euro Hits | custom.stingray-euro-hits-ca-music | US4700002UF | MAPPED_NOT_CURRENTLY_FOUND |
| Canada | Stingray Holidayscapes | StingrayHolidayscapes.ca@HD | USBD3500038R6 | MAPPED_NOT_CURRENTLY_FOUND |
| Canada | Stingray Romance Latino | StingrayRomanceLatino.ca@SD | USBD3500017CE | MAPPED_NOT_CURRENTLY_FOUND |
| Canada | Stingray Today's Latin Pop | StingrayTodaysLatinPop.ca@SD | USBD3500009Y3 | MAPPED_NOT_CURRENTLY_FOUND |
| Canada | ZenLIFE by Stingray | ZenLIFEbyStingray.ca@HD | USBD3500027DS | jtv3286 | MAPPED_NOT_CURRENTLY_FOUND |
| Canada | Pamir TV | PamirTV.ca@SD | - | NO_GUIDE_HIT |
| Canada | Stingray Cityscapes | custom.stingray-cityscapes-ca-music | - | NO_GUIDE_HIT |
| Canada | Stingray Everything '80s | StingrayEverything80s.ca@SD | - | NO_GUIDE_HIT |
| Canada | Stingray Holiday Hits | StingrayHolidayHits.ca@SD | - | NO_GUIDE_HIT |
| Canada | Stingray iConcerts | StingrayiConcerts.ca@HD | - | NO_GUIDE_HIT |
| Canada | Stingray Rock Alternative | StingrayRockAlternative.ca | - | NO_GUIDE_HIT |
| Canada | Stingray Urban Beat | custom.stingray-urban-beat-ca-music | - | NO_GUIDE_HIT |
| Chile | 13 Festival | 13Festival.cl@SD | - | NO_GUIDE_HIT |
| Chile | Genial TV | GenialTV.cl@SD | - | NO_GUIDE_HIT |
| Chile | La Clave | LaClave.cl@SD | - | NO_GUIDE_HIT |
| Chile | Pauta | Pauta.cl@SD | - | NO_GUIDE_HIT |
| Chile | Retromusica Television | RetromusicaTelevision.cl@SD | - | NO_GUIDE_HIT |
| Chile | Ritoque TV | RitoqueTV.cl@SD | - | NO_GUIDE_HIT |
| Chile | Sabor TV | SaborTV.cl@SD | - | NO_GUIDE_HIT |
| Chile | Sensacion Costa | SensacionCosta.cl@SD | - | NO_GUIDE_HIT |
| Chile | Solo Bailalo | SoloBailalo.cl@SD | - | NO_GUIDE_HIT |
| Chile | TCM Latin America Chile | TCMLatinAmerica.us@Chile | - | NO_GUIDE_HIT |
| Chile | V Classic TV | VClassicTV.cl@SD | - | NO_GUIDE_HIT |
| China | CCTV-Storm Music | CCTVStormMusic.cn@HD | - | NO_GUIDE_HIT |
| China | CCTV-Storm Theater | CCTVStormTheater.cn@HD | - | NO_GUIDE_HIT |
| China | CCTV-The First Theater | CCTVTheFirstTheater.cn@HD | - | NO_GUIDE_HIT |
| China | CND Film Middle School Channel | CNDFilmMiddleSchoolChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Harbin Movie Channel | HarbinMovieChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Jiangxi Movie Channel | JiangxiMovieChannel.cn@SD | - | NO_GUIDE_HIT |
| Colombia | Rumba TV | RumbaTV.co@SD | RumbaTV.co | MAPPED_NOT_CURRENTLY_FOUND |
| Colombia | Claro Musica TV | ClaroMusicaTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | Fiesta TV | FiestaTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | La Kalle | custom.la-kalle-co-music | - | NO_GUIDE_HIT |
| Colombia | Parranda Vallenata | ParrandaVallenata.co@SD | - | NO_GUIDE_HIT |
| Colombia | Radiola TV | RadiolaTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | Ranchenato TV | RanchenatoTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | Reyali | Reyali.co@SD | - | NO_GUIDE_HIT |
| Colombia | Supermusica TV | SupermusicaTV.co@SD | - | NO_GUIDE_HIT |
| Costa Rica | 88 Stereo | 88Stereo.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | Cedros TV | custom.cedros-tv-cr-music | - | NO_GUIDE_HIT |
| Costa Rica | Conexión Positiva Televisión | custom.conexion-positiva-television-cr-music | - | NO_GUIDE_HIT |
| Costa Rica | IQ Channel | IQChannel.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | Oldies Hits | custom.oldies-hits-cr-music | - | NO_GUIDE_HIT |
| Costa Rica | SOY Plancha TV | SOYPlanchaTV.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | Urbano TV | UrbanoTV.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | Vintage Music | VintageMusic.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | VM Latino | VMLatino.cr@SD | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ Comedy Czechia | FILMBOXPlusComedy.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ Emotion Czechia | FILMBOXPlusEmotion.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ Hits Czechia | FILMBOXPlusHits.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ One Czechia | FILMBOXPlusOne.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | Ocko Gold | OckoGold.cz@SD | - | NO_GUIDE_HIT |
| DO | Tarima TV | TarimaTV.do@HD | plex.tv.Tarima.TV.plex | MAPPED_NOT_CURRENTLY_FOUND |
| DO | Boreal | Boreal.do@SD | - | NO_GUIDE_HIT |
| DO | Fuego TV | FuegoTV.do@SD | - | NO_GUIDE_HIT |
| DO | Maimon TV Canal 3 | MaimonTVCanal3.do@SD | - | NO_GUIDE_HIT |
| DO | Makao TV | MakaoTV.do@SD | - | NO_GUIDE_HIT |
| DO | Mega Cine TV | MegaCineTV.do@HD | - | NO_GUIDE_HIT |
| DO | Siembra TV (Dominican Republic) | SiembraTV.do@SD | - | NO_GUIDE_HIT |
| DO | Tele Dominicana TV | TeleDominicanaTV.do@SD | - | NO_GUIDE_HIT |
| DO | Topical Moon RD | TopicalMoonRD.do@HD | - | NO_GUIDE_HIT |
| DO | TV Exitos | TVExitos.do@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | 4K Travel | Travel.us | 4K.TRAVEL.TV.distro | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Crime & Justice | CrimeJustice.us | plex.tv.Crime.&.Justice.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Crime Scene TV | CrimeSceneTV.us | IN24000030L | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | House of Crime | HouseOfCrime.us | IN4600004HW | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | InFast | INFAST.nl | INBA4900004W9 | USBA300022JX | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | InWild | INWILD.nl | INBA4900007JX | jtv3389 | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Life+Style | LifeStyle.us | IN2400001L0 | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Nature Time | NatureTime.us | IN2100014K1 | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Real Wild | RealWild.uk | RealWild.uk | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Robot Wars by Mech+ | RobotWarsByMech.us | plex.tv.Robot.Wars.by.Mech+.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Wheel World | WheelWorld.us | IN460000250 | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | WildEarth | WildEarth.za | US3800007CR | jtv2437 | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Adventure Earth | AdventureEarth.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Alone | Alone.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic Adventure Earth | AutenticAdventureEarth.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic History | AutenticHistory.de | - | NO_GUIDE_HIT |
| Documentary & Wildlife | CGTN Documentary | CGTNDocumentary.cn | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Inside Crime | InsideCrime.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Love the Planet | LoveThePlanet.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Mystery TV | MysteryTV.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Nat Geo TV | NatGeoTV.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | PBS Arts | PBSArts.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Watch Mojo | WatchMojo.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Wild Planet | WildPlanet.us | - | NO_GUIDE_HIT |
| Estonia | Best of Dance TV | BestofDanceTV.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV Algorhythm | DanceTVAlgorhythm.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV Deep House District | DanceTVDeepHouseDistrict.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV House Floor | DanceTVHouseFloor.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV Techno Warehouse | DanceTVTechnoWarehouse.ee@SD | - | NO_GUIDE_HIT |
| Estonia | Vantage Rock | VantageRock.ee@HD | - | NO_GUIDE_HIT |
| France | Trace Brazuca | TraceBrazuca.fr@HD | plex.tv.TRACE.Brazuca.plex | MAPPED_NOT_CURRENTLY_FOUND |
| France | 4 Music | 4Music.fr@SD | - | NO_GUIDE_HIT |
| France | 4Kurd | 4Kurd.fr@SD | - | NO_GUIDE_HIT |
| France | DBM TV | DBMTV.fr@SD | - | NO_GUIDE_HIT |
| France | P2M TV | P2MTV.fr@SD | - | NO_GUIDE_HIT |
| France | Persiana Cinema | PersianaCinema.fr@SD | - | NO_GUIDE_HIT |
| France | Persiana Folk | PersianaFolk.fr@HD | - | NO_GUIDE_HIT |
| France | Persiana Nostalgia | PersianaNostalgia.fr@SD | - | NO_GUIDE_HIT |
| France | Persiana SetMix | custom.persiana-setmix-fr-music | - | NO_GUIDE_HIT |
| France | Persiana Vibe | PersianaVibe.fr@HD | - | NO_GUIDE_HIT |
| France | Qwest TV Jazz & Beyond | QwestTVJazzBeyond.fr@SD | - | NO_GUIDE_HIT |
| France | ScreamIN | ScreamIN.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Afrikora | TraceAfrikora.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Ayiti | TraceAyiti.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Ivoire | TraceIvoire.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Jama | TraceJama.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Kitoko | TraceKitoko.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Mboa | TraceMboa.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Muzika | TraceMuzika.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Mziki | TraceMziki.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Naija | TraceNaija.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Ngoma | TraceNgoma.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Urban Africa Franco | TraceUrban.fr@AfricaFranco | - | NO_GUIDE_HIT |
| France | Trace Urban Caribbean And Indian Ocean | TraceUrban.fr@CaribbeanAndIndianOcean | - | NO_GUIDE_HIT |
| France | Trace Urban Southern Africa | TraceUrban.fr@SouthernAfrica | - | NO_GUIDE_HIT |
| France | Trace Vanilla Islands | TraceVanillaIslands.fr@SD | - | NO_GUIDE_HIT |
| Germany | Adria Music Television | AdriaMusicTelevision.de@SD | - | NO_GUIDE_HIT |
| Germany | Bibel TV Musik | BibelTVMusik.de@SD | - | NO_GUIDE_HIT |
| Germany | Cine 666 by Pluto TV | Cine666byPlutoTV.de@FR | - | NO_GUIDE_HIT |
| Germany | Cine Action by Pluto TV | CineActionbyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| Germany | Cine by Pluto TV | CinebyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| Germany | Cine Catastrophe by Pluto TV | CineCatastrophebyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| Germany | Cine d'Asie by Pluto TV | CinedAsiebyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| Germany | Cine Horreur by Pluto TV | CineHorreurbyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| Germany | Cine Retro by Pluto TV | CineRetrobyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| Germany | Cine Romance by Pluto TV | CineRomancebyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| Germany | Cine Sci-Fi by Pluto TV | CineSciFibyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| Germany | Cine Thrillers by Pluto TV | CineThrillersbyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| Germany | Cine Western by Pluto TV | CineWesternbyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| Germany | DASDING 90.8 | DASDING908.de@SD | - | NO_GUIDE_HIT |
| Germany | Deluxe Dance | DeluxeDance.de@SD | - | NO_GUIDE_HIT |
| Germany | Medium (Germany) | Medium.de@ES | - | NO_GUIDE_HIT |
| Germany | One Adria | OneAdria.de@SD | - | NO_GUIDE_HIT |
| Germany | Pluto TV 90's Classics | PlutoTV90sClassics.de@FR | - | NO_GUIDE_HIT |
| Germany | Pluto TV Alberto Sordi | PlutoTVAlbertoSordi.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Bud & Terence (Germany) | PlutoTVBudTerence.de@DACH | - | NO_GUIDE_HIT |
| Germany | Pluto TV Catastrofes | PlutoTVCatastrofes.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Christmas tutto l'anno | PlutoTVChristmastuttolanno.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Cine Comedia (Germany) | PlutoTVCineComedia.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Cine de autor | PlutoTVCinedeautor.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Cine Romantico | PlutoTVCineRomantico.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Cinema Italiano | PlutoTVCinemaItaliano.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Cinema Orientale | PlutoTVCinemaOrientale.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Comedias Romanticas | PlutoTVComediasRomanticas.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Comedies Cultes | PlutoTVComediesCultes.de@FR | - | NO_GUIDE_HIT |
| Germany | Pluto TV Cult Films (Germany) | PlutoTVCultFilms.de@GB | - | NO_GUIDE_HIT |
| Germany | Pluto TV Family Movie Club | PlutoTVFamilyMovieClub.de@GB | - | NO_GUIDE_HIT |
| Germany | Pluto TV Fantasy & Horror | PlutoTVFantasyHorror.de@GB | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film (Germany) | PlutoTVFilm.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film Azione | PlutoTVFilmAzione.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film Commedia | PlutoTVFilmCommedia.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film Romantici | PlutoTVFilmRomantici.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film Storici | PlutoTVFilmStorici.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film Thriller | PlutoTVFilmThriller.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Haialarm | PlutoTVHaialarm.de@DACH | - | NO_GUIDE_HIT |
| Germany | Pluto TV Invasion Alien | PlutoTVInvasionAlien.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Legami Letali | PlutoTVLegamiLetali.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Movies GB | PlutoTVMovies.de@GB | - | NO_GUIDE_HIT |
| Germany | Pluto TV Notti di Passione | PlutoTVNottidiPassione.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Psycho | PlutoTVPsycho.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Serie Sci-Fi | PlutoTVSerieSciFi.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Toto | PlutoTVToto.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Western ES | PlutoTVWestern.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Western IT | PlutoTVWestern.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Westerns (Germany) | PlutoTVWesterns.de@GB | - | NO_GUIDE_HIT |
| Germany | Pluto TV Zombies | PlutoTVZombies.de@ES | - | NO_GUIDE_HIT |
| Germany | Rakuten TV Comedy Movies Germany | custom.rakuten-tv-comedy-movies-germany-de-movie | - | NO_GUIDE_HIT |
| Germany | Rakuten TV Drama Movies Germany | RakutenTVDramaMovies.es@Germany | - | NO_GUIDE_HIT |
| Germany | Rakuten TV Family Movies Germany | RakutenTVFamilyMovies.es@Germany | - | NO_GUIDE_HIT |
| Germany | Rakuten TV Top Movies Germany | RakutenTVTopMovies.es@Germany | - | NO_GUIDE_HIT |
| Germany | TV Bozsike Hamburg | TVBozsikeHamburgHD.de@HD | - | NO_GUIDE_HIT |
| Greece | Baraza TV | BarazaTV.gr@SD | - | NO_GUIDE_HIT |
| Greece | Baraza TV Deep House | BarazaTVDeepHouse.gr@SD | - | NO_GUIDE_HIT |
| Greece | Baraza TV Relaxing | BarazaTVRelaxing.gr@SD | - | NO_GUIDE_HIT |
| Greece | Messatida TV | MessatidaTV.gr@SD | - | NO_GUIDE_HIT |
| Greece | NRG 91 | NRG91.gr@SD | - | NO_GUIDE_HIT |
| Greece | Play TV (Greece) | PlayTV.gr@SD | - | NO_GUIDE_HIT |
| Hungary | AMC Europe Hungary | AMCEurope.uk@Hungary | - | NO_GUIDE_HIT |
| Hungary | Cinemax 2 Central Europe | Cinemax2CentralEurope.hu@SD | - | NO_GUIDE_HIT |
| Hungary | Cinemax Central Europe | CinemaxCentralEurope.hu@SD | - | NO_GUIDE_HIT |
| Hungary | Film Cafe | FilmCafe.hu@Hungary | - | NO_GUIDE_HIT |
| Hungary | Film+ (Hungary) | FilmPlus.hu@SD | - | NO_GUIDE_HIT |
| Hungary | FILMBOX+ Emotion Hungary | FILMBOXPlusEmotion.pl@Hungary | - | NO_GUIDE_HIT |
| Hungary | FILMBOX+ Hits Hungary | FILMBOXPlusHits.pl@Hungary | - | NO_GUIDE_HIT |
| Hungary | Oxygen Music | OxygenMusic.hu@HD | - | NO_GUIDE_HIT |
| Indian Bangla | Tara TV | TaraTV.in | Tara.TV.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Bangla | ZB Cinema | ZBCinema.in | jtv3322 | 3322 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Bangla | Bangla Plus | BanglaPlus.in | - | NO_GUIDE_HIT |
| Indian Bangla | Jhankar TV | JhankarTV.ca | - | NO_GUIDE_HIT |
| Indian Bangla | JTV Bangla | JTVBangla.in@SD | - | NO_GUIDE_HIT |
| Indian Bangla | JTV Classic | JTVClassic.in | - | NO_GUIDE_HIT |
| Indian Bangla | Matribhumi TV | MatribhumiTV.bd | - | NO_GUIDE_HIT |
| Indian Bangla | News 21 | News21BanglaTV.bd@SD | - | NO_GUIDE_HIT |
| Indian Bangla | Orange Bangla TV | OrangeBanglaTV.in@SD | - | NO_GUIDE_HIT |
| Indian Bangla | Sananda | SanandaTV.in | - | NO_GUIDE_HIT |
| Indian Bangla | Sananda TV | custom.sananda-tv | - | NO_GUIDE_HIT |
| Indian Bangla | SNB Cinema | SNBCinema.in | - | NO_GUIDE_HIT |
| Indian Bangla | Zodiak TV | ZodiakTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Friends TV | FriendsTV.in | Friends.TV.in | jtv2354 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Manoranjan Prime | ManoranjanPrime.in@SD | 154892 | 10000000075992492 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | One Paschima | OnePaschima.in@SD | One.Paschima.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Shemaroo Umang | ShemarooUmang.in@SD | ShemarooUmang.in | 143779 | SHEMAROO.UMANG.in | Shemaroo.Umang.in | jtv2078 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Suriyan TV | SuriyanTV.in@SD | ts1384 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Zingabad | Zingabad.in@SD | 7258 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Amazing Discoveries TV | AmazingDiscoveriesTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Asianet Middle East | AsianetMiddleEast.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Baiscope TV | BaiscopeTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | BT TV | BTTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | CCV | CCV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors MENA | ColorsMENA.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors MENA | ColorsMENA.in@HD | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors Rishtey Americas | ColorsRishteyAmericas.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Epic TV Digital | EpicTV.in@Digital | - | NO_GUIDE_HIT |
| Indian Entertainment | Flowers US | Flowers.us | - | NO_GUIDE_HIT |
| Indian Entertainment | GTC Punjabi UK | GTCPunjabi.in@UK | - | NO_GUIDE_HIT |
| Indian Entertainment | GTC Punjabi US | GTCPunjabi.in@US | - | NO_GUIDE_HIT |
| Indian Entertainment | JTBS Classic | JTBSClassic.in@Main | - | NO_GUIDE_HIT |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Kalika TV | KalikaTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | KCL TV | KCLTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Kerala Vision | KeralaVision.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Maha Punjabi | MahaPunjabi.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Mango Mobile TV | MangoMobileTV.in@HD | - | NO_GUIDE_HIT |
| Indian Entertainment | Marutam TV | MarutamTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Mei Alai TV | MeiAlaiTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | MNTV (Tamil) | MarutamTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | NKR TV Kannada | NKRTVKannada.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Oli TV | OliTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Pardesi TV | PardesiTV.ca | - | NO_GUIDE_HIT |
| Indian Entertainment | Pulari TV | PulariTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Punjabi TV | PunjabiTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Q TV | QTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | SADA TV | SADATV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | SADA TV | SADATV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Swantham | Swantham.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Tamilan TV | TamilanTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Thendral TV | ThendralTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | UTV Palakkad | UTVPalakkad.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Ekamra Cinema | EkamraCinema.in | Ekamra.Cinema.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Movies | Namma Bangalore | NammaBangalore.in@SD | 3237 | Namma.Bangalore.in | jtv3237 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Movies | Asian Sony Max 2 | custom.asian-sony-max-2 | - | NO_GUIDE_HIT |
| Indian Movies | B4U Bhojpuri Plus | B4UBhojpuri.in@Plus | - | NO_GUIDE_HIT |
| Indian Movies | Chhaya Chitram Telugu | ChhayaChitramTelugu.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Epic Bhojpuri Digital | EpicBhojpuri.in@Digital | - | NO_GUIDE_HIT |
| Indian Movies | Goldmines 2 | Goldmines2.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Goldmines Action | GoldminesAction.in | - | NO_GUIDE_HIT |
| Indian Movies | Goldmines Action | GoldminesAction.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Hindi Movie Classic 24 | new.hindi.movie.classic.24 | - | NO_GUIDE_HIT |
| Indian Movies | India Talkies | IndiaTalkies.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Indywood TV | IndywoodTV.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | JA TV | JATV.bin | - | NO_GUIDE_HIT |
| Indian Movies | K Cine | KCine.in | - | NO_GUIDE_HIT |
| Indian Movies | KCM India | KCM.sg@India | - | NO_GUIDE_HIT |
| Indian Movies | Maha Movie | MahaMovie.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Mango | Mango.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | MH One Movies | MHOneMovies.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Movie Punjab | MoviePunjab.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Pravasi Channel | PravasiChannel.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | - | NO_GUIDE_HIT |
| Indian Movies | Soneri Cinema | SoneriCinema.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Sony Movies | SonyMovies.in | - | NO_GUIDE_HIT |
| Indian Movies | Zee Cinema APAC | ZeeCinema.in@APAC | - | NO_GUIDE_HIT |
| Indian Music | Ekamra Musiq | EkamraMusiq.in | Ekamra.Musiq.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Music | Mastiii | Mastiii.in@SD | Mastiii.in | 143308 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Music | Steelbird Music | SteelbirdMusic.in@SD | Steelbird.Music.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Music | 7X Punjabi | 7XPunjabi.in | - | NO_GUIDE_HIT |
| Indian Music | Andy Haryana | AndyHaryana.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Hindi Hits | HindiHits.in | - | NO_GUIDE_HIT |
| Indian Music | Hindi Hits | HindiHits.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Pankh | Pankh.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Punjabi Music | PunjabiMusicHD.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Rang Rangoli | RangRangoli.in | - | NO_GUIDE_HIT |
| Indian Music | Vision Beats | VisionBeats.in@SD | - | NO_GUIDE_HIT |
| Indian Music | YRF Music Nepal | YRFMusic.in@Nepal | - | NO_GUIDE_HIT |
| International | Al Jazeera | AlJazeera.qa | ts190 | jtv494 | MAPPED_NOT_CURRENTLY_FOUND |
| International | AMC Thrillers | plex.tv.AMC.Thrillers.plex | plex.tv.AMC.Thrillers.plex | MAPPED_NOT_CURRENTLY_FOUND |
| International | Bang Bang TV | BangBangTV | 6590 | MAPPED_NOT_CURRENTLY_FOUND |
| International | MAX TV | custom.max-tv-az-music | Max.ca2 | MAPPED_NOT_CURRENTLY_FOUND |
| International | MN+ | MNPlus.mn@SD | 143548 | ts210 | jtv477 | MAPPED_NOT_CURRENTLY_FOUND |
| International | PMC | PMC.ae@SD | 4906 | MAPPED_NOT_CURRENTLY_FOUND |
| International | Stingray Today's Latin Pop | StingrayTodaysLatinPop.ca | USBD3500009Y3 | MAPPED_NOT_CURRENTLY_FOUND |
| International | XITE Hits | XITEHits.nl | USBD3300004RH | MAPPED_NOT_CURRENTLY_FOUND |
| International | 24 Hour Free Movies | custom.24hourfreemovies | - | NO_GUIDE_HIT |
| International | 30A Music | custom.30amusic | - | NO_GUIDE_HIT |
| International | 4ever Cinema | custom.4evercinema | - | NO_GUIDE_HIT |
| International | 4ever Music | custom.4evermusic | - | NO_GUIDE_HIT |
| International | A2i Music | A2iMusic.sn@SD | - | NO_GUIDE_HIT |
| International | Action Hollywood Movies | plex.tv.Action.Hollywood.Movies.plex | - | NO_GUIDE_HIT |
| International | Afrobeats | Afrobeats.us | - | NO_GUIDE_HIT |
| International | Allo Cine | AlloCine.cm@SD | - | NO_GUIDE_HIT |
| International | Antenne Kaernten | AntenneKaernten.at@SD | - | NO_GUIDE_HIT |
| International | Antenne Steiermark | AntenneSteiermark.at@SD | - | NO_GUIDE_HIT |
| International | Audiokiss | Audiokiss.bo@SD | - | NO_GUIDE_HIT |
| International | Aurora Media Films | AuroraMediaFilms.gt@SD | - | NO_GUIDE_HIT |
| International | BOKTV | BOKTV.za@SD | - | NO_GUIDE_HIT |
| International | BTA TV | BTATV.ve@SD | - | NO_GUIDE_HIT |
| International | CEACOM TV | custom.ceacom-tv-bo-music | - | NO_GUIDE_HIT |
| International | Celestial Movies | CelestialMovies.hk@SD | - | NO_GUIDE_HIT |
| International | Cinema (Mongolia) | Cinema.mn@SD | - | NO_GUIDE_HIT |
| International | CMC TV | CMCTV.hr | - | NO_GUIDE_HIT |
| International | CMC TV | custom.cmctv | - | NO_GUIDE_HIT |
| International | Dance TV | DanceTV.us | - | NO_GUIDE_HIT |
| International | DM Sat | custom.dm-sat-rs-music | - | NO_GUIDE_HIT |
| International | DW News | DWNews.de | - | NO_GUIDE_HIT |
| International | E40 | E40.py@SD | - | NO_GUIDE_HIT |
| International | El Sol Network TV | ElSolNetworkTV.ec@SD | - | NO_GUIDE_HIT |
| International | EU Music | custom.eumusic | - | NO_GUIDE_HIT |
| International | Europa Plus TV Belarus | EuropaPlusTV.ru@Belarus | - | NO_GUIDE_HIT |
| International | Falastini TV | FalastiniTV.ps@SD | - | NO_GUIDE_HIT |
| International | Fashion&LifeStyle | FashionLifeStyle.ru@SD | - | NO_GUIDE_HIT |
| International | FashionTV | FashionTV.ru@SD | - | NO_GUIDE_HIT |
| International | FashionTV Paris L'Original | FashionTVParisLOriginal.fr@SD | - | NO_GUIDE_HIT |
| International | FashionTV Secrets | FashionTVSecrets.fr@HD | - | NO_GUIDE_HIT |
| International | First Music Channel | FirstMusicChannel.by@SD | - | NO_GUIDE_HIT |
| International | First Music Channel Russia | FirstMusicChannelRussia.by@SD | - | NO_GUIDE_HIT |
| International | Folk Klub TV | FolkKlubTV.au@SD | - | NO_GUIDE_HIT |
| International | Folk TV | FolkTV.mk@SD | - | NO_GUIDE_HIT |
| International | Folx Slovenija | FolxSlovenija.si@SD | - | NO_GUIDE_HIT |
| International | FON Music | FONMusic.us | - | NO_GUIDE_HIT |
| International | Fun Vision | FunVision.be@SD | - | NO_GUIDE_HIT |
| International | Fusion TV | FUSIONTV.mq@SD | - | NO_GUIDE_HIT |
| International | Global Fashion Channel | GlobalFashionChannel.us@SD | - | NO_GUIDE_HIT |
| International | Gugak TV | GugakTV.kr@SD | - | NO_GUIDE_HIT |
| International | HBO Asia Taiwan | HBOAsia.sg@Taiwan | - | NO_GUIDE_HIT |
| International | HEi Now | HEiNow.py@SD | - | NO_GUIDE_HIT |
| International | Hero [ ] | Hero.fi@SD | - | NO_GUIDE_HIT |
| International | HMTV (Nigeria) | HMTV.ng@SD | - | NO_GUIDE_HIT |
| International | Identite Tele Caraibes | IdentiteTeleCaraibes.mq@SD | - | NO_GUIDE_HIT |
| International | iFilm English | iFilmEnglish.ir | - | NO_GUIDE_HIT |
| International | Infinita TV | InfinitaTV.ec@SD | - | NO_GUIDE_HIT |
| International | INTV Australia | INTVAustralia.au@SD | - | NO_GUIDE_HIT |
| International | Isango TV [ ] | IsangoTV.rw@SD | - | NO_GUIDE_HIT |
| International | Ivoire Channel | IvoireChannel.ci@SD | - | NO_GUIDE_HIT |
| International | Jordan Songs | JordanSongs.jo@SD | - | NO_GUIDE_HIT |
| International | JRTV Jarviradio | JRTVJarviradio.fi@SD | - | NO_GUIDE_HIT |
| International | K100 | K100.is@SD | - | NO_GUIDE_HIT |
| International | Kantipur Max [ ] | KantipurMax.np@SD | - | NO_GUIDE_HIT |
| International | Kayhan TV | KayhanTV.af@SD | - | NO_GUIDE_HIT |
| International | Klape i Tambure TV | KlapeiTambureTV.hr@SD | - | NO_GUIDE_HIT |
| International | Klara | Klara.be@SD | - | NO_GUIDE_HIT |
| International | KN Music TV | KNMusicTV.az@SD | - | NO_GUIDE_HIT |
| International | Konul Music TV | custom.konul-music-tv-az-music | - | NO_GUIDE_HIT |
| International | Kuriakos Music | KuriakosMusic.pt@SD | - | NO_GUIDE_HIT |
| International | La Elegida Television | LaElegidaTelevision.uy@SD | - | NO_GUIDE_HIT |
| International | La Top 102.9 | LaTop1029.hn@SD | - | NO_GUIDE_HIT |
| International | La Top 107.7 | LaTop1077.hn@SD | - | NO_GUIDE_HIT |
| International | La-X | LaX.pr@SD | - | NO_GUIDE_HIT |
| International | Live99FM | Live99FM.bq@SD | - | NO_GUIDE_HIT |
| International | Lollywood HD TV | LollywoodHDTV.cd@SD | - | NO_GUIDE_HIT |
| International | Look Thoong TV | LookThoongTV.la@SD | - | NO_GUIDE_HIT |
| International | Love TV | LoveTV.mk@SD | - | NO_GUIDE_HIT |
| International | LRT Klasika | LRTKlasika.lt@SD | - | NO_GUIDE_HIT |
| International | LRT Opus | LRTOpus.lt@SD | - | NO_GUIDE_HIT |
| International | M-1 | M1.lt@SD | - | NO_GUIDE_HIT |
| International | M20 Music | M20Music.us | - | NO_GUIDE_HIT |
| International | Maah TV | MaahTV.my@SD | - | NO_GUIDE_HIT |
| International | Mazzika | Mazzika.eg@SD | - | NO_GUIDE_HIT |
| International | MegaBox | MegaBox.ni@SD | - | NO_GUIDE_HIT |
| International | Metropoli Medios TV | MetropoliMediosTV.ec@SD | - | NO_GUIDE_HIT |
| International | Mix Hollywood | MixHollywood.eg@SD | - | NO_GUIDE_HIT |
| International | Mix Hollywood | custom.mixhollywood | - | NO_GUIDE_HIT |
| International | Movie Dome Family | MovieDomeFamily.us | - | NO_GUIDE_HIT |
| International | MovieBox | MovieBox.mn@SD | - | NO_GUIDE_HIT |
| International | Movies Thriller | MoviesThriller.sa@SD | - | NO_GUIDE_HIT |
| International | MovieSphere UK | custom.moviesphereuk | - | NO_GUIDE_HIT |
| International | Muzangala TV | MuzangalaTV.ao@SD | - | NO_GUIDE_HIT |
| International | MWD Movies | MWDMovies.mm@SD | - | NO_GUIDE_HIT |
| International | My Cinema | MyCinema.us | - | NO_GUIDE_HIT |
| International | My Cinema Europe | MyCinemaEurope.ch@SD | - | NO_GUIDE_HIT |
| International | Navahang TV | NavahangTV.fi@SD | - | NO_GUIDE_HIT |
| International | NogoumFMTV | NogoumFMTV.eg@SD | - | NO_GUIDE_HIT |
| International | Noroc TV | NorocTV.md@SD | - | NO_GUIDE_HIT |
| International | Ocko Expres | custom.ockoexpres | - | NO_GUIDE_HIT |
| International | Oxygen Music | OxygenMusic.us | - | NO_GUIDE_HIT |
| International | Play TV (Cameroon) | PlayTV.cm@SD | - | NO_GUIDE_HIT |
| International | PMC Royale | PMCRoyale.ae@SD | - | NO_GUIDE_HIT |
| International | POP World TV | POPWorldTV.es | - | NO_GUIDE_HIT |
| International | Rakuten Movies | RakutenMovies | - | NO_GUIDE_HIT |
| International | Rakuten TV Action Movies UK | RakutenTVActionMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Comedy Movies UK | RakutenTVComedyMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Family Movies UK | RakutenTVFamilyMovies.es@UK | - | NO_GUIDE_HIT |
| International | RFPtv | RFPtv.pt@SD | - | NO_GUIDE_HIT |
| International | RHT Guadeloupe | RHTGuadeloupe.gp@SD | - | NO_GUIDE_HIT |
| International | RTL Gold (Luxembourg) | RTLGold.lu@SD | - | NO_GUIDE_HIT |
| International | Scorch TV | ScorchTV.tt@SD | - | NO_GUIDE_HIT |
| International | Shanson TV | ShansonTV.ru | - | NO_GUIDE_HIT |
| International | ShowVen TV | ShowVenTV.ve@SD | - | NO_GUIDE_HIT |
| International | Silk Way Cinema | SilkWayCinema.kz@SD | - | NO_GUIDE_HIT |
| International | Sky Folk TV | SkyFolkTV.mk@SD | - | NO_GUIDE_HIT |
| International | Sparkle Movies | GBAJ400042T1 | - | NO_GUIDE_HIT |
| International | StuBru | StuBru.be@SD | - | NO_GUIDE_HIT |
| International | Tele Zoukla | TeleZoukla.mq@SD | - | NO_GUIDE_HIT |
| International | Tezaur TV | TezaurTV.md@SD | - | NO_GUIDE_HIT |
| International | The Retro Channel | custom.the-retro-channel-pr-music | - | NO_GUIDE_HIT |
| International | Tjil TV | TjilTV.na@SD | - | NO_GUIDE_HIT |
| International | TMA | TMA.gp@SD | - | NO_GUIDE_HIT |
| International | TopEstrada TV | TopEstradaTV.mk@SD | - | NO_GUIDE_HIT |
| International | Totalmusic | Totalmusic.uk | - | NO_GUIDE_HIT |
| International | Totalmusic Dance | custom.totalmusicdance | - | NO_GUIDE_HIT |
| International | Trace Latina | TraceLatina.us | - | NO_GUIDE_HIT |
| International | Trace UK | custom.traceuk | - | NO_GUIDE_HIT |
| International | Turkmen Owazy | TurkmenOwazy.tm@SD | - | NO_GUIDE_HIT |
| International | TV Cidade | TVCidade.cv@SD | - | NO_GUIDE_HIT |
| International | TVCARiB Cinema | TVCARiBCinema.sx@SD | - | NO_GUIDE_HIT |
| International | TVONE Nicaragua | TVONENicaragua.ni@SD | - | NO_GUIDE_HIT |
| International | V2 Beat | custom.v2beat | - | NO_GUIDE_HIT |
| International | VAM TV | VAMTV.cw@SD | - | NO_GUIDE_HIT |
| International | Venus Media | VenusMedia.py@SD | - | NO_GUIDE_HIT |
| International | Vevo Hip Hop & R&B | GBBD2300001C0 | - | NO_GUIDE_HIT |
| International | VIP TV | custom.vip-tv-aw-music | - | NO_GUIDE_HIT |
| International | Vox Kongo TV | custom.vox-kongo-tv-cd-music | - | NO_GUIDE_HIT |
| International | XITE Summer | custom.xitesummer | - | NO_GUIDE_HIT |
| International | ZICO TV | ZICOTV.rs@SD | - | NO_GUIDE_HIT |
| Iran | T2 TV | T2TV.ir@SD | USBC600001QL | MAPPED_NOT_CURRENTLY_FOUND |
| Iran | Afra Film | custom.afra-film-ir-movie | - | NO_GUIDE_HIT |
| Iran | Cafe Film | CafeFilm.ir@SD | - | NO_GUIDE_HIT |
| Iran | Gold Star | GoldStar.ir@SD | - | NO_GUIDE_HIT |
| Iran | iFilm 2 | iFilm2.ir@SD | - | NO_GUIDE_HIT |
| Iran | iFilm Arabic | iFilmArabic.ir@SD | - | NO_GUIDE_HIT |
| Iran | iFilm English | iFilmEnglish.ir@SD | - | NO_GUIDE_HIT |
| Iran | iFilm Persian | iFilmPersian.ir@SD | - | NO_GUIDE_HIT |
| Iran | Meta Film TV | MetaFilmTV.ir@SD | - | NO_GUIDE_HIT |
| Iran | SL 1 | custom.sl-1-ir-movie | - | NO_GUIDE_HIT |
| Iran | SL 2 | custom.sl-2-ir-movie | - | NO_GUIDE_HIT |
| Italy | 70-80 TV | 7080TV.it@SD | - | NO_GUIDE_HIT |
| Italy | Company TV | CompanyTV.it@SD | - | NO_GUIDE_HIT |
| Italy | Euro Indie Music Chart TV | EuroIndieMusicChartTV.it@SD | - | NO_GUIDE_HIT |
| Italy | Kiss Kiss Napoli TV | KissKissNapoliTV.it@SD | - | NO_GUIDE_HIT |
| Italy | m2o TV | m2oTV.it@SD | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Action Movies Italy | custom.rakuten-tv-action-movies-italy-it-movie | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Comedy Movies Italy | RakutenTVComedyMovies.es@Italy | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Drama Movies Italy | custom.rakuten-tv-drama-movies-italy-it-movie | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Family Movies Italy | RakutenTVFamilyMovies.es@Italy | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Top Movies Italy | RakutenTVTopMovies.es@Italy | - | NO_GUIDE_HIT |
| Italy | RDS Social TV | RDSSocialTV.it | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Best | RTL1025Best.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Bro&Sis | RTL1025BroSis.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Disco | RTL1025Disco.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Napule | RTL1025Napule.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Traffic | RTL1025Traffic.it@SD | - | NO_GUIDE_HIT |
| Kids | Discovery Kids | DiscoveryKids.au | 159011 | ts119 | LIVETV_LIVETVCHANNEL_DISCOVERY_KIDS | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | KidDo MATIX | KidDoMATIX.us | IN4600008T4 | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Zoo Moo | ZooMoo.sg | USBC2400019EF | ZooMoo.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | ADN TV+ | ADNTVPlus.fr | - | NO_GUIDE_HIT |
| Kids | Afarin TV | AfarinTV.iq | - | NO_GUIDE_HIT |
| Kids | Disney Jr | DisneyJr.us | - | NO_GUIDE_HIT |
| Kids | Duronto TV | DurontoTV.bd | - | NO_GUIDE_HIT |
| Kids | Epic Kids Digital | EpicKidsDigital.us | - | NO_GUIDE_HIT |
| Kids | God Stands Kids Club TV | GodStandsKidsClubTV.pk@English | - | NO_GUIDE_HIT |
| Kids | God Stands Kids Club TV Arabic | GodStandsKidsClubTV.pk@Arabic | - | NO_GUIDE_HIT |
| Kids | God Stands Kids Club TV Chinese | GodStandsKidsClubTV.pk@Chinese | - | NO_GUIDE_HIT |
| Kids | God Stands Kids Club TV Urdu | GodStandsKidsClubTV.pk@Urdu | - | NO_GUIDE_HIT |
| Kids | Lego Channel | LegoChannel.us@SD | - | NO_GUIDE_HIT |
| Kids | Moonbug Kids | MoonbugKids.uk | - | NO_GUIDE_HIT |
| Kids | Powerkids Kartoon Channel | PowerkidsKartoonChannel.us | - | NO_GUIDE_HIT |
| Kids | Smurf TV | SmurfTV.us | - | NO_GUIDE_HIT |
| Kids | Tooku | Tooku.ru | - | NO_GUIDE_HIT |
| Kids | Toon Goggles Junior | ToonGogglesJunior.us | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Hindi | WOWKidz.in@Hindi | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Tamil | WOWKidzTamil.in | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Telugu | WOWKidz.in@Telugu | - | NO_GUIDE_HIT |
| Lebanon | One TV | OneTV.lb@SD | TV.ONE.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Lebanon | Aghani Aghani TV | AghaniAghaniTV.lb@SD | - | NO_GUIDE_HIT |
| Lebanon | Arabica TV | custom.arabica-tv | - | NO_GUIDE_HIT |
| Lebanon | mfm | mfm.lb@HD | - | NO_GUIDE_HIT |
| Lebanon | MTV Lebanon | MTVLebanon.lb@SD | - | NO_GUIDE_HIT |
| Lebanon | OneFM | OneFM.lb@SD | - | NO_GUIDE_HIT |
| Mexico | MultiPremier | MultiPremier.mx@SD | Multipremier.mx | MAPPED_NOT_CURRENTLY_FOUND |
| Mexico | Az Cinema | AzCinema.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Claro Cinema | ClaroCinema.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Conecta TV | ConectaTV.mx@SD | - | NO_GUIDE_HIT |
| Mexico | De Pelicula Latin America | DePeliculaLatinAmerica.mx@SD | - | NO_GUIDE_HIT |
| Mexico | De Pelicula Plus | DePeliculaPlus.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Lobo TV | LoboTV.mx@SD | - | NO_GUIDE_HIT |
| Mexico | MyTime Movie Network (Mexico) | MyTimeMovieNetwork.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Popcorn Central | PopcornCentral.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Vision Television | VisionTelevision.mx@SD | - | NO_GUIDE_HIT |
| Netherlands | XITE Just Chill | XITEJustChill.nl@US | USBB2300003JZ | MAPPED_NOT_CURRENTLY_FOUND |
| Netherlands | XITE Reggae Vibes | custom.xite-reggae-vibes-nl-music | US4600008JA | MAPPED_NOT_CURRENTLY_FOUND |
| Netherlands | XITE Rock x Metal | XITERockxMetal.nl | USBB2300004KV | MAPPED_NOT_CURRENTLY_FOUND |
| Netherlands | BEATTV | BEATTV.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | Canal+ Action Europe Magyar | CanalPlusActionEurope.nl@Magyar | - | NO_GUIDE_HIT |
| Netherlands | FomixTV | custom.fomixtv-nl-music | - | NO_GUIDE_HIT |
| Netherlands | Qmusic | Qmusic.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | RadioNL TV | RadioNLTV.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | TMF | TMF.nl@HDFAST | - | NO_GUIDE_HIT |
| Pakistani | 8XM | 8XM.pk@HD | - | NO_GUIDE_HIT |
| Pakistani | 8XM | 8XM.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | aur LIFE | aurLIFE.pk | - | NO_GUIDE_HIT |
| Pakistani | Bol Entertainment | BolEntertainment.pk@HD | - | NO_GUIDE_HIT |
| Pakistani | Bol Entertainment | BolEntertainment.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Cartoon Network (Pakistan) | CartoonNetwork.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Falak TV | FalakTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Filmax | Filmax.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | HUM Masala | HUMMasala.pk | - | NO_GUIDE_HIT |
| Pakistani | HUM Sitaray | HUMSitaray.pk | - | NO_GUIDE_HIT |
| Pakistani | Jalwa TV | JalwaTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Joo Music | JooMusic.pk | - | NO_GUIDE_HIT |
| Pakistani | JooMusic | JooMusic.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Minimax (Pakistan) | Minimax.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Paighan TV | PaighanTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | See TV | SeeTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Tag TV | TagTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Waseb TV | WasebTV.pk | - | NO_GUIDE_HIT |
| Panama | Corazon TV | CorazonTV.pa@SD | - | NO_GUIDE_HIT |
| Panama | Mas23 TV | Mas23TV.pa@SD | - | NO_GUIDE_HIT |
| Panama | Pindin TV | PindinTV.pa@SD | - | NO_GUIDE_HIT |
| Panama | Super Q Panama | SuperQPanama.pa@SD | - | NO_GUIDE_HIT |
| Panama | Tropical Moon Urban TV | TropicalMoonUrbanTV.pa@SD | - | NO_GUIDE_HIT |
| Peru | Karibena | Karibena.pe@SD | - | NO_GUIDE_HIT |
| Peru | La Fabulosa TV | LaFabulosaTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | Metropolitana del Cuzco | custom.metropolitana-del-cuzco-pe-music | - | NO_GUIDE_HIT |
| Peru | Miel TV | MielTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | RumbaMix TV | RumbaMixTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | Top Latino TV | TopLatinoTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | TV Peruanisima | TVPeruanisima.pe@SD | - | NO_GUIDE_HIT |
| Peru | TVUNO | TVUNO.pe@SD | - | NO_GUIDE_HIT |
| Poland | Stingray Greatest Hits | custom.stingray-greatest-hits-pl-music | USBD3500022DN | jtv3479 | MAPPED_NOT_CURRENTLY_FOUND |
| Poland | FILMBOX+ Comedy | FILMBOXPlusComedy.pl@Poland | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Comedy Magyar | FILMBOXPlusComedy.pl@Magyar | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Emotion | FILMBOXPlusEmotion.pl@Poland | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Emotion Adria | custom.filmbox-emotion-adria-pl-movie | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Festival | FILMBOXPlusFestival.pl@SD | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Festival Poland | FILMBOXPlusFestival.pl@Poland | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Hits | FILMBOXPlusHits.pl@Poland | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Hits Adria | custom.filmbox-hits-adria-pl-movie | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Love & Crime Adria | custom.filmbox-love-crime-adria-pl-movie | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Love & Crime Magyar | FILMBOXPlusLoveCrime.pl@Magyar | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ One Magyar | FILMBOXPlusOne.pl@Magyar | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ One Ukraine & Baltics [ ] | FILMBOXPlusOne.pl@UkraineBaltics | - | NO_GUIDE_HIT |
| Religious | Al Istiqama | AlistiqamaTV.om | - | NO_GUIDE_HIT |
| Religious | Al Quran Al Kareem TV | AlQuranAlKareemTV.sa | - | NO_GUIDE_HIT |
| Religious | Al-Zahra TV Turkic | AlZahraTVTurkic.sa | - | NO_GUIDE_HIT |
| Religious | ARY Q TV | ARYQTV.pk | - | NO_GUIDE_HIT |
| Religious | Azan TV | custom.azantv | - | NO_GUIDE_HIT |
| Religious | Bahrain Quran | BahrainQuran.bh | - | NO_GUIDE_HIT |
| Religious | Dua Channel | DuaChannel.sa | - | NO_GUIDE_HIT |
| Religious | Iqraa TV | IqraaTV | - | NO_GUIDE_HIT |
| Religious | Islam Channel Bangla | custom.islamchannelbangla | - | NO_GUIDE_HIT |
| Religious | Islam TV | IslamTV.sa | - | NO_GUIDE_HIT |
| Religious | Madani TV | MadaniTV.sa | - | NO_GUIDE_HIT |
| Religious | Makkah Live | MakkahLive.sa | - | NO_GUIDE_HIT |
| Religious | Makkah TV | MakkahTV.sa | - | NO_GUIDE_HIT |
| Religious | Medina Live | MedinaLive.bd | - | NO_GUIDE_HIT |
| Religious | Peace TV Bangla | PeaceTVBangla.ae | - | NO_GUIDE_HIT |
| Religious | Peace TV English | PeaceTVEnglish.ae | - | NO_GUIDE_HIT |
| Religious | Peace TV Urdu | PeaceTVUrdu.pk | - | NO_GUIDE_HIT |
| Religious | Quran TV | QuranTV.iq | - | NO_GUIDE_HIT |
| Religious | Zainabia Channel | ZainabiaChannel.sa | - | NO_GUIDE_HIT |
| Romania | Atomic Academy TV | AtomicAcademyTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | Atomic TV | AtomicTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | Bollywood Classic Romania | BollywoodClassic.ro@Romania | - | NO_GUIDE_HIT |
| Romania | Boom TV | BoomTV.ro@HD | - | NO_GUIDE_HIT |
| Romania | Cinemaraton Plus | CinemaratonPlus.ro@HD | - | NO_GUIDE_HIT |
| Romania | CineWow | CineWow.ro@SD | - | NO_GUIDE_HIT |
| Romania | FILMBOX+ Comedy Romania | FILMBOXPlusComedy.pl@Romania | - | NO_GUIDE_HIT |
| Romania | FILMBOX+ Hits Romania | FILMBOXPlusHits.pl@Romania | - | NO_GUIDE_HIT |
| Romania | FILMBOX+ Love & Crime Romania | FILMBOXPlusLoveCrime.pl@Romania | - | NO_GUIDE_HIT |
| Romania | FILMBOX+ One Romania | FILMBOXPlusOne.pl@Romania | - | NO_GUIDE_HIT |
| Romania | Halloween Non Stop | HalloweenNonStop.ro@SD | - | NO_GUIDE_HIT |
| Romania | Impact TV (Romania) | ImpactTV.ro@HD | - | NO_GUIDE_HIT |
| Romania | Impact TV 2 | ImpactTV2.ro@HD | - | NO_GUIDE_HIT |
| Romania | Impact TV Dance | ImpactTVDance.ro@SD | - | NO_GUIDE_HIT |
| Romania | Impact TV Manele | ImpactTVManele.ro@SD | - | NO_GUIDE_HIT |
| Romania | Super TV (Romania) | SuperTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | Tequila Music TV | TequilaMusicTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | Traditional TV | TraditionalTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | TV AS | TVAS.ro@SD | - | NO_GUIDE_HIT |
| Russia | 1HD Music Television | 1HDMusicTelevision.ru@HD | - | NO_GUIDE_HIT |
| Russia | Bollywood | Bollywood.ru@HD | - | NO_GUIDE_HIT |
| Russia | Bollywood HD Russia | BollywoodHD.ro@Russia | - | NO_GUIDE_HIT |
| Russia | BRIDGE Rock | BRIDGERock.ru@SD | - | NO_GUIDE_HIT |
| Russia | City Eden Classic Music | CityEdenClassicMusic.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoAsia [ ] | CityEdenKinoAsia.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoDetektiv | CityEdenKinoDetektiv.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoFantastika | CityEdenKinoFantastika.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoKomediya | CityEdenKinoKomediya.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoMistika | CityEdenKinoMistika.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden Play | CityEdenPlay.ru@HD | - | NO_GUIDE_HIT |
| Russia | DanceHits80 | DanceHits80.ru@SD | - | NO_GUIDE_HIT |
| Russia | Dom kino | custom.dom-kino-ru-movie | - | NO_GUIDE_HIT |
| Russia | Evrokino | Evrokino.ru@HD | - | NO_GUIDE_HIT |
| Russia | Horoshee Kino | HorosheeKino.ru@SD | - | NO_GUIDE_HIT |
| Russia | Illusion+ | IllusionPlus.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kino 1 (Russia) | Kino1.ru@International | - | NO_GUIDE_HIT |
| Russia | Kino TV | KinoTV.ru@HD | - | NO_GUIDE_HIT |
| Russia | Kinopokaz | custom.kinopokaz-ru-movie | - | NO_GUIDE_HIT |
| Russia | Kinoseriya | custom.kinoseriya-ru-movie | - | NO_GUIDE_HIT |
| Russia | Live Music Channel | LiveMusicChannel.ru@HD | - | NO_GUIDE_HIT |
| Russia | MTV Volgograd | MTVVolgograd.ru@SD | - | NO_GUIDE_HIT |
| Russia | Muz Soyuz | MuzSoyuz.ru@SD | - | NO_GUIDE_HIT |
| Russia | Muzhskoy | Muzhskoy.ru@HD | - | NO_GUIDE_HIT |
| Russia | Muzyka 1 | Muzyka1.ru@International | - | NO_GUIDE_HIT |
| Russia | Muzyka Kino | MuzykaKino.ru@International | - | NO_GUIDE_HIT |
| Russia | Nash Kinopokaz | NashKinopokaz.ru@HD | - | NO_GUIDE_HIT |
| Russia | Premialnoe | Premialnoe.ru@HD | - | NO_GUIDE_HIT |
| Russia | Rodnoe Kino | custom.rodnoe-kino-ru-movie | - | NO_GUIDE_HIT |
| Russia | Russkiy roman | custom.russkiy-roman-ru-movie | - | NO_GUIDE_HIT |
| Russia | Shanson TV | ShansonTV.ru@SD | - | NO_GUIDE_HIT |
| Russia | Smotrim 100% Klassika | Smotrim100Klassika.ru@SD | - | NO_GUIDE_HIT |
| Russia | SONGTV Russia | SONGTVRussia.ru@SD | - | NO_GUIDE_HIT |
| Russia | Star Cinema | StarCinema.ru@SD | - | NO_GUIDE_HIT |
| Russia | Star Family | StarFamily.ru@SD | - | NO_GUIDE_HIT |
| Russia | TV 21 | TV21.ru@SD | - | NO_GUIDE_HIT |
| Russia | TV1000 Russian Kino Global | TV1000RussianKinoGlobal.ru@SD | - | NO_GUIDE_HIT |
| Russia | viju TV1000 action | custom.viju-tv1000-action-ru-movie | - | NO_GUIDE_HIT |
| Russia | viju TV1000 novella | vijuTV1000novella.ru@HD | - | NO_GUIDE_HIT |
| Russia | viju TV1000 russkoe | custom.viju-tv1000-russkoe-ru-movie | - | NO_GUIDE_HIT |
| Russia | Кино 1 International | custom.1-international-ru-movie | - | NO_GUIDE_HIT |
| Saudi Arabia | Aflam | custom.aflam | - | NO_GUIDE_HIT |
| Saudi Arabia | Fairuz | Fairuz.sa@HD | - | NO_GUIDE_HIT |
| Saudi Arabia | Majid Al Mohandis | MajidAlMohandis.sa@SD | - | NO_GUIDE_HIT |
| Saudi Arabia | MBC Loud | MBCLoud.sa@SD | - | NO_GUIDE_HIT |
| Saudi Arabia | MBC Mood | MBCMood.sa@HD | - | NO_GUIDE_HIT |
| Saudi Arabia | Movies Action | MoviesAction.sa@SD | - | NO_GUIDE_HIT |
| Saudi Arabia | Rabeh Saqer | RabehSaqer.sa@HD | - | NO_GUIDE_HIT |
| Saudi Arabia | Tarab | Tarab.sa@SD | - | NO_GUIDE_HIT |
| Singapore | Cinemax Asia | CinemaxAsia.sg@HD | - | NO_GUIDE_HIT |
| Singapore | HBO Asia SD [ ] | HBOAsia.sg@SD | - | NO_GUIDE_HIT |
| Singapore | HBO Hits Asia | HBOHitsAsia.sg@HD | - | NO_GUIDE_HIT |
| Singapore | HBO Signature Asia | HBOSignatureAsia.sg@HD | - | NO_GUIDE_HIT |
| Spain | Activa TV | ActivaTV.es@SD | - | NO_GUIDE_HIT |
| Spain | Cadena Elite | CadenaElite.es@SD | - | NO_GUIDE_HIT |
| Spain | LiraTV | LiraTV.es@SD | - | NO_GUIDE_HIT |
| Spain | Molahits TV | custom.molahits-tv-es-music | - | NO_GUIDE_HIT |
| Spain | Music TV Granada | MusicTVGranada.es@SD | - | NO_GUIDE_HIT |
| Spain | Onda 15 TV | Onda15TV.es@SD | - | NO_GUIDE_HIT |
| Spain | Onda Valencia TV | OndaValenciaTV.es@SD | - | NO_GUIDE_HIT |
| Spain | POP World TV | POPWorldTV.es@SD | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Action Movies | RakutenTVActionMovies.es@Spain | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Action Movies Germany | RakutenTVActionMoviesGermany.es | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Comedy Movies | RakutenTVComedyMovies.es@Spain | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Drama Movies | RakutenTVDramaMovies.es@Spain | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Family Movies | RakutenTVFamilyMovies.es | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Top Movies | RakutenTVTopMovies.es@Spain | - | NO_GUIDE_HIT |
| Spain | RTV Vida | RTVVida.es@SD | - | NO_GUIDE_HIT |
| Spain | SpektraTV | SpektraTV.es@SD | - | NO_GUIDE_HIT |
| Spain | TVOMIX | TVOMIX.es@HD | - | NO_GUIDE_HIT |
| Spain | XPTV1 | XPTV1.es@SD | - | NO_GUIDE_HIT |
| Sports | FIFA+ | custom.fifa | IN270000230 | USBD12000255B | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | FITE 24/7 | FITE247.us@SD | FITE247.us | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Red Bull TV | RedBullTV.at@EUMENA | jtv2779 | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | A Sports | ASports.pk | - | NO_GUIDE_HIT |
| Sports | ACCDN | custom.accdn | - | NO_GUIDE_HIT |
| Sports | ATG Live | custom.atglive | - | NO_GUIDE_HIT |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | - | NO_GUIDE_HIT |
| Sports | beIN Sports XTRA en Espanol | custom.beinsportsxtraenespanol | - | NO_GUIDE_HIT |
| Sports | Fight Network | custom.fightnetwork | - | NO_GUIDE_HIT |
| Sports | Goal TV | GoalTV.in | - | NO_GUIDE_HIT |
| Sports | Horse & Country | custom.horseandcountry | - | NO_GUIDE_HIT |
| Sports | Inter TV (Italy) | custom.intertv | - | NO_GUIDE_HIT |
| Sports | Kabaddi 24x7 | Kabaddi24x7.in@SD | - | NO_GUIDE_HIT |
| Sports | MTRSPT1 | custom.mtrspt | - | NO_GUIDE_HIT |
| Sports | Rally TV | custom.rallytv | - | NO_GUIDE_HIT |
| Sports | Realitatea Sportiva | custom.realitateasportiva | - | NO_GUIDE_HIT |
| Sports | Sportivnyy | custom.sportivnyy | - | NO_GUIDE_HIT |
| Sports | Sports First TV | SportsFirstTV.us | - | NO_GUIDE_HIT |
| Sports | TAPMAD | custom.tapmad | - | NO_GUIDE_HIT |
| Sports | TR Sport | custom.trsport | - | NO_GUIDE_HIT |
| Sports | Trace Sport | custom.tracesport | - | NO_GUIDE_HIT |
| Sports | TSN The Ocho | custom.tsntheocho | - | NO_GUIDE_HIT |
| Sports | TYC Sports | custom.tycsports | - | NO_GUIDE_HIT |
| Sports | World of Freesports | custom.worldoffreesports | - | NO_GUIDE_HIT |
| Sweden | Merry Christmas from Viafree | MerryChristmasfromViafree.se@SE | - | NO_GUIDE_HIT |
| Sweden | Merry Christmas from Viafree DK | MerryChristmasfromViafree.se@DK | - | NO_GUIDE_HIT |
| Sweden | Merry Christmas from Viafree NO | MerryChristmasfromViafree.se@NO | - | NO_GUIDE_HIT |
| Sweden | NonStop Kung Fu | NonStopKungFu.se@SE | - | NO_GUIDE_HIT |
| Sweden | NonStop Kung Fu DK | NonStopKungFu.se@DK | - | NO_GUIDE_HIT |
| Sweden | NonStop Kung Fu NO | NonStopKungFu.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Action (Sweden) DK | PlutoTVAction.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Action (Sweden) NO | PlutoTVAction.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Bud & Terence (Sweden) DK | PlutoTVBudTerence.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Bud & Terence (Sweden) NO | PlutoTVBudTerence.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Danske klassikere | PlutoTVDanskeklassikere.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Film (Sweden) DK | PlutoTVFilm.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Film (Sweden) NO | PlutoTVFilm.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Harlequin DK | PlutoTVHarlequin.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Harlequin NO | PlutoTVHarlequin.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Horror (Sweden) DK | PlutoTVHorror.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Horror (Sweden) NO | PlutoTVHorror.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Humor (Sweden) | PlutoTVHumor.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV John Wayne DK | PlutoTVJohnWayne.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV John Wayne NO | PlutoTVJohnWayne.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Komedie | PlutoTVKomedie.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Kultfilm | PlutoTVKultfilm.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Kultfilmer NO | PlutoTVKultfilmer.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Paranormal (Sweden) DK | PlutoTVParanormal.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Romantik DK | PlutoTVRomantik.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Romantikk | PlutoTVRomantikk.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Sci-Fi (Sweden) DK | PlutoTVSciFi.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Sci-Fi (Sweden) NO | PlutoTVSciFi.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Star Trek (Sweden) | PlutoTVStarTrek.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Wild West DK | PlutoTVWildWest.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Wild West NO | PlutoTVWildWest.se@NO | - | NO_GUIDE_HIT |
| Turkey | Dream Turk | DreamTurk.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Grand Cinema | GrandCinema.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Med Muzik | MedMuzik.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Number 1 Ask | Number1Ask.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Number 1 Damar | Number1Damar.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Number 1 Dance | Number1Dance.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Number 1 TV | Number1TV.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Power Dance | PowerDance.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Power Love | PowerLove.tr@SD | - | NO_GUIDE_HIT |
| Turkey | PowerTurk Akustik | PowerTurkAkustik.tr@SD | - | NO_GUIDE_HIT |
| Turkey | PowerTurk Slow | PowerTurkSlow.tr@SD | - | NO_GUIDE_HIT |
| Turkey | PowerTurk Taptaze | PowerTurkTaptaze.tr@SD | - | NO_GUIDE_HIT |
| Turkey | PowerTürk TV | PowerTurkTV.tr | - | NO_GUIDE_HIT |
| Turkey | TRT Muzik | TRTMuzik.tr@SD | - | NO_GUIDE_HIT |
| Ukraine | 4ever Music | 4everMusic.ua | - | NO_GUIDE_HIT |
| Ukraine | Cine+ Legend | CinePlusLegend.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | FilmUA Live | FilmUALive.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | FilmUADrama | custom.filmuadrama-ua-movie | - | NO_GUIDE_HIT |
| Ukraine | InRating TV | InRatingTV.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Kino 1 (Ukraine) | Kino1.ua | - | NO_GUIDE_HIT |
| Ukraine | M1 (Ukraine) | M1.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Megogo Music | MegogoMusic.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | NASHE Music | NASHEMusic.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Viasat Kino | custom.viasat-kino-ua-movie | - | NO_GUIDE_HIT |
| Ukraine | Viasat Kino Action | custom.viasat-kino-action-ua-movie | - | NO_GUIDE_HIT |
| Ukraine | Viasat Kino World | ViasatKinoWorld.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Viasat Serial | ViasatSerial.ua@HD | - | NO_GUIDE_HIT |
| Ukraine | ¡Viva Latino! | VivaLatino.ua@SD | - | NO_GUIDE_HIT |
| United Kingdom | MTV Classic | mtv.classic.gb | MTV.Classic.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| United Kingdom | AMC Europe Bulgary | AMCEurope.uk@Bulgary | - | NO_GUIDE_HIT |
| United Kingdom | Clubbing TV UK | custom.clubbing-tv-uk-gb-music | - | NO_GUIDE_HIT |
| United Kingdom | FMTV | custom.fmtv-gb-music | - | NO_GUIDE_HIT |
| United Kingdom | MovieSphere UK | custom.moviesphere-uk | - | NO_GUIDE_HIT |
| United Kingdom | Rakuten TV Drama Movies UK | RakutenTVDramaMovies.es@UK | - | NO_GUIDE_HIT |
| United Kingdom | Rakuten TV Top Movies UK | RakutenTVTopMovies.es@UK | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic 2000s | Totalmusic2000s.uk@HD | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic 80s | Totalmusic80s.uk | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic Concerts | TotalmusicConcerts.uk | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic Dance | TotalmusicDance.uk@HD | - | NO_GUIDE_HIT |
| United Kingdom | Trace UK | TraceUK.uk@HD | - | NO_GUIDE_HIT |
| United Kingdom | V2BEAT TV | V2BEATTV.uk@SD | - | NO_GUIDE_HIT |
| United Kingdom | Vantage Music UK | VantageMusic.ee@UK | - | NO_GUIDE_HIT |
| United States | 24 Hour Free Movies | custom.24-hour-free-movies | plex.tv.24.Hour.Free.Movies.plex | MAPPED_NOT_CURRENTLY_FOUND |
| United States | 00s Replay | 00sReplay.us@SD | - | NO_GUIDE_HIT |
| United States | 1Mus | 1Mus.us | - | NO_GUIDE_HIT |
| United States | 30A Music | 30AMusic.us | - | NO_GUIDE_HIT |
| United States | 30A TV Classic Movies | 30ATVClassicMovies.us@SD | - | NO_GUIDE_HIT |
| United States | Adrenalina Pura TV | AdrenalinaPuraTV.us@SD | - | NO_GUIDE_HIT |
| United States | AMC Latin America | AMCLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| United States | AMC Series Latin America | AMCSeriesLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| United States | American Horrors | AmericanHorrors.us@SD | - | NO_GUIDE_HIT |
| United States | AMG TV Classic | AMGTVClassic.us | - | NO_GUIDE_HIT |
| United States | ARTFLIX Movie Classics | ARTFLIXMovieClassics.us@SD | - | NO_GUIDE_HIT |
| United States | Avang TV | AvangTV.us@SD | - | NO_GUIDE_HIT |
| United States | AVI Rewind | AVIRewind.us@SD | - | NO_GUIDE_HIT |
| United States | Battlestar Galactica | BattlestarGalactica.us@SD | - | NO_GUIDE_HIT |
| United States | BET Cinema | BETCinema.us@SD | - | NO_GUIDE_HIT |
| United States | BET Comedy Movies | BETComedyMovies.us@SD | - | NO_GUIDE_HIT |
| United States | BET Visionaries | BETVisionaries.us@SD | - | NO_GUIDE_HIT |
| United States | Bonanza | Bonanza.us@SD | - | NO_GUIDE_HIT |
| United States | Bonanza CA | Bonanza.us@CA | - | NO_GUIDE_HIT |
| United States | Botflix Radioo | BotflixRadioo.us@HD | - | NO_GUIDE_HIT |
| United States | California Music Channel | CaliforniaMusicChannel.us | - | NO_GUIDE_HIT |
| United States | Cine Amor | CineAmor.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Familiar | CineFamiliar.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Hispano | CineHispano.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Premium | CinePremium.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Terror BR | CineTerror.us@BR | - | NO_GUIDE_HIT |
| United States | Cinecanal | Cinecanal.us@Panregional | - | NO_GUIDE_HIT |
| United States | Cinecanal Pacific | Cinecanal.us@Pacific | - | NO_GUIDE_HIT |
| United States | Cinecanal Panregional | custom.cinecanal-panregional-us-movie | - | NO_GUIDE_HIT |
| United States | Cinecanal South | Cinecanal.us@South | - | NO_GUIDE_HIT |
| United States | Cinemax Latin America | CinemaxLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | DHE | DHE.us@SD | - | NO_GUIDE_HIT |
| United States | DUST | custom.dust-us-movie | - | NO_GUIDE_HIT |
| United States | Epix | epix.us | - | NO_GUIDE_HIT |
| United States | Epix Hits | epixhits.us | - | NO_GUIDE_HIT |
| United States | Filmes Suspense | FilmesSuspense.us@BR | - | NO_GUIDE_HIT |
| United States | FilmRise Forensic Files [ ] | FilmRiseForensicFiles.us@SD | - | NO_GUIDE_HIT |
| United States | FrightFlix | custom.frightflix-us-movie | - | NO_GUIDE_HIT |
| United States | FXM | fxm.us | - | NO_GUIDE_HIT |
| United States | HBO 2 Latin America | HBO2LatinAmerica.us@HD | - | NO_GUIDE_HIT |
| United States | HBO Family Latin America | HBOFamilyLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | HBO Latin America | HBOLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | HBO Mundi Latin America | HBOMundiLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | HBO Xtreme Latin America | HBOXtremeLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | High Vision TV | HighVisionTV.us@SD | - | NO_GUIDE_HIT |
| United States | HTV | HTV.us@SD | - | NO_GUIDE_HIT |
| United States | Lifetime Movies | lifetimemovies.us | - | NO_GUIDE_HIT |
| United States | MCN6 Music Channel | custom.mcn6-music-channel-us-music | - | NO_GUIDE_HIT |
| United States | Mi Musica Hits | MiMusicaHits.us@SD | - | NO_GUIDE_HIT |
| United States | Mi Musica Reggaeton | MiMusicaReggaeton.us@SD | - | NO_GUIDE_HIT |
| United States | Mi Musica Romantica | MiMusicaRomantica.us@SD | - | NO_GUIDE_HIT |
| United States | Mi Musica Salsa | MiMusicaSalsa.us@SD | - | NO_GUIDE_HIT |
| United States | Movies! KPVM-LD | Movies.us@KPVMLD | - | NO_GUIDE_HIT |
| United States | MovieSphere CA | MovieSphere.us@CA | - | NO_GUIDE_HIT |
| United States | MovieSphere Gold WFXT | MovieSphereGold.us@WFXT | - | NO_GUIDE_HIT |
| United States | Now 70s | NOW70s.us | - | NO_GUIDE_HIT |
| United States | Now 80s | NOW80s.us | - | NO_GUIDE_HIT |
| United States | Pluto TV Action Movies | PlutoTVActionMovies.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Bang Bang | PlutoTVBangBang.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Classicos | PlutoTVCineClassicos.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Comedia (United States) BR | PlutoTVCineComedia.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Comedia Romantica | PlutoTVCineComediaRomantica.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Crime | PlutoTVCineCrime.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Inspiracao | PlutoTVCineInspiracao.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Sucessos | PlutoTVCineSucessos.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Comedy Movies | PlutoTVComedyMovies.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Crime Drama CA | PlutoTVCrimeDrama.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Drama Movies | PlutoTVDramaMovies.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Estrellas de Accion | PlutoTVEstrellasdeAccion.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Ficcao Cientifica | PlutoTVFiccaoCientifica.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Filmes Acao | PlutoTVFilmesAcao.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Filmes Aventura | PlutoTVFilmesAventura.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Filmes de Luta | PlutoTVFilmesdeLuta.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Filmes Nacionais | PlutoTVFilmesNacionais.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Franchise Favorites | PlutoTVFranchiseFavorites.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Horror (United States) CA | PlutoTVHorror.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Netmovies | PlutoTVNetmovies.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Retro Action Movies | PlutoTVRetroActionMovies.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Sci-Fi (United States) CA | PlutoTVSciFi.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Terror Trash | PlutoTVTerrorTrash.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Westerns (United States) CA | PlutoTVWesterns.us@CA | - | NO_GUIDE_HIT |
| United States | Rawhide (United States) | Rawhide.us@SD | - | NO_GUIDE_HIT |
| United States | RJTV | RJTV.us@SD | - | NO_GUIDE_HIT |
| United States | Sony Movies | sony.us | - | NO_GUIDE_HIT |
| United States | Sony Movies (United States) | SonyMovies.us@SD | - | NO_GUIDE_HIT |
| United States | Spirit TV [ ] | SpiritTV.us@SD | - | NO_GUIDE_HIT |
| United States | Stryk TV | StrykTV.us@HD | - | NO_GUIDE_HIT |
| United States | TCM Latin America South | TCMLatinAmerica.us@South | - | NO_GUIDE_HIT |
| United States | The Country Network | custom.the-country-network-us-music | - | NO_GUIDE_HIT |
| United States | Universal Cinema | UniversalCinema.us@SD | - | NO_GUIDE_HIT |
| United States | Vevo '70s & '80s | Vevo70s80s.us | - | NO_GUIDE_HIT |
| United States | Vevo '90s & '00s | Vevo90s00s.us | - | NO_GUIDE_HIT |
| United States | Video Mix TV | VideoMixTV.us@SD | - | NO_GUIDE_HIT |
| United States | Watch it Scream! | custom.watch-it-scream-us-movie | - | NO_GUIDE_HIT |
| United States | Whiplash Cinema | WhiplashCinema.us | - | NO_GUIDE_HIT |
| United States | WVCU-LP | WVCULP.us@SD | - | NO_GUIDE_HIT |
| United States | Young Hollywood | YoungHollywood.us@SD | - | NO_GUIDE_HIT |
| Uzbekistan | BIZ Cinema | custom.biz-cinema-uz-movie | - | NO_GUIDE_HIT |
| Uzbekistan | BIZ Music | custom.biz-music-uz-music | - | NO_GUIDE_HIT |
| Uzbekistan | FTV (Uzbekistan) | FTV.uz@SD | - | NO_GUIDE_HIT |
| Uzbekistan | Kinoteatr | Kinoteatr.uz@SD | - | NO_GUIDE_HIT |
| Uzbekistan | Muz TV Uzbekistan | MuzTVUzbekistan.uz@SD | - | NO_GUIDE_HIT |
| Vietnam | HTVC Movies | HTVCMovies.vn@SD | - | NO_GUIDE_HIT |
| Vietnam | ON Cine | ONCine.vn@SD | - | NO_GUIDE_HIT |
| Vietnam | ON Movies | ONMovies.vn@SD | - | NO_GUIDE_HIT |
| Vietnam | ON Music | ONMusic.vn@SD | - | NO_GUIDE_HIT |
| Vietnam | Tra Vinh TV | TraVinhTV.vn@SD | - | NO_GUIDE_HIT |
| Vietnam | Vinh Long TV 3 | VinhLongTV3.vn@SD | - | NO_GUIDE_HIT |

## Published Guide Validation

- XMLTV channel IDs published: **720**
- Active playlist IDs present in the published guide: **720/1966 (36.6%)**
- Active playlist IDs with usable current/future programmes: **631/1966 (32.1%)**
- Active playlist IDs with usable programmes anywhere in the guide window (-6h/+7d): **631/1966 (32.1%)**
- Mapped playlist IDs present in the guide: **720/733 (98.2%)**
- Mapped playlist IDs with usable current/future programmes: **631/733 (86.1%)**
- Mapped playlist IDs with usable programmes anywhere in the guide window: **631/733 (86.1%)**
- Eligible programme rows published in the guide window: **59219**
- Mapped playlist IDs missing from the published XMLTV channel list: **13**
- Missing mapped playlist IDs: BangU.us, LEOTV.cz, MusicBoxSexy.cz@SD, PlutoTVCineFamilia.us@BR, PlutoTVCineRomance.us@BR, StingrayPopAdult.ca@SD, custom.24-7-xxx-metro, custom.24-7-xxx-reality-kings, custom.xxx-brazzers-europe, custom.xxx-ero-xxx, custom.xxx-hustler, custom.xxx-super-one, custom.xxx-vivid-red
- Published mapped IDs without usable current/future programmes: **89**
- IDs without usable current/future programmes: AamarBangla.in, AaryaaTV.in, AaryaaTV.in@SD, AlJazeera.qa, BangBangTV, CineWestern.es@SD, CosmosTv.ar@HD, CrimeJustice.us, CrimeSceneTV.us, DiscoveryKids.au, EkamraCinema.in, EkamraMusiq.in, FITE247.us@SD, FriendsTV.in, HouseOfCrime.us, INFAST.nl, INWILD.nl, KTVBangla.in@SD, KidDoMATIX.us, KissKissTV.it@SD, LifeStyle.us, MNPlus.mn@SD, MaasrangaTV.bd, ManoranjanPrime.in@SD, Mastiii.in@SD, MetroTV.in@SD, MultiPremier.mx@SD, NTCTV.in@SD, NammaBangalore.in@SD, NatureTime.us, OnePaschima.in@SD, OneTV.lb@SD, Only.Music.in, PMC.ae@SD, RTL1025Caliente.it@SD, RTV.bd, RealWild.uk, RedBullTV.at@EUMENA, RobotWarsByMech.us, RumbaTV.co@SD, ShemarooUmang.in@SD, SonarBangla.in@SD, SteelbirdMusic.in@SD, StingrayClassicRock.ca, StingrayEasyListening.ca@SD, StingrayFlashback70s.ca@SD, StingrayGreatestHolidayHits.us@SD, StingrayHitList.ca, StingrayHolidayscapes.ca@HD, StingrayHotCountry.ca@SD, StingrayJukeboxOldies.ca@SD, StingrayNothinBut90s.ca@SD, StingrayRememberthe80s.ca, StingrayRomanceLatino.ca@SD, StingraySmoothJazz.ca@SD, StingraySoulStorm.ca@SD, StingrayTheSpa.ca, StingrayTheSpa.ca@SD, StingrayTodaySKPOP.us, StingrayTodaysLatinPop.ca (and 29 more)

## Source / Published Schedule Reconciliation

- IDs with usable current/future source schedule data: **673/1966 (34.2%)**
- IDs with usable current/future schedules in published XMLTV at report time: **631/1966 (32.1%)**
- IDs with usable programmes in the published guide's common -6h/+7d window: **631/1966 (32.1%)**
- Current/future source IDs without any usable published programme in that common window: **42**
- Source-scheduled IDs without a usable published programme in the common window: Amar Bangla (`AamarBangla.in`), Aaryaa TV (`AaryaaTV.in`), Aaryaa TV (`AaryaaTV.in@SD`), Bang U (`BangU.us`), Cine Western (Spain) (`CineWestern.es@SD`), KTV Bangla (`KTVBangla.in@SD`), Kiss Kiss TV (`KissKissTV.it@SD`), LEO TV (`LEOTV.cz`), Metro TV (`MetroTV.in@SD`), Music Box Sexy (`MusicBoxSexy.cz@SD`), NTC TV (`NTCTV.in@SD`), Only Music (`Only.Music.in`), Pluto TV Cine Familia (`PlutoTVCineFamilia.us@BR`), Pluto TV Cine Romance (`PlutoTVCineRomance.us@BR`), RTL 102.5 Caliente (`RTL1025Caliente.it@SD`), Sonar Bangla (`SonarBangla.in@SD`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray Easy Listening (`StingrayEasyListening.ca@SD`), Stingray Flashback 70's (`StingrayFlashback70s.ca@SD`), Stingray Greatest Holiday Hits (`StingrayGreatestHolidayHits.us@SD`), Stingray Hit List (`StingrayHitList.ca`), Stingray Hot Country (`StingrayHotCountry.ca@SD`), Stingray Jukebox Oldies (`StingrayJukeboxOldies.ca@SD`), Stingray Nothin' But 90s (`StingrayNothinBut90s.ca@SD`), Stingray Pop Adult (`StingrayPopAdult.ca@SD`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray Smooth Jazz (`StingraySmoothJazz.ca@SD`), Stingray Soul Storm (`StingraySoulStorm.ca@SD`), Stingray The Spa (`StingrayTheSpa.ca`), Stingray The Spa (`StingrayTheSpa.ca@SD`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Suriya TV (`SuriyaTV.in`), Suriya TV (`SuriyaTV.in@SD`), Ultimate TV (`UltimateTV.in@SD`), Metro (`custom.24-7-xxx-metro`), Reality Kings (`custom.24-7-xxx-reality-kings`), Dhoom Music Bangla (`custom.bdix.dhoom-music-bangla`), Brazzers Europe (`custom.xxx-brazzers-europe`), Ero Xxx (`custom.xxx-ero-xxx`), Hustler (`custom.xxx-hustler`), Super One (`custom.xxx-super-one`), Vivid Red (`custom.xxx-vivid-red`)
- IDs with an in-window published programme but no current/future source match at the later scan: **0**
- In-window published IDs not counted source-current/future: none
- Source-current/future IDs whose published programme is no longer current by report time: **42**
- Source-current/future IDs no longer current in the published guide: Amar Bangla (`AamarBangla.in`), Aaryaa TV (`AaryaaTV.in`), Aaryaa TV (`AaryaaTV.in@SD`), Bang U (`BangU.us`), Cine Western (Spain) (`CineWestern.es@SD`), KTV Bangla (`KTVBangla.in@SD`), Kiss Kiss TV (`KissKissTV.it@SD`), LEO TV (`LEOTV.cz`), Metro TV (`MetroTV.in@SD`), Music Box Sexy (`MusicBoxSexy.cz@SD`), NTC TV (`NTCTV.in@SD`), Only Music (`Only.Music.in`), Pluto TV Cine Familia (`PlutoTVCineFamilia.us@BR`), Pluto TV Cine Romance (`PlutoTVCineRomance.us@BR`), RTL 102.5 Caliente (`RTL1025Caliente.it@SD`), Sonar Bangla (`SonarBangla.in@SD`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray Easy Listening (`StingrayEasyListening.ca@SD`), Stingray Flashback 70's (`StingrayFlashback70s.ca@SD`), Stingray Greatest Holiday Hits (`StingrayGreatestHolidayHits.us@SD`), Stingray Hit List (`StingrayHitList.ca`), Stingray Hot Country (`StingrayHotCountry.ca@SD`), Stingray Jukebox Oldies (`StingrayJukeboxOldies.ca@SD`), Stingray Nothin' But 90s (`StingrayNothinBut90s.ca@SD`), Stingray Pop Adult (`StingrayPopAdult.ca@SD`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray Smooth Jazz (`StingraySmoothJazz.ca@SD`), Stingray Soul Storm (`StingraySoulStorm.ca@SD`), Stingray The Spa (`StingrayTheSpa.ca`), Stingray The Spa (`StingrayTheSpa.ca@SD`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Suriya TV (`SuriyaTV.in`), Suriya TV (`SuriyaTV.in@SD`), Ultimate TV (`UltimateTV.in@SD`), Metro (`custom.24-7-xxx-metro`), Reality Kings (`custom.24-7-xxx-reality-kings`), Dhoom Music Bangla (`custom.bdix.dhoom-music-bangla`), Brazzers Europe (`custom.xxx-brazzers-europe`), Ero Xxx (`custom.xxx-ero-xxx`), Hustler (`custom.xxx-hustler`), Super One (`custom.xxx-super-one`), Vivid Red (`custom.xxx-vivid-red`)
- Published current/future IDs not counted source-current/future: **0**
- Published current/future IDs not counted source-current/future: none


## Playlist EPG Headers

| Playlist | Header status |
|---|---|
| IPTV-Playlist.m3u | OK |
| International-Playlist.m3u | OK |

## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **c0c115f5324a59094ecc502e03a3358f243ec4f6e74dc583e650e5009bf997b6**
- International-Playlist.m3u SHA-256: **0b7ad38c19aeedcba6d5b239ca9a83747bc8ae4c21ec6983a355e214665ebde1**

