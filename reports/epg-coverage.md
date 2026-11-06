# EPG Coverage & Mapping Report

Generated: **2026-11-06T14:12:23+00:00**

This report audits active unique channel identities across the two maintained playlists configured in the automated EPG pipeline. A source mapping is not counted as usable current/future coverage unless it has a valid programme interval and valid non-empty multilingual title data within the generator's -6-hour/+7-day window; English titles rank first, then Bengali, then other valid languages.
The XMLTV guide is published at **epg/epg.xml**. The published guide uses the playlist's tvg-id as the XMLTV channel ID, not the upstream provider's source ID.

## Overall Coverage

- Active unique playlist channel IDs audited: **2785**
- IDs with an EPG source mapping: **1159/2785 (41.6%)**
- IDs with usable current/future source schedules (nonblank multilingual titles (English preferred, then Bengali, then other valid languages)): **1109/2785 (39.8%)**
- IDs with no EPG source mapping: **1626**

## Coverage by Playlist Group

| Group | Active IDs | Mapped IDs | Current/future | No mapping |
|---|---:|---:|---:|---:|
| Adult | 351 | 11 | 11 | 340 |
| Argentina | 18 | 1 | 1 | 17 |
| Aruba | 6 | 0 | 0 | 6 |
| Austria | 4 | 0 | 0 | 4 |
| Bangladesh | 77 | 5 | 3 | 72 |
| Brazil | 12 | 3 | 3 | 9 |
| Bulgaria | 20 | 6 | 6 | 14 |
| Canada | 34 | 25 | 25 | 9 |
| Chile | 24 | 1 | 1 | 23 |
| China | 13 | 3 | 3 | 10 |
| Colombia | 15 | 1 | 0 | 14 |
| Costa Rica | 13 | 0 | 0 | 13 |
| Czech Republic | 26 | 17 | 17 | 9 |
| Documentary & Wildlife | 201 | 148 | 140 | 53 |
| Dominican Republic | 11 | 1 | 0 | 10 |
| Ecuador | 8 | 0 | 0 | 8 |
| Estonia | 6 | 1 | 1 | 5 |
| France | 48 | 17 | 16 | 31 |
| Germany | 40 | 29 | 29 | 11 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 18 | 8 | 8 | 10 |
| Indian Bangla | 40 | 32 | 29 | 8 |
| Indian Entertainment | 219 | 183 | 174 | 36 |
| Indian Movies | 84 | 63 | 62 | 21 |
| Indian Music | 73 | 59 | 56 | 14 |
| International | 200 | 61 | 56 | 139 |
| Iran | 18 | 3 | 3 | 15 |
| Italy | 32 | 13 | 13 | 19 |
| Kids | 204 | 106 | 101 | 98 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 17 | 7 | 6 | 10 |
| Netherlands | 21 | 9 | 9 | 12 |
| New Backups | 9 | 8 | 8 | 1 |
| New Channels | 117 | 22 | 20 | 95 |
| Pakistani | 17 | 2 | 2 | 15 |
| Panama | 6 | 0 | 0 | 6 |
| Paraguay | 10 | 0 | 0 | 10 |
| Peru | 13 | 0 | 0 | 13 |
| Poland | 33 | 18 | 18 | 15 |
| Portugal | 5 | 1 | 1 | 4 |
| Religious | 35 | 10 | 9 | 25 |
| Romania | 33 | 10 | 10 | 23 |
| Russia | 86 | 35 | 32 | 51 |
| Saudi Arabia | 10 | 0 | 0 | 10 |
| Serbia | 6 | 1 | 1 | 5 |
| Singapore | 6 | 1 | 1 | 5 |
| Spain | 17 | 4 | 4 | 13 |
| Sports | 254 | 123 | 120 | 131 |
| Sweden | 12 | 6 | 6 | 6 |
| Turkey | 15 | 0 | 0 | 15 |
| Ukraine | 28 | 9 | 9 | 19 |
| United Kingdom | 14 | 3 | 3 | 11 |
| United States | 180 | 90 | 89 | 90 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Source Status

- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz — 946 channel IDs; 701 IDs with usable current/future programmes; 87270 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz — 54 channel IDs; 5 IDs with usable current/future programmes; 42 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz — 557 channel IDs; 522 IDs with usable current/future programmes; 17961 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — https://iptv-epg.org/files/epg-pk.xml.gz — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 404: Not Found
- **FAILED** — https://www.free-epg.de/api/epg/pk.xml.gz — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 503: Service Unavailable
- **OK** — https://iptv-epg.org/files/epg-in.xml.gz — 419 channel IDs; 269 IDs with usable current/future programmes; 52400 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://epg.lat/files/in.xml.gz — 1166 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://epg.lat/files/us.xml.gz — 4456 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.free-epg.de/api/epg/in.xml.gz — 947 channel IDs; 763 IDs with usable current/future programmes; 60904 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.free-epg.de/api/epg/us.xml.gz — 5541 channel IDs; 5538 IDs with usable current/future programmes; 163206 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.open-epg.com/files/india.xml.gz — 1178 channel IDs; 643 IDs with usable current/future programmes; 30881 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ar.xml.gz — 185 channel IDs; 139 IDs with usable current/future programmes; 13872 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-bg.xml.gz — 116 channel IDs; 90 IDs with usable current/future programmes; 11714 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-br.xml.gz — 182 channel IDs; 133 IDs with usable current/future programmes; 23976 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ca.xml.gz — 808 channel IDs; 802 IDs with usable current/future programmes; 111520 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://iptv-epg.org/files/epg-cl.xml.gz — 184 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://iptv-epg.org/files/epg-co.xml.gz — 180 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-cz.xml.gz — 261 channel IDs; 221 IDs with usable current/future programmes; 49779 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-de.xml.gz — 438 channel IDs; 381 IDs with usable current/future programmes; 65186 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-es.xml.gz — 300 channel IDs; 276 IDs with usable current/future programmes; 31212 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-fr.xml.gz — 485 channel IDs; 377 IDs with usable current/future programmes; 38500 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-gr.xml.gz — 177 channel IDs; 163 IDs with usable current/future programmes; 14665 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-hk.xml.gz — 176 channel IDs; 128 IDs with usable current/future programmes; 21147 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-hu.xml.gz — 152 channel IDs; 131 IDs with usable current/future programmes; 28465 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-it.xml.gz — 306 channel IDs; 264 IDs with usable current/future programmes; 33236 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-mx.xml.gz — 175 channel IDs; 139 IDs with usable current/future programmes; 16391 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-nl.xml.gz — 184 channel IDs; 154 IDs with usable current/future programmes; 37153 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://iptv-epg.org/files/epg-pe.xml.gz — 128 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-pl.xml.gz — 447 channel IDs; 403 IDs with usable current/future programmes; 85540 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-pt.xml.gz — 195 channel IDs; 145 IDs with usable current/future programmes; 28811 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ro.xml.gz — 282 channel IDs; 257 IDs with usable current/future programmes; 41266 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ru.xml.gz — 223 channel IDs; 198 IDs with usable current/future programmes; 44572 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-rs.xml.gz — 265 channel IDs; 240 IDs with usable current/future programmes; 25089 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-se.xml.gz — 95 channel IDs; 80 IDs with usable current/future programmes; 15215 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-tr.xml.gz — 108 channel IDs; 81 IDs with usable current/future programmes; 17439 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-gb.xml.gz — 932 channel IDs; 875 IDs with usable current/future programmes; 87412 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-at.xml.gz — 286 channel IDs; 262 IDs with usable current/future programmes; 41446 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-au.xml.gz — 490 channel IDs; 486 IDs with usable current/future programmes; 45936 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-cr.xml.gz — 84 channel IDs; 78 IDs with usable current/future programmes; 8269 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-pa.xml.gz — 121 channel IDs; 113 IDs with usable current/future programmes; 10142 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-py.xml.gz — 79 channel IDs; 70 IDs with usable current/future programmes; 8497 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-sg.xml.gz — 209 channel IDs; 153 IDs with usable current/future programmes; 26397 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/at.xml.gz — 286 channel IDs; 262 IDs with usable current/future programmes; 41446 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/cn.xml.gz — 711 channel IDs; 561 IDs with usable current/future programmes; 16255 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/cr.xml.gz — 84 channel IDs; 78 IDs with usable current/future programmes; 8269 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://free-epg.de/api/epg/ec.xml.gz — 104 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — https://free-epg.de/api/epg/ee.xml.gz — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 503: Service Unavailable
- **OK** — https://free-epg.de/api/epg/pa.xml.gz — 121 channel IDs; 113 IDs with usable current/future programmes; 10141 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/sa.xml.gz — 138 channel IDs; 18 IDs with usable current/future programmes; 810 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://free-epg.de/api/epg/ua.xml.gz — 231 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/in.xml — 206 channel IDs; 200 IDs with usable current/future programmes; 2054 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/us.xml — 593 channel IDs; 592 IDs with usable current/future programmes; 5015 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml — 697 channel IDs; 629 IDs with usable current/future programmes; 51712 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz — 717 channel IDs; 494 IDs with usable current/future programmes; 8550 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=IN1.xml.gz — 946 channel IDs; 701 IDs with usable current/future programmes; 62044 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=IN4.xml.gz — 557 channel IDs; 495 IDs with usable current/future programmes; 8533 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://m3u-edit.com/epg-source.php?file=india_dishtv.in.xml — 394 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml — 762 channel IDs; 738 IDs with usable current/future programmes; 75698 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml — 1496 channel IDs; 1320 IDs with usable current/future programmes; 62623 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml — 286 channel IDs; 243 IDs with usable current/future programmes; 6727 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml — 120 channel IDs; 107 IDs with usable current/future programmes; 22247 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/slingtv.xml — 6 channel IDs; 6 IDs with usable current/future programmes; 137 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/epg.xml.gz — 2272 channel IDs; 1357 IDs with usable current/future programmes; 21093 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/jioepg.xml.gz — 1173 channel IDs; 85 IDs with usable current/future programmes; 1206 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/tsepg.xml.gz — 717 channel IDs; 697 IDs with usable current/future programmes; 32440 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz — 487 channel IDs; 385 IDs with usable current/future programmes; 28482 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.open-epg.com/files/unitedkingdom.xml.gz — 566 channel IDs; 539 IDs with usable current/future programmes; 26340 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz — 791 channel IDs; 771 IDs with usable current/future programmes; 59572 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-us.xml.gz — 12843 channel IDs; 12106 IDs with usable current/future programmes; 928569 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz — 912 channel IDs; 822 IDs with usable current/future programmes; 87347 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz — 345 channel IDs; 282 IDs with usable current/future programmes; 37493 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz — 696 channel IDs; 695 IDs with usable current/future programmes; 65581 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CH1.xml.gz — 751 channel IDs; 726 IDs with usable current/future programmes; 60051 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CZ1.xml.gz — 1087 channel IDs; 537 IDs with usable current/future programmes; 39759 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DE1.xml.gz — 266 channel IDs; 250 IDs with usable current/future programmes; 19812 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DO1.xml.gz — 56 channel IDs; 55 IDs with usable current/future programmes; 3211 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_ES1.xml.gz — 256 channel IDs; 240 IDs with usable current/future programmes; 17190 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_FR1.xml.gz — 574 channel IDs; 531 IDs with usable current/future programmes; 53470 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_GR1.xml.gz — 321 channel IDs; 303 IDs with usable current/future programmes; 19515 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz — 143 channel IDs; 132 IDs with usable current/future programmes; 13444 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HU1.xml.gz — 193 channel IDs; 169 IDs with usable current/future programmes; 16116 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IT1.xml.gz — 195 channel IDs; 155 IDs with usable current/future programmes; 14456 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz — 163 channel IDs; 131 IDs with usable current/future programmes; 10141 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MX1.xml.gz — 178 channel IDs; 164 IDs with usable current/future programmes; 11924 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_NL1.xml.gz — 159 channel IDs; 156 IDs with usable current/future programmes; 21303 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_PL1.xml.gz — 636 channel IDs; 581 IDs with usable current/future programmes; 83525 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_RO1.xml.gz — 370 channel IDs; 356 IDs with usable current/future programmes; 33311 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_SA2.xml.gz — 31 channel IDs; 31 IDs with usable current/future programmes; 3246 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_TR1.xml.gz — 178 channel IDs; 141 IDs with usable current/future programmes; 12970 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR1.xml.gz — 266 channel IDs; 109 IDs with usable current/future programmes; 16187 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR2.xml.gz — 97 channel IDs; 92 IDs with usable current/future programmes; 7880 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://hum.tv/schedule/ — 1 channel IDs; 1 IDs with usable current/future programmes; 22 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — RTV official daily schedule (Bangladesh) — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; Could not obtain a current official RTV schedule over verified HTTPS (rtvonline: no daily schedule article link on homepage; rtvbd.tv: URLError; www.rtvbd.tv: URLError)
- **OK** — https://migrate.btvlive.gov.bd/channel/BTV — 1 channel IDs; 1 IDs with usable current/future programmes; 64 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — Maasranga official weekly grid (undated) — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 403: Forbidden
- **NO_PROGRAMMES** — M3U4U XMLTV (private Actions secret) — 229 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — iptv-org/epg (targeted build-time guide) — 218 channel IDs; 178 IDs with usable current/future programmes; 9105 eligible programme rows with valid non-empty titles in any language in the guide window

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
| Argentina | Allegro | AllegroHD.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Azahares Radiovisual Multimedia | AzaharesRadiovisualMultimedia.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Beats Radio | custom.beats-radio-ar-music | - | NO_GUIDE_HIT |
| Argentina | Chamame TV | ChamameTV.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Cumbia Mix | CumbiaMix.ar@HD | - | NO_GUIDE_HIT |
| Argentina | HTV Argentina | HTV.us@Argentina | - | NO_GUIDE_HIT |
| Argentina | La 100 | La100.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Mas FM | custom.mas-fm-ar-music | - | NO_GUIDE_HIT |
| Argentina | Quiero Musica en mi Idioma | QuieroMusicaenmiIdioma.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Radio Realpolitik | custom.radio-realpolitik-ar-music | - | NO_GUIDE_HIT |
| Argentina | Retroclub | custom.retroclub-ar-music | - | NO_GUIDE_HIT |
| Argentina | Rock & Pop | RockPop.ar@SD | - | NO_GUIDE_HIT |
| Argentina | The Cabbin FM | custom.the-cabbin-fm-ar-music | - | NO_GUIDE_HIT |
| Argentina | X Level Media | XLevelMedia.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Xtrema Accion | XtremaAccion.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Xtrema Cine Clasico | XtremaCineClasico.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Xtrema Terror | XtremaTerror.ar@SD | - | NO_GUIDE_HIT |
| Aruba | Cool FM 98.9 | custom.cool-fm-98-9-aw-music | - | NO_GUIDE_HIT |
| Aruba | Heart Radio Aruba | custom.heart-radio-aruba-aw-music | - | NO_GUIDE_HIT |
| Aruba | Power 101.7 FM | custom.power-101-7-fm-aw-music | - | NO_GUIDE_HIT |
| Aruba | VIP TV | custom.vip-tv-aw-music | - | NO_GUIDE_HIT |
| Aruba | Wavez FM | custom.wavez-fm-aw-music | - | NO_GUIDE_HIT |
| Aruba | X 102.7 FM | custom.x-102-7-fm-aw-music | - | NO_GUIDE_HIT |
| Austria | Antenne Kaernten | AntenneKaernten.at@SD | - | NO_GUIDE_HIT |
| Austria | Antenne Steiermark | AntenneSteiermark.at@SD | - | NO_GUIDE_HIT |
| Austria | Hitradio O3 | custom.hitradio-o3-at-music | - | NO_GUIDE_HIT |
| Austria | Melodie TV | custom.melodie-tv-at-music | - | NO_GUIDE_HIT |
| Bangladesh | Maasranga TV | MaasrangaTV.bd | MaasrangaTV.bd | MAPPED_NOT_CURRENTLY_FOUND |
| Bangladesh | RTV | RTV.bd | RTV.bd | MAPPED_NOT_CURRENTLY_FOUND |
| Bangladesh | Ananda TV | AnandaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Asian TV | AsianTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | ATN Bangla | ATNBangla.bd | - | NO_GUIDE_HIT |
| Bangladesh | ATN Bangla | ATNBangla.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | ATN News | ATNNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ayna TV | custom.bdix.ayna-tv | - | NO_GUIDE_HIT |
| Bangladesh | Bangla TV | BanglaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bangla Vision | BanglaVision.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bengali Beats | BengaliBeats.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bijoy TV | BijoyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Boishakhi TV | BoishakhiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV Chattogram | BTVChattogram.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV News | BTVNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 1 | Channel1.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 16 | Channel16.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 24 | Channel24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 52 | Channel52.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel I | ChannelI.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel S | ChannelS.uk | - | NO_GUIDE_HIT |
| Bangladesh | Channel S UK | ChannelS.uk@679aa9 | - | NO_GUIDE_HIT |
| Bangladesh | DBC News | DBCNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Deepto TV | DeeptoTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Desh TV | DeshTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Deshe Bideshe | DesheBideshe.ca | - | NO_GUIDE_HIT |
| Bangladesh | Deshi TV | DeshiTV.ca@SD | - | NO_GUIDE_HIT |
| Bangladesh | Doyel TV | DoyelTV.ca@SD | - | NO_GUIDE_HIT |
| Bangladesh | Drama 24 | custom.bdix.drama-24 | - | NO_GUIDE_HIT |
| Bangladesh | Duronto TV | DurontoTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekattor TV | EkattorTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekhon TV | EkhonTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekushey TV | EkusheyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Enter TV | EnterTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | G Series Drama | GSeriesDrama.bd | - | NO_GUIDE_HIT |
| Bangladesh | G TV | GaziTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Global TV | GlobalTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Green TV | GreenTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | Independent TV | IndependentTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jago News 24 | JagoNews24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jalsha Bangla BD | JalshaBanglaBD.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jamuna TV | JamunaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jhankar TV | JhankarTV.ca | - | NO_GUIDE_HIT |
| Bangladesh | Jonmobhumi TV | JonmobhumiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Matribhumi TV | MatribhumiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Matribhumi TV | MatribhumiTV.bd@HD | - | NO_GUIDE_HIT |
| Bangladesh | ME TV | METV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Mohona TV | MohonaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Movie Bangla | MovieBangla.bd | - | NO_GUIDE_HIT |
| Bangladesh | Movie Bangla | MovieBangla.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | MUSIC BANGLA | MUSICBANGLA | - | NO_GUIDE_HIT |
| Bangladesh | My TV | MyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Nagorik TV | NagorikTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | NAN TV | NANTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | News 21 | News21BanglaTV.bd@SD | - | NO_GUIDE_HIT |
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
| Bangladesh | Star News | StarNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | TBN24 | TBN24.us | - | NO_GUIDE_HIT |
| Bangladesh | Thikana | ThikanaTV.us | - | NO_GUIDE_HIT |
| Bangladesh | Time Television | TimeTelevision.us | - | NO_GUIDE_HIT |
| Brazil | +MaisUm | PlusMaisUm.br@HD | - | NO_GUIDE_HIT |
| Brazil | AMC Latin America Brazil | AMCLatinAmerica.us@Brazil | - | NO_GUIDE_HIT |
| Brazil | CINDIE TV | CINDIETV.br@HD | - | NO_GUIDE_HIT |
| Brazil | Classique TV | ClassiqueTV.br@SD | - | NO_GUIDE_HIT |
| Brazil | Ghost TV (712p) [Not 24/7] | GhostTV.br@SD | - | NO_GUIDE_HIT |
| Brazil | KpopTV Play | KpopTVPlay.br@SD | - | NO_GUIDE_HIT |
| Brazil | Lamore Rock Show WebTV | LamoreRockShowWebTV.br@SD | - | NO_GUIDE_HIT |
| Brazil | Rádio Temas de Novelas | custom.radio-temas-de-novelas-br-music | - | NO_GUIDE_HIT |
| Brazil | TikTok Radio Brasil | custom.tiktok-radio-brasil-br-music | - | NO_GUIDE_HIT |
| Bulgaria | AMC Europe Bulgary | AMCEurope.uk@Bulgary | - | NO_GUIDE_HIT |
| Bulgaria | BOX TV | BOXTV.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | bTV Lady | bTVLady.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | cine.box | cinebox.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | CineStar 1 Bulgaria | CineStar1Bulgaria.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | CineStar Action Bulgaria | CineStarActionBulgaria.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | City TV (Bulgaria) | CityTV.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | DSTV (Bulgaria) | DSTV.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | FILMBOX+ Emotion Bulgaria | FILMBOXPlusEmotion.pl@Bulgaria | - | NO_GUIDE_HIT |
| Bulgaria | Hit Mix Music | HitMixMusic.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | Movie Star (720p) | MovieStar.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | Tiankov Folk | TiankovFolk.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | Tiankov Orient Folk | TiankovOrientFolk.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | TV1000 | TV1000.bg@SD | - | NO_GUIDE_HIT |
| Canada | Afghan Nobel Movies (720p) | AfghanNobelMovies.ca@SD | - | NO_GUIDE_HIT |
| Canada | CKNO-FM | custom.ckno-fm-ca-music | - | NO_GUIDE_HIT |
| Canada | Pamir TV | PamirTV.ca@SD | - | NO_GUIDE_HIT |
| Canada | Stingray Cityscapes | custom.stingray-cityscapes-ca-music | - | NO_GUIDE_HIT |
| Canada | Stingray Everything '80s | StingrayEverything80s.ca@SD | - | NO_GUIDE_HIT |
| Canada | Stingray Holiday Hits | StingrayHolidayHits.ca@SD | - | NO_GUIDE_HIT |
| Canada | Stingray Rock Alternative | StingrayRockAlternative.ca | - | NO_GUIDE_HIT |
| Canada | Stingray TikTok Radio | custom.stingray-tiktok-radio-ca-music | - | NO_GUIDE_HIT |
| Canada | Stingray Urban Beat | custom.stingray-urban-beat-ca-music | - | NO_GUIDE_HIT |
| Chile | 13 Festival | 13Festival.cl@SD | - | NO_GUIDE_HIT |
| Chile | AE Radio TV | custom.ae-radio-tv-cl-music | - | NO_GUIDE_HIT |
| Chile | Chocolate FM | custom.chocolate-fm-cl-music | - | NO_GUIDE_HIT |
| Chile | Dance FM | custom.dance-fm-cl-music | - | NO_GUIDE_HIT |
| Chile | FM Plus TV | custom.fm-plus-tv-cl-music | - | NO_GUIDE_HIT |
| Chile | Genial TV | GenialTV.cl@SD | - | NO_GUIDE_HIT |
| Chile | La Clave | LaClave.cl@SD | - | NO_GUIDE_HIT |
| Chile | Patagonia Radio TV | custom.patagonia-radio-tv-cl-music | - | NO_GUIDE_HIT |
| Chile | Pauta | Pauta.cl@SD | - | NO_GUIDE_HIT |
| Chile | Radio Duna | custom.radio-duna-cl-music | - | NO_GUIDE_HIT |
| Chile | Radio Edelweiss | custom.radio-edelweiss-cl-music | - | NO_GUIDE_HIT |
| Chile | Radio La Serena TV | custom.radio-la-serena-tv-cl-music | - | NO_GUIDE_HIT |
| Chile | Radio Pudahuel | custom.radio-pudahuel-cl-music | - | NO_GUIDE_HIT |
| Chile | Radio Suyai TV | custom.radio-suyai-tv-cl-music | - | NO_GUIDE_HIT |
| Chile | Radio Zona 90.3 | custom.radio-zona-90-3-cl-music | - | NO_GUIDE_HIT |
| Chile | Retromusica Television | RetromusicaTelevision.cl@SD | - | NO_GUIDE_HIT |
| Chile | Ritoque TV | RitoqueTV.cl@SD | - | NO_GUIDE_HIT |
| Chile | Sabor TV | SaborTV.cl@SD | - | NO_GUIDE_HIT |
| Chile | Sensacion Costa | SensacionCosta.cl@SD | - | NO_GUIDE_HIT |
| Chile | Solo Bailalo | SoloBailalo.cl@SD | - | NO_GUIDE_HIT |
| Chile | TCM Latin America Chile | TCMLatinAmerica.us@Chile | - | NO_GUIDE_HIT |
| Chile | Teleangol Radio | custom.teleangol-radio-cl-music | - | NO_GUIDE_HIT |
| Chile | V Classic TV | VClassicTV.cl@SD | - | NO_GUIDE_HIT |
| China | CCTV-6 [Geo-blocked] | CCTV6.cn@SD | - | NO_GUIDE_HIT |
| China | CCTV-Storm Music | CCTVStormMusic.cn@HD | - | NO_GUIDE_HIT |
| China | CCTV-Storm Theater | CCTVStormTheater.cn@HD | - | NO_GUIDE_HIT |
| China | CCTV-The First Theater | CCTVTheFirstTheater.cn@HD | - | NO_GUIDE_HIT |
| China | CHC Action (1080p) | CHCAction.cn@SD | - | NO_GUIDE_HIT |
| China | CND Film Middle School Channel | CNDFilmMiddleSchoolChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Harbin Movie Channel | HarbinMovieChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Jiangsu Movie Channel (576p) | JiangsuMovieChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Jiangxi Movie Channel | JiangxiMovieChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Jilin Movie Channel | JilinMovieChannel.cn@SD | - | NO_GUIDE_HIT |
| Colombia | Rumba TV | RumbaTV.co@SD | RumbaTV.co | MAPPED_NOT_CURRENTLY_FOUND |
| Colombia | Buenisima Radio TV | custom.buenisima-radio-tv-co-music | - | NO_GUIDE_HIT |
| Colombia | Canal Cine Dios | custom.canal-cine-dios-co-movie | - | NO_GUIDE_HIT |
| Colombia | Claro Musica TV | ClaroMusicaTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | Fiesta TV | FiestaTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | La Kalle | custom.la-kalle-co-music | - | NO_GUIDE_HIT |
| Colombia | La Morada Radio TV | custom.la-morada-radio-tv-co-music | - | NO_GUIDE_HIT |
| Colombia | MasMusica FM | custom.masmusica-fm-co-music | - | NO_GUIDE_HIT |
| Colombia | MCI Television | custom.mci-television-co-movie | - | NO_GUIDE_HIT |
| Colombia | Parranda Vallenata | ParrandaVallenata.co@SD | - | NO_GUIDE_HIT |
| Colombia | Radiola TV | RadiolaTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | Ranchenato TV | RanchenatoTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | Reyali | Reyali.co@SD | - | NO_GUIDE_HIT |
| Colombia | Salsa Gorda Television | SalsaGordaTelevision.co@SD | - | NO_GUIDE_HIT |
| Colombia | Supermusica TV | SupermusicaTV.co@SD | - | NO_GUIDE_HIT |
| Costa Rica | 88 Stereo | 88Stereo.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | Canal 3 KMK TV | Canal3KMKTV.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | Cedros TV | custom.cedros-tv-cr-music | - | NO_GUIDE_HIT |
| Costa Rica | Conexión Positiva Televisión | custom.conexion-positiva-television-cr-music | - | NO_GUIDE_HIT |
| Costa Rica | Gex TV | GexTV.cr@HD | - | NO_GUIDE_HIT |
| Costa Rica | IQ Channel | IQChannel.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | Oldies Hits | custom.oldies-hits-cr-music | - | NO_GUIDE_HIT |
| Costa Rica | SOY Plancha TV | SOYPlanchaTV.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | Urbano TV | UrbanoTV.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | Video Tour Channel | custom.video-tour-channel-cr-music | - | NO_GUIDE_HIT |
| Costa Rica | Vintage Music | VintageMusic.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | VM Latino | VMLatino.cr@SD | - | NO_GUIDE_HIT |
| Costa Rica | VoiceOver Radio TV | custom.voiceover-radio-tv-cr-music | - | NO_GUIDE_HIT |
| Czech Republic | AXN Black (United States) Czech Republic | AXNBlack.us@CzechRepublic | - | NO_GUIDE_HIT |
| Czech Republic | AXN CEE Czech Republic | AXNCEE.es@CzechRepublic | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ Comedy Czechia | FILMBOXPlusComedy.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ Emotion Czechia | FILMBOXPlusEmotion.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ Hits Czechia | FILMBOXPlusHits.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ One Czechia | FILMBOXPlusOne.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | Ocko Gold | OckoGold.cz@SD | - | NO_GUIDE_HIT |
| Czech Republic | Slager Muzika | SlagerMuzika.cz@SD | - | NO_GUIDE_HIT |
| Czech Republic | Slager Original | SlagerOriginal.cz@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | 4K Travel | Travel.us | 4K.TRAVEL.TV.distro | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | China Travel | ChinaTravel.cn@SD | China.Travel.distro | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Crime & Justice | CrimeJustice.us | plex.tv.Crime.&.Justice.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Discovering China | DiscoveringChina.cn@SD | Discovering.China.distro | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Love The Planet | LoveThePlanet.es@EN | Love.The.Planet.es | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Love the Planet | LoveThePlanet.us | Love.The.Planet.es | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Real Wild | RealWild.uk | RealWild.uk | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Robot Wars by Mech+ | RobotWarsByMech.us | plex.tv.Robot.Wars.by.Mech+.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Adventure Earth | AdventureEarth.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Alone | Alone.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | AlternaTV | AlternaTV.ar@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Amazing Discoveries TV | AmazingDiscoveriesTV.in | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Animal Planet Latin America | AnimalPlanetLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Atlas | Atlas.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic Adventure Earth | AutenticAdventureEarth.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic History | AutenticHistory.de | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic History | AutenticHistory.de@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | BBC Earth Czechia | BBCEarth.uk@Czechia | - | NO_GUIDE_HIT |
| Documentary & Wildlife | BBC Earth Hungary | BBCEarth.uk@Hungary | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Better Life Nature Channel | BetterLifeNatureChannel.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | CCTV-Weapon & Technology | CCTVWeaponTechnology.cn@HD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | ClickTV Chile | ClickTVChile.cl@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | CNA Originals | CNAOriginals.sg@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Asia Taiwan | DiscoveryAsiaTaiwan.tw@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Bangla | custom.bdix.discoverybangla | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Channel Latin America | DiscoveryChannelLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Science Latin America | DiscoveryScienceLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Theater Latin America | DiscoveryTheaterLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Turbo (Italy) | DiscoveryTurbo.it@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Turbo Latin America | DiscoveryTurboLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Velocity | discoveryvelocity.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Ecovision | Ecovision.do@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | History 2 Latin America | History2LatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Documentary & Wildlife | History Asia | HistoryAsia.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | History Latin America | HistoryLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Inside Crime | InsideCrime.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Investigation Discovery (Czech Republic) | InvestigationDiscovery.cz@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Italiana | Italiana.it@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Love Nature en Espanol | LoveNatureenEspanol.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | MWD Documentary | MWDDocumentary.mm@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Mystery TV | MysteryTV.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Nano | Nano.ru@HD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Nat Geo TV | NatGeoTV.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | National Geographic (United States) HD East | NationalGeographic.us@HDEast | - | NO_GUIDE_HIT |
| Documentary & Wildlife | National Geographic Wild (United States) HD East | NationalGeographicWild.us@HDEast | - | NO_GUIDE_HIT |
| Documentary & Wildlife | NatureTime AU | NatureTime.ca@AU | - | NO_GUIDE_HIT |
| Documentary & Wildlife | O'zbekiston Tarixi | OzbekistonTarixi.uz@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | PBS Arts | PBSArts.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Persiana Docs | PersianaDocs.fr@HD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Persiana Travel | PersianaTravel.fr@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | RT Documentary | RTDocumentary.ru@English | - | NO_GUIDE_HIT |
| Documentary & Wildlife | RT Documentary Russian | RTDocumentary.ru@Russian | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Smotrim 100% Fakty | Smotrim100Fakty.ru@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Tochka.rf | Tochkarf.ru | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Travel Channel East | travel.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Travel XP Bangla | custom.bdix.travelxp-bangla | - | NO_GUIDE_HIT |
| Documentary & Wildlife | TVS Hollywood History | TVSHollywoodHistory.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Viasat Nature (Ukraine) | ViasatNature.ua@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Watch Mojo | WatchMojo.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | WaterBear | WaterBear.ch@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Wild Planet | WildPlanet.us | - | NO_GUIDE_HIT |
| Dominican Republic | Tarima TV | TarimaTV.do@HD | plex.tv.Tarima.TV.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Dominican Republic | Boreal | Boreal.do@SD | - | NO_GUIDE_HIT |
| Dominican Republic | Fuego TV | FuegoTV.do@SD | - | NO_GUIDE_HIT |
| Dominican Republic | Maimon TV Canal 3 | MaimonTVCanal3.do@SD | - | NO_GUIDE_HIT |
| Dominican Republic | Makao TV | MakaoTV.do@SD | - | NO_GUIDE_HIT |
| Dominican Republic | Mega Cine TV | MegaCineTV.do@HD | - | NO_GUIDE_HIT |
| Dominican Republic | Montones TV | MontonesTV.do@HD | - | NO_GUIDE_HIT |
| Dominican Republic | Siembra TV (Dominican Republic) | SiembraTV.do@SD | - | NO_GUIDE_HIT |
| Dominican Republic | Tele Dominicana TV | TeleDominicanaTV.do@SD | - | NO_GUIDE_HIT |
| Dominican Republic | Topical Moon RD | TopicalMoonRD.do@HD | - | NO_GUIDE_HIT |
| Dominican Republic | TV Exitos | TVExitos.do@SD | - | NO_GUIDE_HIT |
| Ecuador | El Sol Network TV | ElSolNetworkTV.ec@SD | - | NO_GUIDE_HIT |
| Ecuador | FM Mundo | custom.fm-mundo-ec-music | - | NO_GUIDE_HIT |
| Ecuador | Infinita TV | InfinitaTV.ec@SD | - | NO_GUIDE_HIT |
| Ecuador | Metropoli Medios TV | MetropoliMediosTV.ec@SD | - | NO_GUIDE_HIT |
| Ecuador | Radio Bonita 106.7 | custom.radio-bonita-106-7-ec-music | - | NO_GUIDE_HIT |
| Ecuador | Radio Cuenca Estereo | custom.radio-cuenca-estereo-ec-music | - | NO_GUIDE_HIT |
| Ecuador | Radio Monumental TV | custom.radio-monumental-tv-ec-music | - | NO_GUIDE_HIT |
| Ecuador | Vos y TV | custom.vos-y-tv-ec-music | - | NO_GUIDE_HIT |
| Estonia | Best of Dance TV | BestofDanceTV.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV Algorhythm | DanceTVAlgorhythm.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV Deep House District | DanceTVDeepHouseDistrict.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV House Floor | DanceTVHouseFloor.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV Techno Warehouse | DanceTVTechnoWarehouse.ee@SD | - | NO_GUIDE_HIT |
| France | Trace Brazuca | TraceBrazuca.fr@HD | plex.tv.TRACE.Brazuca.plex | MAPPED_NOT_CURRENTLY_FOUND |
| France | 4 Music | 4Music.fr@SD | - | NO_GUIDE_HIT |
| France | 4Kurd | 4Kurd.fr@SD | - | NO_GUIDE_HIT |
| France | Cine+ Classic | CinePlusClassic.fr@SD | - | NO_GUIDE_HIT |
| France | Cine+ Frisson (1080p) | CinePlusFrisson.fr@SD | - | NO_GUIDE_HIT |
| France | DBM TV | DBMTV.fr@SD | - | NO_GUIDE_HIT |
| France | Littoral FM TV | custom.littoral-fm-tv-fr-music | - | NO_GUIDE_HIT |
| France | P2M TV | P2MTV.fr@SD | - | NO_GUIDE_HIT |
| France | Persiana Cinema | PersianaCinema.fr@SD | - | NO_GUIDE_HIT |
| France | Persiana Folk | PersianaFolk.fr@HD | - | NO_GUIDE_HIT |
| France | Persiana Latino | PersianaLatino.fr@SD | - | NO_GUIDE_HIT |
| France | Persiana Nostalgia | PersianaNostalgia.fr@SD | - | NO_GUIDE_HIT |
| France | Persiana SetMix | custom.persiana-setmix-fr-music | - | NO_GUIDE_HIT |
| France | Persiana Vibe | PersianaVibe.fr@HD | - | NO_GUIDE_HIT |
| France | Qwest TV Jazz & Beyond | QwestTVJazzBeyond.fr@SD | - | NO_GUIDE_HIT |
| France | ScreamIN | ScreamIN.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Afrikora | TraceAfrikora.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Ayiti | TraceAyiti.fr@SD | - | NO_GUIDE_HIT |
| France | Trace Gospel Nigeria and East Africa | custom.trace-gospel-nigeria-and-east-africa-fr-music | - | NO_GUIDE_HIT |
| France | Trace Gospel Southern Africa | custom.trace-gospel-southern-africa-fr-music | - | NO_GUIDE_HIT |
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
| Germany | DASDING 90.8 | DASDING908.de@SD | - | NO_GUIDE_HIT |
| Germany | Deluxe Dance | DeluxeDance.de@SD | - | NO_GUIDE_HIT |
| Germany | Finest TV | FinestTV.de@SD | - | NO_GUIDE_HIT |
| Germany | Medium (Germany) | Medium.de@ES | - | NO_GUIDE_HIT |
| Germany | One Adria | OneAdria.de@SD | - | NO_GUIDE_HIT |
| Germany | Pluto TV Bud & Terence (Germany) | PlutoTVBudTerence.de@DACH | - | NO_GUIDE_HIT |
| Germany | Rakuten TV Action Movies Germany | RakutenTVActionMoviesGermany.es | - | NO_GUIDE_HIT |
| Germany | Rakuten TV Comedy Movies Germany | custom.rakuten-tv-comedy-movies-germany-de-movie | - | NO_GUIDE_HIT |
| Germany | TV Bozsike Hamburg | TVBozsikeHamburgHD.de@HD | - | NO_GUIDE_HIT |
| Greece | Baraza TV | BarazaTV.gr@SD | - | NO_GUIDE_HIT |
| Greece | Baraza TV Deep House | BarazaTVDeepHouse.gr@SD | - | NO_GUIDE_HIT |
| Greece | Baraza TV Relaxing | BarazaTVRelaxing.gr@SD | - | NO_GUIDE_HIT |
| Greece | Ellinikos FM | custom.ellinikos-fm-gr-music | - | NO_GUIDE_HIT |
| Greece | Messatida TV | MessatidaTV.gr@SD | - | NO_GUIDE_HIT |
| Greece | NRG 91 | NRG91.gr@SD | - | NO_GUIDE_HIT |
| Greece | Play TV (Greece) | PlayTV.gr@SD | - | NO_GUIDE_HIT |
| Hungary | AMC Europe Hungary | AMCEurope.uk@Hungary | - | NO_GUIDE_HIT |
| Hungary | AXN Black (United States) Hungary | AXNBlack.us@Hungary | - | NO_GUIDE_HIT |
| Hungary | AXN CEE | AXNCEE.es@Hungary | - | NO_GUIDE_HIT |
| Hungary | Cinemax 2 Central Europe | Cinemax2CentralEurope.hu@SD | - | NO_GUIDE_HIT |
| Hungary | Cinemax Central Europe | CinemaxCentralEurope.hu@SD | - | NO_GUIDE_HIT |
| Hungary | Film Cafe Romania | FilmCafe.hu@Romania | - | NO_GUIDE_HIT |
| Hungary | Film+ (Hungary) | FilmPlus.hu@SD | - | NO_GUIDE_HIT |
| Hungary | FILMBOX+ Emotion Hungary | FILMBOXPlusEmotion.pl@Hungary | - | NO_GUIDE_HIT |
| Hungary | FILMBOX+ Hits Hungary | FILMBOXPlusHits.pl@Hungary | - | NO_GUIDE_HIT |
| Hungary | Oxygen Music | OxygenMusic.hu@HD | - | NO_GUIDE_HIT |
| Indian Bangla | Bangla Jago TV | BanglaJagoTV.in | Bangla.Jago.in | 3019 | jtv3019 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Bangla | Tara TV | TaraTV.in | Tara.TV.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Bangla | ZB Cinema | ZBCinema.in | jtv3322 | 3322 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Bangla | Bangla Plus | BanglaPlus.in | - | NO_GUIDE_HIT |
| Indian Bangla | JTV Bangla | JTVBangla.in@SD | - | NO_GUIDE_HIT |
| Indian Bangla | JTV Classic | JTVClassic.in | - | NO_GUIDE_HIT |
| Indian Bangla | Orange Bangla TV | OrangeBanglaTV.in@SD | - | NO_GUIDE_HIT |
| Indian Bangla | Sananda | SanandaTV.in | - | NO_GUIDE_HIT |
| Indian Bangla | Sananda TV | custom.sananda-tv | - | NO_GUIDE_HIT |
| Indian Bangla | SNB Cinema | SNBCinema.in | - | NO_GUIDE_HIT |
| Indian Bangla | Zodiak TV | ZodiakTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | 4 SiDES TV | 4SiDESTV.in@SD | jtv3529 | 3529 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Friends TV | FriendsTV.in@SD | Friends.TV.in | jtv2354 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Global Punjab | GlobalPunjab.in | Global.Punjab.in | 2019 | jtv2019 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Jatra Ekamra | JatraEkamra.in@SD | Jatra.Ekamra.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Manoranjan Prime | ManoranjanPrime.in@SD | 154892 | 10000000075992492 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | One Paschima | OnePaschima.in@SD | One.Paschima.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Shemaroo Umang | ShemarooUmang.in@SD | ShemarooUmang.in | 143779 | SHEMAROO.UMANG.in | Shemaroo.Umang.in | jtv2078 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Suriyan TV | SuriyanTV.in@SD | ts1384 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Zingabad | Zingabad.in@SD | 7258 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Asianet Middle East | AsianetMiddleEast.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Baiscope TV | BaiscopeTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | BT TV | BTTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | CCV | CCV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors MENA | ColorsMENA.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors MENA | ColorsMENA.in@HD | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors Rishtey Americas | ColorsRishteyAmericas.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Flowers US | Flowers.us | - | NO_GUIDE_HIT |
| Indian Entertainment | GTC Punjabi US | GTCPunjabi.in@US | - | NO_GUIDE_HIT |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Kalika TV | KalikaTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | KCL TV | KCLTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Kerala Vision | KeralaVision.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Maha Punjabi | MahaPunjabi.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Marutam TV | MarutamTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Mei Alai TV | MeiAlaiTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Mh 1 Prime | Mh1Prime.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | MH One Prime | Mh1Prime.in | - | NO_GUIDE_HIT |
| Indian Entertainment | MNTV (Tamil) | MarutamTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | NKR TV Kannada | NKRTVKannada.in | - | NO_GUIDE_HIT |
| Indian Entertainment | NKR TV Kannada | NKRTVKannada.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Pankh | Pankh.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Pardesi TV | PardesiTV.ca | - | NO_GUIDE_HIT |
| Indian Entertainment | Pulari TV | PulariTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Punjabi TV | PunjabiTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | SADA TV | SADATV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | SADA TV | SADATV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Sooriyan TV | SooriyanTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Starnet | Starnet.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Swantham | Swantham.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Tamilan TV | TamilanTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Thendral TV | ThendralTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | TV BRICS English | TVBRICSEnglish.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | UTV Palakkad | UTVPalakkad.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | VCV | VCV.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Ekamra Cinema | EkamraCinema.in | Ekamra.Cinema.in | MAPPED_NOT_CURRENTLY_FOUND |
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
| Indian Movies | K Cine | KCine.in | - | NO_GUIDE_HIT |
| Indian Movies | KCM India | KCM.sg@India | - | NO_GUIDE_HIT |
| Indian Movies | Maha Movie | MahaMovie.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Mango | Mango.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | MH One Movies | MHOneMovies.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Movie Punjab | MoviePunjab.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | - | NO_GUIDE_HIT |
| Indian Movies | Soneri Cinema | SoneriCinema.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Sony Movies | SonyMovies.in | - | NO_GUIDE_HIT |
| Indian Movies | South Movies | SouthMovies.in | - | NO_GUIDE_HIT |
| Indian Movies | Zee Cinema APAC | ZeeCinema.in@APAC | - | NO_GUIDE_HIT |
| Indian Music | Ekamra Musiq | EkamraMusiq.in | Ekamra.Musiq.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Music | Mastiii | Mastiii.in@SD | Mastiii.in | 143308 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Music | Steelbird Music | SteelbirdMusic.in@SD | Steelbird.Music.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Music | 7X Punjabi | 7XPunjabi.in | - | NO_GUIDE_HIT |
| Indian Music | AMN TV | AMNTV.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Andy Haryana | AndyHaryana.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Deewana | DeewanaHD.in | - | NO_GUIDE_HIT |
| Indian Music | Deewana | DeewanaHD.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Hindi Hits | HindiHits.in | - | NO_GUIDE_HIT |
| Indian Music | Hindi Hits | HindiHits.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Oli TV | OliTV.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Punjabi Beats | PunjabiBeatsHD.in@HD | - | NO_GUIDE_HIT |
| Indian Music | Punjabi Music | PunjabiMusicHD.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Rang Rangoli | RangRangoli.in | - | NO_GUIDE_HIT |
| Indian Music | Vision Beats | VisionBeats.in@SD | - | NO_GUIDE_HIT |
| Indian Music | YRF Music Nepal | YRFMusic.in@Nepal | - | NO_GUIDE_HIT |
| Indian Music | Zoom (India) Nepal | Zoom.in@Nepal | - | NO_GUIDE_HIT |
| International | Action Hollywood Movies | plex.tv.Action.Hollywood.Movies.plex | ActionHollywoodMovies.au | MAPPED_NOT_CURRENTLY_FOUND |
| International | AMC Thrillers | plex.tv.AMC.Thrillers.plex | plex.tv.AMC.Thrillers.plex | MAPPED_NOT_CURRENTLY_FOUND |
| International | BBC Drama | BBCDrama.uk | BBCDrama.au | MAPPED_NOT_CURRENTLY_FOUND |
| International | Fashion One | FashionOne.uk | Fashion.One.cz | MAPPED_NOT_CURRENTLY_FOUND |
| International | Shanson TV | ShansonTV.ru | Shanson.TV.cz | MAPPED_NOT_CURRENTLY_FOUND |
| International | 1Mus | 1Mus.us | - | NO_GUIDE_HIT |
| International | 24 Hour Free Movies | custom.24hourfreemovies | - | NO_GUIDE_HIT |
| International | 30A Music | custom.30amusic | - | NO_GUIDE_HIT |
| International | 4ever Cinema | custom.4evercinema | - | NO_GUIDE_HIT |
| International | 4ever Music | custom.4evermusic | - | NO_GUIDE_HIT |
| International | A2i Music | A2iMusic.sn@SD | - | NO_GUIDE_HIT |
| International | Afrobeats | Afrobeats.us | - | NO_GUIDE_HIT |
| International | AlbKanale Music TV | AlbKanaleMusicTV.al@HD | - | NO_GUIDE_HIT |
| International | Allo Cine | AlloCine.cm@SD | - | NO_GUIDE_HIT |
| International | AMG TV Classic | AMGTVClassic.us | - | NO_GUIDE_HIT |
| International | AMusic Channel | custom.amusic-channel-ng-music | - | NO_GUIDE_HIT |
| International | Arabica TV | ArabicaTV.us | - | NO_GUIDE_HIT |
| International | Armenia Premium (720p) | ArmeniaPremium.am@SD | - | NO_GUIDE_HIT |
| International | Asia Flix TV | custom.asia-flix-tv-ph-movie | - | NO_GUIDE_HIT |
| International | Audiokiss | Audiokiss.bo@SD | - | NO_GUIDE_HIT |
| International | Aurora Media Films | AuroraMediaFilms.gt@SD | - | NO_GUIDE_HIT |
| International | AVA FAMILY | AVAFAMILY.us | - | NO_GUIDE_HIT |
| International | AVA SERIES | AVASERIES.us | - | NO_GUIDE_HIT |
| International | Baraza Music TV | custom.barazamusictv | - | NO_GUIDE_HIT |
| International | Bigscreen TV | custom.bigscreen-tv-ph-movie | - | NO_GUIDE_HIT |
| International | Blues TV | custom.bluestv | - | NO_GUIDE_HIT |
| International | BOKTV | BOKTV.za@SD | - | NO_GUIDE_HIT |
| International | BTA TV | BTATV.ve@SD | - | NO_GUIDE_HIT |
| International | CBS TV | CBSTV.us | - | NO_GUIDE_HIT |
| International | CEACOM TV | custom.ceacom-tv-bo-music | - | NO_GUIDE_HIT |
| International | Celestial Movies (576i) | CelestialMovies.hk@SD | - | NO_GUIDE_HIT |
| International | Cinema (Mongolia) (1080p) | Cinema.mn@SD | - | NO_GUIDE_HIT |
| International | CinemaWorld (720p) | CinemaWorld.my@SD | - | NO_GUIDE_HIT |
| International | CMC TV | custom.cmctv | - | NO_GUIDE_HIT |
| International | CTB Perth Movies Channel (720p) | CTBPerthMoviesChannel.au@SD | - | NO_GUIDE_HIT |
| International | Dance TV | DanceTV.us | - | NO_GUIDE_HIT |
| International | Digital Fashion | DigitalFashion.us | - | NO_GUIDE_HIT |
| International | Dong Nai TV 2 | custom.dongnaitv2 | - | NO_GUIDE_HIT |
| International | DW News | DWNews.de | - | NO_GUIDE_HIT |
| International | EBC Foreign Movie | EBCForeignMovie.tw@SD | - | NO_GUIDE_HIT |
| International | EU Music | custom.eumusic | - | NO_GUIDE_HIT |
| International | First Music Channel | FirstMusicChannel.by@SD | - | NO_GUIDE_HIT |
| International | First Music Channel Russia | FirstMusicChannelRussia.by@SD | - | NO_GUIDE_HIT |
| International | Folk Klub TV | FolkKlubTV.au@SD | - | NO_GUIDE_HIT |
| International | Folk TV | FolkTV.mk@SD | - | NO_GUIDE_HIT |
| International | Folx Slovenija | FolxSlovenija.si@SD | - | NO_GUIDE_HIT |
| International | FON Music | FONMusic.us | - | NO_GUIDE_HIT |
| International | Fun Vision | FunVision.be@SD | - | NO_GUIDE_HIT |
| International | Fusion TV | FUSIONTV.mq@SD | - | NO_GUIDE_HIT |
| International | GROOVE | custom.groove | - | NO_GUIDE_HIT |
| International | Gugak TV | GugakTV.kr@SD | - | NO_GUIDE_HIT |
| International | HBO Asia Taiwan | HBOAsia.sg@Taiwan | - | NO_GUIDE_HIT |
| International | Hero | custom.hero-fi-movie | - | NO_GUIDE_HIT |
| International | HMTV (Nigeria) | HMTV.ng@SD | - | NO_GUIDE_HIT |
| International | Identite Tele Caraibes | IdentiteTeleCaraibes.mq@SD | - | NO_GUIDE_HIT |
| International | iFilm English | iFilmEnglish.ir | - | NO_GUIDE_HIT |
| International | INTV Australia | INTVAustralia.au@SD | - | NO_GUIDE_HIT |
| International | Isango TV [ ] | IsangoTV.rw@SD | - | NO_GUIDE_HIT |
| International | Itage TV | ItageTV.ng@SD | - | NO_GUIDE_HIT |
| International | Ivoire Channel | IvoireChannel.ci@SD | - | NO_GUIDE_HIT |
| International | Jordan Songs | JordanSongs.jo@SD | - | NO_GUIDE_HIT |
| International | JRTV Jarviradio | JRTVJarviradio.fi@SD | - | NO_GUIDE_HIT |
| International | K100 | K100.is@SD | - | NO_GUIDE_HIT |
| International | Kantipur Max [Geo-blocked] | KantipurMax.np@SD | - | NO_GUIDE_HIT |
| International | Kayhan TV | KayhanTV.af@SD | - | NO_GUIDE_HIT |
| International | Klara | Klara.be@SD | - | NO_GUIDE_HIT |
| International | Klasik (576p) [Not 24/7] | Klasik.hr@SD | - | NO_GUIDE_HIT |
| International | KN Music TV | KNMusicTV.az@SD | - | NO_GUIDE_HIT |
| International | Konul Music TV | custom.konul-music-tv-az-music | - | NO_GUIDE_HIT |
| International | Kronehit | Kronehit.at | - | NO_GUIDE_HIT |
| International | La Elegida Television | LaElegidaTelevision.uy@SD | - | NO_GUIDE_HIT |
| International | La Top 102.9 | LaTop1029.hn@SD | - | NO_GUIDE_HIT |
| International | La Top 107.7 | LaTop1077.hn@SD | - | NO_GUIDE_HIT |
| International | La-X | LaX.pr@SD | - | NO_GUIDE_HIT |
| International | Live99FM | Live99FM.bq@SD | - | NO_GUIDE_HIT |
| International | Look Thoong TV | LookThoongTV.la@SD | - | NO_GUIDE_HIT |
| International | Love TV | LoveTV.mk@SD | - | NO_GUIDE_HIT |
| International | LRT Klasika | LRTKlasika.lt@SD | - | NO_GUIDE_HIT |
| International | LRT Opus | LRTOpus.lt@SD | - | NO_GUIDE_HIT |
| International | M20 Music | M20Music.us | - | NO_GUIDE_HIT |
| International | Maah TV | MaahTV.my@SD | - | NO_GUIDE_HIT |
| International | Marina TV | custom.marina-tv-kw-music | - | NO_GUIDE_HIT |
| International | MBC 3 USA | custom.mbc3usa | - | NO_GUIDE_HIT |
| International | MBC Drama USA | MBCDramaUSA.us | - | NO_GUIDE_HIT |
| International | MegaBox | MegaBox.ni@SD | - | NO_GUIDE_HIT |
| International | Mei Ah Movie Channel | MeiAhMovieChannel.hk@SD | - | NO_GUIDE_HIT |
| International | Mix Hollywood | MixHollywood.eg@SD | - | NO_GUIDE_HIT |
| International | Mix Hollywood | custom.mixhollywood | - | NO_GUIDE_HIT |
| International | Movie Dome Family | MovieDomeFamily.us | - | NO_GUIDE_HIT |
| International | MovieBox (1080p) | MovieBox.mn@SD | - | NO_GUIDE_HIT |
| International | Movies Thriller | MoviesThriller.sa@SD | - | NO_GUIDE_HIT |
| International | MovieSphere UK | custom.moviesphereuk | - | NO_GUIDE_HIT |
| International | Music Channel | custom.musicchannel | - | NO_GUIDE_HIT |
| International | Muzangala TV | MuzangalaTV.ao@SD | - | NO_GUIDE_HIT |
| International | MWD Movies | MWDMovies.mm@SD | - | NO_GUIDE_HIT |
| International | My Cinema | MyCinema.us | - | NO_GUIDE_HIT |
| International | My Cinema [Geo-blocked] | MyCinema.id@SD | - | NO_GUIDE_HIT |
| International | My Cinema Europe | MyCinemaEurope.ch@SD | - | NO_GUIDE_HIT |
| International | Navahang TV | NavahangTV.fi@SD | - | NO_GUIDE_HIT |
| International | NogoumFMTV | NogoumFMTV.eg@SD | - | NO_GUIDE_HIT |
| International | Noroc TV | NorocTV.md@SD | - | NO_GUIDE_HIT |
| International | Ocko Expres | custom.ockoexpres | - | NO_GUIDE_HIT |
| International | OSN Movies Action (1080p) | OSNMoviesAction.ae@SD | - | NO_GUIDE_HIT |
| International | Oxygen Music | OxygenMusic.us | - | NO_GUIDE_HIT |
| International | Pantalla Clasica EC (512p) [Not 24/7] | PantallaClasicaEC.ec@SD | - | NO_GUIDE_HIT |
| International | Play TV (Cameroon) | PlayTV.cm@SD | - | NO_GUIDE_HIT |
| International | PMC Royale | PMCRoyale.ae@SD | - | NO_GUIDE_HIT |
| International | POP World TV | POPWorldTV.es | - | NO_GUIDE_HIT |
| International | PowerTürk TV | PowerTurkTV.tr | - | NO_GUIDE_HIT |
| International | Rakuten Movies | RakutenMovies | - | NO_GUIDE_HIT |
| International | Rakuten TV Action Movies UK | RakutenTVActionMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Comedy Movies UK | RakutenTVComedyMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Family Movies UK | RakutenTVFamilyMovies.es@UK | - | NO_GUIDE_HIT |
| International | RHT Guadeloupe | RHTGuadeloupe.gp@SD | - | NO_GUIDE_HIT |
| International | RTL Gold (Luxembourg) | RTLGold.lu@SD | - | NO_GUIDE_HIT |
| International | Scorch TV | ScorchTV.tt@SD | - | NO_GUIDE_HIT |
| International | ShowVen TV | ShowVenTV.ve@SD | - | NO_GUIDE_HIT |
| International | Silk Way Cinema | SilkWayCinema.kz@SD | - | NO_GUIDE_HIT |
| International | Sine Plus | custom.sine-plus-ph-movie | - | NO_GUIDE_HIT |
| International | Sky Folk TV | SkyFolkTV.mk@SD | - | NO_GUIDE_HIT |
| International | Sony One Hits Comedie | custom.sonyonehitscomedie | - | NO_GUIDE_HIT |
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
| International | Trace UK | custom.traceuk | - | NO_GUIDE_HIT |
| International | Turkmen Owazy | TurkmenOwazy.tm@SD | - | NO_GUIDE_HIT |
| International | TV Cidade | TVCidade.cv@SD | - | NO_GUIDE_HIT |
| International | TVCARiB Cinema | TVCARiBCinema.sx@SD | - | NO_GUIDE_HIT |
| International | TVONE Nicaragua | TVONENicaragua.ni@SD | - | NO_GUIDE_HIT |
| International | V2 Beat | custom.v2beat | - | NO_GUIDE_HIT |
| International | VAM TV | VAMTV.cw@SD | - | NO_GUIDE_HIT |
| International | Vevo Hip Hop & R&B | GBBD2300001C0 | - | NO_GUIDE_HIT |
| International | Vox Kongo TV | custom.vox-kongo-tv-cd-music | - | NO_GUIDE_HIT |
| International | VTU | VTU.in@SD | - | NO_GUIDE_HIT |
| International | XITE Summer | custom.xitesummer | - | NO_GUIDE_HIT |
| International | Yes Movies Action | YesMoviesAction.il@SD | - | NO_GUIDE_HIT |
| International | Young Hollywood | YoungHollywood.us | - | NO_GUIDE_HIT |
| Iran | AFN TV | AFNTV.ir@SD | - | NO_GUIDE_HIT |
| Iran | Afra Film | custom.afra-film-ir-movie | - | NO_GUIDE_HIT |
| Iran | Bravo Farsi TV (360p) | BravoFarsiTV.ir@SD | - | NO_GUIDE_HIT |
| Iran | Cafe Film | CafeFilm.ir@SD | - | NO_GUIDE_HIT |
| Iran | iFilm 2 | iFilm2.ir@SD | - | NO_GUIDE_HIT |
| Iran | iFilm English | iFilmEnglish.ir@SD | - | NO_GUIDE_HIT |
| Iran | iFilm Persian | iFilmPersian.ir@SD | - | NO_GUIDE_HIT |
| Iran | Meta Film TV | MetaFilmTV.ir@SD | - | NO_GUIDE_HIT |
| Iran | NewFlix | NewFlix.ir@SD | - | NO_GUIDE_HIT |
| Iran | Persiana Family | custom.persiana-family-ir-movie | - | NO_GUIDE_HIT |
| Iran | Persiana Iranian | custom.persiana-iranian-ir-movie | - | NO_GUIDE_HIT |
| Iran | Persiana Korea | custom.persiana-korea-ir-movie | - | NO_GUIDE_HIT |
| Iran | Persiana Plus | custom.persiana-plus-ir-movie | - | NO_GUIDE_HIT |
| Iran | SL 1 | custom.sl-1-ir-movie | - | NO_GUIDE_HIT |
| Iran | SL 2 | custom.sl-2-ir-movie | - | NO_GUIDE_HIT |
| Italy | 7 RadioVisione | 7RadioVisione.it@HD | - | NO_GUIDE_HIT |
| Italy | 70-80 TV | 7080TV.it@SD | - | NO_GUIDE_HIT |
| Italy | Company TV | CompanyTV.it@SD | - | NO_GUIDE_HIT |
| Italy | Euro Indie Music Chart TV | EuroIndieMusicChartTV.it@SD | - | NO_GUIDE_HIT |
| Italy | FM ITALIA | custom.fm-italia-it-music | - | NO_GUIDE_HIT |
| Italy | Kiss Kiss Napoli TV | KissKissNapoliTV.it@SD | - | NO_GUIDE_HIT |
| Italy | m2o TV | m2oTV.it@SD | - | NO_GUIDE_HIT |
| Italy | Radio Bruno TV | custom.radio-bruno-tv-it-music | - | NO_GUIDE_HIT |
| Italy | Radio Capital TiVu | custom.radio-capital-tivu-it-music | - | NO_GUIDE_HIT |
| Italy | Radio Piter Pan TV | custom.radio-piter-pan-tv-it-music | - | NO_GUIDE_HIT |
| Italy | Radio Zeta | custom.radio-zeta-it-music | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Action Movies Italy | custom.rakuten-tv-action-movies-italy-it-movie | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Drama Movies Italy | custom.rakuten-tv-drama-movies-italy-it-movie | - | NO_GUIDE_HIT |
| Italy | RDS Social TV | RDSSocialTV.it | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Best | RTL1025Best.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Bro&Sis | RTL1025BroSis.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Disco | RTL1025Disco.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Napule | RTL1025Napule.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Traffic | RTL1025Traffic.it@SD | - | NO_GUIDE_HIT |
| Kids | Atfal & Mawaheb TV | AtfalMawahebTV.sa@SD | Atfal.&.Mawaheb.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Disney Channel (Bulgaria) | DisneyChannel.bg@SD | DisneyChannel.bg | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | EKids | EKids.bg@SD | EKids.bg | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Nickelodeon (Brazil) | Nickelodeon.br@SD | Nickelodeon.br | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Taha TV | TahaTV.lb@SD | Taha.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | 13 Kids | 13Kids.cl@SD | - | NO_GUIDE_HIT |
| Kids | ADN TV+ | ADNTVPlus.fr | - | NO_GUIDE_HIT |
| Kids | ADO TV | ADOTV.bj@SD | - | NO_GUIDE_HIT |
| Kids | Afarin Baxcha | AfarinBaxcha.iq@SD | - | NO_GUIDE_HIT |
| Kids | Afarin TV | AfarinTV.iq | - | NO_GUIDE_HIT |
| Kids | Afarin TV | AfarinTV.iq@SD | - | NO_GUIDE_HIT |
| Kids | Akili Kids! | AkiliKids.ke@SD | - | NO_GUIDE_HIT |
| Kids | Amou Yazid TV | AmouYazidTV.dz@SD | - | NO_GUIDE_HIT |
| Kids | Aqlvoy | Aqlvoy.uz@SD | - | NO_GUIDE_HIT |
| Kids | BabyFirst Spanish | BabyFirst.us@Spanish | - | NO_GUIDE_HIT |
| Kids | Balapan | Balapan.kz@HD | - | NO_GUIDE_HIT |
| Kids | Bantul the Great | BantulTheGreat.us | - | NO_GUIDE_HIT |
| Kids | Bolajon | Bolajon.uz@SD | - | NO_GUIDE_HIT |
| Kids | Box Kids TV | BoxKidsTV.br@SD | - | NO_GUIDE_HIT |
| Kids | Carousel +4 | Carousel.ru@Plus4 | - | NO_GUIDE_HIT |
| Kids | Cartoon Network (Pakistan) | CartoonNetwork.pk@SD | - | NO_GUIDE_HIT |
| Kids | Cartoon Network Arabic | CartoonNetworkArabic.ae@SD | - | NO_GUIDE_HIT |
| Kids | Cartoon Network Asia | CartoonNetworkAsia.sg@SD | - | NO_GUIDE_HIT |
| Kids | Cartoon Network CEE Poland | CartoonNetworkCEE.uk@Poland | - | NO_GUIDE_HIT |
| Kids | Cartoon Network CEE Ukraine | CartoonNetworkCEE.uk@Ukraine | - | NO_GUIDE_HIT |
| Kids | Cartoon Network Latin America Brazil | CartoonNetworkLatinAmerica.us@Brazil | - | NO_GUIDE_HIT |
| Kids | Cartoon Network Latin America South Atlantic | CartoonNetworkLatinAmerica.us@SouthAtlantic | - | NO_GUIDE_HIT |
| Kids | Cartoon Network Latin America South Pacific | CartoonNetworkLatinAmerica.us@SouthPacific | - | NO_GUIDE_HIT |
| Kids | Cartoonito Asia | CartoonitoAsia.sg@SD | - | NO_GUIDE_HIT |
| Kids | Cartoonito CEE Czechia | CartoonitoCEE.uk@Czechia | - | NO_GUIDE_HIT |
| Kids | Cartoonito CEE Poland | CartoonitoCEE.uk@Poland | - | NO_GUIDE_HIT |
| Kids | Cartoonito Latin America | CartoonitoLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| Kids | CBeebies (Poland) | CBeebies.pl@SD | - | NO_GUIDE_HIT |
| Kids | Chikitoonz | Chikitoonz.pe@SD | - | NO_GUIDE_HIT |
| Kids | Chinola TV | ChinolaTV.do@SD | - | NO_GUIDE_HIT |
| Kids | Clan | Clan.es@SD | - | NO_GUIDE_HIT |
| Kids | Detskiy | Detskiy.ru@SD | - | NO_GUIDE_HIT |
| Kids | Discovery Kids Latin America | DiscoveryKidsLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Kids | Discovery Kids Latin America Chile | DiscoveryKidsLatinAmerica.us@Chile | - | NO_GUIDE_HIT |
| Kids | Discovery Kids Latin America Colombia | DiscoveryKidsLatinAmerica.us@Colombia | - | NO_GUIDE_HIT |
| Kids | Disney Channel Latin America Center | DisneyChannelLatinAmerica.ar@Center | - | NO_GUIDE_HIT |
| Kids | Disney Channel Latin America Mexico | DisneyChannelLatinAmerica.ar@Mexico | - | NO_GUIDE_HIT |
| Kids | Disney Channel Latin America North | DisneyChannelLatinAmerica.ar@North | - | NO_GUIDE_HIT |
| Kids | Disney Channel Latin America Panregional | DisneyChannelLatinAmerica.ar@PanregionalHD | - | NO_GUIDE_HIT |
| Kids | Disney Jr. Latin America | DisneyJrLatinAmerica.ar@North | - | NO_GUIDE_HIT |
| Kids | Disney Jr. Latin America North | DisneyJrLatinAmerica.ar@NorthHD | - | NO_GUIDE_HIT |
| Kids | Doraemon TV | DoraemonTV.us | - | NO_GUIDE_HIT |
| Kids | DumDum | DumDum.br@SD | - | NO_GUIDE_HIT |
| Kids | Duronto TV | DurontoTV.bd@SD | - | NO_GUIDE_HIT |
| Kids | EBS Kids | EBSKids.kr@SD | - | NO_GUIDE_HIT |
| Kids | El Chavo TV | ElChavoTV.mx@HD | - | NO_GUIDE_HIT |
| Kids | Epic Kids Digital | EpicKidsDigital.us | - | NO_GUIDE_HIT |
| Kids | ETV 2 | ETV2.ee@SD | - | NO_GUIDE_HIT |
| Kids | Extrema Kids TV | ExtremaKidsTV.cr@HD | - | NO_GUIDE_HIT |
| Kids | Gopal Bhar TV | custom.bdix.gopal-bhar-tv | - | NO_GUIDE_HIT |
| Kids | Iunior TV | IuniorTV.it@SD | - | NO_GUIDE_HIT |
| Kids | JapanimTV | JapanimTV.be@SD | - | NO_GUIDE_HIT |
| Kids | Kuriakos Kids | KuriakosKids.pt@SD | - | NO_GUIDE_HIT |
| Kids | Lego Channel | LegoChannel.us@SD | - | NO_GUIDE_HIT |
| Kids | Maxcine Kids | MaxcineKids.us@HD | - | NO_GUIDE_HIT |
| Kids | MBC 3 USA | MBC3USA.us@SD | - | NO_GUIDE_HIT |
| Kids | MiMi TV | MiMiTV.uz@SD | - | NO_GUIDE_HIT |
| Kids | Minika Cocuk | MinikaCocuk.tr@SD | - | NO_GUIDE_HIT |
| Kids | Minimax (Pakistan) | Minimax.pk@SD | - | NO_GUIDE_HIT |
| Kids | Moonbug Kids | MoonbugKids.uk | - | NO_GUIDE_HIT |
| Kids | Motu Patlu | custom.bdix.motu-patlu | - | NO_GUIDE_HIT |
| Kids | Mr Bean Animated FR | MrBeanAnimated.uk@FR | - | NO_GUIDE_HIT |
| Kids | Nick Jr. Latin America | NickJrLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Kids | Nickelodeon (Germany) | Nickelodeon.de@SD | - | NO_GUIDE_HIT |
| Kids | Nickelodeon CIS | NickelodeonCIS.kz@SD | - | NO_GUIDE_HIT |
| Kids | NickOnline | NickOnline.br@HD | - | NO_GUIDE_HIT |
| Kids | Nicktoons CIS | NicktoonsCIS.ru@SD | - | NO_GUIDE_HIT |
| Kids | O! International | O.ru@International | - | NO_GUIDE_HIT |
| Kids | ON Kids | ONKids.vn@SD | - | NO_GUIDE_HIT |
| Kids | Peques TV | PequesTV.pe@SD | - | NO_GUIDE_HIT |
| Kids | Plim Plim | PlimPlim.ar@SD | - | NO_GUIDE_HIT |
| Kids | Pooya TV | PooyaTV.ir@SD | - | NO_GUIDE_HIT |
| Kids | Powerkids Kartoon Channel | PowerkidsKartoonChannel.us | - | NO_GUIDE_HIT |
| Kids | Reino Infantil | ReinoInfantil.mz@SD | - | NO_GUIDE_HIT |
| Kids | Retro Cartoon | RetroCartoon.br@SD | - | NO_GUIDE_HIT |
| Kids | Skwad Play | SkwadPlay.us@SD | - | NO_GUIDE_HIT |
| Kids | Smotrim 100% Detskoe | Smotrim100Detskoe.ru@SD | - | NO_GUIDE_HIT |
| Kids | Smurf TV | SmurfTV.us | - | NO_GUIDE_HIT |
| Kids | Spacetoon Arabic | SpacetoonArabic.ae@SD | - | NO_GUIDE_HIT |
| Kids | Super Simple Songs | SuperSimpleSongs.us@SD | - | NO_GUIDE_HIT |
| Kids | Tiguerito TV | TigueritoTV.do@HD | - | NO_GUIDE_HIT |
| Kids | Tom and Jerry | TomAndJerry.do | - | NO_GUIDE_HIT |
| Kids | Tom And Jerry | TomAndJerry.do@HD | - | NO_GUIDE_HIT |
| Kids | Tooku | Tooku.ru | - | NO_GUIDE_HIT |
| Kids | Toon Goggles Junior | ToonGogglesJunior.us | - | NO_GUIDE_HIT |
| Kids | Toonami Aftermath | ToonamiAftermath.us@East | - | NO_GUIDE_HIT |
| Kids | Toonami Aftermath West | ToonamiAftermath.us@West | - | NO_GUIDE_HIT |
| Kids | Tooncast SouthAmerica | Tooncast.us@SouthAmerica | - | NO_GUIDE_HIT |
| Kids | TRT Cocuk | TRTCocuk.tr@SD | - | NO_GUIDE_HIT |
| Kids | TRT Diyanet Cocuk | TRTDiyanetCocuk.tr@SD | - | NO_GUIDE_HIT |
| Kids | TVC Arabic Kids | custom.tvcarabickids | - | NO_GUIDE_HIT |
| Kids | TVOKids | TVOKids.ca@SD | - | NO_GUIDE_HIT |
| Kids | TVS Hi Tops | TVSHiTops.us@SD | - | NO_GUIDE_HIT |
| Kids | WOW Kidz | WOWKidz.in@Hindi | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Tamil | WOWKidzTamil.in | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Telugu | WOWKidz.in@Telugu | - | NO_GUIDE_HIT |
| Kids | Xtrema Cartoons | XtremaCartoons.ar@SD | - | NO_GUIDE_HIT |
| Kids | Yu-Gi-Oh! en espanol | YuGiOhenespanol.us@SD | - | NO_GUIDE_HIT |
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
| Mexico | Exa TV | ExaTV.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Lobo TV | LoboTV.mx@SD | - | NO_GUIDE_HIT |
| Mexico | MyTime Movie Network (Mexico) | MyTimeMovieNetwork.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Popcorn Central | PopcornCentral.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Vision Television | VisionTelevision.mx@SD | - | NO_GUIDE_HIT |
| Netherlands | BEATTV | BEATTV.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | Canal+ Action Europe (360p) | CanalPlusActionEurope.nl@Netherlands | - | NO_GUIDE_HIT |
| Netherlands | Canal+ Action Europe Czechia | CanalPlusActionEurope.nl@Czechia | - | NO_GUIDE_HIT |
| Netherlands | Canal+ Action Europe Magyar | CanalPlusActionEurope.nl@Magyar | - | NO_GUIDE_HIT |
| Netherlands | Canal+ Action Europe Slovakia (720p) | CanalPlusActionEurope.nl@Slovakia | - | NO_GUIDE_HIT |
| Netherlands | FomixTV | custom.fomixtv-nl-music | - | NO_GUIDE_HIT |
| Netherlands | Gigant FM | custom.gigant-fm-nl-music | - | NO_GUIDE_HIT |
| Netherlands | Hype Visual Radio | custom.hype-visual-radio-nl-music | - | NO_GUIDE_HIT |
| Netherlands | Qmusic | Qmusic.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | Radio JND | custom.radio-jnd-nl-music | - | NO_GUIDE_HIT |
| Netherlands | RadioNL TV | RadioNLTV.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | TMF | TMF.nl@HDFAST | - | NO_GUIDE_HIT |
| New Backups | Gazi TV | GaziTV.bd@SD | - | NO_GUIDE_HIT |
| New Channels | Aryan TV National | AryanTVNational.in@SD | 1761 | Aryan.TV.National.in | jtv1761 | MAPPED_NOT_CURRENTLY_FOUND |
| New Channels | Captain (576p) | Captain.in@SD | 3069 | jtv3069 | MAPPED_NOT_CURRENTLY_FOUND |
| New Channels | DocuBay TV (1080p) | DocuBayTV.in@SD | - | NO_GUIDE_HIT |
| New Channels | Epic TV Digital (1080p) | EpicTV.in@Digital | - | NO_GUIDE_HIT |
| New Channels | JTBS Classic | JTBSClassic.in@Main | - | NO_GUIDE_HIT |
| New Channels | Mango Mobile TV (1080p) | MangoMobileTV.in@HD | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cine Familia | PlutoTVCineFamilia.us@BR | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cine Familia LatAm | PlutoTVCineFamilia.us@LatAm | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cine Inspiracao | PlutoTVCineInspiracao.us@BR | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cine Inspirador | PlutoTVCineInspirador.us@LatAm | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cine Romance LatAm | PlutoTVCineRomance.us@LatAm | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cine Romantico | PlutoTVCineRomantico.de@ES | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cine Sucessos | PlutoTVCineSucessos.us@BR | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cine Suspenso | PlutoTVCineSuspenso.us@LatAm | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cinema Italiano | PlutoTVCinemaItaliano.de@IT | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cinema Orientale | PlutoTVCinemaOrientale.de@IT | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Comedias Romanticas | PlutoTVComediasRomanticas.de@ES | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Comedies Cultes | PlutoTVComediesCultes.de@FR | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Comedy Movies | PlutoTVComedyMovies.us@CA | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Crime Drama | PlutoTVCrimeDrama.us@SD | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Crime Drama CA | PlutoTVCrimeDrama.us@CA | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Crime Movies | PlutoTVCrimeMovies.us@SD | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cult Films (Germany) | PlutoTVCultFilms.de@GB | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Cult Films (United States) | PlutoTVCultFilms.us@US | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Danske klassikere | PlutoTVDanskeklassikere.se@DK | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Drama | PlutoTVDrama.us@US | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Drama Movies | PlutoTVDramaMovies.us@CA | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Estrellas de Accion | PlutoTVEstrellasdeAccion.us@SD | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Family Movie Club | PlutoTVFamilyMovieClub.de@GB | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Fantasy & Horror | PlutoTVFantasyHorror.de@GB | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Ficcao Cientifica | PlutoTVFiccaoCientifica.us@BR | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Film (Germany) | PlutoTVFilm.de@IT | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Film (Sweden) | PlutoTVFilm.se@SE | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Film (Sweden) DK | PlutoTVFilm.se@DK | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Film (Sweden) NO | PlutoTVFilm.se@NO | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Film Azione | PlutoTVFilmAzione.de@IT | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Film Commedia | PlutoTVFilmCommedia.de@IT | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Film Romantici | PlutoTVFilmRomantici.de@IT | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Film Storici | PlutoTVFilmStorici.de@IT | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Film Thriller | PlutoTVFilmThriller.de@IT | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Filmes Acao | PlutoTVFilmesAcao.us@BR | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Filmes Aventura | PlutoTVFilmesAventura.us@BR | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Filmes de Luta | PlutoTVFilmesdeLuta.us@BR | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Filmes Nacionais | PlutoTVFilmesNacionais.us@BR | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Franchise Favorites | PlutoTVFranchiseFavorites.us@SD | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Haialarm | PlutoTVHaialarm.de@DACH | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Harlequin | PlutoTVHarlequin.se@SE | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Harlequin DK | PlutoTVHarlequin.se@DK | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Harlequin NO | PlutoTVHarlequin.se@NO | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Horror (Sweden) | PlutoTVHorror.se@SE | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Horror (Sweden) DK | PlutoTVHorror.se@DK | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Horror (Sweden) NO | PlutoTVHorror.se@NO | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Horror (United States) | PlutoTVHorror.us@US | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Horror (United States) CA | PlutoTVHorror.us@CA | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Humor (Sweden) | PlutoTVHumor.se@DK | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Icons | PlutoTVIcons.us@SD | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Invasion Alien | PlutoTVInvasionAlien.de@ES | - | NO_GUIDE_HIT |
| New Channels | Pluto TV John Wayne | PlutoTVJohnWayne.se@SE | - | NO_GUIDE_HIT |
| New Channels | Pluto TV John Wayne DK | PlutoTVJohnWayne.se@DK | - | NO_GUIDE_HIT |
| New Channels | Pluto TV John Wayne NO | PlutoTVJohnWayne.se@NO | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Komedi | PlutoTVKomedi.se@SE | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Komedie | PlutoTVKomedie.se@NO | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Kult Comedies | PlutoTVKultComedies.de@DACH | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Kultfilm | PlutoTVKultfilm.se@DK | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Kultfilme | PlutoTVKultfilme.de@DACH | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Kultfilmer | PlutoTVKultfilmer.se@SE | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Kultfilmer NO | PlutoTVKultfilmer.se@NO | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Legami Letali | PlutoTVLegamiLetali.de@IT | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Movies | PlutoTVMovies.de@DACH | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Movies GB | PlutoTVMovies.de@GB | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Netmovies | PlutoTVNetmovies.us@BR | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Notti di Passione | PlutoTVNottidiPassione.de@IT | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Nuestro Cine | PlutoTVNuestroCine.us@LatAm | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Paranormal (Sweden) | PlutoTVParanormal.se@SE | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Paranormal (Sweden) DK | PlutoTVParanormal.se@DK | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Psycho | PlutoTVPsycho.de@ES | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Reaction | PlutoTVReaction.us@SD | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Retro Action Movies | PlutoTVRetroActionMovies.us@CA | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Romance | PlutoTVRomance.us@US | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Romantik | PlutoTVRomantik.se@SE | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Romantik DK | PlutoTVRomantik.se@DK | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Romantikk | PlutoTVRomantikk.se@NO | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Sci-Fi (Sweden) | PlutoTVSciFi.se@SE | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Sci-Fi (Sweden) DK | PlutoTVSciFi.se@DK | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Sci-Fi (Sweden) NO | PlutoTVSciFi.se@NO | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Sci-Fi (United States) | PlutoTVSciFi.us@US | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Sci-Fi (United States) CA | PlutoTVSciFi.us@CA | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Sci-Fi (United States) LatAm | PlutoTVSciFi.us@LatAm | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Serie Sci-Fi | PlutoTVSerieSciFi.de@IT | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Staff Picks | PlutoTVStaffPicks.us@SD | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Star Trek (Germany) | PlutoTVStarTrek.de@DACH | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Star Trek (Sweden) | PlutoTVStarTrek.se@DK | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Terror | PlutoTVTerror.us@SD | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Terror Trash | PlutoTVTerrorTrash.us@BR | - | NO_GUIDE_HIT |
| New Channels | Pluto TV Thrillers | PlutoTVThrillers.us@US | - | NO_GUIDE_HIT |
| New Channels | Pravasi Channel | PravasiChannel.in@SD | - | NO_GUIDE_HIT |
| New Channels | Vokta TV | VoktaTV.bd@SD | - | NO_GUIDE_HIT |
| Pakistani | 8XM | 8XM.pk@HD | - | NO_GUIDE_HIT |
| Pakistani | 8XM | 8XM.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | aur LIFE | aurLIFE.pk | - | NO_GUIDE_HIT |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Falak TV | FalakTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Filmax (576p) | Filmax.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Filmazia (576p) | Filmazia.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | HUM Sitaray | HUMSitaray.pk | - | NO_GUIDE_HIT |
| Pakistani | Jalwa TV | JalwaTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Joo Music | JooMusic.pk | - | NO_GUIDE_HIT |
| Pakistani | JooMusic | JooMusic.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Paighan TV | PaighanTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | See TV | SeeTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Tag TV | TagTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Waseb TV | WasebTV.pk | - | NO_GUIDE_HIT |
| Panama | Corazon TV | CorazonTV.pa@SD | - | NO_GUIDE_HIT |
| Panama | Mas23 TV | Mas23TV.pa@SD | - | NO_GUIDE_HIT |
| Panama | Pindin TV | PindinTV.pa@SD | - | NO_GUIDE_HIT |
| Panama | Planet 100.9 FM | custom.planet-100-9-fm-pa-music | - | NO_GUIDE_HIT |
| Panama | Super Q Panama | SuperQPanama.pa@SD | - | NO_GUIDE_HIT |
| Panama | Tropical Moon Urban TV | TropicalMoonUrbanTV.pa@SD | - | NO_GUIDE_HIT |
| Paraguay | Alcance FM PLAY TV | custom.alcance-fm-play-tv-py-music | - | NO_GUIDE_HIT |
| Paraguay | Dismar Radio TV | custom.dismar-radio-tv-py-music | - | NO_GUIDE_HIT |
| Paraguay | E40 | E40.py@SD | - | NO_GUIDE_HIT |
| Paraguay | HEi Now | HEiNow.py@SD | - | NO_GUIDE_HIT |
| Paraguay | Los Angeles TV Radio | custom.los-angeles-tv-radio-py-music | - | NO_GUIDE_HIT |
| Paraguay | Nande Portetepe TV | NandePortetepeTV.py@SD | - | NO_GUIDE_HIT |
| Paraguay | Next | NextHD.py@SD | - | NO_GUIDE_HIT |
| Paraguay | Radio Colmenar 92.5 FM | custom.radio-colmenar-92-5-fm-py-music | - | NO_GUIDE_HIT |
| Paraguay | Radio San Cristobal 88.7 FM | custom.radio-san-cristobal-88-7-fm-py-music | - | NO_GUIDE_HIT |
| Paraguay | Venus Media | VenusMedia.py@SD | - | NO_GUIDE_HIT |
| Peru | Karibena | Karibena.pe@SD | - | NO_GUIDE_HIT |
| Peru | La Fabulosa TV | LaFabulosaTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | Metropolitana del Cuzco | custom.metropolitana-del-cuzco-pe-music | - | NO_GUIDE_HIT |
| Peru | Miel TV | MielTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | Radio Master | custom.radio-master-pe-music | - | NO_GUIDE_HIT |
| Peru | Radio Onda Digital | custom.radio-onda-digital-pe-music | - | NO_GUIDE_HIT |
| Peru | Radio Rumba TV | custom.radio-rumba-tv-pe-music | - | NO_GUIDE_HIT |
| Peru | Radio Tropical | custom.radio-tropical-pe-music | - | NO_GUIDE_HIT |
| Peru | RumbaMix TV | RumbaMixTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | Top Latino TV | TopLatinoTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | Turbo Mix Radio TV | custom.turbo-mix-radio-tv-pe-music | - | NO_GUIDE_HIT |
| Peru | TV Peruanisima | TVPeruanisima.pe@SD | - | NO_GUIDE_HIT |
| Peru | TVUNO | TVUNO.pe@SD | - | NO_GUIDE_HIT |
| Poland | AXN Black (United States) Poland | AXNBlack.us@Poland | - | NO_GUIDE_HIT |
| Poland | AXN Poland | AXNPoland.pl@SD | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Comedy Magyar | FILMBOXPlusComedy.pl@Magyar | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Emotion Adria | custom.filmbox-emotion-adria-pl-movie | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Emotion Romania | FILMBOXPlusEmotion.pl@Romania | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Festival Poland | FILMBOXPlusFestival.pl@Poland | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Hits Adria | custom.filmbox-hits-adria-pl-movie | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Love & Crime Adria | custom.filmbox-love-crime-adria-pl-movie | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Love & Crime Bulgaria (720p) | FILMBOXPlusLoveCrime.pl@Bulgaria | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Love & Crime Magyar | FILMBOXPlusLoveCrime.pl@Magyar | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ One Bulgaria (576p) | FILMBOXPlusOne.pl@Bulgaria | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ One Magyar | FILMBOXPlusOne.pl@Magyar | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ One Nederland | FILMBOXPlusOne.pl@Nederland | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ One Ukraine & Baltics (450p) [Geo-blocked] | FILMBOXPlusOne.pl@UkraineBaltics | - | NO_GUIDE_HIT |
| Poland | Radio RAM | custom.radio-ram-pl-music | - | NO_GUIDE_HIT |
| Portugal | Famatv | custom.famatv-pt-music | - | NO_GUIDE_HIT |
| Portugal | Kuriakos Music | KuriakosMusic.pt@SD | - | NO_GUIDE_HIT |
| Portugal | ON FM | custom.on-fm-pt-music | - | NO_GUIDE_HIT |
| Portugal | RFPtv | RFPtv.pt@SD | - | NO_GUIDE_HIT |
| Religious | Makkah TV | MakkahTV.sa | Makkah.TV.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Religious | Al Quran Al Kareem TV | AlQuranAlKareemTV.sa | - | NO_GUIDE_HIT |
| Religious | Al Sunnah TV | custom.al-sunnah-tv | - | NO_GUIDE_HIT |
| Religious | Al-Zahra TV Turkic | AlZahraTVTurkic.sa | - | NO_GUIDE_HIT |
| Religious | ARY Q TV | ARYQTV.pk | - | NO_GUIDE_HIT |
| Religious | Azan TV | custom.azantv | - | NO_GUIDE_HIT |
| Religious | Bahrain Quran | BahrainQuran.bh | - | NO_GUIDE_HIT |
| Religious | Islam Channel Bangla | custom.islamchannelbangla | - | NO_GUIDE_HIT |
| Religious | Islam TV | IslamTV.sa | - | NO_GUIDE_HIT |
| Religious | Islam TV Urdu | custom.islam-tv-urdu | - | NO_GUIDE_HIT |
| Religious | Islamic TV | 223000 | - | NO_GUIDE_HIT |
| Religious | Islamic TV | IslamicTV.sa | - | NO_GUIDE_HIT |
| Religious | Madani TV | MadaniTV.sa | - | NO_GUIDE_HIT |
| Religious | Madina Live | custom.bdix.madinalive | - | NO_GUIDE_HIT |
| Religious | Makkah Live | MakkahLive.sa | - | NO_GUIDE_HIT |
| Religious | Medina Live | MedinaLive.bd | - | NO_GUIDE_HIT |
| Religious | Peace TV | custom.peace-tv-tw8cm | - | NO_GUIDE_HIT |
| Religious | Peace TV Bangla | PeaceTVBangla.ae | - | NO_GUIDE_HIT |
| Religious | Peace TV English | PeaceTVEnglish.ae | - | NO_GUIDE_HIT |
| Religious | Peace TV Urdu | PeaceTVUrdu.pk | - | NO_GUIDE_HIT |
| Religious | Q TV | QTV.in@SD | - | NO_GUIDE_HIT |
| Religious | Quran | custom.quran | - | NO_GUIDE_HIT |
| Religious | Quran TV | QuranTV.iq | - | NO_GUIDE_HIT |
| Religious | Sunna TV | SunnaTV.ng@SD | - | NO_GUIDE_HIT |
| Religious | Sunnah TV | custom.sunnah-tv | - | NO_GUIDE_HIT |
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
| Romania | Radio Fx Net | custom.radio-fx-net-ro-music | - | NO_GUIDE_HIT |
| Romania | Radio Romania Oltenia-Craiova | custom.radio-romania-oltenia-craiova-ro-music | - | NO_GUIDE_HIT |
| Romania | Radio Romania Targu Mures | custom.radio-romania-targu-mures-ro-music | - | NO_GUIDE_HIT |
| Romania | Smart Radio | custom.smart-radio-ro-music | - | NO_GUIDE_HIT |
| Romania | Super TV (Romania) | SuperTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | Tequila Music TV | TequilaMusicTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | Traditional TV | TraditionalTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | TV AS | TVAS.ro@SD | - | NO_GUIDE_HIT |
| Russia | Shanson TV | ShansonTV.ru@SD | Shanson.TV.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Russia | Star Cinema | StarCinema.ru@SD | Star.Cinema.pl | MAPPED_NOT_CURRENTLY_FOUND |
| Russia | Star Family | StarFamily.ru@SD | Star.Family.pl | MAPPED_NOT_CURRENTLY_FOUND |
| Russia | 1HD Music Television | 1HDMusicTelevision.ru@HD | - | NO_GUIDE_HIT |
| Russia | alpha Cinema (1080p) | alphaCinema.ru@HD | - | NO_GUIDE_HIT |
| Russia | Blokbaster | Blokbaster.ru@HD | - | NO_GUIDE_HIT |
| Russia | Bollywood HD Russia | BollywoodHD.ro@Russia | - | NO_GUIDE_HIT |
| Russia | BRIDGE Rock | BRIDGERock.ru@SD | - | NO_GUIDE_HIT |
| Russia | City Eden Classic Music | CityEdenClassicMusic.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoAction [ ] | CityEdenKinoAction.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoArt | CityEdenKinoArt.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoAsia [ ] | CityEdenKinoAsia.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoDetektiv | CityEdenKinoDetektiv.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoDrama | CityEdenKinoDrama.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoFantastika | CityEdenKinoFantastika.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoKlassika | CityEdenKinoKlassika.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoKomediya | CityEdenKinoKomediya.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoMistika | CityEdenKinoMistika.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden KinoSemya [Not 24/7] | CityEdenKinoSemya.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden Play | CityEdenPlay.ru@HD | - | NO_GUIDE_HIT |
| Russia | DanceHits80 | DanceHits80.ru@SD | - | NO_GUIDE_HIT |
| Russia | Detskoe kino [Not 24/7] | Detskoekino.ru@International | - | NO_GUIDE_HIT |
| Russia | Dom kino | custom.dom-kino-ru-movie | - | NO_GUIDE_HIT |
| Russia | Europa Plus TV Belarus | EuropaPlusTV.ru@Belarus | - | NO_GUIDE_HIT |
| Russia | Evrokino HD (1080p) | Evrokino.ru@HD | - | NO_GUIDE_HIT |
| Russia | Feniks plus Kino (576p) | FeniksplusKino.ru@SD | - | NO_GUIDE_HIT |
| Russia | FON Music | FONMusic.ru@SD | - | NO_GUIDE_HIT |
| Russia | Hit HD (1080p) | Hit.ru@HD | - | NO_GUIDE_HIT |
| Russia | Horoshee Kino | HorosheeKino.ru@SD | - | NO_GUIDE_HIT |
| Russia | Illusion+ | IllusionPlus.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kino 1 (Russia) | Kino1.ru@International | - | NO_GUIDE_HIT |
| Russia | Kinopokaz | custom.kinopokaz-ru-movie | - | NO_GUIDE_HIT |
| Russia | Kinoseriya | custom.kinoseriya-ru-movie | - | NO_GUIDE_HIT |
| Russia | Live Music Channel | LiveMusicChannel.ru@HD | - | NO_GUIDE_HIT |
| Russia | MTV Volgograd | MTVVolgograd.ru@SD | - | NO_GUIDE_HIT |
| Russia | Muz Soyuz | MuzSoyuz.ru@SD | - | NO_GUIDE_HIT |
| Russia | Muzyka 1 | Muzyka1.ru@International | - | NO_GUIDE_HIT |
| Russia | Muzyka Kino | MuzykaKino.ru@International | - | NO_GUIDE_HIT |
| Russia | Nash Kinopokaz | NashKinopokaz.ru@HD | - | NO_GUIDE_HIT |
| Russia | Nashe HD (576p) | Nashe.ru@HD | - | NO_GUIDE_HIT |
| Russia | Nashe muzhskoe HD (1080p) | Nashemuzhskoe.ru@HD | - | NO_GUIDE_HIT |
| Russia | Ostrosyuzhetnoye HD (1080p) | Ostrosyuzhetnoye.ru@HD | - | NO_GUIDE_HIT |
| Russia | Rodnoe Kino | custom.rodnoe-kino-ru-movie | - | NO_GUIDE_HIT |
| Russia | Russkiy roman | custom.russkiy-roman-ru-movie | - | NO_GUIDE_HIT |
| Russia | Smotrim 100% Klassika | Smotrim100Klassika.ru@SD | - | NO_GUIDE_HIT |
| Russia | SONGTV Russia | SONGTVRussia.ru@SD | - | NO_GUIDE_HIT |
| Russia | Strana FM | custom.strana-fm-ru-music | - | NO_GUIDE_HIT |
| Russia | TV 21 | TV21.ru@SD | - | NO_GUIDE_HIT |
| Russia | TV1000 Russian Kino Global | TV1000RussianKinoGlobal.ru@SD | - | NO_GUIDE_HIT |
| Russia | viju TV1000 action | custom.viju-tv1000-action-ru-movie | - | NO_GUIDE_HIT |
| Russia | viju TV1000 novella | vijuTV1000novella.ru@HD | - | NO_GUIDE_HIT |
| Russia | viju TV1000 russkoe | custom.viju-tv1000-russkoe-ru-movie | - | NO_GUIDE_HIT |
| Russia | Кино 1 International | custom.1-international-ru-movie | - | NO_GUIDE_HIT |
| Russia | Музыка 1 International | custom.1-international-ru-music | - | NO_GUIDE_HIT |
| Saudi Arabia | Aflam | custom.aflam | - | NO_GUIDE_HIT |
| Saudi Arabia | Fairuz | Fairuz.sa@HD | - | NO_GUIDE_HIT |
| Saudi Arabia | Jeddah Radio | custom.jeddah-radio-sa-music | - | NO_GUIDE_HIT |
| Saudi Arabia | Majid Al Mohandis | MajidAlMohandis.sa@SD | - | NO_GUIDE_HIT |
| Saudi Arabia | MBC Loud | MBCLoud.sa@SD | - | NO_GUIDE_HIT |
| Saudi Arabia | MBC Mood | MBCMood.sa@HD | - | NO_GUIDE_HIT |
| Saudi Arabia | Movies Action | MoviesAction.sa@SD | - | NO_GUIDE_HIT |
| Saudi Arabia | Panorama FM | custom.panorama-fm-sa-music | - | NO_GUIDE_HIT |
| Saudi Arabia | Rabeh Saqer | RabehSaqer.sa@HD | - | NO_GUIDE_HIT |
| Saudi Arabia | Tarab | Tarab.sa@SD | - | NO_GUIDE_HIT |
| Serbia | DM Sat | custom.dm-sat-rs-music | - | NO_GUIDE_HIT |
| Serbia | Radio Hit FM TV | custom.radio-hit-fm-tv-rs-music | - | NO_GUIDE_HIT |
| Serbia | Radio Karolina TV | custom.radio-karolina-tv-rs-music | - | NO_GUIDE_HIT |
| Serbia | Radio Lola TV | custom.radio-lola-tv-rs-music | - | NO_GUIDE_HIT |
| Serbia | TDI Radio TV | custom.tdi-radio-tv-rs-music | - | NO_GUIDE_HIT |
| Singapore | Cinemax Asia | CinemaxAsia.sg@HD | - | NO_GUIDE_HIT |
| Singapore | Cinemax Asia (720p) [Geo-blocked] | CinemaxAsia.sg@SD | - | NO_GUIDE_HIT |
| Singapore | HBO Asia SD (720p) [Geo-blocked] | HBOAsia.sg@SD | - | NO_GUIDE_HIT |
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
| Spain | Rakuten TV Family Movies | RakutenTVFamilyMovies.es | - | NO_GUIDE_HIT |
| Spain | RTV Vida | RTVVida.es@SD | - | NO_GUIDE_HIT |
| Spain | SpektraTV | SpektraTV.es@SD | - | NO_GUIDE_HIT |
| Spain | TVOMIX | TVOMIX.es@HD | - | NO_GUIDE_HIT |
| Spain | XPTV1 | XPTV1.es@SD | - | NO_GUIDE_HIT |
| Sports | Sporty TV | SportyTV.cz@SD | Sporty.TV.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Win Sports | WinSports.co@SD | WinSports.co | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | World of Freesports | WorldofFreesports.de@SD | WorldofFreesports.de | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | 30A Golf Kingdom | 30AGolfKingdom.us@SD | - | NO_GUIDE_HIT |
| Sports | A Sports | ASports.pk | - | NO_GUIDE_HIT |
| Sports | ACCDN | custom.accdn | - | NO_GUIDE_HIT |
| Sports | Arena Sport 1 Premium (Serbia) | ArenaSport1Premium.rs@SD | - | NO_GUIDE_HIT |
| Sports | Arena Sport 1 Premium (Slovenia) | ArenaSport1Premium.si@SD | - | NO_GUIDE_HIT |
| Sports | Arena Sport Premium M1 | ArenaSportPremiumM1.mk@SD | - | NO_GUIDE_HIT |
| Sports | Arena Sport Premium M2 | ArenaSportPremiumM2.mk@SD | - | NO_GUIDE_HIT |
| Sports | Arena Sport Premium M3 | ArenaSportPremiumM3.mk@SD | - | NO_GUIDE_HIT |
| Sports | AS3 Sport TV | AS3SportTV.ve@SD | - | NO_GUIDE_HIT |
| Sports | Astrahan.Ru Sport | AstrahanRuSport.ru@SD | - | NO_GUIDE_HIT |
| Sports | ATG Live | custom.atglive | - | NO_GUIDE_HIT |
| Sports | Bahrain Sports 1 | BahrainSports1.bh@SD | - | NO_GUIDE_HIT |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | - | NO_GUIDE_HIT |
| Sports | beIN Sports XTRA en Espanol | custom.beinsportsxtraenespanol | - | NO_GUIDE_HIT |
| Sports | BEK Sports West | BEKSports.us@West | - | NO_GUIDE_HIT |
| Sports | Belarus-5 | Belarus5.by@HD | - | NO_GUIDE_HIT |
| Sports | Canal+ Sport 2 SK | CanalPlusSport2SK.sk@SD | - | NO_GUIDE_HIT |
| Sports | Canal+ Sport 3 SK | CanalPlusSport3SK.sk@SD | - | NO_GUIDE_HIT |
| Sports | Canal+ Sport 4 SK | CanalPlusSport4SK.sk@SD | - | NO_GUIDE_HIT |
| Sports | Canal+ Sport 5 SK | CanalPlusSport5SK.sk@SD | - | NO_GUIDE_HIT |
| Sports | Canal+ Sport 6 SK | CanalPlusSport6SK.sk@SD | - | NO_GUIDE_HIT |
| Sports | Canal+ Sport 7 SK | CanalPlusSport7SK.sk@SD | - | NO_GUIDE_HIT |
| Sports | Canal+ Sport 8 SK | CanalPlusSport8SK.sk@SD | - | NO_GUIDE_HIT |
| Sports | Canal+ Sport SK | CanalPlusSportSK.sk@SD | - | NO_GUIDE_HIT |
| Sports | CazeTV | CazeTV.br@SD | - | NO_GUIDE_HIT |
| Sports | CCTV-Billiards | CCTVBilliards.cn@HD | - | NO_GUIDE_HIT |
| Sports | CCTV-Golf & Tennis | CCTVGolfTennis.cn@HD | - | NO_GUIDE_HIT |
| Sports | CCTV-Storm Football | CCTVStormFootball.cn@HD | - | NO_GUIDE_HIT |
| Sports | CDN Deportes | CDNDeportes.do@SD | - | NO_GUIDE_HIT |
| Sports | Claro Sports | ClaroSports.mx@SD | - | NO_GUIDE_HIT |
| Sports | Colimdo TV | ColimdoTV.do@SD | - | NO_GUIDE_HIT |
| Sports | CRTV (Chile) | CRTV.cl@SD | - | NO_GUIDE_HIT |
| Sports | CRTV Sports and Entertainment | CRTVSportsandEntertainment.cm@SD | - | NO_GUIDE_HIT |
| Sports | DeporTV | DeporTV.ar@SD | - | NO_GUIDE_HIT |
| Sports | ESPN 2 Latin America | ESPN2LatinAmerica.us@South | - | NO_GUIDE_HIT |
| Sports | ESPN 3 Latin America | ESPN3LatinAmerica.us@South | - | NO_GUIDE_HIT |
| Sports | ESPN 4 Latin America | ESPN4LatinAmerica.us@South | - | NO_GUIDE_HIT |
| Sports | ESPN 5 Latin America | ESPN5LatinAmerica.us@South | - | NO_GUIDE_HIT |
| Sports | ESPN 6 Latin America | ESPN6LatinAmerica.us@SD | - | NO_GUIDE_HIT |
| Sports | ESPN 7 Latin America | ESPN7LatinAmerica.us@SD | - | NO_GUIDE_HIT |
| Sports | ESPN Latin America | ESPNLatinAmerica.us@South | - | NO_GUIDE_HIT |
| Sports | ESPN Latin America Colombia | ESPNLatinAmerica.us@Colombia | - | NO_GUIDE_HIT |
| Sports | ESPN Latin America Mexico | ESPNLatinAmerica.us@Mexico | - | NO_GUIDE_HIT |
| Sports | eSports Max TV | eSportsMaxTV.ve@SD | - | NO_GUIDE_HIT |
| Sports | Eurosport 1 Hungary | Eurosport1.fr@Hungary | - | NO_GUIDE_HIT |
| Sports | Eurosport 2 Hungary | Eurosport2.fr@Hungary | - | NO_GUIDE_HIT |
| Sports | Eurosport 4K Czechia | Eurosport4KCzechia.cz@UHD | - | NO_GUIDE_HIT |
| Sports | FIFA+ Spain | FIFAPlus.uk@Spain | - | NO_GUIDE_HIT |
| Sports | FIFA+ Women | FIFAPlusWomen.uk@English | - | NO_GUIDE_HIT |
| Sports | Fight Network | custom.fightnetwork | - | NO_GUIDE_HIT |
| Sports | Formula 1 AntenaPlay | Formula1AntenaPlay.ro@SD | - | NO_GUIDE_HIT |
| Sports | FTV (Bolivia) | FTV.bo@SD | - | NO_GUIDE_HIT |
| Sports | FUEL TV AU | FUELTV.pt@AU | - | NO_GUIDE_HIT |
| Sports | Futbol TV | FutbolTV.uz@HD | - | NO_GUIDE_HIT |
| Sports | Glory Kickboxing Poland | GloryKickboxing.us@Poland | - | NO_GUIDE_HIT |
| Sports | Go3 Sport 1 | Go3Sport1.ee@SD | - | NO_GUIDE_HIT |
| Sports | Goal TV | GoalTV.in | - | NO_GUIDE_HIT |
| Sports | HTSpor TV | HTSporTV.tr@SD | - | NO_GUIDE_HIT |
| Sports | Inter TV (Italy) | custom.intertv | - | NO_GUIDE_HIT |
| Sports | Kabaddi 24x7 | Kabaddi24x7.in@SD | - | NO_GUIDE_HIT |
| Sports | KTV Sport | KTVSport.kw@SD | - | NO_GUIDE_HIT |
| Sports | KTV Sport Plus | KTVSportPlus.kw@SD | - | NO_GUIDE_HIT |
| Sports | L1 Max | L1Max.pe@SD | - | NO_GUIDE_HIT |
| Sports | LRT Plius | LRTPlius.lt@SD | - | NO_GUIDE_HIT |
| Sports | M Sports | MSports.pk@SD | - | NO_GUIDE_HIT |
| Sports | MadeinBO TV | MadeinBOTV.it@SD | - | NO_GUIDE_HIT |
| Sports | Maincast Cybersport | MaincastCybersport.ua@SD | - | NO_GUIDE_HIT |
| Sports | Maincast Sport | MaincastSport.ua@SD | - | NO_GUIDE_HIT |
| Sports | Match! Ultra | MatchUltra.ru@4K | - | NO_GUIDE_HIT |
| Sports | Meridiano TV | MeridianoTV.ve@SD | - | NO_GUIDE_HIT |
| Sports | MNB Sport | MNBSport.mn@SD | - | NO_GUIDE_HIT |
| Sports | Monterrico TV | MonterricoTV.pe@SD | - | NO_GUIDE_HIT |
| Sports | MTRSPT1 | custom.mtrspt | - | NO_GUIDE_HIT |
| Sports | NHL AntenaPlay | NHLAntenaPlay.ro@SD | - | NO_GUIDE_HIT |
| Sports | Okko Futbol | OkkoFutbol.ru@SD | - | NO_GUIDE_HIT |
| Sports | Oman Sports TV | OmanSportsTV.om@SD | - | NO_GUIDE_HIT |
| Sports | Ovacion TV | OvacionTV.pe@SD | - | NO_GUIDE_HIT |
| Sports | Persiana Fight | PersianaFight.fr@HD | - | NO_GUIDE_HIT |
| Sports | PK Sports | PKSports.pk@SD | - | NO_GUIDE_HIT |
| Sports | Prima Sport Czechia | PrimaSportCzechia.cz@SD | - | NO_GUIDE_HIT |
| Sports | Prime (Syria) | Prime.sy@HD | - | NO_GUIDE_HIT |
| Sports | PTV Sports | PTVSports.pk | - | NO_GUIDE_HIT |
| Sports | Rally TV | RallyTV.us@SD | - | NO_GUIDE_HIT |
| Sports | Rally TV | custom.rallytv | - | NO_GUIDE_HIT |
| Sports | Real Madrid TV English | RealMadridTVEnglish.es@SD | - | NO_GUIDE_HIT |
| Sports | Realitatea Sportiva | RealitateaSportiva.ro@SD | - | NO_GUIDE_HIT |
| Sports | Realitatea Sportiva | custom.realitateasportiva | - | NO_GUIDE_HIT |
| Sports | Red Bull TV AU | RedBullTV.at@AU | - | NO_GUIDE_HIT |
| Sports | Red Bull TV BR | RedBullTV.at@BR | - | NO_GUIDE_HIT |
| Sports | Red Bull TV DE | RedBullTV.at@DE | - | NO_GUIDE_HIT |
| Sports | Red Bull TV ES | RedBullTV.at@ES | - | NO_GUIDE_HIT |
| Sports | Red Bull TV UK | RedBullTV.at@UK | - | NO_GUIDE_HIT |
| Sports | Red Bull TV US | RedBullTV.at@US | - | NO_GUIDE_HIT |
| Sports | Spiler 1 | Spiler1.hu@SD | - | NO_GUIDE_HIT |
| Sports | Spiler 2 | Spiler2.hu@SD | - | NO_GUIDE_HIT |
| Sports | Sport 1 (Ukraine) | Sport1.ua@SD | - | NO_GUIDE_HIT |
| Sports | Sport 3 | Sport3.ua@SD | - | NO_GUIDE_HIT |
| Sports | Sport TV | SportTV.by@SD | - | NO_GUIDE_HIT |
| Sports | Sportivnyy | Sportivnyy.ru@SD | - | NO_GUIDE_HIT |
| Sports | Sportivnyy | custom.sportivnyy | - | NO_GUIDE_HIT |
| Sports | Sports Television | SportsTelevision.kp@HD | - | NO_GUIDE_HIT |
| Sports | Sqala TV | SqalaTV.pe@SD | - | NO_GUIDE_HIT |
| Sports | Strongman | Strongman.us@Germany | - | NO_GUIDE_HIT |
| Sports | Strongman UK | Strongman.us@UK | - | NO_GUIDE_HIT |
| Sports | Suspilne. Sport | SuspilneSport.ua@SD | - | NO_GUIDE_HIT |
| Sports | T Sports | TSports.bd | - | NO_GUIDE_HIT |
| Sports | T Sports 7 | TSports7.th@SD | - | NO_GUIDE_HIT |
| Sports | TAPMAD | custom.tapmad | - | NO_GUIDE_HIT |
| Sports | Tigo Sports (Honduras) | TigoSports.hn@SD | - | NO_GUIDE_HIT |
| Sports | TJK TV | TJKTV.tr@SD | - | NO_GUIDE_HIT |
| Sports | TR Sport | TRSport.it@SD | - | NO_GUIDE_HIT |
| Sports | TR Sport | custom.trsport | - | NO_GUIDE_HIT |
| Sports | Trace Sport | custom.tracesport | - | NO_GUIDE_HIT |
| Sports | Trace Sport Stars Russia | TraceSportStars.fr@Russia | - | NO_GUIDE_HIT |
| Sports | TSN The Ocho | custom.tsntheocho | - | NO_GUIDE_HIT |
| Sports | Turf Movil | TurfMovil.cl@SD | - | NO_GUIDE_HIT |
| Sports | Turkmenistan Sport | TurkmenistanSport.tm@SD | - | NO_GUIDE_HIT |
| Sports | TVS Bowling Network | TVSBowlingNetwork.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Boxing | TVSBoxing.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Classic Sports | TVSClassicSports.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Sports | TVSSports.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Sports Bureau | TVSSportsBureau.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Turbo | TVSTurbo.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Women Sports | TVSWomenSports.us@SD | - | NO_GUIDE_HIT |
| Sports | TYC Sports | custom.tycsports | - | NO_GUIDE_HIT |
| Sports | TyC Sports USA | TyCSportsUSA.ar@SD | - | NO_GUIDE_HIT |
| Sports | viju+ Sport | vijuPlusSport.ru@HD | - | NO_GUIDE_HIT |
| Sports | Voyo Sport 1 | VoyoSport1.ro@HD | - | NO_GUIDE_HIT |
| Sports | Win+ Futbol | WinPlusFutbol.co@SD | - | NO_GUIDE_HIT |
| Sports | World of Freesports | custom.worldoffreesports | - | NO_GUIDE_HIT |
| Sports | World Poker Tour Poland | WorldPokerTour.us@Poland | - | NO_GUIDE_HIT |
| Sweden | Merry Christmas from Viafree | MerryChristmasfromViafree.se@SE | - | NO_GUIDE_HIT |
| Sweden | Merry Christmas from Viafree DK | MerryChristmasfromViafree.se@DK | - | NO_GUIDE_HIT |
| Sweden | Merry Christmas from Viafree NO | MerryChristmasfromViafree.se@NO | - | NO_GUIDE_HIT |
| Sweden | NonStop Kung Fu | NonStopKungFu.se@SE | - | NO_GUIDE_HIT |
| Sweden | NonStop Kung Fu DK | NonStopKungFu.se@DK | - | NO_GUIDE_HIT |
| Sweden | NonStop Kung Fu NO | NonStopKungFu.se@NO | - | NO_GUIDE_HIT |
| Turkey | Dream Turk | DreamTurk.tr@SD | - | NO_GUIDE_HIT |
| Turkey | GEM Pixel | GEMPixel.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Grand Cinema | GrandCinema.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Med Muzik | MedMuzik.tr@SD | - | NO_GUIDE_HIT |
| Turkey | MovieSmart Turk (576p) | MovieSmartTurk.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Number 1 Ask | Number1Ask.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Number 1 Damar | Number1Damar.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Number 1 Dance | Number1Dance.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Number 1 TV | Number1TV.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Power Dance | PowerDance.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Power Love | PowerLove.tr@SD | - | NO_GUIDE_HIT |
| Turkey | PowerTurk Akustik | PowerTurkAkustik.tr@SD | - | NO_GUIDE_HIT |
| Turkey | PowerTurk Slow | PowerTurkSlow.tr@SD | - | NO_GUIDE_HIT |
| Turkey | PowerTurk Taptaze | PowerTurkTaptaze.tr@SD | - | NO_GUIDE_HIT |
| Turkey | TRT Muzik | TRTMuzik.tr@SD | - | NO_GUIDE_HIT |
| Ukraine | 4ever Music | 4everMusic.ua | - | NO_GUIDE_HIT |
| Ukraine | Cine+ Legend | CinePlusLegend.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | EU Music | EUMusic.ua | - | NO_GUIDE_HIT |
| Ukraine | FilmUA Live | FilmUALive.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | FilmUADrama | custom.filmuadrama-ua-movie | - | NO_GUIDE_HIT |
| Ukraine | Happy Radio TV | custom.happy-radio-tv-ua-music | - | NO_GUIDE_HIT |
| Ukraine | InRating TV | InRatingTV.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Kino 1 (Ukraine) | Kino1.ua | - | NO_GUIDE_HIT |
| Ukraine | Kino 2 | Kino2.ua | - | NO_GUIDE_HIT |
| Ukraine | M1 (Ukraine) | M1.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | M2 (Ukraine) | M2.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Megogo Music | MegogoMusic.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Nashe Lubimoe Kino Ukraine (1080p) | NasheLubimoeKinoUkraine.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | NASHE Music | NASHEMusic.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Viasat Kino | custom.viasat-kino-ua-movie | - | NO_GUIDE_HIT |
| Ukraine | Viasat Kino Action | custom.viasat-kino-action-ua-movie | - | NO_GUIDE_HIT |
| Ukraine | Viasat Kino World | ViasatKinoWorld.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Viasat Serial | ViasatSerial.ua@HD | - | NO_GUIDE_HIT |
| Ukraine | ¡Viva Latino! | VivaLatino.ua@SD | - | NO_GUIDE_HIT |
| United Kingdom | AMC Europe Romania | AMCEurope.uk@Romania | - | NO_GUIDE_HIT |
| United Kingdom | Clubbing TV UK | custom.clubbing-tv-uk-gb-music | - | NO_GUIDE_HIT |
| United Kingdom | FMTV | custom.fmtv-gb-music | - | NO_GUIDE_HIT |
| United Kingdom | MovieSphere UK | custom.moviesphere-uk | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic 2000s | Totalmusic2000s.uk@HD | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic 80s | Totalmusic80s.uk | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic Concerts | TotalmusicConcerts.uk | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic Dance | TotalmusicDance.uk@HD | - | NO_GUIDE_HIT |
| United Kingdom | Trace UK | TraceUK.uk@HD | - | NO_GUIDE_HIT |
| United Kingdom | V2BEAT TV | V2BEATTV.uk@SD | - | NO_GUIDE_HIT |
| United Kingdom | Vantage Music UK | VantageMusic.ee@UK | - | NO_GUIDE_HIT |
| United States | 24 Hour Free Movies | custom.24-hour-free-movies | plex.tv.24.Hour.Free.Movies.plex | MAPPED_NOT_CURRENTLY_FOUND |
| United States | 00s Replay | 00sReplay.us@SD | - | NO_GUIDE_HIT |
| United States | 30A Music | 30AMusic.us | - | NO_GUIDE_HIT |
| United States | 30A TV Classic Movies | 30ATVClassicMovies.us@SD | - | NO_GUIDE_HIT |
| United States | 3ABN Praise Him Music Network | custom.3abn-praise-him-music-network-us-music | - | NO_GUIDE_HIT |
| United States | ABN Bible Movies Channel | custom.abn-bible-movies-channel-us-movie | - | NO_GUIDE_HIT |
| United States | ACE Country Radio KPVM-LD | custom.ace-country-radio-kpvm-ld-us-music | - | NO_GUIDE_HIT |
| United States | Adrenalina Pura TV (720p) | AdrenalinaPuraTV.us@SD | - | NO_GUIDE_HIT |
| United States | AMC (United States) | AMC.us@EastHD | - | NO_GUIDE_HIT |
| United States | AMC Latin America (1080p) | AMCLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| United States | AMC Series Latin America | AMCSeriesLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| United States | American Horrors | AmericanHorrors.us@SD | - | NO_GUIDE_HIT |
| United States | Aneflix Live | AneflixLive.us@HD | - | NO_GUIDE_HIT |
| United States | ARTFLIX Movie Classics | ARTFLIXMovieClassics.us@SD | - | NO_GUIDE_HIT |
| United States | Avang TV | AvangTV.us@SD | - | NO_GUIDE_HIT |
| United States | AVI Rewind | AVIRewind.us@SD | - | NO_GUIDE_HIT |
| United States | AXN Crime | AXNCrime.us@SD | - | NO_GUIDE_HIT |
| United States | AXN Latin America | AXNLatinAmerica.us@CentralAmerica | - | NO_GUIDE_HIT |
| United States | AXN Latin America Andes | AXNLatinAmerica.us@Andes | - | NO_GUIDE_HIT |
| United States | Battlestar Galactica | BattlestarGalactica.us@SD | - | NO_GUIDE_HIT |
| United States | BET Cinema | BETCinema.us@SD | - | NO_GUIDE_HIT |
| United States | BET Comedy Movies | BETComedyMovies.us@SD | - | NO_GUIDE_HIT |
| United States | BET Visionaries | BETVisionaries.us@SD | - | NO_GUIDE_HIT |
| United States | Bonanza | Bonanza.us@SD | - | NO_GUIDE_HIT |
| United States | Bonanza CA | Bonanza.us@CA | - | NO_GUIDE_HIT |
| United States | Botflix Radioo | BotflixRadioo.us@HD | - | NO_GUIDE_HIT |
| United States | BPX TV Radio | custom.bpx-tv-radio-us-music | - | NO_GUIDE_HIT |
| United States | California Music Channel | CaliforniaMusicChannel.us | - | NO_GUIDE_HIT |
| United States | Cine Amor | CineAmor.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Familiar (1080p) | CineFamiliar.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Hispano (1080p) | CineHispano.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Premium (1080p) | CinePremium.us@SD | - | NO_GUIDE_HIT |
| United States | Cinecanal (1080p) | Cinecanal.us@Panregional | - | NO_GUIDE_HIT |
| United States | Cinecanal Pacific | Cinecanal.us@Pacific | - | NO_GUIDE_HIT |
| United States | Cinecanal Panregional | custom.cinecanal-panregional-us-movie | - | NO_GUIDE_HIT |
| United States | Cinecanal South | Cinecanal.us@South | - | NO_GUIDE_HIT |
| United States | Cinemax Latin America | CinemaxLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | CMC-USA Country Music Channel | CMCUSACountryMusicChannel.us@SD | - | NO_GUIDE_HIT |
| United States | DHE (1080p) | DHE.us@SD | - | NO_GUIDE_HIT |
| United States | DUST | custom.dust-us-movie | - | NO_GUIDE_HIT |
| United States | EBS Cinema | EBSCinema.us@SD | - | NO_GUIDE_HIT |
| United States | EBS Musika | EBSMusika.us@SD | - | NO_GUIDE_HIT |
| United States | Epix | epix.us | - | NO_GUIDE_HIT |
| United States | Epix Hits | epixhits.us | - | NO_GUIDE_HIT |
| United States | Filmes Suspense | FilmesSuspense.us@BR | - | NO_GUIDE_HIT |
| United States | FilmRise Forensic Files (720p) [Geo-blocked] | FilmRiseForensicFiles.us@SD | - | NO_GUIDE_HIT |
| United States | FrightFlix | custom.frightflix-us-movie | - | NO_GUIDE_HIT |
| United States | FXM | fxm.us | - | NO_GUIDE_HIT |
| United States | Harmony Gospel Music TV | custom.harmony-gospel-music-tv-us-music | - | NO_GUIDE_HIT |
| United States | HBO 2 Latin America | HBO2LatinAmerica.us@HD | - | NO_GUIDE_HIT |
| United States | HBO Family Latin America | HBOFamilyLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | HBO Latin America | HBOLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | HBO Mundi Latin America | HBOMundiLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | HBO Xtreme Latin America | HBOXtremeLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | High Vision TV | HighVisionTV.us@SD | - | NO_GUIDE_HIT |
| United States | HMI PROMZ NEWS | custom.hmi-promz-news-us-music | - | NO_GUIDE_HIT |
| United States | HTV | HTV.us@SD | - | NO_GUIDE_HIT |
| United States | Lifetime Movies | lifetimemovies.us | - | NO_GUIDE_HIT |
| United States | Maxcine | Maxcine.us@HD | - | NO_GUIDE_HIT |
| United States | Maxcine 2 | Maxcine2.us@HD | - | NO_GUIDE_HIT |
| United States | Maxcine Comedy | MaxcineComedy.us@HD | - | NO_GUIDE_HIT |
| United States | Maxcine Family | MaxcineFamily.us@HD | - | NO_GUIDE_HIT |
| United States | MCN6 Music Channel | custom.mcn6-music-channel-us-music | - | NO_GUIDE_HIT |
| United States | Mega Extreno | MegaExtrenoHD.us@HD | - | NO_GUIDE_HIT |
| United States | Metaleitor TV | MetaleitorTV.us@SD | - | NO_GUIDE_HIT |
| United States | Mi Musica Hits | MiMusicaHits.us@SD | - | NO_GUIDE_HIT |
| United States | Mi Musica Reggaeton | MiMusicaReggaeton.us@SD | - | NO_GUIDE_HIT |
| United States | Mi Musica Romantica | MiMusicaRomantica.us@SD | - | NO_GUIDE_HIT |
| United States | Mi Musica Salsa | MiMusicaSalsa.us@SD | - | NO_GUIDE_HIT |
| United States | Movies! KPVM-LD | Movies.us@KPVMLD | - | NO_GUIDE_HIT |
| United States | MovieSphere Gold WFXT | MovieSphereGold.us@WFXT | - | NO_GUIDE_HIT |
| United States | RJTV | RJTV.us@SD | - | NO_GUIDE_HIT |
| United States | Sony Movies | sony.us | - | NO_GUIDE_HIT |
| United States | Sony Movies (United States) | SonyMovies.us@SD | - | NO_GUIDE_HIT |
| United States | Spirit TV [ ] | SpiritTV.us@SD | - | NO_GUIDE_HIT |
| United States | Stryk TV | StrykTV.us@HD | - | NO_GUIDE_HIT |
| United States | TCM Latin America South | TCMLatinAmerica.us@South | - | NO_GUIDE_HIT |
| United States | The Country Network | custom.the-country-network-us-music | - | NO_GUIDE_HIT |
| United States | TVS Classic Movies | TVSClassicMovies.us@SD | - | NO_GUIDE_HIT |
| United States | TVS Drive In Movie | TVSDriveInMovie.us@SD | - | NO_GUIDE_HIT |
| United States | TVS Music Network | TVSMusicNetwork.us@SD | - | NO_GUIDE_HIT |
| United States | TVS Nostalgia Movies | TVSNostalgiaMovies.us@SD | - | NO_GUIDE_HIT |
| United States | TVS Western Movie | TVSWesternMovie.us@SD | - | NO_GUIDE_HIT |
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

- XMLTV channel IDs published: **1148**
- Active playlist IDs present in the published guide: **1148/2785 (41.2%)**
- Active playlist IDs with usable current/future programmes: **1047/2785 (37.6%)**
- Active playlist IDs with usable programmes anywhere in the guide window (-6h/+7d): **1047/2785 (37.6%)**
- Mapped playlist IDs present in the guide: **1148/1159 (99.1%)**
- Mapped playlist IDs with usable current/future programmes: **1047/1159 (90.3%)**
- Mapped playlist IDs with usable programmes anywhere in the guide window: **1047/1159 (90.3%)**
- Eligible programme rows published in the guide window: **121058**
- Mapped playlist IDs missing from the published XMLTV channel list: **11**
- Missing mapped playlist IDs: BangU.us, LEOTV.cz, MusicBoxSexy.cz@SD, StingrayPopAdult.ca@SD, custom.24-7-xxx-metro, custom.24-7-xxx-reality-kings, custom.xxx-brazzers-europe, custom.xxx-ero-xxx, custom.xxx-hustler, custom.xxx-super-one, custom.xxx-vivid-red
- Published mapped IDs without usable current/future programmes: **101**
- IDs without usable current/future programmes: 4SiDESTV.in@SD, ACISportTV.it@SD, AamarBangla.in, AaryaaTV.in, AaryaaTV.in@SD, AmericanNinjaWarrior.us@SD, AryanTVNational.in@SD, AtfalMawahebTV.sa@SD, BBCDrama.uk, BanglaJagoTV.in, BeJoykids.it@HD, Caillou.fr@SD, CampSpoopy.us@SD, Captain.in@SD, ChinaTravel.cn@SD, CineWestern.es@SD, CrimeJustice.us, DiscoveringChina.cn@SD, DisneyChannel.bg@SD, EKids.bg@SD, EkamraCinema.in, EkamraMusiq.in, EnterFilm.ua@SD, FashionOne.uk, FriendsTV.in@SD, GlobalPunjab.in, IqraaTV, JatraEkamra.in@SD, KTVBangla.in@SD, KissKissTV.it@SD, LoveThePlanet.es@EN, LoveThePlanet.us, MaasrangaTV.bd, MakkahTV.sa, ManoranjanPrime.in@SD, Mastiii.in@SD, MultiPremier.mx@SD, NTCTV.in@SD, NatureTime.ca@France, Nickelodeon.br@SD, OnePaschima.in@SD, Only.Music.in, PixelTV.ua@SD, QwestTV.fr@SD, RTL1025Caliente.it@SD, RTV.bd, RealWild.uk, RobotWarsByMech.us, RumbaTV.co@SD, ShansonTV.ru, ShansonTV.ru@SD, ShemarooUmang.in@SD, SonarBangla.in@SD, Spondon.in@SD, SportyTV.cz@SD, StarCinema.ru@SD, StarFamily.ru@SD, SteelbirdMusic.in@SD, StingrayClassicRock.ca, StingrayEasyListening.ca@SD (and 41 more)

## Source / Published Schedule Reconciliation

- IDs with usable current/future source schedule data: **1109/2785 (39.8%)**
- IDs with usable current/future schedules in published XMLTV at report time: **1047/2785 (37.6%)**
- IDs with usable programmes in the published guide's common -6h/+7d window: **1047/2785 (37.6%)**
- Current/future source IDs without any usable published programme in that common window: **62**
- Source-scheduled IDs without a usable published programme in the common window: ACI Sport TV (`ACISportTV.it@SD`), Amar Bangla (`AamarBangla.in`), Aaryaa TV (`AaryaaTV.in`), Aaryaa TV (`AaryaaTV.in@SD`), American Ninja Warrior (`AmericanNinjaWarrior.us@SD`), Bang U (`BangU.us`), BeJoy.kids (`BeJoykids.it@HD`), Caillou (`Caillou.fr@SD`), Camp Spoopy (`CampSpoopy.us@SD`), Cine Western (Spain) (`CineWestern.es@SD`), Enter-Film (`EnterFilm.ua@SD`), Iqraa TV (`IqraaTV`), KTV Bangla (`KTVBangla.in@SD`), Kiss Kiss TV (`KissKissTV.it@SD`), LEO TV (`LEOTV.cz`), Music Box Sexy (`MusicBoxSexy.cz@SD`), NTC TV (`NTCTV.in@SD`), NatureTime France (`NatureTime.ca@France`), Only Music (`Only.Music.in`), Pixel TV (`PixelTV.ua@SD`), Qwest TV (`QwestTV.fr@SD`), RTL 102.5 Caliente (`RTL1025Caliente.it@SD`), Sonar Bangla (`SonarBangla.in@SD`), Spondon (`Spondon.in@SD`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray Easy Listening (`StingrayEasyListening.ca@SD`), Stingray Flashback 70's (`StingrayFlashback70s.ca@SD`), Stingray Greatest Holiday Hits (`StingrayGreatestHolidayHits.us@SD`), Stingray Hit List (`StingrayHitList.ca`), Stingray Hot Country (`StingrayHotCountry.ca@SD`), Stingray Jukebox Oldies (`StingrayJukeboxOldies.ca@SD`), Stingray Nothin' But 90s (`StingrayNothinBut90s.ca@SD`), Stingray Pop Adult (`StingrayPopAdult.ca@SD`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray Romance Latino (`StingrayRomanceLatino.ca@SD`), Stingray Smooth Jazz (`StingraySmoothJazz.ca@SD`), Stingray Soul Storm (`StingraySoulStorm.ca@SD`), Stingray The Spa (`StingrayTheSpa.ca`), Stingray The Spa (`StingrayTheSpa.ca@SD`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Stingray Today's K-Pop (`StingrayTodaysKPop.ca@SD`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca@SD`), Strongman Champions League (`StrongmanChampionsLeague.uk@SD`), Suriya TV (`SuriyaTV.in`), Suriya TV (`SuriyaTV.in@SD`), Teletubbies (`Teletubbies.uk@SD`), Terra Mater WILD (`TerraMaterWILD.de@German`), Ultimate TV (`UltimateTV.in@SD`), World Poker Tour (`WorldPokerTour.us@US`), Yu-Gi-Oh! (`YuGiOh.us@SD`), Metro (`custom.24-7-xxx-metro`), Reality Kings (`custom.24-7-xxx-reality-kings`), ACI Sport TV (`custom.acisporttv`), NEW K-POP (`custom.new-k-pop-us-music`), Stingray Cozy Cafe (`custom.stingray-cozy-cafe-ca-music`), Stingray Euro Hits (`custom.stingray-euro-hits-ca-music`), Brazzers Europe (`custom.xxx-brazzers-europe`), Ero Xxx (`custom.xxx-ero-xxx`), Hustler (`custom.xxx-hustler`), Super One (`custom.xxx-super-one`), Vivid Red (`custom.xxx-vivid-red`)
- IDs with an in-window published programme but no current/future source match at the later scan: **0**
- In-window published IDs not counted source-current/future: none
- Source-current/future IDs whose published programme is no longer current by report time: **62**
- Source-current/future IDs no longer current in the published guide: ACI Sport TV (`ACISportTV.it@SD`), Amar Bangla (`AamarBangla.in`), Aaryaa TV (`AaryaaTV.in`), Aaryaa TV (`AaryaaTV.in@SD`), American Ninja Warrior (`AmericanNinjaWarrior.us@SD`), Bang U (`BangU.us`), BeJoy.kids (`BeJoykids.it@HD`), Caillou (`Caillou.fr@SD`), Camp Spoopy (`CampSpoopy.us@SD`), Cine Western (Spain) (`CineWestern.es@SD`), Enter-Film (`EnterFilm.ua@SD`), Iqraa TV (`IqraaTV`), KTV Bangla (`KTVBangla.in@SD`), Kiss Kiss TV (`KissKissTV.it@SD`), LEO TV (`LEOTV.cz`), Music Box Sexy (`MusicBoxSexy.cz@SD`), NTC TV (`NTCTV.in@SD`), NatureTime France (`NatureTime.ca@France`), Only Music (`Only.Music.in`), Pixel TV (`PixelTV.ua@SD`), Qwest TV (`QwestTV.fr@SD`), RTL 102.5 Caliente (`RTL1025Caliente.it@SD`), Sonar Bangla (`SonarBangla.in@SD`), Spondon (`Spondon.in@SD`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray Easy Listening (`StingrayEasyListening.ca@SD`), Stingray Flashback 70's (`StingrayFlashback70s.ca@SD`), Stingray Greatest Holiday Hits (`StingrayGreatestHolidayHits.us@SD`), Stingray Hit List (`StingrayHitList.ca`), Stingray Hot Country (`StingrayHotCountry.ca@SD`), Stingray Jukebox Oldies (`StingrayJukeboxOldies.ca@SD`), Stingray Nothin' But 90s (`StingrayNothinBut90s.ca@SD`), Stingray Pop Adult (`StingrayPopAdult.ca@SD`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray Romance Latino (`StingrayRomanceLatino.ca@SD`), Stingray Smooth Jazz (`StingraySmoothJazz.ca@SD`), Stingray Soul Storm (`StingraySoulStorm.ca@SD`), Stingray The Spa (`StingrayTheSpa.ca`), Stingray The Spa (`StingrayTheSpa.ca@SD`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Stingray Today's K-Pop (`StingrayTodaysKPop.ca@SD`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca@SD`), Strongman Champions League (`StrongmanChampionsLeague.uk@SD`), Suriya TV (`SuriyaTV.in`), Suriya TV (`SuriyaTV.in@SD`), Teletubbies (`Teletubbies.uk@SD`), Terra Mater WILD (`TerraMaterWILD.de@German`), Ultimate TV (`UltimateTV.in@SD`), World Poker Tour (`WorldPokerTour.us@US`), Yu-Gi-Oh! (`YuGiOh.us@SD`), Metro (`custom.24-7-xxx-metro`), Reality Kings (`custom.24-7-xxx-reality-kings`), ACI Sport TV (`custom.acisporttv`), NEW K-POP (`custom.new-k-pop-us-music`), Stingray Cozy Cafe (`custom.stingray-cozy-cafe-ca-music`), Stingray Euro Hits (`custom.stingray-euro-hits-ca-music`), Brazzers Europe (`custom.xxx-brazzers-europe`), Ero Xxx (`custom.xxx-ero-xxx`), Hustler (`custom.xxx-hustler`), Super One (`custom.xxx-super-one`), Vivid Red (`custom.xxx-vivid-red`)
- Published current/future IDs not counted source-current/future: **0**
- Published current/future IDs not counted source-current/future: none


## Playlist EPG Headers

| Playlist | Header status |
|---|---|
| IPTV-Playlist.m3u | OK |
| International-Playlist.m3u | OK |

## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **9984e08ae9e3a60145c9376882c244a81d0f8526b9794a3978714b5dab6d9ed9**
- International-Playlist.m3u SHA-256: **7762b2644675b92a5ab0d59ae1983e213855f70f78ebf265ae7bd62e9430e84a**

