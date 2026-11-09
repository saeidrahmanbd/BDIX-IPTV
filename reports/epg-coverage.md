# EPG Coverage & Mapping Report

Generated: **2026-11-09T03:42:09+00:00**

This report audits active unique channel identities across the two maintained playlists configured in the automated EPG pipeline. A source mapping is not counted as usable current/future coverage unless it has a valid programme interval and valid non-empty multilingual title data within the generator's -6-hour/+7-day window; English titles rank first, then Bengali, then other valid languages.
The XMLTV guide is published at **epg/epg.xml**. The published guide uses the playlist's tvg-id as the XMLTV channel ID, not the upstream provider's source ID.

## Overall Coverage

- Active unique playlist channel IDs audited: **1493**
- IDs with an EPG source mapping: **681/1493 (45.6%)**
- IDs with usable current/future source schedules (nonblank multilingual titles (English preferred, then Bengali, then other valid languages)): **619/1493 (41.5%)**
- IDs with no EPG source mapping: **812**

## Coverage by Playlist Group

| Group | Active IDs | Mapped IDs | Current/future | No mapping |
|---|---:|---:|---:|---:|
| Argentina | 14 | 1 | 0 | 13 |
| Bangladesh | 72 | 4 | 2 | 68 |
| Brazil | 10 | 4 | 4 | 6 |
| Bulgaria | 19 | 6 | 6 | 13 |
| Canada | 30 | 23 | 17 | 7 |
| Chile | 11 | 0 | 0 | 11 |
| China | 9 | 3 | 3 | 6 |
| Colombia | 9 | 1 | 0 | 8 |
| Costa Rica | 9 | 0 | 0 | 9 |
| Czech Republic | 23 | 18 | 18 | 5 |
| DO | 10 | 1 | 0 | 9 |
| Documentary & Wildlife | 60 | 46 | 34 | 14 |
| Estonia | 6 | 0 | 0 | 6 |
| France | 40 | 15 | 14 | 25 |
| Germany | 39 | 13 | 13 | 26 |
| Greece | 8 | 2 | 2 | 6 |
| Hungary | 15 | 7 | 7 | 8 |
| Indian Bangla | 42 | 31 | 29 | 11 |
| Indian Entertainment | 174 | 147 | 142 | 27 |
| Indian Movies | 81 | 60 | 55 | 21 |
| Indian Music | 68 | 57 | 54 | 11 |
| International | 157 | 32 | 24 | 125 |
| Iran | 11 | 1 | 0 | 10 |
| Italy | 24 | 11 | 11 | 13 |
| Kids | 44 | 26 | 23 | 18 |
| Lebanon | 6 | 1 | 0 | 5 |
| Mexico | 15 | 6 | 5 | 9 |
| Netherlands | 15 | 9 | 6 | 6 |
| Pakistani | 18 | 1 | 1 | 17 |
| Panama | 5 | 0 | 0 | 5 |
| Peru | 8 | 0 | 0 | 8 |
| Poland | 25 | 13 | 12 | 12 |
| Religious | 25 | 4 | 4 | 21 |
| Romania | 29 | 9 | 9 | 20 |
| Russia | 53 | 15 | 15 | 38 |
| Saudi Arabia | 8 | 0 | 0 | 8 |
| Singapore | 5 | 1 | 1 | 4 |
| Spain | 18 | 4 | 4 | 14 |
| Sports | 60 | 29 | 26 | 31 |
| Sweden | 12 | 2 | 2 | 10 |
| Turkey | 14 | 0 | 0 | 14 |
| Ukraine | 20 | 6 | 6 | 14 |
| United Kingdom | 14 | 3 | 2 | 11 |
| United States | 147 | 69 | 68 | 78 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Source Status

- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz — 946 channel IDs; 699 IDs with usable current/future programmes; 72680 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz — 54 channel IDs; 2 IDs with usable current/future programmes; 19 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz — 557 channel IDs; 506 IDs with usable current/future programmes; 16540 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — https://www.free-epg.de/api/epg/pk.xml.gz — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 503: Service Unavailable
- **OK** — https://iptv-epg.org/files/epg-in.xml.gz — 419 channel IDs; 267 IDs with usable current/future programmes; 47885 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://epg.lat/files/in.xml.gz — 1166 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://epg.lat/files/us.xml.gz — 4456 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.free-epg.de/api/epg/in.xml.gz — 947 channel IDs; 771 IDs with usable current/future programmes; 64317 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.free-epg.de/api/epg/us.xml.gz — 5546 channel IDs; 5541 IDs with usable current/future programmes; 225359 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.open-epg.com/files/india.xml.gz — 1178 channel IDs; 773 IDs with usable current/future programmes; 48631 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ar.xml.gz — 185 channel IDs; 132 IDs with usable current/future programmes; 4147 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-bg.xml.gz — 116 channel IDs; 91 IDs with usable current/future programmes; 13957 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-br.xml.gz — 182 channel IDs; 133 IDs with usable current/future programmes; 21852 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ca.xml.gz — 808 channel IDs; 802 IDs with usable current/future programmes; 103124 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://iptv-epg.org/files/epg-cl.xml.gz — 184 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://iptv-epg.org/files/epg-co.xml.gz — 180 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-cz.xml.gz — 261 channel IDs; 223 IDs with usable current/future programmes; 45544 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-de.xml.gz — 438 channel IDs; 381 IDs with usable current/future programmes; 59434 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-es.xml.gz — 300 channel IDs; 276 IDs with usable current/future programmes; 28709 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-fr.xml.gz — 485 channel IDs; 373 IDs with usable current/future programmes; 32081 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-gr.xml.gz — 177 channel IDs; 163 IDs with usable current/future programmes; 12427 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-hk.xml.gz — 176 channel IDs; 127 IDs with usable current/future programmes; 18810 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-hu.xml.gz — 152 channel IDs; 130 IDs with usable current/future programmes; 25300 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-it.xml.gz — 306 channel IDs; 261 IDs with usable current/future programmes; 30289 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-mx.xml.gz — 175 channel IDs; 136 IDs with usable current/future programmes; 13946 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-nl.xml.gz — 184 channel IDs; 154 IDs with usable current/future programmes; 33827 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://iptv-epg.org/files/epg-pe.xml.gz — 128 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-pl.xml.gz — 447 channel IDs; 402 IDs with usable current/future programmes; 77654 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-pt.xml.gz — 195 channel IDs; 147 IDs with usable current/future programmes; 26788 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ro.xml.gz — 282 channel IDs; 257 IDs with usable current/future programmes; 44810 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ru.xml.gz — 223 channel IDs; 198 IDs with usable current/future programmes; 42256 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-rs.xml.gz — 265 channel IDs; 239 IDs with usable current/future programmes; 20255 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-se.xml.gz — 95 channel IDs; 80 IDs with usable current/future programmes; 13880 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-tr.xml.gz — 108 channel IDs; 81 IDs with usable current/future programmes; 15902 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-gb.xml.gz — 932 channel IDs; 875 IDs with usable current/future programmes; 80952 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-at.xml.gz — 286 channel IDs; 262 IDs with usable current/future programmes; 38114 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-au.xml.gz — 490 channel IDs; 486 IDs with usable current/future programmes; 50194 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-cr.xml.gz — 84 channel IDs; 75 IDs with usable current/future programmes; 7504 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-pa.xml.gz — 121 channel IDs; 111 IDs with usable current/future programmes; 8844 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-py.xml.gz — 79 channel IDs; 70 IDs with usable current/future programmes; 7472 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-sg.xml.gz — 209 channel IDs; 152 IDs with usable current/future programmes; 24188 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/at.xml.gz — 286 channel IDs; 262 IDs with usable current/future programmes; 38114 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/cn.xml.gz — 711 channel IDs; 533 IDs with usable current/future programmes; 41617 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/cr.xml.gz — 84 channel IDs; 75 IDs with usable current/future programmes; 7502 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://free-epg.de/api/epg/ec.xml.gz — 104 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — https://free-epg.de/api/epg/ee.xml.gz — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 503: Service Unavailable
- **OK** — https://free-epg.de/api/epg/pa.xml.gz — 121 channel IDs; 111 IDs with usable current/future programmes; 8841 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://free-epg.de/api/epg/sa.xml.gz — 138 channel IDs; 18 IDs with usable current/future programmes; 792 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://free-epg.de/api/epg/ua.xml.gz — 231 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/in.xml — 206 channel IDs; 202 IDs with usable current/future programmes; 2094 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/us.xml — 593 channel IDs; 582 IDs with usable current/future programmes; 4853 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml — 698 channel IDs; 621 IDs with usable current/future programmes; 41265 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz — 717 channel IDs; 676 IDs with usable current/future programmes; 35725 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=IN1.xml.gz — 946 channel IDs; 699 IDs with usable current/future programmes; 72679 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=IN4.xml.gz — 557 channel IDs; 506 IDs with usable current/future programmes; 16535 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — https://m3u-edit.com/epg-source.php?file=india_dishtv.in.xml — 394 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml — 762 channel IDs; 760 IDs with usable current/future programmes; 81088 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml — 1496 channel IDs; 1306 IDs with usable current/future programmes; 38652 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml — 286 channel IDs; 2 IDs with usable current/future programmes; 1149 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml — 120 channel IDs; 100 IDs with usable current/future programmes; 20192 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/slingtv.xml — 6 channel IDs; 6 IDs with usable current/future programmes; 119 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/epg.xml.gz — 2233 channel IDs; 884 IDs with usable current/future programmes; 26749 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/jioepg.xml.gz — 1173 channel IDs; 262 IDs with usable current/future programmes; 7898 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/tsepg.xml.gz — 717 channel IDs; 676 IDs with usable current/future programmes; 35722 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz — 487 channel IDs; 385 IDs with usable current/future programmes; 33993 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.open-epg.com/files/unitedkingdom.xml.gz — 566 channel IDs; 539 IDs with usable current/future programmes; 19353 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz — 792 channel IDs; 774 IDs with usable current/future programmes; 69069 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-us.xml.gz — 12843 channel IDs; 12427 IDs with usable current/future programmes; 899986 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz — 912 channel IDs; 823 IDs with usable current/future programmes; 73600 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz — 345 channel IDs; 280 IDs with usable current/future programmes; 32942 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz — 696 channel IDs; 695 IDs with usable current/future programmes; 57237 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CH1.xml.gz — 751 channel IDs; 730 IDs with usable current/future programmes; 69779 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CZ1.xml.gz — 1087 channel IDs; 517 IDs with usable current/future programmes; 45470 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DE1.xml.gz — 266 channel IDs; 250 IDs with usable current/future programmes; 21757 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DO1.xml.gz — 56 channel IDs; 55 IDs with usable current/future programmes; 2328 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_ES1.xml.gz — 256 channel IDs; 237 IDs with usable current/future programmes; 6719 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_FR1.xml.gz — 574 channel IDs; 531 IDs with usable current/future programmes; 42632 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_GR1.xml.gz — 321 channel IDs; 301 IDs with usable current/future programmes; 21939 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz — 143 channel IDs; 132 IDs with usable current/future programmes; 11038 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HU1.xml.gz — 193 channel IDs; 167 IDs with usable current/future programmes; 19378 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IT1.xml.gz — 195 channel IDs; 151 IDs with usable current/future programmes; 17150 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz — 163 channel IDs; 129 IDs with usable current/future programmes; 8508 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MX1.xml.gz — 178 channel IDs; 164 IDs with usable current/future programmes; 14377 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_NL1.xml.gz — 159 channel IDs; 156 IDs with usable current/future programmes; 18115 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_PL1.xml.gz — 636 channel IDs; 581 IDs with usable current/future programmes; 94659 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_RO1.xml.gz — 370 channel IDs; 356 IDs with usable current/future programmes; 38977 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_SA2.xml.gz — 31 channel IDs; 31 IDs with usable current/future programmes; 3451 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_TR1.xml.gz — 178 channel IDs; 138 IDs with usable current/future programmes; 10140 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR1.xml.gz — 266 channel IDs; 98 IDs with usable current/future programmes; 13439 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR2.xml.gz — 97 channel IDs; 92 IDs with usable current/future programmes; 9243 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://hum.tv/schedule/ — 1 channel IDs; 1 IDs with usable current/future programmes; 21 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — RTV official daily schedule (Bangladesh) — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; Could not obtain a current official RTV schedule over verified HTTPS (rtvonline: no daily schedule article link on homepage; www.rtvbd.tv: URLError after retry; rtvbd.tv: URLError after retry)
- **FAILED** — https://migrate.btvlive.gov.bd/channel/BTV — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; <urlopen error [Errno -3] Temporary failure in name resolution>
- **FAILED** — Maasranga official weekly grid (undated) — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 403: Forbidden
- **NO_PROGRAMMES** — M3U4U XMLTV (private Actions secret) — 229 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — iptv-org/epg (targeted build-time guide) — 149 channel IDs; 126 IDs with usable current/future programmes; 4689 eligible programme rows with valid non-empty titles in any language in the guide window

## Channels Requiring Attention

The table includes every active channel identity without usable current/future guide data, not only Indian channels. NO_GUIDE_HIT means no configured source could be matched; MAPPED_ID_ONLY means an identity was found but no usable schedule was available; MAPPED_NOT_CURRENTLY_FOUND means a retained mapping was not found in the currently configured feeds.

| Group | Channel | Playlist ID | EPG source ID | Status |
|---|---|---|---|---|
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
| Bangladesh | Bengali Beats | BengaliBeats.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bijoy TV | BijoyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Boishakhi TV | BoishakhiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV Chattogram | BTVChattogram.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 1 | Channel1.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 24 | Channel24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 52 | Channel52.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel Europe | ChannelEurope.uk | - | NO_GUIDE_HIT |
| Bangladesh | Channel I | ChannelI.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel S | ChannelS.uk | - | NO_GUIDE_HIT |
| Bangladesh | Channel S UK | ChannelS.uk@679aa9 | - | NO_GUIDE_HIT |
| Bangladesh | DBC News | DBCNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Deepto TV | DeeptoTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Desh TV | DeshTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Deshe Bideshe | DesheBideshe.ca | - | NO_GUIDE_HIT |
| Bangladesh | Deshi TV | DeshiTV.ca@SD | - | NO_GUIDE_HIT |
| Bangladesh | Doyel TV | DoyelTV.ca@SD | - | NO_GUIDE_HIT |
| Bangladesh | Duronto TV | DurontoTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Duronto TV | DurontoTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | Ekattor TV | EkattorTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekhon TV | EkhonTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekushey TV | EkusheyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Enter TV | EnterTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | G Series Drama | GSeriesDrama.bd | - | NO_GUIDE_HIT |
| Bangladesh | G TV | GaziTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | GAZI TV | GaziTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | Global TV | GlobalTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Independent TV | IndependentTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | JA TV | JATV.bd | - | NO_GUIDE_HIT |
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
| Bangladesh | Star News | StarNews.bd | - | NO_GUIDE_HIT |
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
| Documentary & Wildlife | Amazing Discoveries TV | AmazingDiscoveriesTV.in | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic Adventure Earth | AutenticAdventureEarth.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic History | AutenticHistory.de | - | NO_GUIDE_HIT |
| Documentary & Wildlife | CGTN Documentary | CGTNDocumentary.cn | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Turbo Latin America | DiscoveryTurboLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
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
| Germany | Rakuten TV Comedy Movies Germany | custom.rakuten-tv-comedy-movies-germany-de-movie | - | NO_GUIDE_HIT |
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
| Indian Entertainment | Shemaroo Umang | ShemarooUmang.in@SD | ShemarooUmang.in | MAPPED_ENDED |
| Indian Entertainment | Manoranjan Prime | ManoranjanPrime.in@SD | 154892 | 10000000075992492 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | One Paschima | OnePaschima.in@SD | One.Paschima.in | MAPPED_NOT_CURRENTLY_FOUND |
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
| Indian Entertainment | GTC Punjabi UK | GTCPunjabi.in@UK | - | NO_GUIDE_HIT |
| Indian Entertainment | GTC Punjabi US | GTCPunjabi.in@US | - | NO_GUIDE_HIT |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Kalika TV | KalikaTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Kerala Vision | KeralaVision.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Maha Punjabi | MahaPunjabi.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Marutam TV | MarutamTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | MNTV (Tamil) | MarutamTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Pardesi TV | PardesiTV.ca | - | NO_GUIDE_HIT |
| Indian Entertainment | Pulari TV | PulariTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Punjabi TV | PunjabiTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Q TV | QTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | SADA TV | SADATV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | SADA TV | SADATV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Sooriyan TV | SooriyanTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Swantham | Swantham.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Thendral TV | ThendralTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | UTV Palakkad | UTVPalakkad.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Thalaa TV | ThalaaTV.in@HD | 6601 | MAPPED_ENDED |
| Indian Movies | Tolly TV | TollyTV.in | 6613 | MAPPED_ENDED |
| Indian Movies | Tolly TV | TollyTV.in@HD | 6613 | MAPPED_ENDED |
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
| Indian Music | AMN TV | AMNTV.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Andy Haryana | AndyHaryana.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Deewana | DeewanaHD.in | - | NO_GUIDE_HIT |
| Indian Music | Hindi Hits | HindiHits.in | - | NO_GUIDE_HIT |
| Indian Music | Hindi Hits | HindiHits.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Oli TV | OliTV.in@SD | - | NO_GUIDE_HIT |
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
| International | First Music Channel | FirstMusicChannel.by@SD | - | NO_GUIDE_HIT |
| International | First Music Channel Russia | FirstMusicChannelRussia.by@SD | - | NO_GUIDE_HIT |
| International | Folk Klub TV | FolkKlubTV.au@SD | - | NO_GUIDE_HIT |
| International | Folk TV | FolkTV.mk@SD | - | NO_GUIDE_HIT |
| International | Folx Slovenija | FolxSlovenija.si@SD | - | NO_GUIDE_HIT |
| International | FON Music | FONMusic.us | - | NO_GUIDE_HIT |
| International | Fun Vision | FunVision.be@SD | - | NO_GUIDE_HIT |
| International | Fusion TV | FUSIONTV.mq@SD | - | NO_GUIDE_HIT |
| International | Gugak TV | GugakTV.kr@SD | - | NO_GUIDE_HIT |
| International | HBO Asia Taiwan | HBOAsia.sg@Taiwan | - | NO_GUIDE_HIT |
| International | HEi Now | HEiNow.py@SD | - | NO_GUIDE_HIT |
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
| International | PORNBOX: NUBILE FILMS | custom.pornbox-nubile-films | - | NO_GUIDE_HIT |
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
| Italy | Rakuten TV Drama Movies Italy | custom.rakuten-tv-drama-movies-italy-it-movie | - | NO_GUIDE_HIT |
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
| Kids | Bantul the Great | BantulTheGreat.us | - | NO_GUIDE_HIT |
| Kids | Discovery Kids Latin America Colombia | DiscoveryKidsLatinAmerica.us@Colombia | - | NO_GUIDE_HIT |
| Kids | Disney Jr | DisneyJr.us | - | NO_GUIDE_HIT |
| Kids | Doraemon TV | DoraemonTV.us | - | NO_GUIDE_HIT |
| Kids | Epic Kids Digital | EpicKidsDigital.us | - | NO_GUIDE_HIT |
| Kids | Lego Channel | LegoChannel.us@SD | - | NO_GUIDE_HIT |
| Kids | Moonbug Kids | MoonbugKids.uk | - | NO_GUIDE_HIT |
| Kids | Powerkids Kartoon Channel | PowerkidsKartoonChannel.us | - | NO_GUIDE_HIT |
| Kids | Smurf TV | SmurfTV.us | - | NO_GUIDE_HIT |
| Kids | Tom and Jerry | TomAndJerry.do | - | NO_GUIDE_HIT |
| Kids | Tooku | Tooku.ru | - | NO_GUIDE_HIT |
| Kids | Toon Goggles Junior | ToonGogglesJunior.us | - | NO_GUIDE_HIT |
| Kids | TRT Cocuk | TRTCocuk.tr@SD | - | NO_GUIDE_HIT |
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
| Pakistani | Bol Entertainment | BolEntertainment.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | BS Film | BSFilm.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Falak TV | FalakTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Filmax | Filmax.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | HUM Masala | HUMMasala.pk | - | NO_GUIDE_HIT |
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
| Religious | Islamic TV | 223000 | - | NO_GUIDE_HIT |
| Religious | Islamic TV | IslamicTV.sa | - | NO_GUIDE_HIT |
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
| Romania | Smart Radio | custom.smart-radio-ro-music | - | NO_GUIDE_HIT |
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
| Russia | Horoshee Kino | HorosheeKino.ru@SD | - | NO_GUIDE_HIT |
| Russia | Illusion+ | IllusionPlus.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kino 1 (Russia) | Kino1.ru@International | - | NO_GUIDE_HIT |
| Russia | Kino TV | KinoTV.ru@HD | - | NO_GUIDE_HIT |
| Russia | Kinopokaz | custom.kinopokaz-ru-movie | - | NO_GUIDE_HIT |
| Russia | Kinoseriya | custom.kinoseriya-ru-movie | - | NO_GUIDE_HIT |
| Russia | Live Music Channel | LiveMusicChannel.ru@HD | - | NO_GUIDE_HIT |
| Russia | MTV Volgograd | MTVVolgograd.ru@SD | - | NO_GUIDE_HIT |
| Russia | Muz Soyuz | MuzSoyuz.ru@SD | - | NO_GUIDE_HIT |
| Russia | Muzyka 1 | Muzyka1.ru@International | - | NO_GUIDE_HIT |
| Russia | Muzyka Kino | MuzykaKino.ru@International | - | NO_GUIDE_HIT |
| Russia | Nash Kinopokaz | NashKinopokaz.ru@HD | - | NO_GUIDE_HIT |
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
| Spain | Rakuten TV Action Movies Germany | RakutenTVActionMoviesGermany.es | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Family Movies | RakutenTVFamilyMovies.es | - | NO_GUIDE_HIT |
| Spain | RTV Vida | RTVVida.es@SD | - | NO_GUIDE_HIT |
| Spain | SpektraTV | SpektraTV.es@SD | - | NO_GUIDE_HIT |
| Spain | TVOMIX | TVOMIX.es@HD | - | NO_GUIDE_HIT |
| Spain | XPTV1 | XPTV1.es@SD | - | NO_GUIDE_HIT |
| Sports | FITE 24/7 | FITE247.us@SD | FITE247.us | MAPPED_ENDED |
| Sports | FIFA+ | custom.fifa | IN270000230 | USBD12000255B | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Red Bull TV | RedBullTV.at@EUMENA | jtv2779 | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | A Sports | ASports.pk | - | NO_GUIDE_HIT |
| Sports | ACCDN | custom.accdn | - | NO_GUIDE_HIT |
| Sports | ATG Live | custom.atglive | - | NO_GUIDE_HIT |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | - | NO_GUIDE_HIT |
| Sports | beIN Sports XTRA en Espanol | custom.beinsportsxtraenespanol | - | NO_GUIDE_HIT |
| Sports | DeporTV | DeporTV.ar@SD | - | NO_GUIDE_HIT |
| Sports | ESPN Premium (Argentina) | ESPNPremium.ar@HD | - | NO_GUIDE_HIT |
| Sports | Fight Network | custom.fightnetwork | - | NO_GUIDE_HIT |
| Sports | Goal TV | GoalTV.in | - | NO_GUIDE_HIT |
| Sports | Horse & Country | custom.horseandcountry | - | NO_GUIDE_HIT |
| Sports | Inter TV (Italy) | custom.intertv | - | NO_GUIDE_HIT |
| Sports | Kabaddi 24x7 | Kabaddi24x7.in@SD | - | NO_GUIDE_HIT |
| Sports | KTV Sport Plus | KTVSportPlus.kw@SD | - | NO_GUIDE_HIT |
| Sports | MTRSPT1 | custom.mtrspt | - | NO_GUIDE_HIT |
| Sports | PK Sports | PKSports.pk@SD | - | NO_GUIDE_HIT |
| Sports | PTV Sports | PTVSports.pk | - | NO_GUIDE_HIT |
| Sports | Rally TV | custom.rallytv | - | NO_GUIDE_HIT |
| Sports | Realitatea Sportiva | custom.realitateasportiva | - | NO_GUIDE_HIT |
| Sports | Sport 1 (Ukraine) | Sport1.ua@SD | - | NO_GUIDE_HIT |
| Sports | Sport 3 | Sport3.ua@SD | - | NO_GUIDE_HIT |
| Sports | Sportivnyy | custom.sportivnyy | - | NO_GUIDE_HIT |
| Sports | Sports First TV | SportsFirstTV.us | - | NO_GUIDE_HIT |
| Sports | Sqala TV | SqalaTV.pe@SD | - | NO_GUIDE_HIT |
| Sports | Suspilne. Sport | SuspilneSport.ua@SD | - | NO_GUIDE_HIT |
| Sports | T Sports | TSports.bd | - | NO_GUIDE_HIT |
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
| United States | Pluto TV Cine Romance | PlutoTVCineRomance.us@BR | - | NO_GUIDE_HIT |
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

- XMLTV channel IDs published: **1072**
- Active playlist IDs present in the published guide: **739/1493 (49.5%)**
- Active playlist IDs with usable current/future programmes: **569/1493 (38.1%)**
- Active playlist IDs with usable programmes anywhere in the guide window (-6h/+7d): **582/1493 (39.0%)**
- Mapped playlist IDs present in the guide: **672/681 (98.7%)**
- Mapped playlist IDs with usable current/future programmes: **512/681 (75.2%)**
- Mapped playlist IDs with usable programmes anywhere in the guide window: **523/681 (76.8%)**
- Eligible programme rows published in the guide window: **79876**
- Mapped playlist IDs missing from the published XMLTV channel list: **9**
- Missing mapped playlist IDs: AllTimeMovies.in@SD, BRIDGE.ru@SD, BRIDGEDeluxe.ru@SD, EmanChannel, Kinowood.ua@SD, MusicBoxSexy.cz@SD, RadionorbaTV.it, RusskiyBestseller.ru@SD, RusskiyDetektiv.ru@SD
- Published mapped IDs without usable current/future programmes: **160**
- IDs without usable current/future programmes: AamarBangla.in, AaryaaTV.in, AaryaaTV.in@SD, AlrightTV.in@SD, AmarBanglaDigital.in, AndPictures.in@SD, B4UKadak.in@SD, B4UMovies.in@India, BabySharkTV.us, BangBangTV, Bollygold.in@HD, CinePlus.ua@SD, CinePlusHit.ua@SD, CineRomantico.us@SD, CineWestern.es@SD, ClassicMovieWesterns.us@SD, CosmosTv.ar@HD, CrimeJustice.us, CrimeSceneTV.us, DhoolTV.in@SD, DiscoveryChannel.in@HD, DocuBayTV.in, ETVBeats.in@HD, ETVComedy.in, ETVComedy.in@HD, ETVJosh.in, ETVJosh.in@HD, EkamraBharatOdia.in@SD, EkamraCinema.in, EkamraMusiq.in, EpicBhojpuri.in@SD, EpicBhojpuriDigital.in, EpicCrimes.in, EpicCrimes.in@SD, FITE247.us@SD, Fast1.in@SD, GoldminesMovies.in@SD, HallmarkMoviesMore.us, HouseOfCrime.us, INFAST.nl, INWILD.nl, InWonder.nl, KTVBangla.in@SD, KappaTV.in@ALT1, KidDoMATIX.us, KinoNova.bg@SD, KissKissTV.it@SD, MaasrangaTV.bd, ManoranjanPrime.in@SD, Mastiii.in@SD, MrBeanAnimated.uk, MultiPremier.mx@SD, Muzvar.ua@SD, MuzykaPervogo.ru@SD, MyTimeMovieNetworkEast.us, NHBollyFlix.in, NHBollyRaga.in, NHBollyRaga.in@HD, NHTamilGold.in, NHTamilGold.in@HD (and 100 more)

## Source / Published Schedule Reconciliation

- IDs with usable current/future source schedule data: **619/1493 (41.5%)**
- IDs with usable current/future schedules in published XMLTV at report time: **569/1493 (38.1%)**
- IDs with usable programmes in the published guide's common -6h/+7d window: **582/1493 (39.0%)**
- Current/future source IDs without any usable published programme in that common window: **107**
- Source-scheduled IDs without a usable published programme in the common window: Amar Bangla (`AamarBangla.in`), Aaryaa TV (`AaryaaTV.in`), Aaryaa TV (`AaryaaTV.in@SD`), All Time Movies (`AllTimeMovies.in@SD`), Alright! TV (`AlrightTV.in@SD`), Amar Bangla Digital (`AmarBanglaDigital.in`), B4U Kadak (`B4UKadak.in@SD`), BRIDGE (`BRIDGE.ru@SD`), BRIDGE Deluxe (`BRIDGEDeluxe.ru@SD`), Baby Shark TV (`BabySharkTV.us`), Bollygold (`Bollygold.in@HD`), Cine Romantico (`CineRomantico.us@SD`), Cine Western (Spain) (`CineWestern.es@SD`), Classic Movie Westerns (`ClassicMovieWesterns.us@SD`), Dhool TV (`DhoolTV.in@SD`), Discovery Channel (India) (`DiscoveryChannel.in@HD`), DocuBay TV (`DocuBayTV.in`), ETV Beats (`ETVBeats.in@HD`), ETV Comedy (`ETVComedy.in`), ETV Comedy (`ETVComedy.in@HD`), ETV Josh (`ETVJosh.in`), ETV Josh (`ETVJosh.in@HD`), Ekamra Bharat Odia (`EkamraBharatOdia.in@SD`), Eman Channel (`EmanChannel`), Epic Crimes (`EpicCrimes.in`), Epic Crimes (`EpicCrimes.in@SD`), Fast1 (`Fast1.in@SD`), Goldmines Movies (`GoldminesMovies.in@SD`), Hallmark Movies & More (`HallmarkMoviesMore.us`), InWonder (`InWonder.nl`), KTV Bangla (`KTVBangla.in@SD`), Kappa TV (Music) (`KappaTV.in@ALT1`), Kino Nova (`KinoNova.bg@SD`), Kinowood (`Kinowood.ua@SD`), Kiss Kiss TV (`KissKissTV.it@SD`), Mr Bean Animated (`MrBeanAnimated.uk`), Music Box Sexy (`MusicBoxSexy.cz@SD`), MyTime Movie Network East (`MyTimeMovieNetworkEast.us`), NH BollyFlix (`NHBollyFlix.in`), NH BollyRaga (`NHBollyRaga.in`), NH BollyRaga (`NHBollyRaga.in@HD`), NH Tamil Gold (`NHTamilGold.in`), NH Tamil Gold (`NHTamilGold.in@HD`), NTC TV (`NTCTV.in@SD`), Nashe Novoe Kino (`NasheNovoeKino.ru@SD`), Nick Bangla (`NickBangla.bd`), Only Music (`Only.Music.in`), OuterSphere (`OuterSphere.us`), OuterSphere (`OuterSphere.us@SD`), PGA Tour (`PGATour.us@SD`), Paramount Movie Channel (`ParamountMovieChannel.us@SD`), Pitaara Comedy (`PitaaraComedy.in@SD`), Public Movies (`PublicMovies.in@SD`), Qello Concerts by Stingray (`QelloConcertsbyStingray.ca@SD`), Qwest TV (`QwestTV.fr@SD`), R Plus Gold (`RPlusGold.in@SD`), RTL 102.5 Caliente (`RTL1025Caliente.it@SD`), Radio Norba TV (`RadionorbaTV.it`), RetroCrush (`RetroCrush.us`), Roja Movies (`RojaMovies.in@SD`), Roja TV (`RojaTV.in`), Russkiy Bestseller (`RusskiyBestseller.ru@SD`), Russkiy Detektiv (`RusskiyDetektiv.ru@SD`), Sonar Bangla (`SonarBangla.in@SD`), South Station (`SouthStation.in`), South Station (`SouthStation.in@HD`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray Easy Listening (`StingrayEasyListening.ca@SD`), Stingray Flashback 70's (`StingrayFlashback70s.ca@SD`), Stingray Greatest Holiday Hits (`StingrayGreatestHolidayHits.us@SD`), Stingray Hit List (`StingrayHitList.ca`), Stingray Hot Country (`StingrayHotCountry.ca@SD`), Stingray Jukebox Oldies (`StingrayJukeboxOldies.ca@SD`), Stingray Nothin' But 90s (`StingrayNothinBut90s.ca@SD`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray Smooth Jazz (`StingraySmoothJazz.ca@SD`), Stingray Soul Storm (`StingraySoulStorm.ca@SD`), Stingray The Spa (`StingrayTheSpa.ca`), Stingray The Spa (`StingrayTheSpa.ca@SD`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Stingray Today's K-Pop (`StingrayTodaysKPop.ca@SD`), Strawberry Shortcake (`StrawberryShortcake.us`), Studio Yuva (`StudioYuva.in`), Studio Yuva (`StudioYuva.in@SD`), Suriya TV (`SuriyaTV.in`), Suriya TV (`SuriyaTV.in@SD`), Survivor (`Survivor.us`), Teletubbies (`Teletubbies.uk`), Telugu One (`TeluguOne.in@HD`), The Movie Club (`TheMovieClub.in@HD`), The Movie Club +2 (`TheMovieClub.in@Plus2`), The Voice (`TheVoice.bg@SD`), Mysteries Xplored (`USBB5200028MM`), Ultimate TV (`UltimateTV.in@SD`), WeatherSpy (India) (`WeatherSpy.in@SD`), Wild Flix Hindi (`WildFlixHindi.in`), Witness to Justice (`WitnessToJustice.us`), ZB Cartoon (`ZBCartoon.in`), ZB Music (`ZBMusic.in@HD`), Dhoom Music Bangla (`custom.bdix.dhoom-music-bangla`), FilmRise Western (`custom.filmrise-western-us-movie`), Hooray Kids (`custom.hooraykids`), Pac 12 Insider (`custom.pac12insider`), Sonic The Hedgehog (`custom.sonicthehedgehog`), Willow Sports (`custom.willowsports`), XITE Celebrates (`custom.xite-celebrates-us-music`), XITE Just Chill (`custom.xitejustchill`)
- IDs with an in-window published programme but no current/future source match at the later scan: **70**
- In-window published IDs not counted source-current/future: Al Jazeera (`AlJazeera.qa`), Al Istiqama (`AlistiqamaTV.om`), Bollywood (`Bollywood.ru@HD`), CGTN Documentary (`CGTNDocumentary.cn`), CMC TV (`CMCTV.hr`), Cine 666 by Pluto TV (`Cine666byPlutoTV.de@FR`), Cine Action by Pluto TV (`CineActionbyPlutoTV.de@FR`), Cine Catastrophe by Pluto TV (`CineCatastrophebyPlutoTV.de@FR`), Cine Horreur by Pluto TV (`CineHorreurbyPlutoTV.de@FR`), Cine Retro by Pluto TV (`CineRetrobyPlutoTV.de@FR`), Cine Romance by Pluto TV (`CineRomancebyPlutoTV.de@FR`), Cine Sci-Fi by Pluto TV (`CineSciFibyPlutoTV.de@FR`), Cine Terror BR (`CineTerror.us@BR`), Cine Thrillers by Pluto TV (`CineThrillersbyPlutoTV.de@FR`), Cine Western by Pluto TV (`CineWesternbyPlutoTV.de@FR`), Cine by Pluto TV (`CinebyPlutoTV.de@FR`), Cine d'Asie by Pluto TV (`CinedAsiebyPlutoTV.de@FR`), Discovery Kids (`DiscoveryKids.au`), Disney Jr (`DisneyJr.us`), Dua Channel (`DuaChannel.sa`), FILMBOX+ Comedy (`FILMBOXPlusComedy.pl@Poland`), FILMBOX+ Emotion (`FILMBOXPlusEmotion.pl@Poland`), FILMBOX+ Festival (`FILMBOXPlusFestival.pl@SD`), FILMBOX+ Hits (`FILMBOXPlusHits.pl@Poland`), Falastini TV (`FalastiniTV.ps@SD`), Film Cafe (`FilmCafe.hu@Hungary`), GTC Punjabi UK (`GTCPunjabi.in@UK`), Gold Star (`GoldStar.ir@SD`), HUM Masala (`HUMMasala.pk`), Kino TV (`KinoTV.ru@HD`), Klape i Tambure TV (`KlapeiTambureTV.hr@SD`), Life+Style (`LifeStyle.us`), M-1 (`M1.lt@SD`), MN+ (`MNPlus.mn@SD`), Mazzika (`Mazzika.eg@SD`), MovieSphere CA (`MovieSphere.us@CA`), Now 70s (`NOW70s.us`), Now 80s (`NOW80s.us`), Nature Time (`NatureTime.us`), One TV (`OneTV.lb@SD`), Pluto TV 90's Classics (`PlutoTV90sClassics.de@FR`), Pluto TV Action (Sweden) DK (`PlutoTVAction.se@DK`), Pluto TV Action (Sweden) NO (`PlutoTVAction.se@NO`), Pluto TV Action Movies (`PlutoTVActionMovies.us@CA`), Pluto TV Alberto Sordi (`PlutoTVAlbertoSordi.de@IT`), Pluto TV Bang Bang (`PlutoTVBangBang.us@BR`), Pluto TV Bud & Terence (Sweden) DK (`PlutoTVBudTerence.se@DK`), Pluto TV Bud & Terence (Sweden) NO (`PlutoTVBudTerence.se@NO`), Pluto TV Catastrofes (`PlutoTVCatastrofes.de@ES`), Pluto TV Christmas tutto l'anno (`PlutoTVChristmastuttolanno.de@IT`), Pluto TV Cine Classicos (`PlutoTVCineClassicos.us@BR`), Pluto TV Cine Comedia (Germany) (`PlutoTVCineComedia.de@ES`), Pluto TV Cine Comedia (United States) BR (`PlutoTVCineComedia.us@BR`), Pluto TV Cine Comedia Romantica (`PlutoTVCineComediaRomantica.us@BR`), Pluto TV Cine Crime (`PlutoTVCineCrime.us@BR`), Pluto TV Cine Romance (`PlutoTVCineRomance.us@BR`), Pluto TV Cine de autor (`PlutoTVCinedeautor.de@ES`), Red Bull TV (`RedBullTV.at@EUMENA`), Sports First TV (`SportsFirstTV.us`), Star Cinema (`StarCinema.ru@SD`), Stingray iConcerts (`StingrayiConcerts.ca@HD`), Trace Latina (`TraceLatina.us`), Vantage Rock (`VantageRock.ee@HD`), WildEarth (`WildEarth.za`), ZICO TV (`ZICOTV.rs@SD`), Zoo Moo (`ZooMoo.sg`), Horse & Country (`custom.horseandcountry`), MAX TV (`custom.max-tv-az-music`), iFilm Arabic (`iFilmArabic.ir@SD`), MTV Classic (`mtv.classic.gb`)
- Source-current/future IDs whose published programme is no longer current by report time: **118**
- Source-current/future IDs no longer current in the published guide: Amar Bangla (`AamarBangla.in`), Aaryaa TV (`AaryaaTV.in`), Aaryaa TV (`AaryaaTV.in@SD`), All Time Movies (`AllTimeMovies.in@SD`), Alright! TV (`AlrightTV.in@SD`), Amar Bangla Digital (`AmarBanglaDigital.in`), &pictures (`AndPictures.in@SD`), B4U Kadak (`B4UKadak.in@SD`), B4U Movies (`B4UMovies.in@India`), BRIDGE (`BRIDGE.ru@SD`), BRIDGE Deluxe (`BRIDGEDeluxe.ru@SD`), Baby Shark TV (`BabySharkTV.us`), Bollygold (`Bollygold.in@HD`), Cine+ (`CinePlus.ua@SD`), Cine+ Hit (`CinePlusHit.ua@SD`), Cine Romantico (`CineRomantico.us@SD`), Cine Western (Spain) (`CineWestern.es@SD`), Classic Movie Westerns (`ClassicMovieWesterns.us@SD`), Dhool TV (`DhoolTV.in@SD`), Discovery Channel (India) (`DiscoveryChannel.in@HD`), DocuBay TV (`DocuBayTV.in`), ETV Beats (`ETVBeats.in@HD`), ETV Comedy (`ETVComedy.in`), ETV Comedy (`ETVComedy.in@HD`), ETV Josh (`ETVJosh.in`), ETV Josh (`ETVJosh.in@HD`), Ekamra Bharat Odia (`EkamraBharatOdia.in@SD`), Eman Channel (`EmanChannel`), Epic Bhojpuri (`EpicBhojpuri.in@SD`), Epic Bhojpuri Digital (`EpicBhojpuriDigital.in`), Epic Crimes (`EpicCrimes.in`), Epic Crimes (`EpicCrimes.in@SD`), Fast1 (`Fast1.in@SD`), Goldmines Movies (`GoldminesMovies.in@SD`), Hallmark Movies & More (`HallmarkMoviesMore.us`), InWonder (`InWonder.nl`), KTV Bangla (`KTVBangla.in@SD`), Kappa TV (Music) (`KappaTV.in@ALT1`), Kino Nova (`KinoNova.bg@SD`), Kinowood (`Kinowood.ua@SD`), Kiss Kiss TV (`KissKissTV.it@SD`), Mr Bean Animated (`MrBeanAnimated.uk`), Music Box Sexy (`MusicBoxSexy.cz@SD`), Muzvar (`Muzvar.ua@SD`), Muzyka Pervogo (`MuzykaPervogo.ru@SD`), MyTime Movie Network East (`MyTimeMovieNetworkEast.us`), NH BollyFlix (`NHBollyFlix.in`), NH BollyRaga (`NHBollyRaga.in`), NH BollyRaga (`NHBollyRaga.in@HD`), NH Tamil Gold (`NHTamilGold.in`), NH Tamil Gold (`NHTamilGold.in@HD`), NTC TV (`NTCTV.in@SD`), Nashe Novoe Kino (`NasheNovoeKino.ru@SD`), Nick Bangla (`NickBangla.bd`), Only Music (`Only.Music.in`), OuterSphere (`OuterSphere.us`), OuterSphere (`OuterSphere.us@SD`), PGA Tour (`PGATour.us@SD`), Paramount Movie Channel (`ParamountMovieChannel.us@SD`), Pitaara Comedy (`PitaaraComedy.in@SD`), Public Movies (`PublicMovies.in@SD`), Qello Concerts by Stingray (`QelloConcertsbyStingray.ca@SD`), Qwest TV (`QwestTV.fr@SD`), R Plus Gold (`RPlusGold.in@SD`), RTL 102.5 Caliente (`RTL1025Caliente.it@SD`), Radio Norba TV (`RadionorbaTV.it`), RetroCrush (`RetroCrush.us`), Roja Movies (`RojaMovies.in@SD`), Roja TV (`RojaTV.in`), Russkiy Bestseller (`RusskiyBestseller.ru@SD`), Russkiy Detektiv (`RusskiyDetektiv.ru@SD`), Sonar Bangla (`SonarBangla.in@SD`), Sony Wah (`SonyWah.in@SD`), South Station (`SouthStation.in`), South Station (`SouthStation.in@HD`), Sport 1 Baltic (`Sport1Baltic.ua@SD`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray Easy Listening (`StingrayEasyListening.ca@SD`), Stingray Flashback 70's (`StingrayFlashback70s.ca@SD`), Stingray Greatest Holiday Hits (`StingrayGreatestHolidayHits.us@SD`), Stingray Hit List (`StingrayHitList.ca`), Stingray Hot Country (`StingrayHotCountry.ca@SD`), Stingray Jukebox Oldies (`StingrayJukeboxOldies.ca@SD`), Stingray Nothin' But 90s (`StingrayNothinBut90s.ca@SD`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray Smooth Jazz (`StingraySmoothJazz.ca@SD`), Stingray Soul Storm (`StingraySoulStorm.ca@SD`), Stingray The Spa (`StingrayTheSpa.ca`), Stingray The Spa (`StingrayTheSpa.ca@SD`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Stingray Today's K-Pop (`StingrayTodaysKPop.ca@SD`), Strawberry Shortcake (`StrawberryShortcake.us`), Studio Yuva (`StudioYuva.in`), Studio Yuva (`StudioYuva.in@SD`), Suriya TV (`SuriyaTV.in`), Suriya TV (`SuriyaTV.in@SD`), Survivor (`Survivor.us`), Teletubbies (`Teletubbies.uk`), Telugu One (`TeluguOne.in@HD`), The Movie Club (`TheMovieClub.in@HD`), The Movie Club +2 (`TheMovieClub.in@Plus2`), The Voice (`TheVoice.bg@SD`), Mysteries Xplored (`USBB5200028MM`), Ultimate TV (`UltimateTV.in@SD`), Viasat Kino Comedy (`ViasatKinoComedy.ua@SD`), WeatherSpy (India) (`WeatherSpy.in@SD`), Wild Flix Hindi (`WildFlixHindi.in`), Witness to Justice (`WitnessToJustice.us`), ZB Cartoon (`ZBCartoon.in`), ZB Music (`ZBMusic.in@HD`), Dhoom Music Bangla (`custom.bdix.dhoom-music-bangla`), FilmRise Western (`custom.filmrise-western-us-movie`), Hooray Kids (`custom.hooraykids`), Pac 12 Insider (`custom.pac12insider`), Sonic The Hedgehog (`custom.sonicthehedgehog`), Willow Sports (`custom.willowsports`), XITE Celebrates (`custom.xite-celebrates-us-music`), XITE Just Chill (`custom.xitejustchill`)
- Published current/future IDs not counted source-current/future: **68**
- Published current/future IDs not counted source-current/future: Al Jazeera (`AlJazeera.qa`), Al Istiqama (`AlistiqamaTV.om`), Bollywood (`Bollywood.ru@HD`), CGTN Documentary (`CGTNDocumentary.cn`), CMC TV (`CMCTV.hr`), Cine Action by Pluto TV (`CineActionbyPlutoTV.de@FR`), Cine Catastrophe by Pluto TV (`CineCatastrophebyPlutoTV.de@FR`), Cine Retro by Pluto TV (`CineRetrobyPlutoTV.de@FR`), Cine Romance by Pluto TV (`CineRomancebyPlutoTV.de@FR`), Cine Sci-Fi by Pluto TV (`CineSciFibyPlutoTV.de@FR`), Cine Terror BR (`CineTerror.us@BR`), Cine Thrillers by Pluto TV (`CineThrillersbyPlutoTV.de@FR`), Cine Western by Pluto TV (`CineWesternbyPlutoTV.de@FR`), Cine by Pluto TV (`CinebyPlutoTV.de@FR`), Cine d'Asie by Pluto TV (`CinedAsiebyPlutoTV.de@FR`), Discovery Kids (`DiscoveryKids.au`), Disney Jr (`DisneyJr.us`), Dua Channel (`DuaChannel.sa`), FILMBOX+ Comedy (`FILMBOXPlusComedy.pl@Poland`), FILMBOX+ Emotion (`FILMBOXPlusEmotion.pl@Poland`), FILMBOX+ Festival (`FILMBOXPlusFestival.pl@SD`), FILMBOX+ Hits (`FILMBOXPlusHits.pl@Poland`), Falastini TV (`FalastiniTV.ps@SD`), Film Cafe (`FilmCafe.hu@Hungary`), GTC Punjabi UK (`GTCPunjabi.in@UK`), Gold Star (`GoldStar.ir@SD`), HUM Masala (`HUMMasala.pk`), Kino TV (`KinoTV.ru@HD`), Klape i Tambure TV (`KlapeiTambureTV.hr@SD`), Life+Style (`LifeStyle.us`), M-1 (`M1.lt@SD`), MN+ (`MNPlus.mn@SD`), Mazzika (`Mazzika.eg@SD`), MovieSphere CA (`MovieSphere.us@CA`), Now 70s (`NOW70s.us`), Now 80s (`NOW80s.us`), Nature Time (`NatureTime.us`), One TV (`OneTV.lb@SD`), Pluto TV 90's Classics (`PlutoTV90sClassics.de@FR`), Pluto TV Action (Sweden) DK (`PlutoTVAction.se@DK`), Pluto TV Action (Sweden) NO (`PlutoTVAction.se@NO`), Pluto TV Action Movies (`PlutoTVActionMovies.us@CA`), Pluto TV Alberto Sordi (`PlutoTVAlbertoSordi.de@IT`), Pluto TV Bang Bang (`PlutoTVBangBang.us@BR`), Pluto TV Bud & Terence (Sweden) DK (`PlutoTVBudTerence.se@DK`), Pluto TV Bud & Terence (Sweden) NO (`PlutoTVBudTerence.se@NO`), Pluto TV Catastrofes (`PlutoTVCatastrofes.de@ES`), Pluto TV Christmas tutto l'anno (`PlutoTVChristmastuttolanno.de@IT`), Pluto TV Cine Classicos (`PlutoTVCineClassicos.us@BR`), Pluto TV Cine Comedia (Germany) (`PlutoTVCineComedia.de@ES`), Pluto TV Cine Comedia (United States) BR (`PlutoTVCineComedia.us@BR`), Pluto TV Cine Comedia Romantica (`PlutoTVCineComediaRomantica.us@BR`), Pluto TV Cine Crime (`PlutoTVCineCrime.us@BR`), Pluto TV Cine Romance (`PlutoTVCineRomance.us@BR`), Pluto TV Cine de autor (`PlutoTVCinedeautor.de@ES`), Red Bull TV (`RedBullTV.at@EUMENA`), Sports First TV (`SportsFirstTV.us`), Star Cinema (`StarCinema.ru@SD`), Stingray iConcerts (`StingrayiConcerts.ca@HD`), Trace Latina (`TraceLatina.us`), Vantage Rock (`VantageRock.ee@HD`), WildEarth (`WildEarth.za`), ZICO TV (`ZICOTV.rs@SD`), Zoo Moo (`ZooMoo.sg`), Horse & Country (`custom.horseandcountry`), MAX TV (`custom.max-tv-az-music`), iFilm Arabic (`iFilmArabic.ir@SD`), MTV Classic (`mtv.classic.gb`)


## Playlist EPG Headers

| Playlist | Header status |
|---|---|
| IPTV-Playlist.m3u | OK |
| International-Playlist.m3u | OK |

## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **8675200ab8b37acc114ba0d5fc456d80611f2715c3226f08837681133391c6b5**
- International-Playlist.m3u SHA-256: **e82b876b16ceeb0ef3eaaf434c50d2d793b985a7e5fe1205230f2c14c620d6ff**

