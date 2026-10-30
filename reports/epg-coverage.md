# EPG Coverage & Mapping Report

Generated: **2026-10-30T03:16:36+00:00**

This report audits active unique channel identities across the three maintained playlists configured in the automated EPG pipeline. A source mapping is not counted as usable current/future coverage unless it has a valid programme interval and valid non-empty multilingual title data within the generator's -6-hour/+7-day window; English titles rank first, then Bengali, then other valid languages.
The XMLTV guide is published at **epg/epg.xml**. The published guide uses the playlist's tvg-id as the XMLTV channel ID, not the upstream provider's source ID.

## Overall Coverage

- Active unique playlist channel IDs audited: **2893**
- IDs with an EPG source mapping: **1030/2893 (35.6%)**
- IDs with usable current/future source schedules (nonblank multilingual titles (English preferred, then Bengali, then other valid languages)): **847/2893 (29.3%)**
- IDs with no EPG source mapping: **1863**

## Coverage by Playlist Group

| Group | Active IDs | Mapped IDs | Current/future | No mapping |
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
| Indian Movies | 92 | 69 | 64 | 23 |
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

## Source Status

- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz — 946 channel IDs; 702 IDs with usable current/future programmes; 72496 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-in.xml.gz — 419 channel IDs; 266 IDs with usable current/future programmes; 47001 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-bg.xml.gz — 116 channel IDs; 96 IDs with usable current/future programmes; 11268 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-br.xml.gz — 182 channel IDs; 138 IDs with usable current/future programmes; 21652 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-co.xml.gz — 180 channel IDs; 141 IDs with usable current/future programmes; 19870 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-de.xml.gz — 439 channel IDs; 379 IDs with usable current/future programmes; 40503 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-es.xml.gz — 300 channel IDs; 276 IDs with usable current/future programmes; 25695 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-hu.xml.gz — 152 channel IDs; 131 IDs with usable current/future programmes; 25392 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-it.xml.gz — 306 channel IDs; 264 IDs with usable current/future programmes; 28419 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-mx.xml.gz — 175 channel IDs; 134 IDs with usable current/future programmes; 12964 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-nl.xml.gz — 184 channel IDs; 154 IDs with usable current/future programmes; 33953 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-pl.xml.gz — 447 channel IDs; 402 IDs with usable current/future programmes; 74040 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-pt.xml.gz — 195 channel IDs; 146 IDs with usable current/future programmes; 25695 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ro.xml.gz — 282 channel IDs; 257 IDs with usable current/future programmes; 33983 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-ru.xml.gz — 223 channel IDs; 196 IDs with usable current/future programmes; 34056 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-se.xml.gz — 95 channel IDs; 80 IDs with usable current/future programmes; 13860 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-tr.xml.gz — 108 channel IDs; 81 IDs with usable current/future programmes; 15527 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-gb.xml.gz — 933 channel IDs; 877 IDs with usable current/future programmes; 79700 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/in.xml — 206 channel IDs; 201 IDs with usable current/future programmes; 2145 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/us.xml — 588 channel IDs; 587 IDs with usable current/future programmes; 4994 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml — 692 channel IDs; 606 IDs with usable current/future programmes; 40692 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz — 717 channel IDs; 680 IDs with usable current/future programmes; 21898 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml — 760 channel IDs; 760 IDs with usable current/future programmes; 80876 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml — 1491 channel IDs; 1316 IDs with usable current/future programmes; 39924 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml — 282 channel IDs; 42 IDs with usable current/future programmes; 2537 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml — 119 channel IDs; 105 IDs with usable current/future programmes; 20165 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/epg.xml.gz — 1717 channel IDs; 387 IDs with usable current/future programmes; 12173 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/jioepg.xml.gz — 1174 channel IDs; 228 IDs with usable current/future programmes; 7443 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/tsepg.xml.gz — 717 channel IDs; 706 IDs with usable current/future programmes; 43598 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.open-epg.com/files/unitedkingdom.xml.gz — 566 channel IDs; 541 IDs with usable current/future programmes; 19670 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-us.xml.gz — 12842 channel IDs; 12395 IDs with usable current/future programmes; 879011 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz — 345 channel IDs; 274 IDs with usable current/future programmes; 27529 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_FR1.xml.gz — 574 channel IDs; 532 IDs with usable current/future programmes; 42938 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_GR1.xml.gz — 321 channel IDs; 304 IDs with usable current/future programmes; 16513 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IT1.xml.gz — 195 channel IDs; 155 IDs with usable current/future programmes; 16195 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz — 163 channel IDs; 132 IDs with usable current/future programmes; 7422 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MX1.xml.gz — 178 channel IDs; 168 IDs with usable current/future programmes; 13625 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_NL1.xml.gz — 159 channel IDs; 156 IDs with usable current/future programmes; 17987 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_PL1.xml.gz — 636 channel IDs; 582 IDs with usable current/future programmes; 89639 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_RO1.xml.gz — 370 channel IDs; 354 IDs with usable current/future programmes; 35474 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_TR1.xml.gz — 178 channel IDs; 141 IDs with usable current/future programmes; 10187 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR1.xml.gz — 266 channel IDs; 231 IDs with usable current/future programmes; 21628 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://hum.tv/schedule/ — 1 channel IDs; 1 IDs with usable current/future programmes; 21 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — https://www.rtvbd.tv/schedule.php — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; Could not fetch the official RTV schedule over verified HTTPS (rtvbd.tv: URLError; www.rtvbd.tv: URLError)
- **OK** — https://migrate.btvlive.gov.bd/channel/BTV — 1 channel IDs; 1 IDs with usable current/future programmes; 30 eligible programme rows with valid non-empty titles in any language in the guide window
- **NO_PROGRAMMES** — M3U4U XMLTV (private Actions secret) — 201 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window

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
| Adult | Bang U | BangU.us | - | NO_GUIDE_HIT |
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
| Adult | Dick Drainers | custom.24-7-xxx-dick-drainers | - | NO_GUIDE_HIT |
| Adult | Dorcel Club | custom.xxx-dorcel-club | - | NO_GUIDE_HIT |
| Adult | Ebony | custom.24-7-xxx-ebony | - | NO_GUIDE_HIT |
| Adult | Elsa Jean | custom.24-7-xxx-elsa-jean | - | NO_GUIDE_HIT |
| Adult | Ember Snow | custom.24-7-xxx-ember-snow | - | NO_GUIDE_HIT |
| Adult | Erox XXX | custom.xxx-erox-xxx-hd | - | NO_GUIDE_HIT |
| Adult | Euro Girls On Girls | custom.xxx-euro-girls-on-girls | - | NO_GUIDE_HIT |
| Adult | Evil Angel | custom.24-7-xxx-evil-angel | - | NO_GUIDE_HIT |
| Adult | Evolved Fights | custom.xxx-evolved-fights | - | NO_GUIDE_HIT |
| Adult | Exxxotica TV | custom.exxxotica-tv | - | NO_GUIDE_HIT |
| Adult | Fake Taxi 1 | custom.24-7-xxx-fake-taxi-1 | - | NO_GUIDE_HIT |
| Adult | Fake Taxi 3 | custom.24-7-xxx-fake-taxi-3 | - | NO_GUIDE_HIT |
| Adult | Fap TV 6 | custom.fap-tv-6 | - | NO_GUIDE_HIT |
| Adult | Fetish | custom.xxx-fetish | - | NO_GUIDE_HIT |
| Adult | FM Therapy 1 | custom.24-7-xxx-fm-therapy-1 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 2 | custom.24-7-xxx-fm-therapy-2 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 3 | custom.24-7-xxx-fm-therapy-3 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 4 | custom.24-7-xxx-fm-therapy-4 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 5 | custom.24-7-xxx-fm-therapy-5 | - | NO_GUIDE_HIT |
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
| Adult | LEO TV | LEOTV.cz | - | NO_GUIDE_HIT |
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
| Adult | Music Box Sexy | MusicBoxSexy.cz@SD | - | NO_GUIDE_HIT |
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
| Adult | Nurse-Doctor | custom.24-7-xxx-nurse-doctor | - | NO_GUIDE_HIT |
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
| Adult | POV | custom.24-7-xxx-pov | - | NO_GUIDE_HIT |
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
| Adult | Stingray Pop Adult | StingrayPopAdult.ca@SD | - | NO_GUIDE_HIT |
| Adult | Strap on | custom.24-7-xxx-strap-on | - | NO_GUIDE_HIT |
| Adult | Super One | custom.xxx-super-one | - | NO_GUIDE_HIT |
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
| Argentina | Chamame TV | ChamameTV.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Cumbia Mix | CumbiaMix.ar@HD | - | NO_GUIDE_HIT |
| Argentina | Film & Arts | FilmArts.ar@Panregional | - | NO_GUIDE_HIT |
| Argentina | La 100 | La100.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Mas FM | MasFM.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Quiero Musica en mi Idioma | QuieroMusicaenmiIdioma.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Rock & Pop | RockPop.ar@SD | - | NO_GUIDE_HIT |
| Argentina | X Level Media | XLevelMedia.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Xtrema Accion | XtremaAccion.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Xtrema Cine Clasico | XtremaCineClasico.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Xtrema Terror | XtremaTerror.ar@SD | - | NO_GUIDE_HIT |
| Austria | Antenne Kaernten | AntenneKaernten.at@SD | - | NO_GUIDE_HIT |
| Austria | Antenne Steiermark | AntenneSteiermark.at@SD | - | NO_GUIDE_HIT |
| Austria | Antenne Vorarlberg [ ] | AntenneVorarlberg.at@SD | - | NO_GUIDE_HIT |
| Austria | Rakuten TV Action Movies Austria | RakutenTVActionMovies.es@Austria | - | NO_GUIDE_HIT |
| Austria | Rakuten TV Comedy Movies Austria | RakutenTVComedyMovies.es@Austria | - | NO_GUIDE_HIT |
| Austria | Rakuten TV Drama Movies Austria | RakutenTVDramaMovies.es@Austria | - | NO_GUIDE_HIT |
| Austria | Rakuten TV Family Movies Austria | RakutenTVFamilyMovies.es@Austria | - | NO_GUIDE_HIT |
| Bangladesh | ATN Bangla UK | ATNBanglaUK.uk | 6753 | MAPPED_NOT_CURRENTLY_FOUND |
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
| Bangladesh | BOISHAKHAI TV HD | custom.bdix.boishakhai | - | NO_GUIDE_HIT |
| Bangladesh | Boishakhi TV | BoishakhiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV Chattogram | BTVChattogram.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV CTG | custom.bdix.btvctg | - | NO_GUIDE_HIT |
| Bangladesh | BTV News | BTVNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV News | custom.btv.news | - | NO_GUIDE_HIT |
| Bangladesh | Channel 1 | Channel1.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 1 | custom.channel.1 | - | NO_GUIDE_HIT |
| Bangladesh | Channel 16 | Channel16.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 24 | 94000 | - | NO_GUIDE_HIT |
| Bangladesh | Channel 24 | Channel24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 52 | Channel52.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 9 | Channel9.bd | - | NO_GUIDE_HIT |
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
| Bangladesh | GAZI TV | GaziTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | GAZI TV HD | custom.bdix.gazi | - | NO_GUIDE_HIT |
| Bangladesh | Global TV | GlobalTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Green TV | GreenTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Green TV | GreenTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | Independent TV | 247000 | - | NO_GUIDE_HIT |
| Bangladesh | Independent TV | IndependentTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jago News 24 | JagoNews24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jalsha Bangla BD | JalshaBanglaBD.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jamuna TV | JamunaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jonmobhumi TV | JonmobhumiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Maasranga TV | MaasrangaTV.bd | - | NO_GUIDE_HIT |
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
| Bangladesh | NTV Europe | NTVEurope.bd | - | NO_GUIDE_HIT |
| Bangladesh | Rajdhani TV | RajdhaniTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Rajdhani TV | custom.rajdhani | - | NO_GUIDE_HIT |
| Bangladesh | Rupashi Bangla TV | RupashiBanglaTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | SA TV | SATV.bd | - | NO_GUIDE_HIT |
| Bangladesh | SATV HD | custom.bdix.satv | - | NO_GUIDE_HIT |
| Bangladesh | Somoy TV | SomoyNewsTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | SRK | SRK.bd | - | NO_GUIDE_HIT |
| Bangladesh | Star News | StarNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Star News | custom.star.news | - | NO_GUIDE_HIT |
| Bangladesh | TBN24 | TBN24.us | - | NO_GUIDE_HIT |
| Bangladesh | Thikana | ThikanaTV.us | - | NO_GUIDE_HIT |
| Bangladesh | Time Television | TimeTelevision.us | - | NO_GUIDE_HIT |
| Brazil | +MaisUm | PlusMaisUm.br@HD | - | NO_GUIDE_HIT |
| Brazil | Adrenalina Pura TV Brazil | AdrenalinaPuraTV.us@Brazil | - | NO_GUIDE_HIT |
| Brazil | AMC Latin America Brazil | AMCLatinAmerica.us@Brazil | - | NO_GUIDE_HIT |
| Brazil | CINDIE TV | CINDIETV.br@HD | - | NO_GUIDE_HIT |
| Brazil | Classique TV | ClassiqueTV.br@SD | - | NO_GUIDE_HIT |
| Brazil | Ghost TV [ ] | GhostTV.br@SD | - | NO_GUIDE_HIT |
| Brazil | KpopTV Play | KpopTVPlay.br@SD | - | NO_GUIDE_HIT |
| Brazil | Lamore Rock Show WebTV | LamoreRockShowWebTV.br@SD | - | NO_GUIDE_HIT |
| Brazil | MyTime Movie Network (Brazil) | MyTimeMovieNetwork.br@SD | - | NO_GUIDE_HIT |
| Bulgaria | Movie Star | MovieStar.bg@SD | MovieSTAR.bg | MAPPED_NOT_CURRENTLY_FOUND |
| Bulgaria | bTV Lady | bTVLady.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | cine.box | cinebox.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | CineStar 1 Bulgaria | CineStar1Bulgaria.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | City TV (Bulgaria) | CityTV.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | DSTV (Bulgaria) | DSTV.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | FILMBOX+ Emotion Bulgaria | FILMBOXPlusEmotion.pl@Bulgaria | - | NO_GUIDE_HIT |
| Bulgaria | FILMBOX+ Love & Crime Bulgaria | FILMBOXPlusLoveCrime.pl@Bulgaria | - | NO_GUIDE_HIT |
| Bulgaria | FILMBOX+ One Bulgaria | FILMBOXPlusOne.pl@Bulgaria | - | NO_GUIDE_HIT |
| Bulgaria | Tiankov Folk | TiankovFolk.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | Tiankov Orient Folk | TiankovOrientFolk.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | TV1000 | TV1000.bg@SD | - | NO_GUIDE_HIT |
| Bulgaria | Viasat Kino Bulgaria | ViasatKino.ua@Bulgaria | - | NO_GUIDE_HIT |
| Canada | HBO East | HBO1.ca | HBO1.ca | MAPPED_NOT_CURRENTLY_FOUND |
| Canada | Stingray Hit List | StingrayHitList.ca | StingrayHitList.ca | MAPPED_NOT_CURRENTLY_FOUND |
| Canada | Stingray Karaoke | StingrayKaraoke.ca@SD | plex.tv.Stingray.Karaoke.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Canada | Stingray Soul Storm | StingraySoulStorm.ca@SD | plex.tv.Stingray.Soul.Storm.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Canada | Afghan Nobel Movies | AfghanNobelMovies.ca@SD | - | NO_GUIDE_HIT |
| Canada | CKNO-FM | CKNOFM.ca@SD | - | NO_GUIDE_HIT |
| Canada | Pamir TV | PamirTV.ca@SD | - | NO_GUIDE_HIT |
| Canada | Stingray Everything '80s | StingrayEverything80s.ca@SD | - | NO_GUIDE_HIT |
| Canada | Stingray Holiday Hits | StingrayHolidayHits.ca@SD | - | NO_GUIDE_HIT |
| Chile | Rewind TV | RewindTV.cl@SD | Rewind.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Chile | 13 Festival | 13Festival.cl@SD | - | NO_GUIDE_HIT |
| Chile | Chocolate FM | ChocolateFM.cl@SD | - | NO_GUIDE_HIT |
| Chile | Dance FM | DanceFM.cl@SD | - | NO_GUIDE_HIT |
| Chile | Genial TV | GenialTV.cl@SD | - | NO_GUIDE_HIT |
| Chile | La Clave | LaClave.cl@SD | - | NO_GUIDE_HIT |
| Chile | Orbita Chile TV | OrbitaChileTV.cl@HD | - | NO_GUIDE_HIT |
| Chile | Pauta | Pauta.cl@SD | - | NO_GUIDE_HIT |
| Chile | Retro Plus | RetroPlus.cl@SD | - | NO_GUIDE_HIT |
| Chile | Retro Plus 2 | RetroPlus2.cl@SD | - | NO_GUIDE_HIT |
| Chile | Retro Plus 3 | RetroPlus3.cl@SD | - | NO_GUIDE_HIT |
| Chile | Retromusica Television | RetromusicaTelevision.cl@SD | - | NO_GUIDE_HIT |
| Chile | Ritoque TV | RitoqueTV.cl@SD | - | NO_GUIDE_HIT |
| Chile | Sabor TV | SaborTV.cl@SD | - | NO_GUIDE_HIT |
| Chile | Sensacion Costa | SensacionCosta.cl@SD | - | NO_GUIDE_HIT |
| Chile | Solo Bailalo | SoloBailalo.cl@SD | - | NO_GUIDE_HIT |
| Chile | TCM Latin America Chile | TCMLatinAmerica.us@Chile | - | NO_GUIDE_HIT |
| Chile | V Classic TV | VClassicTV.cl@SD | - | NO_GUIDE_HIT |
| China | CCTV-11 | CCTV11.cn@SD | - | NO_GUIDE_HIT |
| China | CCTV-15 | CCTV15.cn@SD | - | NO_GUIDE_HIT |
| China | CCTV-6 | CCTV6.cn@HD | - | NO_GUIDE_HIT |
| China | CCTV-Storm Music | CCTVStormMusic.cn@HD | - | NO_GUIDE_HIT |
| China | CCTV-Storm Theater | CCTVStormTheater.cn@HD | - | NO_GUIDE_HIT |
| China | CCTV-The First Theater | CCTVTheFirstTheater.cn@HD | - | NO_GUIDE_HIT |
| China | CHC Action | CHCAction.cn@SD | - | NO_GUIDE_HIT |
| China | CND Film Middle School Channel | CNDFilmMiddleSchoolChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Harbin Movie Channel | HarbinMovieChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Jiangsu Movie Channel | JiangsuMovieChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Jiangxi Movie Channel | JiangxiMovieChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Jilin Movie Channel | JilinMovieChannel.cn@SD | - | NO_GUIDE_HIT |
| Colombia | Claro Musica TV | ClaroMusicaTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | Fiesta TV | FiestaTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | MasMusica FM | MasMusicaFM.co@SD | - | NO_GUIDE_HIT |
| Colombia | Parranda Vallenata | ParrandaVallenata.co@SD | - | NO_GUIDE_HIT |
| Colombia | Radiola TV | RadiolaTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | Ranchenato TV | RanchenatoTV.co@SD | - | NO_GUIDE_HIT |
| Colombia | Reyali | Reyali.co@SD | - | NO_GUIDE_HIT |
| Colombia | Salsa Gorda Television | SalsaGordaTelevision.co@SD | - | NO_GUIDE_HIT |
| Colombia | Supermusica TV | SupermusicaTV.co@SD | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ Love & Crime | FILMBOXPlusLoveCrime.pl@Czechia | Filmbox+.love&crime.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Czech Republic | HBO (Czech Republic) | HBO.cz@SD | HBO.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Czech Republic | Music Box Classic | MusicBoxClassic.cz@SD | Music.Box.Classic.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Czech Republic | Music Box Dance | MusicBoxDance.cz@SD | Music.Box.Dance.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Czech Republic | Music Box Hits | MusicBoxHits.cz@SD | Music.Box.Hits.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Czech Republic | Retro Music TV | RetroMusicTV.cz@SD | Retro.Music.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Czech Republic | AMC Europe Czech Republic | AMCEurope.uk@CzechRepublic | - | NO_GUIDE_HIT |
| Czech Republic | AXN Black (United States) Czech Republic | AXNBlack.us@CzechRepublic | - | NO_GUIDE_HIT |
| Czech Republic | AXN CEE Czech Republic | AXNCEE.es@CzechRepublic | - | NO_GUIDE_HIT |
| Czech Republic | Canal+ Action Europe Czechia | CanalPlusActionEurope.nl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | Cinemax (Czech Republic) | Cinemax.cz@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | Film+ (Czech Republic) | FilmPlus.cz@SD | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ Comedy Czechia | FILMBOXPlusComedy.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ Emotion Czechia | FILMBOXPlusEmotion.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ Hits Czechia | FILMBOXPlusHits.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | FILMBOX+ One Czechia | FILMBOXPlusOne.pl@Czechia | - | NO_GUIDE_HIT |
| Czech Republic | Kino Barrandov | KinoBarrandov.cz@SD | - | NO_GUIDE_HIT |
| Czech Republic | Ocko | Ocko.cz@SD | - | NO_GUIDE_HIT |
| Czech Republic | Ocko Black | OckoBlack.cz@SD | - | NO_GUIDE_HIT |
| Czech Republic | Ocko Expres | OckoExpres.cz@SD | - | NO_GUIDE_HIT |
| Czech Republic | Ocko Gold | OckoGold.cz@SD | - | NO_GUIDE_HIT |
| Czech Republic | Ocko Star | OckoStar.cz@SD | - | NO_GUIDE_HIT |
| Czech Republic | Slager Muzika | SlagerMuzika.cz@SD | - | NO_GUIDE_HIT |
| Czech Republic | Slager Original | SlagerOriginal.cz@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Escape TV | EscapeTV.us | 6944 | MAPPED_ENDED |
| Documentary & Wildlife | 4K Travel | Travel.us | 4K.TRAVEL.TV.distro | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Animal Planet (Czech Republic) | AnimalPlanet.cz@SD | Animal.Planet.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Asharq Discovery | AsharqDiscovery.sa@SD | Asharq.Discovery.HD.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Asharq Documentary | AsharqDocumentary.sa@SD | Asharq.Documentary.HD.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | CCTV-9 | CCTV9.cn@SD | CCTV9.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | China Travel | ChinaTravel.cn@SD | China.Travel.distro | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Cooking Channel | custom.cooking.channel | Cooking.Channel.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Crime & Justice | CrimeJustice.us | plex.tv.Crime.&.Justice.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Discovering China | DiscoveringChina.cn@SD | Discovering.China.distro | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Discovery Channel (Czech Republic) | DiscoveryChannel.cz@SD | Discovery.Channel.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Discovery Family | custom.discoveryfamily | Discovery.Family.Channel.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Documentary+ International | DocumentaryPlus | plex.tv.Documentary+.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Dvojka | Dvojka.sk@SD | Dvojka.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Food Network (Czech Republic) | FoodNetwork.cz@SD | Food.Network.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Get.factual | Getfactual.us@UK | plex.tv.Get.Factual.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | HBO Signature | hbosignature.us | HBO.Signature.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | History Hit | HistoryHit.uk | HistoryHit.uk | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | History Hit | HistoryHit.uk@SD | HistoryHit.uk | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Knowledge Network | KnowledgeNetwork.ca | KnowledgeNetwork.ca | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Love The Planet | LoveThePlanet.es@EN | Love.The.Planet.es | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Love the Planet | LoveThePlanet.us | Love.The.Planet.es | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Military History | militaryhistory.us | Military.History.Channel.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | National Geographic (Czech Republic) | NationalGeographic.cz@SD | NATIONALGEOGRAPHIC.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | National Geographic Wild (Czech Republic) | NationalGeographicWild.cz@SD | National.Geographic.Wild.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Real Wild | RealWild.uk | RealWild.uk | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Robot Wars by Mech+ | RobotWarsByMech.us | plex.tv.Robot.Wars.by.Mech+.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | RT Documentary | RTDocumentary.ru | RTDocumentary.ru | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Smithsonian Channel | smithsonianchannel.us | Smithsonian.Channel.my | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Spektrum (Czech Republic) | Spektrum.cz@SD | Spektrum.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Total Crime | TotalCrime.ca@CA | Total.Crime.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Viasat Explore (Czech Republic) | ViasatExplore.cz@SD | Viasat.Explore.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Viasat History (Czech Republic) | ViasatHistory.cz@SD | Viasat.History.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Viasat Nature (Czech Republic) | ViasatNature.cz@SD | Viasat.Nature.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Wild TV | WildTV.ca@SD | Wild.TV.HD.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Documentary & Wildlife | Adventure Earth | AdventureEarth.de@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Adventure Earth | AdventureEarth.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Alone | Alone.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | AlternaTV | AlternaTV.ar@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Amazing Discoveries TV | AmazingDiscoveriesTV.in | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Animal Planet (Russia) | AnimalPlanet.ru@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Animal Planet (United States) | AnimalPlanet.us@East | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Animal Planet Latin America | AnimalPlanetLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Arsenal | Arsenal.ru@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Atlas | Atlas.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic Adventure Earth | AutenticAdventureEarth.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic History | AutenticHistory.de | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic History | AutenticHistory.de@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | BBC Earth Czechia | BBCEarth.uk@Czechia | - | NO_GUIDE_HIT |
| Documentary & Wildlife | BBC Earth Hungary | BBCEarth.uk@Hungary | - | NO_GUIDE_HIT |
| Documentary & Wildlife | BBC Earth US | BBCEarth.uk@US | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Better Life Nature Channel | BetterLifeNatureChannel.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | CCTV-Weapon & Technology | CCTVWeaponTechnology.cn@HD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | City Eden KinoDok | CityEdenKinoDok.ru@HD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | ClickTV Chile | ClickTVChile.cl@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | CNA Originals | CNAOriginals.sg@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Deadly Women | DeadlyWomen.us@UK | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Asia Taiwan | DiscoveryAsiaTaiwan.tw@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | DISCOVERY BANGLA | custom.bdix.discoverybangla | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Channel (United States) | DiscoveryChannel.us@East | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Channel Latin America | DiscoveryChannelLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Science Latin America | DiscoveryScienceLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Theater Latin America | DiscoveryTheaterLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Turbo (Italy) | DiscoveryTurbo.it@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Turbo Latin America | DiscoveryTurboLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Velocity | discoveryvelocity.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Documentary+ 2 | Documentary2.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Documentary+ International | DocumentaryPlus.us@International | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Ecovision | Ecovision.do@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | History (Brazil) | History.br@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | History (Czech Republic) | History.cz@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | History (United States) | History.us@East | - | NO_GUIDE_HIT |
| Documentary & Wildlife | History 2 Latin America | History2LatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Documentary & Wildlife | History 2 Latin America Brazil | History2LatinAmerica.us@Brazil | - | NO_GUIDE_HIT |
| Documentary & Wildlife | History Asia | HistoryAsia.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | History Latin America | HistoryLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Inside Crime | InsideCrime.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Into Crime | IntoCrime.fr@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Investigation Discovery (Czech Republic) | InvestigationDiscovery.cz@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Investigation Discovery (United States) | InvestigationDiscovery.us@East | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Investigation Discovery Latin America South | InvestigationDiscoveryLatinAmerica.us@South | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Italiana | Italiana.it@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Love Nature en Espanol | LoveNatureenEspanol.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | MRTV Farmer | MRTVFarmer.mm@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | MWD Documentary | MWDDocumentary.mm@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Mystery TV | MysteryTV.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Nano | Nano.ru@HD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | National Geographic (Croatia) | NationalGeographic.hr@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | National Geographic (United States) | NationalGeographic.us@East | - | NO_GUIDE_HIT |
| Documentary & Wildlife | National Geographic (United States) HD East | NationalGeographic.us@HDEast | - | NO_GUIDE_HIT |
| Documentary & Wildlife | National Geographic Wild (United States) HD East | NationalGeographicWild.us@HDEast | - | NO_GUIDE_HIT |
| Documentary & Wildlife | NatureTime AU | NatureTime.ca@AU | - | NO_GUIDE_HIT |
| Documentary & Wildlife | NatureTime France | NatureTime.ca@France | - | NO_GUIDE_HIT |
| Documentary & Wildlife | O'zbekiston Tarixi | OzbekistonTarixi.uz@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | PBS Arts | PBSArts.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Persiana Docs | PersianaDocs.fr@HD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Persiana Travel | PersianaTravel.fr@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | RT Documentary | RTDocumentary.ru@English | - | NO_GUIDE_HIT |
| Documentary & Wildlife | RT Documentary Russian | RTDocumentary.ru@Russian | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Smotrim 100% Fakty | Smotrim100Fakty.ru@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Terra Mater WILD | TerraMaterWILD.de@German | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Tochka.rf | Tochkarf.ru | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Travel Channel East | travel.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Travel XP Bangla | custom.bdix.travelxp-bangla | - | NO_GUIDE_HIT |
| Documentary & Wildlife | TVS Hollywood History | TVSHollywoodHistory.us@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | UMSA TVU Internacional | UMSATVUInternacional.bo@HD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Viasat Nature (Ukraine) | ViasatNature.ua@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | viju Explore | vijuExplore.ru@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | viju History | vijuHistory.ru@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | viju+ Planet | vijuPlusPlanet.ru@HD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Watch Mojo | WatchMojo.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | WaterBear | WaterBear.ch | - | NO_GUIDE_HIT |
| Documentary & Wildlife | WaterBear | WaterBear.ch@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Wedo Big Stories | WedoBigStories.ch@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Wild Planet | WildPlanet.us | - | NO_GUIDE_HIT |
| Estonia | Vantage Rock | VantageRock.ee@HD | Vantage.Rock.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Estonia | Best of Dance TV | BestofDanceTV.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV Algorhythm | DanceTVAlgorhythm.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV Deep House District | DanceTVDeepHouseDistrict.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV House Floor | DanceTVHouseFloor.ee@SD | - | NO_GUIDE_HIT |
| Estonia | DanceTV Techno Warehouse | DanceTVTechnoWarehouse.ee@SD | - | NO_GUIDE_HIT |
| Finland | Hero [ ] | Hero.fi@SD | - | NO_GUIDE_HIT |
| Finland | JRTV Jarviradio | JRTVJarviradio.fi@SD | - | NO_GUIDE_HIT |
| Finland | Navahang TV | NavahangTV.fi@SD | - | NO_GUIDE_HIT |
| Finland | Rakuten TV Action Movies Finland | RakutenTVActionMovies.es@Finland | - | NO_GUIDE_HIT |
| Finland | Rakuten TV Comedy Movies Finland | RakutenTVComedyMovies.es@Finland | - | NO_GUIDE_HIT |
| Finland | Rakuten TV Drama Movies Finland | RakutenTVDramaMovies.es@Finland | - | NO_GUIDE_HIT |
| Finland | Rakuten TV Family Movies Finland | RakutenTVFamilyMovies.es@Finland | - | NO_GUIDE_HIT |
| Finland | Rakuten TV Nordic Films | RakutenTVNordicFilms.es@Finland | - | NO_GUIDE_HIT |
| Finland | Rakuten TV Top Movies Finland | RakutenTVTopMovies.es@Finland | - | NO_GUIDE_HIT |
| France | TF1 Series Films | TF1SeriesFilms.fr@SD | TF1Series-Films.fr | MAPPED_NOT_CURRENTLY_FOUND |
| France | Trace Brazuca | TraceBrazuca.fr@HD | plex.tv.TRACE.Brazuca.plex | MAPPED_NOT_CURRENTLY_FOUND |
| France | 4 Music | 4Music.fr@SD | - | NO_GUIDE_HIT |
| France | 4Kurd | 4Kurd.fr@SD | - | NO_GUIDE_HIT |
| France | Cine Nanar | CineNanar.fr@SD | - | NO_GUIDE_HIT |
| France | Cine Western (France) | CineWestern.fr@SD | - | NO_GUIDE_HIT |
| France | Cine+ Classic | CinePlusClassic.fr@SD | - | NO_GUIDE_HIT |
| France | Cine+ Frisson | CinePlusFrisson.fr@SD | - | NO_GUIDE_HIT |
| France | DBM TV | DBMTV.fr@SD | - | NO_GUIDE_HIT |
| France | Emotion L | EmotionL.fr@SD | - | NO_GUIDE_HIT |
| France | Littoral FM TV | LittoralFMTV.fr@SD | - | NO_GUIDE_HIT |
| France | P2M TV | P2MTV.fr@SD | - | NO_GUIDE_HIT |
| France | Persiana Cinema | PersianaCinema.fr@SD | - | NO_GUIDE_HIT |
| France | Persiana Folk | PersianaFolk.fr@HD | - | NO_GUIDE_HIT |
| France | Persiana Latino | PersianaLatino.fr@SD | - | NO_GUIDE_HIT |
| France | Persiana Nostalgia | PersianaNostalgia.fr@SD | - | NO_GUIDE_HIT |
| France | Persiana Vibe | PersianaVibe.fr@HD | - | NO_GUIDE_HIT |
| France | Qwest TV Jazz & Beyond | QwestTVJazzBeyond.fr@SD | - | NO_GUIDE_HIT |
| France | ScreamIN | ScreamIN.fr@SD | - | NO_GUIDE_HIT |
| France | Sony One Favoris | SonyOneFavoris.fr@HD | - | NO_GUIDE_HIT |
| France | Sony One Hits Action | SonyOneHitsAction.fr@HD | - | NO_GUIDE_HIT |
| France | Sony One Hits Comedie | SonyOneHitsComedie.fr@HD | - | NO_GUIDE_HIT |
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
| France | Trace Urban International | TraceUrban.fr@InternationalHD | - | NO_GUIDE_HIT |
| France | Trace Urban Southern Africa | TraceUrban.fr@SouthernAfrica | - | NO_GUIDE_HIT |
| France | Trace Vanilla Islands | TraceVanillaIslands.fr@SD | - | NO_GUIDE_HIT |
| Germany | DMF | DMF.de@SD | DMF.ch | MAPPED_NOT_CURRENTLY_FOUND |
| Germany | Grjngo Western Movies | GrjngoWesternMovies.de@SD | plex.tv.Grjngo.-.Western.Movies.plex | MAPPED_NOT_CURRENTLY_FOUND |
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
| Germany | Finest TV | FinestTV.de@SD | - | NO_GUIDE_HIT |
| Germany | Medium (Germany) | Medium.de@ES | - | NO_GUIDE_HIT |
| Germany | More TV Sci-fi | MoreTVScifi.de@GB | - | NO_GUIDE_HIT |
| Germany | Moviedome | Moviedome.us@Germany | - | NO_GUIDE_HIT |
| Germany | Nash Kinomir | NashKinomir.de@SD | - | NO_GUIDE_HIT |
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
| Germany | Pluto TV Ferne Galaxien | PlutoTVFerneGalaxien.de@DACH | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film (Germany) | PlutoTVFilm.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film Ancora Piu Romantici | PlutoTVFilmAncoraPiuRomantici.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film Azione | PlutoTVFilmAzione.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film Commedia | PlutoTVFilmCommedia.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film Romantici | PlutoTVFilmRomantici.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film Storici | PlutoTVFilmStorici.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Film Thriller | PlutoTVFilmThriller.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Haialarm | PlutoTVHaialarm.de@DACH | - | NO_GUIDE_HIT |
| Germany | Pluto TV Invasion Alien | PlutoTVInvasionAlien.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Kult Comedies | PlutoTVKultComedies.de@DACH | - | NO_GUIDE_HIT |
| Germany | Pluto TV Kultfilme | PlutoTVKultfilme.de@DACH | - | NO_GUIDE_HIT |
| Germany | Pluto TV Legami Letali | PlutoTVLegamiLetali.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Movies | PlutoTVMovies.de@DACH | - | NO_GUIDE_HIT |
| Germany | Pluto TV Movies GB | PlutoTVMovies.de@GB | - | NO_GUIDE_HIT |
| Germany | Pluto TV Notti di Passione | PlutoTVNottidiPassione.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Notti di Sangue | PlutoTVNottidiSangue.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Notti di Terrore | PlutoTVNottidiTerrore.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Psycho | PlutoTVPsycho.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Serie Sci-Fi | PlutoTVSerieSciFi.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Star Trek (Germany) | PlutoTVStarTrek.de@DACH | - | NO_GUIDE_HIT |
| Germany | Pluto TV Toto | PlutoTVToto.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Weihnachten im Sommer | PlutoTVWeihnachtenimSommer.de@DACH | - | NO_GUIDE_HIT |
| Germany | Pluto TV Western ES | PlutoTVWestern.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Western IT | PlutoTVWestern.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Westerns (Germany) | PlutoTVWesterns.de@GB | - | NO_GUIDE_HIT |
| Germany | Pluto TV Zombies | PlutoTVZombies.de@ES | - | NO_GUIDE_HIT |
| Germany | Rakuten TV Action Movies Germany | RakutenTVActionMovies.es@Germany | - | NO_GUIDE_HIT |
| Germany | Rakuten TV Comedy Movies Germany | RakutenTVComedyMovies.es@Germany | - | NO_GUIDE_HIT |
| Germany | Rakuten TV Drama Movies Germany | RakutenTVDramaMovies.es@Germany | - | NO_GUIDE_HIT |
| Germany | Rakuten TV Family Movies Germany | RakutenTVFamilyMovies.es@Germany | - | NO_GUIDE_HIT |
| Germany | Rakuten TV Top Movies Germany | RakutenTVTopMovies.es@Germany | - | NO_GUIDE_HIT |
| Germany | SensaCine TV x Pluto | SensaCineTVxPluto.de@ES | - | NO_GUIDE_HIT |
| Germany | Star Trek: The Next Generation (Germany) | StarTrekTheNextGeneration.de@DACH | - | NO_GUIDE_HIT |
| Germany | Star Trek: The Original Series (Germany) | StarTrekTheOriginalSeries.de@DACH | - | NO_GUIDE_HIT |
| Germany | Star Trek: Voyager (Germany) | StarTrekVoyager.de@ES | - | NO_GUIDE_HIT |
| Germany | Star Trek: Voyager (Germany) IT | StarTrekVoyager.de@IT | - | NO_GUIDE_HIT |
| Germany | TV Bozsike Hamburg | TVBozsikeHamburgHD.de@HD | - | NO_GUIDE_HIT |
| Germany | XITE Hits Germany | XITEHits.nl@Germany | - | NO_GUIDE_HIT |
| Greece | Baraza TV | BarazaTV.gr@SD | - | NO_GUIDE_HIT |
| Greece | Baraza TV Deep House | BarazaTVDeepHouse.gr@SD | - | NO_GUIDE_HIT |
| Greece | Baraza TV Relaxing | BarazaTVRelaxing.gr@SD | - | NO_GUIDE_HIT |
| Greece | Ellinikos FM | EllinikosFM.gr@SD | - | NO_GUIDE_HIT |
| Greece | Messatida TV | MessatidaTV.gr@SD | - | NO_GUIDE_HIT |
| Greece | NRG 91 | NRG91.gr@SD | - | NO_GUIDE_HIT |
| Greece | Play TV (Greece) | PlayTV.gr@SD | - | NO_GUIDE_HIT |
| Hungary | Magyar Mozi TV | MagyarMoziTV.hu@SD | Magyar.Mozi.TV.hu | MAPPED_NOT_CURRENTLY_FOUND |
| Hungary | MAX4 | MAX4.hu@SD | Max4.hu | MAPPED_NOT_CURRENTLY_FOUND |
| Hungary | AMC Europe Hungary | AMCEurope.uk@Hungary | - | NO_GUIDE_HIT |
| Hungary | AXN Black (United States) Hungary | AXNBlack.us@Hungary | - | NO_GUIDE_HIT |
| Hungary | AXN CEE | AXNCEE.es@Hungary | - | NO_GUIDE_HIT |
| Hungary | Film+ (Hungary) | FilmPlus.hu@SD | - | NO_GUIDE_HIT |
| Hungary | FILMBOX+ Emotion Hungary | FILMBOXPlusEmotion.pl@Hungary | - | NO_GUIDE_HIT |
| Hungary | FILMBOX+ Hits Hungary | FILMBOXPlusHits.pl@Hungary | - | NO_GUIDE_HIT |
| Hungary | Oxygen Music | OxygenMusic.hu@HD | - | NO_GUIDE_HIT |
| Indian Bangla | BANGLA JAGO | custom.bdix.banglajago | Bangla.Jago.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Bangla | Bangla Jago TV | BanglaJagoTV.in | Bangla.Jago.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Bangla | ENTER 10 BANGLA | Enterr10 Bangla.in | Enterr10Bangla.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Bangla | Enter10 Bangla | Enter10Bangla.in | Enterr10Bangla.in | Enterr10Bangla.in@SD | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Bangla | Tara TV | TaraTV.in | Tara.TV.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Bangla | ZB Cinema | ZBCinema.in | jtv3322 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Bangla | Bangla Cinema | BanglaCinema.in | - | NO_GUIDE_HIT |
| Indian Bangla | Bangla Plus | BanglaPlus.in | - | NO_GUIDE_HIT |
| Indian Bangla | Jhankar TV | JhankarTV.ca | - | NO_GUIDE_HIT |
| Indian Bangla | JTV Bangla | JTVBangla.in@SD | - | NO_GUIDE_HIT |
| Indian Bangla | JTV Classic | JTVClassic.in | - | NO_GUIDE_HIT |
| Indian Bangla | Orange Bangla TV | OrangeBanglaTV.in@SD | - | NO_GUIDE_HIT |
| Indian Bangla | Sananda | SanandaTV.in | - | NO_GUIDE_HIT |
| Indian Bangla | Sananda TV | custom.sananda-tv | - | NO_GUIDE_HIT |
| Indian Bangla | SNB Cinema | SNBCinema.in | - | NO_GUIDE_HIT |
| Indian Bangla | Star Bangla | StarBangla.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Sarv Dharm Sangam | SarvDharmSangam.in@SD | 6926 | MAPPED_ENDED |
| Indian Entertainment | 4 SiDES TV | 4SiDESTV.in@SD | jtv3529 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Ekamra Bharat Odia | EkamraBharatOdia.in@SD | ts1196 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Ekamra Manoranjan | EkamraManoranjan.in | ts1207 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Friends TV | FriendsTV.in@SD | Friends.TV.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Global Punjab | GlobalPunjab.in | Global.Punjab.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Kalaignar Murasu | KalaignarMurasu.in | KalaignarMurasu.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Manoranjan Prime | ManoranjanPrime.in@SD | 154892 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Odisha TV | OdishaTV.in@SD | OdishaTV.in | OdishaTV.in@SD | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | One Paschima | OnePaschima.in@SD | One.Paschima.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Shemaroo Umang | ShemarooUmang.in@SD | Shemaroo.Umang.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Sony Entertainment TV | SonyEntertainmentTelevision.in@SD | Sony.Entertainment.Television.in | SonyEntertainmentTelevision.in@SD | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Sony KAL | SonyKALHindi.us | Sony.KAL.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Suriyan TV | SuriyanTV.in@SD | ts1384 | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Asianet Middle East | AsianetMiddleEast.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Baiscope TV | BaiscopeTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | BT TV | BTTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | CCV | CCV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors MENA | ColorsMENA.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors MENA | ColorsMENA.in@HD | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors Rishtey Americas | ColorsRishteyAmericas.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Flowers US | Flowers.us | - | NO_GUIDE_HIT |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Kalaignar Murasu | KalaignarMurasu.in@SD | - | NO_GUIDE_HIT |
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
| Indian Entertainment | Oli TV | OliTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Pankh | Pankh.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Pardesi TV | PardesiTV.ca | - | NO_GUIDE_HIT |
| Indian Entertainment | Pravasi Channel | PravasiChannel.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Pulari TV | PulariTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Punjabi TV | PunjabiTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Q TV | QTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | SADA TV | SADATV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | SADA TV | SADATV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Sooriyan TV | SooriyanTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Star Vijay UK | StarVijay.in@UK | - | NO_GUIDE_HIT |
| Indian Entertainment | Starnet | Starnet.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Swantham | Swantham.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Tamilan TV | TamilanTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Thendral TV | ThendralTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | UTV Palakkad | UTVPalakkad.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Goldmines Movies | GoldminesMovies.in@SD | ts1499 | MAPPED_ENDED |
| Indian Movies | Ekamra Cinema | EkamraCinema.in | Ekamra.Cinema.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Movies | MBC Bollywood | MBCBollywood.ae | MBC.Bollywood.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Movies | NH Tamil Gold | NHTamilGold.in | IN400061DB | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Movies | NH Tamil Gold | NHTamilGold.in@HD | IN400061DB | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Movies | &TV International | AndTV.in@International | - | NO_GUIDE_HIT |
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
| Indian Movies | MH One Movies | MHOneMovies.in | - | NO_GUIDE_HIT |
| Indian Movies | MH One Movies | MHOneMovies.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Movie Punjab | MoviePunjab.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Shemaroo Filmi Gaane | ShemarooFilmiGaane.in@HD | - | NO_GUIDE_HIT |
| Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | - | NO_GUIDE_HIT |
| Indian Movies | Soneri Cinema | SoneriCinema.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | South Movies | SouthMovies.in | - | NO_GUIDE_HIT |
| Indian Movies | Zee Cinema APAC | ZeeCinema.in@APAC | - | NO_GUIDE_HIT |
| Indian Music | Ekamra Musiq | EkamraMusiq.in | Ekamra.Musiq.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Music | Mastiii | Mastiii.in@SD | Mastiii.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Music | Steelbird Music | SteelbirdMusic.in@SD | Steelbird.Music.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Music | 7X Punjabi | 7XPunjabi.in | - | NO_GUIDE_HIT |
| Indian Music | Andy Haryana | AndyHaryana.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Deewana | DeewanaHD.in | - | NO_GUIDE_HIT |
| Indian Music | Deewana | DeewanaHD.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Hindi Hits | HindiHits.in | - | NO_GUIDE_HIT |
| Indian Music | Hindi Hits | HindiHits.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Kalika TV | KalikaTV.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Punjabi Beats | PunjabiBeatsHD.in@HD | - | NO_GUIDE_HIT |
| Indian Music | Punjabi Music | PunjabiMusicHD.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Rang Rangoli | RangRangoli.in | - | NO_GUIDE_HIT |
| Indian Music | Superhitz | Superhitz.in@SD | - | NO_GUIDE_HIT |
| Indian Music | YRF Music Nepal | YRFMusic.in@Nepal | - | NO_GUIDE_HIT |
| Indian Music | Zoom (India) Nepal | Zoom.in@Nepal | - | NO_GUIDE_HIT |
| International | LoL TV | LoLTV.in | 6609 | MAPPED_ENDED |
| International | Action Hollywood Movies | plex.tv.Action.Hollywood.Movies.plex | ActionHollywoodMovies.au | MAPPED_NOT_CURRENTLY_FOUND |
| International | AMC Thrillers | plex.tv.AMC.Thrillers.plex | plex.tv.AMC.Thrillers.plex | MAPPED_NOT_CURRENTLY_FOUND |
| International | BBC Drama | BBCDrama.uk | BBCDrama.au | MAPPED_NOT_CURRENTLY_FOUND |
| International | Fashion One | FashionOne.uk | Fashion.One.cz | MAPPED_NOT_CURRENTLY_FOUND |
| International | MBC 1 | MBC1.sa | MBC.1.ae | MAPPED_NOT_CURRENTLY_FOUND |
| International | MBC 4 | MBC4.sa | MBC.4.ae | MAPPED_NOT_CURRENTLY_FOUND |
| International | MBC+ Drama | MBCPlusDrama.sa@SD | MBC.Drama.ae | MAPPED_NOT_CURRENTLY_FOUND |
| International | Retro Music TV | RetroMusicTV.cz | Retro.Music.cz | MAPPED_NOT_CURRENTLY_FOUND |
| International | Saudi TV | SaudiTV.sa | Saudi.HD.ae | MAPPED_NOT_CURRENTLY_FOUND |
| International | Shanson TV | ShansonTV.ru | Shanson.TV.cz | MAPPED_NOT_CURRENTLY_FOUND |
| International | 1Mus | 1Mus.us | - | NO_GUIDE_HIT |
| International | Afrobeats | Afrobeats.us | - | NO_GUIDE_HIT |
| International | AMG TV Classic | AMGTVClassic.us | - | NO_GUIDE_HIT |
| International | Arabica TV | ArabicaTV.us | - | NO_GUIDE_HIT |
| International | AVA FAMILY | AVAFAMILY.us | - | NO_GUIDE_HIT |
| International | AVA SERIES | AVASERIES.us | - | NO_GUIDE_HIT |
| International | CANADA ONE | custom.bdix.canadaone | - | NO_GUIDE_HIT |
| International | Classic Movies | ClassicMovies.us | - | NO_GUIDE_HIT |
| International | Dance TV | DanceTV.us | - | NO_GUIDE_HIT |
| International | Digital Fashion | DigitalFashion.us | - | NO_GUIDE_HIT |
| International | DW News | DWNews.de | - | NO_GUIDE_HIT |
| International | FON Music | FONMusic.us | - | NO_GUIDE_HIT |
| International | iFilm English | iFilmEnglish.ir | - | NO_GUIDE_HIT |
| International | Kronehit | Kronehit.at | - | NO_GUIDE_HIT |
| International | M20 Music | M20Music.us | - | NO_GUIDE_HIT |
| International | MBC Drama USA | MBCDramaUSA.us | - | NO_GUIDE_HIT |
| International | Mei Ah Movie Channel | MeiAhMovieChannel.hk | - | NO_GUIDE_HIT |
| International | Movie Dome Family | MovieDomeFamily.us | - | NO_GUIDE_HIT |
| International | Movies Thriller | MoviesThriller.sa@SD | - | NO_GUIDE_HIT |
| International | My Cinema | MyCinema.us | - | NO_GUIDE_HIT |
| International | MyTime Movie | MyTimeMovieNetwork.uk@SD | - | NO_GUIDE_HIT |
| International | MyTime Movie Network East | MyTimeMovieNetworkEast.us | - | NO_GUIDE_HIT |
| International | Oxygen Music | OxygenMusic.us | - | NO_GUIDE_HIT |
| International | POP World TV | POPWorldTV.es | - | NO_GUIDE_HIT |
| International | PowerTürk TV | PowerTurkTV.tr | - | NO_GUIDE_HIT |
| International | Rakuten Movies | RakutenMovies | - | NO_GUIDE_HIT |
| International | Rakuten TV Action Movies UK | RakutenTVActionMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Comedy Movies UK | RakutenTVComedyMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Drama Movies UK | RakutenTVDramaMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Family Movies UK | RakutenTVFamilyMovies.es@UK | - | NO_GUIDE_HIT |
| International | Sony Movies | SonyMovies.in | - | NO_GUIDE_HIT |
| International | Sparkle Movies | GBAJ400042T1 | - | NO_GUIDE_HIT |
| International | Stingray Rock Alternative | StingrayRockAlternative.ca | - | NO_GUIDE_HIT |
| International | Totalmusic | Totalmusic.uk | - | NO_GUIDE_HIT |
| International | Trace UK | TraceUK.uk | - | NO_GUIDE_HIT |
| International | TV BRICS English | TVBRICSEnglish.in@SD | - | NO_GUIDE_HIT |
| International | Vevo '70s & '80s | Vevo70s80s.us | - | NO_GUIDE_HIT |
| International | Vevo '90s & '00s | Vevo90s00s.us | - | NO_GUIDE_HIT |
| International | Vevo Hip Hop & R&B | GBBD2300001C0 | - | NO_GUIDE_HIT |
| International | VTU | VTU.in@SD | - | NO_GUIDE_HIT |
| International | XITE Hits UK | XITEHits.nl@UK | - | NO_GUIDE_HIT |
| International | Young Hollywood | YoungHollywood.us | - | NO_GUIDE_HIT |
| Iran | iFilm Arabic | iFilmArabic.ir@SD | iFilm.Arabic.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Iran | AFN TV | AFNTV.ir@SD | - | NO_GUIDE_HIT |
| Iran | Afra Film | AfraFilm.ir@SD | - | NO_GUIDE_HIT |
| Iran | Bravo Farsi TV | BravoFarsiTV.ir@SD | - | NO_GUIDE_HIT |
| Iran | Cafe Film | CafeFilm.ir@SD | - | NO_GUIDE_HIT |
| Iran | HomePlus | HomePlus.ir@SD | - | NO_GUIDE_HIT |
| Iran | iFilm 2 | iFilm2.ir@SD | - | NO_GUIDE_HIT |
| Iran | iFilm English | iFilmEnglish.ir@SD | - | NO_GUIDE_HIT |
| Iran | iFilm Persian | iFilmPersian.ir@SD | - | NO_GUIDE_HIT |
| Iran | Meta Film TV | MetaFilmTV.ir@SD | - | NO_GUIDE_HIT |
| Iran | NewFlix | NewFlix.ir@SD | - | NO_GUIDE_HIT |
| Iran | SL 1 | SL1.ir@SD | - | NO_GUIDE_HIT |
| Iran | SL 2 | SL2.ir@SD | - | NO_GUIDE_HIT |
| Iran | Tamasha | Tamasha.ir@SD | - | NO_GUIDE_HIT |
| Italy | 7 RadioVisione | 7RadioVisione.it@HD | - | NO_GUIDE_HIT |
| Italy | 70-80 TV | 7080TV.it@SD | - | NO_GUIDE_HIT |
| Italy | Company TV | CompanyTV.it@SD | - | NO_GUIDE_HIT |
| Italy | Euro Indie Music Chart TV | EuroIndieMusicChartTV.it@SD | - | NO_GUIDE_HIT |
| Italy | FM ITALIA | FMITALIA.it@SD | - | NO_GUIDE_HIT |
| Italy | Kiss Kiss Napoli TV | KissKissNapoliTV.it@SD | - | NO_GUIDE_HIT |
| Italy | Kiss Kiss TV | KissKissTV.it@SD | - | NO_GUIDE_HIT |
| Italy | m2o TV | m2oTV.it@SD | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Action Movies Italy | RakutenTVActionMovies.es@Italy | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Comedy Movies Italy | RakutenTVComedyMovies.es@Italy | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Drama Movies Italy | RakutenTVDramaMovies.es@Italy | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Family Movies Italy | RakutenTVFamilyMovies.es@Italy | - | NO_GUIDE_HIT |
| Italy | Rakuten TV Top Movies Italy | RakutenTVTopMovies.es@Italy | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Best | RTL1025Best.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Bro&Sis | RTL1025BroSis.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Caliente | RTL1025Caliente.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Disco | RTL1025Disco.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Napule | RTL1025Napule.it@SD | - | NO_GUIDE_HIT |
| Italy | RTL 102.5 Traffic | RTL1025Traffic.it@SD | - | NO_GUIDE_HIT |
| Italy | Twentyseven HD [ ] | Twentyseven.it@HD | - | NO_GUIDE_HIT |
| Italy | V2BEAT | custom.v2beat | - | NO_GUIDE_HIT |
| Kids | Atfal & Mawaheb TV | AtfalMawahebTV.sa@SD | Atfal.&.Mawaheb.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | BabyFirst | BabyFirst.us@US | BabyFirst.TV.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Bravo! Kids TV | BravoKidsTV.hr@SD | Bravo!.Kids.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Camp Spoopy | CampSpoopy.us@SD | plex.tv.Camp.Spoopy.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Disney Channel (Bulgaria) | DisneyChannel.bg@SD | DisneyChannel.bg | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Disney Channel (Czech Republic) | DisneyChannel.cz@SD | Disney.Channel.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Disney Jr | DisneyJr.us | Disney.Jr.HD.uk | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Disney Junior (Czech Republic) | DisneyJunior.cz@SD | Disney.Junior.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | EKids | EKids.bg@SD | EKids.bg | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | KidsFlix | KidsFlix.us@SD | plex.tv.KidsFlix.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Kolyokklub | Kolyokklub.hu@SD | Kolyokklub.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Nick Jr. (Czech Republic) | NickJr.cz@SD | Nick.Jr..cz | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Nick Jr. (Russia) | NickJr.ru@SD | NickJr.ru | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Nickelodeon (Brazil) | Nickelodeon.br@SD | Nickelodeon.br | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Nickelodeon (Czech Republic) | Nickelodeon.cz@SD | Nickelodeon.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Nickelodeon (Russia) | Nickelodeon.ru@SD | Nickelodeon.ru | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Nicktoons (Czech Republic) | Nicktoons.cz@SD | Nicktoons.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Niki Junior | NikiJunior.ua@SD | Niki.Junior.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Pakapaka | Pakapaka.ar@SD | Pakapaka.ar | MAPPED_NOT_CURRENTLY_FOUND |
| Kids | Pixel TV | PixelTV.ua@SD | Pixel.ch | MAPPED_NOT_CURRENTLY_FOUND |
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
| Kids | Baby Time | BabyTime.ru@SD | - | NO_GUIDE_HIT |
| Kids | BabyFirst Spanish | BabyFirst.us@Spanish | - | NO_GUIDE_HIT |
| Kids | Balapan | Balapan.kz@HD | - | NO_GUIDE_HIT |
| Kids | Balapan International | BalapanInternational.kz@SD | - | NO_GUIDE_HIT |
| Kids | Bantul the Great | BantulTheGreat.us | - | NO_GUIDE_HIT |
| Kids | BeJoy.kids | BeJoykids.it@HD | - | NO_GUIDE_HIT |
| Kids | Bolajon | Bolajon.uz@SD | - | NO_GUIDE_HIT |
| Kids | Box Kids TV | BoxKidsTV.br@SD | - | NO_GUIDE_HIT |
| Kids | Carousel +4 | Carousel.ru@Plus4 | - | NO_GUIDE_HIT |
| Kids | Cartoon Network (Pakistan) | CartoonNetwork.pk@SD | - | NO_GUIDE_HIT |
| Kids | Cartoon Network Arabic | CartoonNetworkArabic.ae@SD | - | NO_GUIDE_HIT |
| Kids | Cartoon Network Asia | CartoonNetworkAsia.sg@SD | - | NO_GUIDE_HIT |
| Kids | Cartoon Network CEE Czech Republic | CartoonNetworkCEE.uk@CzechRepublic | - | NO_GUIDE_HIT |
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
| Kids | CCTV-14 | CCTV14.cn@HD | - | NO_GUIDE_HIT |
| Kids | Chikitoonz | Chikitoonz.pe@SD | - | NO_GUIDE_HIT |
| Kids | Chinola TV | ChinolaTV.do@SD | - | NO_GUIDE_HIT |
| Kids | Clan | Clan.es@SD | - | NO_GUIDE_HIT |
| Kids | CT Decko | CTDecko.cz@SD | - | NO_GUIDE_HIT |
| Kids | Detskiy | Detskiy.ru@SD | - | NO_GUIDE_HIT |
| Kids | Discovery Kids Latin America | DiscoveryKidsLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Kids | Discovery Kids Latin America Chile | DiscoveryKidsLatinAmerica.us@Chile | - | NO_GUIDE_HIT |
| Kids | Discovery Kids Latin America Colombia | DiscoveryKidsLatinAmerica.us@Colombia | - | NO_GUIDE_HIT |
| Kids | Discovery Kids Latin America Mexico | DiscoveryKidsLatinAmerica.us@Mexico | - | NO_GUIDE_HIT |
| Kids | Disney Channel Latin America Center | DisneyChannelLatinAmerica.ar@Center | - | NO_GUIDE_HIT |
| Kids | Disney Channel Latin America Mexico | DisneyChannelLatinAmerica.ar@Mexico | - | NO_GUIDE_HIT |
| Kids | Disney Channel Latin America North | DisneyChannelLatinAmerica.ar@North | - | NO_GUIDE_HIT |
| Kids | Disney Channel Latin America Panregional | DisneyChannelLatinAmerica.ar@PanregionalHD | - | NO_GUIDE_HIT |
| Kids | Disney Jr. Latin America | DisneyJrLatinAmerica.ar@North | - | NO_GUIDE_HIT |
| Kids | Disney Jr. Latin America North | DisneyJrLatinAmerica.ar@NorthHD | - | NO_GUIDE_HIT |
| Kids | Disney XD (United States) | DisneyXD.us@East | - | NO_GUIDE_HIT |
| Kids | Doraemon TV | DoraemonTV.us | - | NO_GUIDE_HIT |
| Kids | DumDum | DumDum.br@SD | - | NO_GUIDE_HIT |
| Kids | Duronto TV | DurontoTV.bd@SD | - | NO_GUIDE_HIT |
| Kids | EBS Kids | EBSKids.kr@SD | - | NO_GUIDE_HIT |
| Kids | El Chavo TV | ElChavoTV.mx@HD | - | NO_GUIDE_HIT |
| Kids | Epic Kids Digital | EpicKidsDigital.us | - | NO_GUIDE_HIT |
| Kids | ETV 2 | ETV2.ee@SD | - | NO_GUIDE_HIT |
| Kids | Extrema Kids TV | ExtremaKidsTV.cr@HD | - | NO_GUIDE_HIT |
| Kids | Gopal Bhar TV | custom.bdix.gopal-bhar-tv | - | NO_GUIDE_HIT |
| Kids | Groovia Kids | GrooviaKids.id@HD | - | NO_GUIDE_HIT |
| Kids | Iunior TV | IuniorTV.it@SD | - | NO_GUIDE_HIT |
| Kids | JapanimTV | JapanimTV.be@SD | - | NO_GUIDE_HIT |
| Kids | JimJam Europe | JimJamEurope.uk@SD | - | NO_GUIDE_HIT |
| Kids | Kapitan Fantastika | KapitanFantastika.ru@SD | - | NO_GUIDE_HIT |
| Kids | Kuriakos Kids | KuriakosKids.pt@SD | - | NO_GUIDE_HIT |
| Kids | Lale | Lale.ua@SD | - | NO_GUIDE_HIT |
| Kids | Lego Channel | LegoChannel.us@SD | - | NO_GUIDE_HIT |
| Kids | Lucas & Friends | LucasFriends.us@SD | - | NO_GUIDE_HIT |
| Kids | Mama | Mama.ru@SD | - | NO_GUIDE_HIT |
| Kids | Maxcine Kids | MaxcineKids.us@HD | - | NO_GUIDE_HIT |
| Kids | MBC 3 USA | MBC3USA.us@SD | - | NO_GUIDE_HIT |
| Kids | MiMi TV | MiMiTV.uz@SD | - | NO_GUIDE_HIT |
| Kids | Minika Cocuk | MinikaCocuk.tr@SD | - | NO_GUIDE_HIT |
| Kids | Minimax (Pakistan) | Minimax.pk@SD | - | NO_GUIDE_HIT |
| Kids | Minimax CEE | MinimaxCEE.cz@SD | - | NO_GUIDE_HIT |
| Kids | Moonbug Kids | MoonbugKids.uk | - | NO_GUIDE_HIT |
| Kids | Motu Patlu | custom.bdix.motu-patlu | - | NO_GUIDE_HIT |
| Kids | Mr Bean Animated ES | MrBeanAnimated.uk@ES | - | NO_GUIDE_HIT |
| Kids | Mr Bean Animated FR | MrBeanAnimated.uk@FR | - | NO_GUIDE_HIT |
| Kids | Nick Bangla | NickBangla.bd | - | NO_GUIDE_HIT |
| Kids | Nick Jr East | custom.nick-jr-east | - | NO_GUIDE_HIT |
| Kids | Nick Jr. (Croatia) | NickJr.hr@SD | - | NO_GUIDE_HIT |
| Kids | Nick Jr. (United States) | NickJr.us@East | - | NO_GUIDE_HIT |
| Kids | Nick Jr. Latin America | NickJrLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| Kids | Nickelodeon (Croatia) | Nickelodeon.hr@SD | - | NO_GUIDE_HIT |
| Kids | Nickelodeon (Germany) | Nickelodeon.de@SD | - | NO_GUIDE_HIT |
| Kids | Nickelodeon (United States) | Nickelodeon.us@East | - | NO_GUIDE_HIT |
| Kids | Nickelodeon CIS | NickelodeonCIS.kz@SD | - | NO_GUIDE_HIT |
| Kids | Nickelodeon Global | NickelodeonGlobal.uk@SD | - | NO_GUIDE_HIT |
| Kids | NickOnline | NickOnline.br@HD | - | NO_GUIDE_HIT |
| Kids | Nicktoons (United States) | Nicktoons.us@East | - | NO_GUIDE_HIT |
| Kids | Nicktoons CIS | NicktoonsCIS.ru@SD | - | NO_GUIDE_HIT |
| Kids | O! International | O.ru@International | - | NO_GUIDE_HIT |
| Kids | ON Kids | ONKids.vn@SD | - | NO_GUIDE_HIT |
| Kids | Peques TV | PequesTV.pe@SD | - | NO_GUIDE_HIT |
| Kids | Persiana Junior | PersianaJunior.fr@SD | - | NO_GUIDE_HIT |
| Kids | Plim Plim | PlimPlim.ar@SD | - | NO_GUIDE_HIT |
| Kids | PLUSPLUS | PLUSPLUS.ua@SD | - | NO_GUIDE_HIT |
| Kids | Pooya TV | PooyaTV.ir@SD | - | NO_GUIDE_HIT |
| Kids | Powerkids Kartoon Channel | PowerkidsKartoonChannel.us | - | NO_GUIDE_HIT |
| Kids | Reino Infantil | ReinoInfantil.mz@SD | - | NO_GUIDE_HIT |
| Kids | Retro Cartoon | RetroCartoon.br@SD | - | NO_GUIDE_HIT |
| Kids | Ryzhiy | Ryzhiy.ru@SD | - | NO_GUIDE_HIT |
| Kids | Skwad Play | SkwadPlay.us@SD | - | NO_GUIDE_HIT |
| Kids | Smotrim 100% Detskoe | Smotrim100Detskoe.ru@SD | - | NO_GUIDE_HIT |
| Kids | Smurf TV | SmurfTV.us | - | NO_GUIDE_HIT |
| Kids | Spacetoon Arabic | SpacetoonArabic.ae@SD | - | NO_GUIDE_HIT |
| Kids | Spacetoon Turkey | SpacetoonTurkey.tr@SD | - | NO_GUIDE_HIT |
| Kids | Starz Kids & Family | StarzKidsFamily.us@East | - | NO_GUIDE_HIT |
| Kids | Super Simple Songs | SuperSimpleSongs.us@SD | - | NO_GUIDE_HIT |
| Kids | Tamyr | Tamyr.ru@SD | - | NO_GUIDE_HIT |
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
| Kids | TVCARiB Kids & Teens | TVCARiBKidsTeens.sx@SD | - | NO_GUIDE_HIT |
| Kids | TVOKids | TVOKids.ca@SD | - | NO_GUIDE_HIT |
| Kids | TVS Hi Tops | TVSHiTops.us@SD | - | NO_GUIDE_HIT |
| Kids | V gostyakh u skazki | Vgostyakhuskazki.ru@SD | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Hindi | WOWKidz.in@Hindi | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Tamil | WOWKidzTamil.in | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Telugu | WOWKidz.in@Telugu | - | NO_GUIDE_HIT |
| Kids | Xtrema Cartoons | XtremaCartoons.ar@SD | - | NO_GUIDE_HIT |
| Kids | Yu-Gi-Oh! en espanol | YuGiOhenespanol.us@SD | - | NO_GUIDE_HIT |
| Kids | Zoom (Israel) | Zoom.il@SD | - | NO_GUIDE_HIT |
| Lebanon | Aghani Aghani TV | AghaniAghaniTV.lb@SD | - | NO_GUIDE_HIT |
| Lebanon | Arabica TV | custom.arabica-tv | - | NO_GUIDE_HIT |
| Lebanon | mfm | mfm.lb@HD | - | NO_GUIDE_HIT |
| Lebanon | MTV Lebanon | MTVLebanon.lb@SD | - | NO_GUIDE_HIT |
| Lebanon | OneFM | OneFM.lb@SD | - | NO_GUIDE_HIT |
| Mexico | CineLatino | CineLatino.mx@SD | CineLatino.mx | MAPPED_ENDED |
| Mexico | MultiPremier | MultiPremier.mx@SD | Multipremier.mx | MAPPED_NOT_CURRENTLY_FOUND |
| Mexico | AXN Latin America Mexico | AXNLatinAmerica.us@Mexico | - | NO_GUIDE_HIT |
| Mexico | Az Cinema | AzCinema.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Claro Cinema | ClaroCinema.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Conecta TV | ConectaTV.mx@SD | - | NO_GUIDE_HIT |
| Mexico | De Pelicula Latin America | DePeliculaLatinAmerica.mx@SD | - | NO_GUIDE_HIT |
| Mexico | De Pelicula Plus | DePeliculaPlus.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Exa TV | ExaTV.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Filmex [ ] | Filmex.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Filmex Clasico [ ] | FilmexClasico.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Lobo TV | LoboTV.mx@SD | - | NO_GUIDE_HIT |
| Mexico | MyTime Movie Network (Mexico) | MyTimeMovieNetwork.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Popcorn Central | PopcornCentral.mx@SD | - | NO_GUIDE_HIT |
| Mexico | Vision Television | VisionTelevision.mx@SD | - | NO_GUIDE_HIT |
| Netherlands | BEATTV | BEATTV.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | Canal+ Action Europe | CanalPlusActionEurope.nl@Netherlands | - | NO_GUIDE_HIT |
| Netherlands | Deep House District | DeepHouseDistrict.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | FomixTV | FomixTV.nl@HD | - | NO_GUIDE_HIT |
| Netherlands | Gigant FM | GigantFM.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | Qmusic | Qmusic.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | RadioNL TV | RadioNLTV.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | Salto Brasa Music | SaltoBrasaMusic.nl@SD | - | NO_GUIDE_HIT |
| Netherlands | TMF | TMF.nl@HDFAST | - | NO_GUIDE_HIT |
| New Backup | GTC Punjabi US | GTCPunjabi.in@US | - | NO_GUIDE_HIT |
| New Channels | Falastini TV | FalastiniTV.ps@SD | Falastini.TV.ae | MAPPED_NOT_CURRENTLY_FOUND |
| New Channels | Klape i Tambure TV | KlapeiTambureTV.hr@SD | Klape.i.Tambure.cz | MAPPED_NOT_CURRENTLY_FOUND |
| New Channels | Mazzika | Mazzika.eg@SD | Mazzika.ae | MAPPED_NOT_CURRENTLY_FOUND |
| New Channels | Rotana Cinema Egypt | RotanaCinemaEgypt.eg@SD | Rotana.Cinema.Egypt.ae | MAPPED_NOT_CURRENTLY_FOUND |
| New Channels | Tarima TV | TarimaTV.do@HD | plex.tv.Tarima.TV.plex | MAPPED_NOT_CURRENTLY_FOUND |
| New Channels | ZICO TV | ZICOTV.rs@SD | Zico.TV.ch | MAPPED_NOT_CURRENTLY_FOUND |
| New Channels | 2TV | 2TV.lt@SD | - | NO_GUIDE_HIT |
| New Channels | 312 Kino | 312Kino.kg@SD | - | NO_GUIDE_HIT |
| New Channels | 88 Stereo | 88Stereo.cr@SD | - | NO_GUIDE_HIT |
| New Channels | 98.1 Pearl FM | 981PearlFM.sx@SD | - | NO_GUIDE_HIT |
| New Channels | A2i Music | A2iMusic.sn@SD | - | NO_GUIDE_HIT |
| New Channels | ACW UG TV | ACWUGTV.ug@SD | - | NO_GUIDE_HIT |
| New Channels | AlbKanale Music TV | AlbKanaleMusicTV.al@HD | - | NO_GUIDE_HIT |
| New Channels | Alcance FM Play TV | AlcanceFMPLAYTV.py@SD | - | NO_GUIDE_HIT |
| New Channels | Alegria TV | AlegriaTV.bo@SD | - | NO_GUIDE_HIT |
| New Channels | Allo Cine | AlloCine.cm@SD | - | NO_GUIDE_HIT |
| New Channels | AMC (Afghanistan) | AMC.af@SD | - | NO_GUIDE_HIT |
| New Channels | AMN TV | AMNTV.in@SD | - | NO_GUIDE_HIT |
| New Channels | AMusic Channel | AMusicChannel.ng@SD | - | NO_GUIDE_HIT |
| New Channels | Armenia Premium | ArmeniaPremium.am@SD | - | NO_GUIDE_HIT |
| New Channels | Audiokiss | Audiokiss.bo@SD | - | NO_GUIDE_HIT |
| New Channels | Aurora Media Films | AuroraMediaFilms.gt@SD | - | NO_GUIDE_HIT |
| New Channels | AXN Asia Taiwan | AXNAsia.sg@Taiwan | - | NO_GUIDE_HIT |
| New Channels | BOKTV | BOKTV.za@SD | - | NO_GUIDE_HIT |
| New Channels | Boreal | Boreal.do@SD | - | NO_GUIDE_HIT |
| New Channels | BTA TV | BTATV.ve@SD | - | NO_GUIDE_HIT |
| New Channels | Canal 3 KMK TV | Canal3KMKTV.cr@SD | - | NO_GUIDE_HIT |
| New Channels | Canal+ Action Europe Slovakia | CanalPlusActionEurope.nl@Slovakia | - | NO_GUIDE_HIT |
| New Channels | Cinema (Mongolia) | Cinema.mn@SD | - | NO_GUIDE_HIT |
| New Channels | CinemaWorld | CinemaWorld.my@SD | - | NO_GUIDE_HIT |
| New Channels | Cinemax Asia | CinemaxAsia.sg@HD | - | NO_GUIDE_HIT |
| New Channels | Cool FM 98.9 | CoolFM989.aw@SD | - | NO_GUIDE_HIT |
| New Channels | Corazon TV | CorazonTV.pa@SD | - | NO_GUIDE_HIT |
| New Channels | CTB Perth Movies Channel | CTBPerthMoviesChannel.au@SD | - | NO_GUIDE_HIT |
| New Channels | E40 | E40.py@SD | - | NO_GUIDE_HIT |
| New Channels | EBC Foreign Movie | EBCForeignMovie.tw@SD | - | NO_GUIDE_HIT |
| New Channels | El Sol Network TV | ElSolNetworkTV.ec@SD | - | NO_GUIDE_HIT |
| New Channels | Fabulosa Estéreo 100.5 FM | FabulosaEstereo1005FM.pa@SD | - | NO_GUIDE_HIT |
| New Channels | First Music Channel | FirstMusicChannel.by@SD | - | NO_GUIDE_HIT |
| New Channels | FM Mundo | FMMundo.ec@SD | - | NO_GUIDE_HIT |
| New Channels | Folk Klub TV | FolkKlubTV.au@SD | - | NO_GUIDE_HIT |
| New Channels | Folk TV | FolkTV.mk@SD | - | NO_GUIDE_HIT |
| New Channels | Fuego TV | FuegoTV.do@SD | - | NO_GUIDE_HIT |
| New Channels | Fun Vision | FunVision.be@SD | - | NO_GUIDE_HIT |
| New Channels | Fusion TV | FUSIONTV.mq@SD | - | NO_GUIDE_HIT |
| New Channels | Gex TV | GexTV.cr@HD | - | NO_GUIDE_HIT |
| New Channels | Gugak TV | GugakTV.kr@SD | - | NO_GUIDE_HIT |
| New Channels | HBO Asia SD [ ] | HBOAsia.sg@SD | - | NO_GUIDE_HIT |
| New Channels | HBO Asia Taiwan | HBOAsia.sg@Taiwan | - | NO_GUIDE_HIT |
| New Channels | HEi Now | HEiNow.py@SD | - | NO_GUIDE_HIT |
| New Channels | Hit FM | HitFM.md@SD | - | NO_GUIDE_HIT |
| New Channels | HMTV (Nigeria) | HMTV.ng@SD | - | NO_GUIDE_HIT |
| New Channels | Identite Tele Caraibes | IdentiteTeleCaraibes.mq@SD | - | NO_GUIDE_HIT |
| New Channels | Imagen FM 105.1 | ImagenFM1051.hn@SD | - | NO_GUIDE_HIT |
| New Channels | Infinita TV | InfinitaTV.ec@SD | - | NO_GUIDE_HIT |
| New Channels | INTV Australia | INTVAustralia.au@SD | - | NO_GUIDE_HIT |
| New Channels | IQ Channel | IQChannel.cr@SD | - | NO_GUIDE_HIT |
| New Channels | Isango TV | IsangoTV.rw@SD | - | NO_GUIDE_HIT |
| New Channels | Itage TV | ItageTV.ng@SD | - | NO_GUIDE_HIT |
| New Channels | Ivoire Channel | IvoireChannel.ci@SD | - | NO_GUIDE_HIT |
| New Channels | Jordan Songs | JordanSongs.jo@SD | - | NO_GUIDE_HIT |
| New Channels | K100 | K100.is@SD | - | NO_GUIDE_HIT |
| New Channels | Kabaddi 24x7 | Kabaddi24x7.in@SD | - | NO_GUIDE_HIT |
| New Channels | KandelaTV | KandelaTV.ve@SD | - | NO_GUIDE_HIT |
| New Channels | Kantipur Max [ ] | KantipurMax.np@SD | - | NO_GUIDE_HIT |
| New Channels | Kayhan TV | KayhanTV.af@SD | - | NO_GUIDE_HIT |
| New Channels | Klara | Klara.be@SD | - | NO_GUIDE_HIT |
| New Channels | Klasik [ ] | Klasik.hr@SD | - | NO_GUIDE_HIT |
| New Channels | KN Music TV | KNMusicTV.az@SD | - | NO_GUIDE_HIT |
| New Channels | Komsan TV [ ] | KomsanTV.kh@SD | - | NO_GUIDE_HIT |
| New Channels | La Elegida Television | LaElegidaTelevision.uy@SD | - | NO_GUIDE_HIT |
| New Channels | La Top 102.9 | LaTop1029.hn@SD | - | NO_GUIDE_HIT |
| New Channels | La Top 107.7 | LaTop1077.hn@SD | - | NO_GUIDE_HIT |
| New Channels | La-X | LaX.pr@SD | - | NO_GUIDE_HIT |
| New Channels | Live99FM | Live99FM.bq@SD | - | NO_GUIDE_HIT |
| New Channels | Look Thoong TV | LookThoongTV.la@SD | - | NO_GUIDE_HIT |
| New Channels | Love TV | LoveTV.mk@SD | - | NO_GUIDE_HIT |
| New Channels | LRT Klasika | LRTKlasika.lt@SD | - | NO_GUIDE_HIT |
| New Channels | LRT Opus | LRTOpus.lt@SD | - | NO_GUIDE_HIT |
| New Channels | Maah TV | MaahTV.my@SD | - | NO_GUIDE_HIT |
| New Channels | Madras FM TV | MadrasFMTV.gp@SD | - | NO_GUIDE_HIT |
| New Channels | Maimon TV Canal 3 | MaimonTVCanal3.do@SD | - | NO_GUIDE_HIT |
| New Channels | Makao TV | MakaoTV.do@SD | - | NO_GUIDE_HIT |
| New Channels | Mas23 TV | Mas23TV.pa@SD | - | NO_GUIDE_HIT |
| New Channels | Mega Cine TV | MegaCineTV.do@HD | - | NO_GUIDE_HIT |
| New Channels | MegaBox | MegaBox.ni@SD | - | NO_GUIDE_HIT |
| New Channels | Mei Ah Movie Channel | MeiAhMovieChannel.hk@SD | - | NO_GUIDE_HIT |
| New Channels | Metropoli Medios TV | MetropoliMediosTV.ec@SD | - | NO_GUIDE_HIT |
| New Channels | Mix Hollywood | MixHollywood.eg@SD | - | NO_GUIDE_HIT |
| New Channels | Montones TV | MontonesTV.do@HD | - | NO_GUIDE_HIT |
| New Channels | Mosaique FM | MosaiqueFM.tn@SD | - | NO_GUIDE_HIT |
| New Channels | MovieBox | MovieBox.mn@SD | - | NO_GUIDE_HIT |
| New Channels | Movify Kino | MovifyKino.lv@SD | - | NO_GUIDE_HIT |
| New Channels | Muzangala TV | MuzangalaTV.ao@SD | - | NO_GUIDE_HIT |
| New Channels | MWD Movies | MWDMovies.mm@SD | - | NO_GUIDE_HIT |
| New Channels | My Cinema [ ] | MyCinema.id@SD | - | NO_GUIDE_HIT |
| New Channels | My Cinema Europe | MyCinemaEurope.ch@SD | - | NO_GUIDE_HIT |
| New Channels | Nande Portetepe TV | NandePortetepeTV.py@SD | - | NO_GUIDE_HIT |
| New Channels | Next | NextHD.py@SD | - | NO_GUIDE_HIT |
| New Channels | Nickelodeon (India) | Nickelodeon.in@SD | - | NO_GUIDE_HIT |
| New Channels | NogoumFMTV | NogoumFMTV.eg@SD | - | NO_GUIDE_HIT |
| New Channels | Noroc TV | NorocTV.md@SD | - | NO_GUIDE_HIT |
| New Channels | Pantalla Clasica EC [ ] | PantallaClasicaEC.ec@SD | - | NO_GUIDE_HIT |
| New Channels | Pindin TV | PindinTV.pa@SD | - | NO_GUIDE_HIT |
| New Channels | Planet 100.9 FM | Planet1009FM.pa@SD | - | NO_GUIDE_HIT |
| New Channels | Play TV (Cameroon) | PlayTV.cm@SD | - | NO_GUIDE_HIT |
| New Channels | Power 101.7 FM | Power1017FM.aw@SD | - | NO_GUIDE_HIT |
| New Channels | Rakuten TV Family Movies Switzerland | RakutenTVFamilyMovies.es@Switzerland | - | NO_GUIDE_HIT |
| New Channels | RHT Guadeloupe | RHTGuadeloupe.gp@SD | - | NO_GUIDE_HIT |
| New Channels | RTL Gold (Luxembourg) | RTLGold.lu@SD | - | NO_GUIDE_HIT |
| New Channels | Scorch TV | ScorchTV.tt@SD | - | NO_GUIDE_HIT |
| New Channels | ShowVen TV | ShowVenTV.ve@SD | - | NO_GUIDE_HIT |
| New Channels | Siembra TV (Dominican Republic) | SiembraTV.do@SD | - | NO_GUIDE_HIT |
| New Channels | Silk Way Cinema | SilkWayCinema.kz@SD | - | NO_GUIDE_HIT |
| New Channels | Sky Folk TV | SkyFolkTV.mk@SD | - | NO_GUIDE_HIT |
| New Channels | SOY Plancha TV | SOYPlanchaTV.cr@SD | - | NO_GUIDE_HIT |
| New Channels | Star 101 FM | Star101FM.gu@SD | - | NO_GUIDE_HIT |
| New Channels | Star Movies (Slovenia) | StarMovies.si@SD | - | NO_GUIDE_HIT |
| New Channels | Star Tamil Television | StarTamilTelevision.lk@SD | - | NO_GUIDE_HIT |
| New Channels | StuBru | StuBru.be@SD | - | NO_GUIDE_HIT |
| New Channels | Super Q Panama | SuperQPanama.pa@SD | - | NO_GUIDE_HIT |
| New Channels | Tele Dominicana TV | TeleDominicanaTV.do@SD | - | NO_GUIDE_HIT |
| New Channels | Tele Zoukla | TeleZoukla.mq@SD | - | NO_GUIDE_HIT |
| New Channels | Ten Cricket | TenCricket.in@SD | - | NO_GUIDE_HIT |
| New Channels | Tezaur TV | TezaurTV.md@SD | - | NO_GUIDE_HIT |
| New Channels | Thrill | Thrill.hk@SD | - | NO_GUIDE_HIT |
| New Channels | Tjil TV | TjilTV.na@SD | - | NO_GUIDE_HIT |
| New Channels | TMA | TMA.gp@SD | - | NO_GUIDE_HIT |
| New Channels | TopEstrada TV | TopEstradaTV.mk@SD | - | NO_GUIDE_HIT |
| New Channels | Topical Moon RD | TopicalMoonRD.do@HD | - | NO_GUIDE_HIT |
| New Channels | Tropi Q 99.7 FM | TropiQ997FM.pa@SD | - | NO_GUIDE_HIT |
| New Channels | Tropical Moon Urban TV | TropicalMoonUrbanTV.pa@SD | - | NO_GUIDE_HIT |
| New Channels | Turkmen Owazy | TurkmenOwazy.tm@SD | - | NO_GUIDE_HIT |
| New Channels | TV Cidade | TVCidade.cv@SD | - | NO_GUIDE_HIT |
| New Channels | TV Exitos | TVExitos.do@SD | - | NO_GUIDE_HIT |
| New Channels | TVCARiB Cinema | TVCARiBCinema.sx@SD | - | NO_GUIDE_HIT |
| New Channels | TVONE Nicaragua | TVONENicaragua.ni@SD | - | NO_GUIDE_HIT |
| New Channels | UA Music | custom.ua-music | - | NO_GUIDE_HIT |
| New Channels | Urbano TV | UrbanoTV.cr@SD | - | NO_GUIDE_HIT |
| New Channels | VAM TV | VAMTV.cw@SD | - | NO_GUIDE_HIT |
| New Channels | VCV (720p) [Not 24/7] | VCV.in@SD | - | NO_GUIDE_HIT |
| New Channels | Venus Media | VenusMedia.py@SD | - | NO_GUIDE_HIT |
| New Channels | Video Tour Channel | VideoTourChannel.cr@SD | - | NO_GUIDE_HIT |
| New Channels | Vintage Music | VintageMusic.cr@SD | - | NO_GUIDE_HIT |
| New Channels | VM Latino | VMLatino.cr@SD | - | NO_GUIDE_HIT |
| New Channels | Vokta TV | VoktaTV.bd@SD | - | NO_GUIDE_HIT |
| New Channels | Vos y TV | VosyTV.ec@SD | - | NO_GUIDE_HIT |
| New Channels | Vyas Channel | VyasChannel.in@SD | - | NO_GUIDE_HIT |
| New Channels | Wavez FM | WavezFM.aw@SD | - | NO_GUIDE_HIT |
| New Channels | WeatherSpy (India) | WeatherSpy.in@SD | - | NO_GUIDE_HIT |
| New Channels | X 102.7 FM | X1027FM.aw@SD | - | NO_GUIDE_HIT |
| New Channels | Yes Movies Action | YesMoviesAction.il@SD | - | NO_GUIDE_HIT |
| New Channels | Zodiak TV | ZodiakTV.in@SD | - | NO_GUIDE_HIT |
| Pakistani | 8XM | 8XM.pk@HD | - | NO_GUIDE_HIT |
| Pakistani | 8XM | 8XM.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | ARY Music | custom.ary-music-tumyo | - | NO_GUIDE_HIT |
| Pakistani | aur LIFE | aurLIFE.pk | - | NO_GUIDE_HIT |
| Pakistani | BS Film | BSFilm.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Falak TV | FalakTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Filmazia | Filmazia.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | HUM Sitaray | HUMSitaray.pk | - | NO_GUIDE_HIT |
| Pakistani | Jalwa TV | JalwaTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Joo Music | JooMusic.pk | - | NO_GUIDE_HIT |
| Pakistani | JooMusic | JooMusic.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Lollywood HD TV | LollywoodHDTV.cd@SD | - | NO_GUIDE_HIT |
| Pakistani | Paighan TV | PaighanTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | See TV | SeeTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Tag TV | TagTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Waseb TV | WasebTV.pk | - | NO_GUIDE_HIT |
| Peru | Andina RTV | AndinaRTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | Karibena | Karibena.pe@SD | - | NO_GUIDE_HIT |
| Peru | La Fabulosa TV | LaFabulosaTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | Miel TV | MielTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | Millenium 109 FM | Millenium109FM.pe@SD | - | NO_GUIDE_HIT |
| Peru | RumbaMix TV | RumbaMixTV.pe@SD | - | NO_GUIDE_HIT |
| Peru | TV Peruanisima | TVPeruanisima.pe@SD | - | NO_GUIDE_HIT |
| Peru | TVUNO | TVUNO.pe@SD | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Comedy | FILMBOXPlusComedy.pl@Poland | Filmbox+.comedy.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Poland | FILMBOX+ Emotion | FILMBOXPlusEmotion.pl@Poland | Filmbox+.emotion.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Poland | FILMBOX+ Festival | FILMBOXPlusFestival.pl@SD | Filmbox+.festival.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Poland | FILMBOX+ Hits | FILMBOXPlusHits.pl@Poland | Filmbox+.hits.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Poland | AXN Black (United States) Poland | AXNBlack.us@Poland | - | NO_GUIDE_HIT |
| Poland | AXN Poland | AXNPoland.pl@SD | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Comedy Magyar | FILMBOXPlusComedy.pl@Magyar | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Emotion Adria | FILMBOXPlusEmotion.pl@Adria | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Festival Poland | FILMBOXPlusFestival.pl@Poland | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Hits Adria | FILMBOXPlusHits.pl@Adria | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Love & Crime Adria | FILMBOXPlusLoveCrime.pl@Adria | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ Love & Crime Magyar | FILMBOXPlusLoveCrime.pl@Magyar | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ One Magyar | FILMBOXPlusOne.pl@Magyar | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ One Nederland | FILMBOXPlusOne.pl@Nederland | - | NO_GUIDE_HIT |
| Poland | FILMBOX+ One Ukraine & Baltics [ ] | FILMBOXPlusOne.pl@UkraineBaltics | - | NO_GUIDE_HIT |
| Portugal | Kuriakos Cine | KuriakosCine.pt@SD | - | NO_GUIDE_HIT |
| Portugal | Kuriakos Music | KuriakosMusic.pt@SD | - | NO_GUIDE_HIT |
| Portugal | ON FM | ONFM.pt@SD | - | NO_GUIDE_HIT |
| Portugal | RFPtv | RFPtv.pt@SD | - | NO_GUIDE_HIT |
| Religious | Al Istiqama | AlistiqamaTV.om | Alistiqama.TV.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Religious | Al Qamar | AlQamarTV.ae | Al.Qamar.TV.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Religious | Dua Channel | DuaChannel.sa | Dua.Channel.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Religious | Iqra Bangla | IqraBangla.uk | IqraBangla.uk | MAPPED_NOT_CURRENTLY_FOUND |
| Religious | Makkah TV | MakkahTV.sa | Makkah.TV.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Religious | Al Quran Al Kareem TV | AlQuranAlKareemTV.sa | - | NO_GUIDE_HIT |
| Religious | Al Sunnah TV | custom.al-sunnah-tv | - | NO_GUIDE_HIT |
| Religious | Al-Zahra TV Turkic | AlZahraTVTurkic.sa | - | NO_GUIDE_HIT |
| Religious | ARY Q TV | ARYQTV.pk | - | NO_GUIDE_HIT |
| Religious | Bahrain Quran | BahrainQuran.bh | - | NO_GUIDE_HIT |
| Religious | Islam TV Urdu | custom.islam-tv-urdu | - | NO_GUIDE_HIT |
| Religious | Islamic TV | 223000 | - | NO_GUIDE_HIT |
| Religious | Islamic TV | IslamicTV.sa | - | NO_GUIDE_HIT |
| Religious | Madani Channel | custom.madani-channel | - | NO_GUIDE_HIT |
| Religious | Madani TV | MadaniTV.sa | - | NO_GUIDE_HIT |
| Religious | MADANI TV BANGLA | custom.bdix.madanibangla | - | NO_GUIDE_HIT |
| Religious | MADINA LIVE | custom.bdix.madinalive | - | NO_GUIDE_HIT |
| Religious | Makkah Live | MakkahLive.sa | - | NO_GUIDE_HIT |
| Religious | Makkah Live | custom.makkah.live | - | NO_GUIDE_HIT |
| Religious | Medina Live | MedinaLive.bd | - | NO_GUIDE_HIT |
| Religious | Peace TV | custom.peace-tv-tw8cm | - | NO_GUIDE_HIT |
| Religious | Peace TV Bangla | PeaceTVBangla.ae | - | NO_GUIDE_HIT |
| Religious | Peace TV English | PeaceTVEnglish.ae | - | NO_GUIDE_HIT |
| Religious | Peace TV Urdu | PeaceTVUrdu.pk | - | NO_GUIDE_HIT |
| Religious | Q TV | QTV.in@SD | - | NO_GUIDE_HIT |
| Religious | QTV-3 | QTV3.cn@SD | - | NO_GUIDE_HIT |
| Religious | Quran | custom.quran | - | NO_GUIDE_HIT |
| Religious | Quran TV | QuranTV.iq | - | NO_GUIDE_HIT |
| Religious | Sunna TV | SunnaTV.ng@SD | - | NO_GUIDE_HIT |
| Religious | Sunnah TV | custom.sunnah-tv | - | NO_GUIDE_HIT |
| Religious | Zainabia Channel | ZainabiaChannel.sa | - | NO_GUIDE_HIT |
| Romania | AMC Europe Romania | AMCEurope.uk@Romania | - | NO_GUIDE_HIT |
| Romania | Atomic Academy TV | AtomicAcademyTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | Atomic TV | AtomicTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | AXN Black (United States) Romania | AXNBlack.us@Romania | - | NO_GUIDE_HIT |
| Romania | AXN CEE Romania | AXNCEE.es@Romania | - | NO_GUIDE_HIT |
| Romania | Bollywood Classic Romania | BollywoodClassic.ro@Romania | - | NO_GUIDE_HIT |
| Romania | Boom TV | BoomTV.ro@HD | - | NO_GUIDE_HIT |
| Romania | Cinemaraton Plus | CinemaratonPlus.ro@HD | - | NO_GUIDE_HIT |
| Romania | CineWow | CineWow.ro@SD | - | NO_GUIDE_HIT |
| Romania | Film Cafe Romania | FilmCafe.hu@Romania | - | NO_GUIDE_HIT |
| Romania | FILMBOX+ Comedy Romania | FILMBOXPlusComedy.pl@Romania | - | NO_GUIDE_HIT |
| Romania | FILMBOX+ Emotion Romania | FILMBOXPlusEmotion.pl@Romania | - | NO_GUIDE_HIT |
| Romania | FILMBOX+ Hits Romania | FILMBOXPlusHits.pl@Romania | - | NO_GUIDE_HIT |
| Romania | FILMBOX+ Love & Crime Romania | FILMBOXPlusLoveCrime.pl@Romania | - | NO_GUIDE_HIT |
| Romania | FILMBOX+ One Romania | FILMBOXPlusOne.pl@Romania | - | NO_GUIDE_HIT |
| Romania | Halloween Non Stop | HalloweenNonStop.ro@SD | - | NO_GUIDE_HIT |
| Romania | Impact TV (Romania) | ImpactTV.ro@HD | - | NO_GUIDE_HIT |
| Romania | Impact TV 2 | ImpactTV2.ro@HD | - | NO_GUIDE_HIT |
| Romania | Impact TV Dance | ImpactTVDance.ro@SD | - | NO_GUIDE_HIT |
| Romania | Impact TV Manele | ImpactTVManele.ro@SD | - | NO_GUIDE_HIT |
| Romania | Super TV (Romania) | SuperTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | Tele7music | Tele7music.ro@SD | - | NO_GUIDE_HIT |
| Romania | Tequila Music TV | TequilaMusicTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | Traditional TV | TraditionalTV.ro@SD | - | NO_GUIDE_HIT |
| Romania | TV AS | TVAS.ro@SD | - | NO_GUIDE_HIT |
| Romania | Viasat Kino Romania | ViasatKino.ua@Romania | - | NO_GUIDE_HIT |
| Russia | Dom kino Premium | DomkinoPremium.ru@HD | Dom.Kino.Premium.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Russia | Shanson TV | ShansonTV.ru@SD | Shanson.TV.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Russia | VIVA Russia | VIVARussia.ru@SD | Viva.Russia.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Russia | 15+ Music | 15PlusMusic.ru@HD | - | NO_GUIDE_HIT |
| Russia | 1HD Music Television | 1HDMusicTelevision.ru@HD | - | NO_GUIDE_HIT |
| Russia | alpha Cinema | alphaCinema.ru@HD | - | NO_GUIDE_HIT |
| Russia | Blokbaster | Blokbaster.ru@HD | - | NO_GUIDE_HIT |
| Russia | Bollywood HD Russia | BollywoodHD.ro@Russia | - | NO_GUIDE_HIT |
| Russia | Bolt (Russia) | Bolt.ru@SD | - | NO_GUIDE_HIT |
| Russia | BRIDGE Rock | BRIDGERock.ru@SD | - | NO_GUIDE_HIT |
| Russia | Cinema (Russia) | Cinema.ru@SD | - | NO_GUIDE_HIT |
| Russia | City Eden Birma Play | CityEdenBirmaPlay.ru@HD | - | NO_GUIDE_HIT |
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
| Russia | City Eden KinoSemya [ ] | CityEdenKinoSemya.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden Play | CityEdenPlay.ru@HD | - | NO_GUIDE_HIT |
| Russia | City Eden Sirtaki TV | CityEdenSirtakiTV.ru@HD | - | NO_GUIDE_HIT |
| Russia | DanceHits80 | DanceHits80.ru@SD | - | NO_GUIDE_HIT |
| Russia | Detskoe kino [ ] | Detskoekino.ru@International | - | NO_GUIDE_HIT |
| Russia | Dom kino | Domkino.ru@SD | - | NO_GUIDE_HIT |
| Russia | Europa Plus TV Belarus | EuropaPlusTV.ru@Belarus | - | NO_GUIDE_HIT |
| Russia | Evrokino | Evrokino.ru@HD | - | NO_GUIDE_HIT |
| Russia | Feniks plus Kino | FeniksplusKino.ru@SD | - | NO_GUIDE_HIT |
| Russia | FON Music | FONMusic.ru@SD | - | NO_GUIDE_HIT |
| Russia | Hit | Hit.ru@HD | - | NO_GUIDE_HIT |
| Russia | Horoshee Kino | HorosheeKino.ru@SD | - | NO_GUIDE_HIT |
| Russia | Illusion+ | IllusionPlus.ru@SD | - | NO_GUIDE_HIT |
| Russia | Indiyskoye Kino | IndiyskoyeKino.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kineko | Kineko.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kino 1 (Russia) | Kino1.ru@International | - | NO_GUIDE_HIT |
| Russia | Kino 24 | Kino24.ru@SD | - | NO_GUIDE_HIT |
| Russia | KinoHit | KinoHit.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kinomix | Kinomix.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kinopokaz | Kinopokaz.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kinopremyera | Kinopremyera.ru@SD | - | NO_GUIDE_HIT |
| Russia | KinoSat | KinoSat.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kinosemja | Kinosemja.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kinoseriya | Kinoseriya.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kinosvidanie | Kinosvidanie.ru@SD | - | NO_GUIDE_HIT |
| Russia | Kinouzhas | Kinouzhas.ru@SD | - | NO_GUIDE_HIT |
| Russia | Live Music Channel | LiveMusicChannel.ru@HD | - | NO_GUIDE_HIT |
| Russia | Maidan | Maidan.ru@SD | - | NO_GUIDE_HIT |
| Russia | Mosfilm Gold Collection | MosfilmGoldCollection.ru@SD | - | NO_GUIDE_HIT |
| Russia | MTV Volgograd | MTVVolgograd.ru@SD | - | NO_GUIDE_HIT |
| Russia | Muzhskoe kino | Muzhskoekino.ru@SD | - | NO_GUIDE_HIT |
| Russia | Muzyka 1 | Muzyka1.ru@International | - | NO_GUIDE_HIT |
| Russia | Muzyka Kino | MuzykaKino.ru@International | - | NO_GUIDE_HIT |
| Russia | Muzyka Live | MuzykaLive.ru@SD | - | NO_GUIDE_HIT |
| Russia | Nash Kinopokaz | NashKinopokaz.ru@HD | - | NO_GUIDE_HIT |
| Russia | Nashe | Nashe.ru@HD | - | NO_GUIDE_HIT |
| Russia | Nashe Lubimoe Kino | NasheLubimoeKino.ru@SD | - | NO_GUIDE_HIT |
| Russia | Nashe muzhskoe | Nashemuzhskoe.ru@HD | - | NO_GUIDE_HIT |
| Russia | Nashe Novoe Kino | NasheNovoeKino.ru@SD | - | NO_GUIDE_HIT |
| Russia | Ostrosyuzhetnoye | Ostrosyuzhetnoye.ru@HD | - | NO_GUIDE_HIT |
| Russia | Patriot | Patriot.ru@SD | - | NO_GUIDE_HIT |
| Russia | Premialnoe | Premialnoe.ru@HD | - | NO_GUIDE_HIT |
| Russia | Rodnoe Kino | RodnoeKino.ru@SD | - | NO_GUIDE_HIT |
| Russia | Russkiy Bestseller | RusskiyBestseller.ru@SD | - | NO_GUIDE_HIT |
| Russia | Russkiy Detektiv | RusskiyDetektiv.ru@SD | - | NO_GUIDE_HIT |
| Russia | Russkiy Illusion | RusskiyIllusion.ru@SD | - | NO_GUIDE_HIT |
| Russia | Russkiy roman | Russkiyroman.ru@SD | - | NO_GUIDE_HIT |
| Russia | Shokiruyushchee | Shokiruyushchee.ru@HD | - | NO_GUIDE_HIT |
| Russia | Smotrim 100% Klassika | Smotrim100Klassika.ru@SD | - | NO_GUIDE_HIT |
| Russia | SONGTV Russia | SONGTVRussia.ru@SD | - | NO_GUIDE_HIT |
| Russia | START Air | STARTAir.ru@SD | - | NO_GUIDE_HIT |
| Russia | Strana FM | StranaFM.ru@SD | - | NO_GUIDE_HIT |
| Russia | TV 21 | TV21.ru@SD | - | NO_GUIDE_HIT |
| Russia | TV 21 International | TV21International.ru@SD | - | NO_GUIDE_HIT |
| Russia | TV1000 Russian Kino Global | TV1000RussianKinoGlobal.ru@SD | - | NO_GUIDE_HIT |
| Russia | Velvet. European Movies | VelvetEuropeanMovies.ru@HD | - | NO_GUIDE_HIT |
| Russia | Velvet. Golden Collection | VelvetGoldenCollection.ru@HD | - | NO_GUIDE_HIT |
| Russia | Velvet. Scary | VelvetScary.ru@HD | - | NO_GUIDE_HIT |
| Russia | Velvet. Sovetskoe Kino | VelvetSovetskoeKino.ru@HD | - | NO_GUIDE_HIT |
| Russia | viju TV1000 | vijuTV1000.ru@SD | - | NO_GUIDE_HIT |
| Russia | viju TV1000 action | vijuTV1000action.ru@SD | - | NO_GUIDE_HIT |
| Russia | viju TV1000 novella | vijuTV1000novella.ru@HD | - | NO_GUIDE_HIT |
| Russia | viju+ Megahit | vijuPlusMegahit.ru@HD | - | NO_GUIDE_HIT |
| Russia | viju+ Premiere | vijuPlusPremiere.ru@HD | - | NO_GUIDE_HIT |
| Saudi Arabia | Rotana Cinema KSA | RotanaCinemaKSA.sa@SD | Rotana.Cinema.KSA.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Saudi Arabia | Rotana Khalijia | RotanaKhalijia.sa@SD | Rotana.Khalijia.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Saudi Arabia | Abdulmajeed Abdullah | AbdulmajeedAbdullah.sa@SD | - | NO_GUIDE_HIT |
| Saudi Arabia | Aflam | custom.aflam | - | NO_GUIDE_HIT |
| Saudi Arabia | Fairuz | Fairuz.sa@HD | - | NO_GUIDE_HIT |
| Saudi Arabia | Majid Al Mohandis | MajidAlMohandis.sa@SD | - | NO_GUIDE_HIT |
| Saudi Arabia | MBC Loud | MBCLoud.sa@SD | - | NO_GUIDE_HIT |
| Saudi Arabia | MBC Mood | MBCMood.sa@HD | - | NO_GUIDE_HIT |
| Saudi Arabia | Movies Action | MoviesAction.sa@SD | - | NO_GUIDE_HIT |
| Saudi Arabia | Panorama FM | PanoramaFM.sa@SD | - | NO_GUIDE_HIT |
| Saudi Arabia | Rabeh Saqer | RabehSaqer.sa@HD | - | NO_GUIDE_HIT |
| Saudi Arabia | Tarab | Tarab.sa@SD | - | NO_GUIDE_HIT |
| Spain | AXN Movies (Spain) | AXNMovies.es@SD | AXN.Movies.es | MAPPED_NOT_CURRENTLY_FOUND |
| Spain | Cine Friki | CineFriki.es@SD | Cine.Friki.es | MAPPED_NOT_CURRENTLY_FOUND |
| Spain | Cine Western (Spain) | CineWestern.es@SD | Cine.Western.es | MAPPED_NOT_CURRENTLY_FOUND |
| Spain | Activa TV | ActivaTV.es@SD | - | NO_GUIDE_HIT |
| Spain | AXN CEE Bulgary | AXNCEE.es@Bulgary | - | NO_GUIDE_HIT |
| Spain | Cadena Elite | CadenaElite.es@SD | - | NO_GUIDE_HIT |
| Spain | LiraTV | LiraTV.es@SD | - | NO_GUIDE_HIT |
| Spain | Music TV Granada | MusicTVGranada.es@SD | - | NO_GUIDE_HIT |
| Spain | MyTime Movie Network (Spain) | MyTimeMovieNetwork.es@SD | - | NO_GUIDE_HIT |
| Spain | POP World TV | POPWorldTV.es@SD | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Action Movies | RakutenTVActionMovies.es@Spain | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Comedy Movies | RakutenTVComedyMovies.es@Spain | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Drama Movies | RakutenTVDramaMovies.es@Spain | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Family Movies | RakutenTVFamilyMovies.es@Spain | - | NO_GUIDE_HIT |
| Spain | Rakuten TV Top Movies | RakutenTVTopMovies.es@Spain | - | NO_GUIDE_HIT |
| Spain | RTV Vida | RTVVida.es@SD | - | NO_GUIDE_HIT |
| Spain | SpektraTV | SpektraTV.es@SD | - | NO_GUIDE_HIT |
| Spain | Sundance TV (Spain) | SundanceTV.es@SD | - | NO_GUIDE_HIT |
| Spain | TVOMIX | TVOMIX.es@HD | - | NO_GUIDE_HIT |
| Spain | XPTV1 | XPTV1.es@SD | - | NO_GUIDE_HIT |
| Sports | Arena Sport 1 | ArenaSport1.sk@SD | Arena.Sport.1.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Arena Sport 2 | ArenaSport2.sk@SD | Arena.Sport.2.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | ESPN Premium (Argentina) | ESPNPremium.ar@HD | ESPNPremium.ar | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | FITE 24/7 | FITE247.us@SD | FITE247.us | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | FTF Sports | FTFSports.us@SD | FTFSports.us | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Game+ | GamePlus.ca@SD | Game.TV.ch | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | IN: -HINDI- STAR SPORTS 1 HD | Star Sports 1 Hindi HD.in | StarSports1HindiHD.in | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | ITV Deportes | ITVDeportes.mx@SD | plex.tv.ITV.Deportes.plex | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Jordan Sport | JordanSport.jo@SD | Jordan.Sport.HD.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Marquee Sports Network | MarqueeSportsNetwork.us | Marquee.Sports.Network.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Match4 | Match4.hu@SD | Match.4.hu | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Right Now TV | RightNowTV.us@SD | Right.Now.TV.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Sky Sports Cricket | SkySportsCricket.ie | SkySportsCricket.ie | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Sky Sports Football | SkySportsFootball.ie | SkySportsFootball.ie | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Sky Sports NFL | SkySportsNFL.uk@SD | Sky.Sports.NFL.uk | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Sport2 | Sport2.cz@SD | Sport2.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Sports First TV | SportsFirstTV.us | Sports.First.ae | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Sporty TV | SportyTV.cz@SD | Sporty.TV.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | TSN The Ocho | TSNTheOcho.ca@SD | TSNTheOcho.ca | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | TyC Sports | TyCSports.ar@SD | TyCSports.ar | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | Win Sports | WinSports.co@SD | WinSports.co | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | World of Freesports | WorldofFreesports.de@SD | WorldofFreesports.de | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | WWE Network | WWENetwork.us@SD | WWE.Network.my | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | 30A Golf Kingdom | 30AGolfKingdom.us@SD | - | NO_GUIDE_HIT |
| Sports | A Sports | ASports.pk | - | NO_GUIDE_HIT |
| Sports | Al Iraqia Sport | AlIraqiaSport.iq@SD | - | NO_GUIDE_HIT |
| Sports | Arena Sport 1 Premium (Serbia) | ArenaSport1Premium.rs@SD | - | NO_GUIDE_HIT |
| Sports | Arena Sport 1 Premium (Slovenia) | ArenaSport1Premium.si@SD | - | NO_GUIDE_HIT |
| Sports | Arena Sport Premium M1 | ArenaSportPremiumM1.mk@SD | - | NO_GUIDE_HIT |
| Sports | Arena Sport Premium M2 | ArenaSportPremiumM2.mk@SD | - | NO_GUIDE_HIT |
| Sports | Arena Sport Premium M3 | ArenaSportPremiumM3.mk@SD | - | NO_GUIDE_HIT |
| Sports | AS3 Sport TV | AS3SportTV.ve@SD | - | NO_GUIDE_HIT |
| Sports | Astrahan.Ru Sport | AstrahanRuSport.ru@SD | - | NO_GUIDE_HIT |
| Sports | Bahrain Sports 1 | BahrainSports1.bh@SD | - | NO_GUIDE_HIT |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | - | NO_GUIDE_HIT |
| Sports | BEK Sports West | BEKSports.us@West | - | NO_GUIDE_HIT |
| Sports | Belarus-5 | Belarus5.by@HD | - | NO_GUIDE_HIT |
| Sports | Canal Showsport | CanalShowsport.ar@SD | - | NO_GUIDE_HIT |
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
| Sports | CT Sport | CTSport.cz@SD | - | NO_GUIDE_HIT |
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
| Sports | FIFA+ French | FIFAPlus.uk@French | - | NO_GUIDE_HIT |
| Sports | FIFA+ German | FIFAPlus.uk@German | - | NO_GUIDE_HIT |
| Sports | FIFA+ Hispanic America | FIFAPlus.uk@HispanicAmerica | - | NO_GUIDE_HIT |
| Sports | FIFA+ Italy | FIFAPlus.uk@Italy | - | NO_GUIDE_HIT |
| Sports | FIFA+ Portuguese | FIFAPlus.uk@Portuguese | - | NO_GUIDE_HIT |
| Sports | FIFA+ Spain | FIFAPlus.uk@Spain | - | NO_GUIDE_HIT |
| Sports | FIFA+ United States | FIFAPlus.uk@UnitedStates | - | NO_GUIDE_HIT |
| Sports | FIFA+ Women | FIFAPlusWomen.uk@English | - | NO_GUIDE_HIT |
| Sports | FightBox Poland | FightBox.nl@Poland | - | NO_GUIDE_HIT |
| Sports | Formula 1 AntenaPlay | Formula1AntenaPlay.ro@SD | - | NO_GUIDE_HIT |
| Sports | FTV (Bolivia) | FTV.bo@SD | - | NO_GUIDE_HIT |
| Sports | FUEL TV AU | FUELTV.pt@AU | - | NO_GUIDE_HIT |
| Sports | Futbol TV | FutbolTV.uz@HD | - | NO_GUIDE_HIT |
| Sports | FUTV | FUTV.cr@SD | - | NO_GUIDE_HIT |
| Sports | Glory Kickboxing Poland | GloryKickboxing.us@Poland | - | NO_GUIDE_HIT |
| Sports | Go3 Sport 1 | Go3Sport1.ee@SD | - | NO_GUIDE_HIT |
| Sports | Goal TV | GoalTV.in | - | NO_GUIDE_HIT |
| Sports | HTSpor TV | HTSporTV.tr@SD | - | NO_GUIDE_HIT |
| Sports | HTV Sports | HTVSports.vn@SD | - | NO_GUIDE_HIT |
| Sports | KTV Sport | KTVSport.kw@SD | - | NO_GUIDE_HIT |
| Sports | KTV Sport Plus | KTVSportPlus.kw@SD | - | NO_GUIDE_HIT |
| Sports | L1 Max | L1Max.pe@SD | - | NO_GUIDE_HIT |
| Sports | Lacrosse TV | LacrosseTV.us@SD | - | NO_GUIDE_HIT |
| Sports | LRT Plius | LRTPlius.lt@SD | - | NO_GUIDE_HIT |
| Sports | M Sports | MSports.pk@SD | - | NO_GUIDE_HIT |
| Sports | MadeinBO TV | MadeinBOTV.it@SD | - | NO_GUIDE_HIT |
| Sports | Maincast Cybersport | MaincastCybersport.ua@SD | - | NO_GUIDE_HIT |
| Sports | Maincast Sport | MaincastSport.ua@SD | - | NO_GUIDE_HIT |
| Sports | Match! Boets | MatchBoets.ru@SD | - | NO_GUIDE_HIT |
| Sports | Match! Ultra | MatchUltra.ru@4K | - | NO_GUIDE_HIT |
| Sports | Meridiano TV | MeridianoTV.ve@SD | - | NO_GUIDE_HIT |
| Sports | MNB Sport | MNBSport.mn@SD | - | NO_GUIDE_HIT |
| Sports | Monterrico TV | MonterricoTV.pe@SD | - | NO_GUIDE_HIT |
| Sports | MRTV Sports | MRTVSports.mm@SD | - | NO_GUIDE_HIT |
| Sports | NHL AntenaPlay | NHLAntenaPlay.ro@SD | - | NO_GUIDE_HIT |
| Sports | Okko Futbol | OkkoFutbol.ru@SD | - | NO_GUIDE_HIT |
| Sports | Oman Sports TV | OmanSportsTV.om@SD | - | NO_GUIDE_HIT |
| Sports | Ovacion TV | OvacionTV.pe@SD | - | NO_GUIDE_HIT |
| Sports | Persiana Fight | PersianaFight.fr@HD | - | NO_GUIDE_HIT |
| Sports | PK Sports | PKSports.pk@SD | - | NO_GUIDE_HIT |
| Sports | PK: GEO SUPER | custom.bdix.geosuper | - | NO_GUIDE_HIT |
| Sports | Prima Sport Czechia | PrimaSportCzechia.cz@SD | - | NO_GUIDE_HIT |
| Sports | Prime (Syria) | Prime.sy@HD | - | NO_GUIDE_HIT |
| Sports | PTV Sports | PTVSports.pk | - | NO_GUIDE_HIT |
| Sports | RACER International | RACERInternational.pl@FAST | - | NO_GUIDE_HIT |
| Sports | Rally TV | RallyTV.us@SD | - | NO_GUIDE_HIT |
| Sports | Real Madrid TV English | RealMadridTVEnglish.es@SD | - | NO_GUIDE_HIT |
| Sports | Realitatea Sportiva | RealitateaSportiva.ro@SD | - | NO_GUIDE_HIT |
| Sports | Red Bull TV AU | RedBullTV.at@AU | - | NO_GUIDE_HIT |
| Sports | Red Bull TV BR | RedBullTV.at@BR | - | NO_GUIDE_HIT |
| Sports | Red Bull TV DE | RedBullTV.at@DE | - | NO_GUIDE_HIT |
| Sports | Red Bull TV ES | RedBullTV.at@ES | - | NO_GUIDE_HIT |
| Sports | Red Bull TV UK | RedBullTV.at@UK | - | NO_GUIDE_HIT |
| Sports | Red Bull TV US | RedBullTV.at@US | - | NO_GUIDE_HIT |
| Sports | Russian Extreme Ultra | RussianExtremeUltra.ru@SD | - | NO_GUIDE_HIT |
| Sports | Setanta Sports 2 Eurasia | SetantaSports2Eurasia.ie@SD | - | NO_GUIDE_HIT |
| Sports | Spiler 1 | Spiler1.hu@SD | - | NO_GUIDE_HIT |
| Sports | Spiler 2 | Spiler2.hu@SD | - | NO_GUIDE_HIT |
| Sports | Sport (Slovakia) | Sport.sk@SD | - | NO_GUIDE_HIT |
| Sports | Sport 1 (Ukraine) | Sport1.ua@SD | - | NO_GUIDE_HIT |
| Sports | Sport 1 Baltic | Sport1Baltic.ua@SD | - | NO_GUIDE_HIT |
| Sports | Sport 3 | Sport3.ua@SD | - | NO_GUIDE_HIT |
| Sports | Sport 4 | Sport4.ua@SD | - | NO_GUIDE_HIT |
| Sports | Sport TV | SportTV.by@SD | - | NO_GUIDE_HIT |
| Sports | Sportivnyy | Sportivnyy.ru@SD | - | NO_GUIDE_HIT |
| Sports | Sports Television | SportsTelevision.kp@HD | - | NO_GUIDE_HIT |
| Sports | Sqala TV | SqalaTV.pe@SD | - | NO_GUIDE_HIT |
| Sports | Strongman | Strongman.us@Germany | - | NO_GUIDE_HIT |
| Sports | Strongman Champions League | StrongmanChampionsLeague.uk@SD | - | NO_GUIDE_HIT |
| Sports | Strongman UK | Strongman.us@UK | - | NO_GUIDE_HIT |
| Sports | Suspilne. Sport | SuspilneSport.ua@SD | - | NO_GUIDE_HIT |
| Sports | Swerve Sports | SwerveSports.us@SD | - | NO_GUIDE_HIT |
| Sports | T Sports | TSports.bd | - | NO_GUIDE_HIT |
| Sports | T SPORTS | TSports.bd@SD | - | NO_GUIDE_HIT |
| Sports | T Sports 7 | TSports7.th@SD | - | NO_GUIDE_HIT |
| Sports | Teletrak TV | TeletrakTV.cl@SD | - | NO_GUIDE_HIT |
| Sports | Ten Sports | TenSports.pk | - | NO_GUIDE_HIT |
| Sports | Tigo Sports (Honduras) | TigoSports.hn@SD | - | NO_GUIDE_HIT |
| Sports | Tigo Sports (Paraguay) | TigoSports.py@SD | - | NO_GUIDE_HIT |
| Sports | TJK TV | TJKTV.tr@SD | - | NO_GUIDE_HIT |
| Sports | TR Sport | TRSport.it@SD | - | NO_GUIDE_HIT |
| Sports | Trace Sport Stars Russia | TraceSportStars.fr@Russia | - | NO_GUIDE_HIT |
| Sports | Turf Movil | TurfMovil.cl@SD | - | NO_GUIDE_HIT |
| Sports | Turkmenistan Sport | TurkmenistanSport.tm@SD | - | NO_GUIDE_HIT |
| Sports | TVS Bowling Network | TVSBowlingNetwork.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Boxing | TVSBoxing.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Classic Sports | TVSClassicSports.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Sports | TVSSports.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Sports Bureau | TVSSportsBureau.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Turbo | TVSTurbo.us@SD | - | NO_GUIDE_HIT |
| Sports | TVS Women Sports | TVSWomenSports.us@SD | - | NO_GUIDE_HIT |
| Sports | TyC Sports USA | TyCSportsUSA.ar@SD | - | NO_GUIDE_HIT |
| Sports | viju+ Sport | vijuPlusSport.ru@HD | - | NO_GUIDE_HIT |
| Sports | Vinh Long TV 4 | VinhLongTV4.vn@SD | - | NO_GUIDE_HIT |
| Sports | Voyo Sport 1 | VoyoSport1.ro@HD | - | NO_GUIDE_HIT |
| Sports | Win+ Futbol | WinPlusFutbol.co@SD | - | NO_GUIDE_HIT |
| Sports | World Poker Tour Poland | WorldPokerTour.us@Poland | - | NO_GUIDE_HIT |
| Sports | World Poker Tour UK | WorldPokerTour.us@UK | - | NO_GUIDE_HIT |
| Sweden | Merry Christmas from Viafree | MerryChristmasfromViafree.se@SE | - | NO_GUIDE_HIT |
| Sweden | Merry Christmas from Viafree DK | MerryChristmasfromViafree.se@DK | - | NO_GUIDE_HIT |
| Sweden | Merry Christmas from Viafree NO | MerryChristmasfromViafree.se@NO | - | NO_GUIDE_HIT |
| Sweden | NonStop Kung Fu | NonStopKungFu.se@SE | - | NO_GUIDE_HIT |
| Sweden | NonStop Kung Fu DK | NonStopKungFu.se@DK | - | NO_GUIDE_HIT |
| Sweden | NonStop Kung Fu NO | NonStopKungFu.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Action (Sweden) | PlutoTVAction.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Action (Sweden) DK | PlutoTVAction.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Action (Sweden) NO | PlutoTVAction.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Bud & Terence (Sweden) | PlutoTVBudTerence.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Bud & Terence (Sweden) DK | PlutoTVBudTerence.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Bud & Terence (Sweden) NO | PlutoTVBudTerence.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Danske klassikere | PlutoTVDanskeklassikere.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Film (Sweden) | PlutoTVFilm.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Film (Sweden) DK | PlutoTVFilm.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Film (Sweden) NO | PlutoTVFilm.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Harlequin | PlutoTVHarlequin.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Harlequin DK | PlutoTVHarlequin.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Harlequin NO | PlutoTVHarlequin.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Horror (Sweden) | PlutoTVHorror.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Horror (Sweden) DK | PlutoTVHorror.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Horror (Sweden) NO | PlutoTVHorror.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Humor (Sweden) | PlutoTVHumor.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV John Wayne | PlutoTVJohnWayne.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV John Wayne DK | PlutoTVJohnWayne.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV John Wayne NO | PlutoTVJohnWayne.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Komedi | PlutoTVKomedi.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Komedie | PlutoTVKomedie.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Kultfilm | PlutoTVKultfilm.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Kultfilmer | PlutoTVKultfilmer.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Kultfilmer NO | PlutoTVKultfilmer.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Paranormal (Sweden) | PlutoTVParanormal.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Paranormal (Sweden) DK | PlutoTVParanormal.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Romantik | PlutoTVRomantik.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Romantik DK | PlutoTVRomantik.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Romantikk | PlutoTVRomantikk.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Sci-Fi (Sweden) | PlutoTVSciFi.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Sci-Fi (Sweden) DK | PlutoTVSciFi.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Sci-Fi (Sweden) NO | PlutoTVSciFi.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Star Trek (Sweden) | PlutoTVStarTrek.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Wild West | PlutoTVWildWest.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Wild West DK | PlutoTVWildWest.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Wild West NO | PlutoTVWildWest.se@NO | - | NO_GUIDE_HIT |
| Sweden | Star Trek Movies | StarTrekMovies.se@SE | - | NO_GUIDE_HIT |
| Sweden | Star Trek Movies DK | StarTrekMovies.se@DK | - | NO_GUIDE_HIT |
| Sweden | Star Trek Movies NO | StarTrekMovies.se@NO | - | NO_GUIDE_HIT |
| Sweden | Star Trek: The Original Series (Sweden) | StarTrekTheOriginalSeries.se@SE | - | NO_GUIDE_HIT |
| Sweden | Star Trek: The Original Series (Sweden) DK | StarTrekTheOriginalSeries.se@DK | - | NO_GUIDE_HIT |
| Sweden | Star Trek: The Original Series (Sweden) NO | StarTrekTheOriginalSeries.se@NO | - | NO_GUIDE_HIT |
| Sweden | The Twilight Zone | TheTwilightZone.se@SE | - | NO_GUIDE_HIT |
| Sweden | The Twilight Zone DK | TheTwilightZone.se@DK | - | NO_GUIDE_HIT |
| Sweden | The Twilight Zone NO | TheTwilightZone.se@NO | - | NO_GUIDE_HIT |
| Sweden | Viafree Movies | ViafreeMovies.se@SE | - | NO_GUIDE_HIT |
| Sweden | Viafree Movies DK | ViafreeMovies.se@DK | - | NO_GUIDE_HIT |
| Sweden | Viafree Movies NO | ViafreeMovies.se@NO | - | NO_GUIDE_HIT |
| Turkey | MovieSmart Turk | MovieSmartTurk.tr@SD | MovieSmartTurk.tr | MAPPED_NOT_CURRENTLY_FOUND |
| Turkey | beIN Box Office 1 | beINBoxOffice1.tr@SD | - | NO_GUIDE_HIT |
| Turkey | beIN Box Office 2 | beINBoxOffice2.tr@SD | - | NO_GUIDE_HIT |
| Turkey | beIN Box Office 3 | beINBoxOffice3.tr@SD | - | NO_GUIDE_HIT |
| Turkey | beIN Movies Stars | beINMoviesStars.tr@SD | - | NO_GUIDE_HIT |
| Turkey | beIN Movies Turk | beINMoviesTurk.tr@SD | - | NO_GUIDE_HIT |
| Turkey | Dream Turk | DreamTurk.tr@SD | - | NO_GUIDE_HIT |
| Turkey | GEM Pixel | GEMPixel.tr@SD | - | NO_GUIDE_HIT |
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
| Turkey | TRT Muzik | TRTMuzik.tr@SD | - | NO_GUIDE_HIT |
| Ukraine | Enter-Film | EnterFilm.ua@SD | Enter-Film.ch | MAPPED_NOT_CURRENTLY_FOUND |
| Ukraine | Muzvar | Muzvar.ua@SD | Muzvar.cz | MAPPED_NOT_CURRENTLY_FOUND |
| Ukraine | 4ever Cinema | 4everCinema.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | 4ever Music | 4everMusic.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Black | Black.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Bolt (Ukraine) | Bolt.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Cine+ | CinePlus.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Cine+ Hit | CinePlusHit.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Cine+ Legend | CinePlusLegend.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | EU Music | EUMusic.ua | - | NO_GUIDE_HIT |
| Ukraine | FilmUA Live | FilmUALive.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Hollywood Ukraine | HollywoodUkraine.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | InRating TV | InRatingTV.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Kino 1 (Ukraine) | Kino1.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Kino 2 | Kino2.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Kinoliving | Kinoliving.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Kinowood | Kinowood.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | M2 (Ukraine) | M2.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Megogo Music | MegogoMusic.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Music Box Polska Ukraine | MusicBoxPolska.pl@Ukraine | - | NO_GUIDE_HIT |
| Ukraine | Nashe Lubimoe Kino Ukraine | NasheLubimoeKinoUkraine.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | NASHE Music | NASHEMusic.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Prokino | Prokino.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Viasat Kino Action | ViasatKinoAction.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Viasat Kino Balkan | ViasatKino.ua@Balkan | - | NO_GUIDE_HIT |
| Ukraine | Viasat Kino Comedy | ViasatKinoComedy.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Viasat Kino World | ViasatKinoWorld.ua@SD | - | NO_GUIDE_HIT |
| Ukraine | Viasat Serial | ViasatSerial.ua@HD | - | NO_GUIDE_HIT |
| Ukraine | ¡Viva Latino! | VivaLatino.ua@SD | - | NO_GUIDE_HIT |
| United Arab Emirates | PMC | PMC.ae@SD | 4906 | MAPPED_ENDED |
| United Arab Emirates | MBC FM | MBCFM.ae@SD | MBC.FM.ae | MAPPED_NOT_CURRENTLY_FOUND |
| United Arab Emirates | OSN Movies Action | OSNMoviesAction.ae@SD | - | NO_GUIDE_HIT |
| United Arab Emirates | PMC Royale | PMCRoyale.ae@SD | - | NO_GUIDE_HIT |
| United Kingdom | MTV Classic | mtv.classic.gb | MTV.Classic.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| United Kingdom | AMC Europe Bulgary | AMCEurope.uk@Bulgary | - | NO_GUIDE_HIT |
| United Kingdom | Clubbing TV UK | ClubbingTV.us@UK | - | NO_GUIDE_HIT |
| United Kingdom | MovieSphere UK | custom.moviesphere-uk | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic 2000s | Totalmusic2000s.uk@HD | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic 80s | Totalmusic80s.uk | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic Concerts | TotalmusicConcerts.uk | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic Dance | TotalmusicDance.uk@HD | - | NO_GUIDE_HIT |
| United Kingdom | Trace UK | TraceUK.uk@HD | - | NO_GUIDE_HIT |
| United Kingdom | V2BEAT TV | V2BEATTV.uk@SD | - | NO_GUIDE_HIT |
| United Kingdom | Vantage Music UK | VantageMusic.ee@UK | - | NO_GUIDE_HIT |
| United States | 24 Hour Free Movies | custom.24-hour-free-movies | plex.tv.24.Hour.Free.Movies.plex | MAPPED_NOT_CURRENTLY_FOUND |
| United States | Cinemax Classics | CinemaxClassics.us@East | Cinemax.Classics.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| United States | Cinemax Hits | CinemaxHits.us@East | Cinemax.Hits.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| United States | CMT | CMT.us@East | CMT.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| United States | Fuse | fusetv.us | Fuse.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| United States | HBO Zone | hbozone.us | HBO.Zone.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| United States | IFC | independentfilmchannel.us | IFC.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| United States | MBC America | MBCAmerica.us@SD | MBC.America.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| United States | MTV Live | custom.mtv-live | MTV.Live.gr | MAPPED_NOT_CURRENTLY_FOUND |
| United States | Pluto TV Cine Crimen | PlutoTVCineCrimen.us@LatAm | CineCrimen.pluto | MAPPED_NOT_CURRENTLY_FOUND |
| United States | Starz Comedy | StarzComedy.us@East | Starz.Comedy.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| United States | Turner Classic Movies | turnerclassicmovies.us | Turner.Classic.Movies.HD.us2 | MAPPED_NOT_CURRENTLY_FOUND |
| United States | 00s Replay | 00sReplay.us@SD | - | NO_GUIDE_HIT |
| United States | 30A Music | 30AMusic.us@SD | - | NO_GUIDE_HIT |
| United States | 30A TV Classic Movies | 30ATVClassicMovies.us@SD | - | NO_GUIDE_HIT |
| United States | 70s Cinema | 70sCinema.us@SD | - | NO_GUIDE_HIT |
| United States | 80s Rewind | 80sRewind.us@SD | - | NO_GUIDE_HIT |
| United States | 90s Throwback | 90sThrowback.us@SD | - | NO_GUIDE_HIT |
| United States | Adrenalina Pura TV | AdrenalinaPuraTV.us@SD | - | NO_GUIDE_HIT |
| United States | AMC (United States) | AMC.us@EastHD | - | NO_GUIDE_HIT |
| United States | AMC Latin America | AMCLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| United States | AMC Series Latin America | AMCSeriesLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| United States | American Horrors | AmericanHorrors.us@SD | - | NO_GUIDE_HIT |
| United States | Aneflix Live | AneflixLive.us@HD | - | NO_GUIDE_HIT |
| United States | ARTFLIX Movie Classics | ARTFLIXMovieClassics.us@SD | - | NO_GUIDE_HIT |
| United States | Avang TV | AvangTV.us@SD | - | NO_GUIDE_HIT |
| United States | AVI Rewind | AVIRewind.us@SD | - | NO_GUIDE_HIT |
| United States | AXN Adria | AXNAdria.us@SD | - | NO_GUIDE_HIT |
| United States | AXN Black (United States) | AXNBlack.us@Bulgary | - | NO_GUIDE_HIT |
| United States | AXN Crime | AXNCrime.us@SD | - | NO_GUIDE_HIT |
| United States | AXN Latin America | AXNLatinAmerica.us@CentralAmerica | - | NO_GUIDE_HIT |
| United States | AXN Latin America Andes | AXNLatinAmerica.us@Andes | - | NO_GUIDE_HIT |
| United States | AXN Latin America South | AXNLatinAmerica.us@South | - | NO_GUIDE_HIT |
| United States | Battlestar Galactica | BattlestarGalactica.us@SD | - | NO_GUIDE_HIT |
| United States | BET Cinema | BETCinema.us@SD | - | NO_GUIDE_HIT |
| United States | BET Comedy Movies | BETComedyMovies.us@SD | - | NO_GUIDE_HIT |
| United States | BET Visionaries | BETVisionaries.us@SD | - | NO_GUIDE_HIT |
| United States | Bonanza | Bonanza.us@SD | - | NO_GUIDE_HIT |
| United States | Bonanza CA | Bonanza.us@CA | - | NO_GUIDE_HIT |
| United States | Botflix Radioo | BotflixRadioo.us@HD | - | NO_GUIDE_HIT |
| United States | California Music Channel | CaliforniaMusicChannel.us | - | NO_GUIDE_HIT |
| United States | Cine Adrenalina | CineAdrenalina.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Amor | CineAmor.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Familiar | CineFamiliar.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Hispano | CineHispano.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Premiere | CinePremiere.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Premium | CinePremium.us@SD | - | NO_GUIDE_HIT |
| United States | Cine Terror | CineTerror.us@US | - | NO_GUIDE_HIT |
| United States | Cine Terror BR | CineTerror.us@BR | - | NO_GUIDE_HIT |
| United States | Cine Terror LatAm | CineTerror.us@LatAm | - | NO_GUIDE_HIT |
| United States | Cinecanal | Cinecanal.us@Panregional | - | NO_GUIDE_HIT |
| United States | Cinecanal Pacific | Cinecanal.us@Pacific | - | NO_GUIDE_HIT |
| United States | Cinecanal South | Cinecanal.us@South | - | NO_GUIDE_HIT |
| United States | Cinemax (United States) West | Cinemax.us@West | - | NO_GUIDE_HIT |
| United States | Cinemax Latin America | CinemaxLatinAmerica.us@HD | - | NO_GUIDE_HIT |
| United States | Cinevault 80s | Cinevault80s.us@SD | - | NO_GUIDE_HIT |
| United States | Classic Movies Channel | ClassicMoviesChannel.us@SD | - | NO_GUIDE_HIT |
| United States | CMC-USA Country Music Channel | CMCUSACountryMusicChannel.us@SD | - | NO_GUIDE_HIT |
| United States | De Pelicula US | DePeliculaUS.us@SD | - | NO_GUIDE_HIT |
| United States | DHE | DHE.us@SD | - | NO_GUIDE_HIT |
| United States | DUST | DUST.us@SD | - | NO_GUIDE_HIT |
| United States | EBS Cinema | EBSCinema.us@SD | - | NO_GUIDE_HIT |
| United States | EBS Musika | EBSMusika.us@SD | - | NO_GUIDE_HIT |
| United States | Epix | epix.us | - | NO_GUIDE_HIT |
| United States | Epix Hits | epixhits.us | - | NO_GUIDE_HIT |
| United States | Filmes Suspense | FilmesSuspense.us@BR | - | NO_GUIDE_HIT |
| United States | FilmRise Forensic Files [ ] | FilmRiseForensicFiles.us@SD | - | NO_GUIDE_HIT |
| United States | Flicks of Fury | FlicksofFury.us@SD | - | NO_GUIDE_HIT |
| United States | FrightFlix | FrightFlix.us@SD | - | NO_GUIDE_HIT |
| United States | FXM | fxm.us | - | NO_GUIDE_HIT |
| United States | Girlfriends Films | GirlfriendsFilms.us@SD | - | NO_GUIDE_HIT |
| United States | Hallmark Mystery [ ] | HallmarkMystery.us@East | - | NO_GUIDE_HIT |
| United States | HBO (United States) | HBO.us@East | - | NO_GUIDE_HIT |
| United States | HBO 2 Latin America | HBO2LatinAmerica.us@HD | - | NO_GUIDE_HIT |
| United States | HBO Family Latin America | HBOFamilyLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | HBO Hits | HBOHits.us@East | - | NO_GUIDE_HIT |
| United States | HBO Latin America | HBOLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | HBO Mundi Latin America | HBOMundiLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | HBO Xtreme Latin America | HBOXtremeLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | High Vision TV | HighVisionTV.us@SD | - | NO_GUIDE_HIT |
| United States | HTV | HTV.us@SD | - | NO_GUIDE_HIT |
| United States | ICC plus | ICCplus.us@SD | - | NO_GUIDE_HIT |
| United States | Lifetime Movies | lifetimemovies.us | - | NO_GUIDE_HIT |
| United States | Magnificent Movies Network | MagnificentMoviesNetwork.us@SD | - | NO_GUIDE_HIT |
| United States | Maxcine | Maxcine.us@HD | - | NO_GUIDE_HIT |
| United States | Maxcine 2 | Maxcine2.us@HD | - | NO_GUIDE_HIT |
| United States | Maxcine Comedy | MaxcineComedy.us@HD | - | NO_GUIDE_HIT |
| United States | Maxcine Family | MaxcineFamily.us@HD | - | NO_GUIDE_HIT |
| United States | Mega Extreno | MegaExtrenoHD.us@HD | - | NO_GUIDE_HIT |
| United States | Metaleitor TV | MetaleitorTV.us@SD | - | NO_GUIDE_HIT |
| United States | Mi Musica Reggaeton | MiMusicaReggaeton.us@SD | - | NO_GUIDE_HIT |
| United States | Mi Musica Romantica | MiMusicaRomantica.us@SD | - | NO_GUIDE_HIT |
| United States | Mi Musica Salsa | MiMusicaSalsa.us@SD | - | NO_GUIDE_HIT |
| United States | Movies! KPVM-LD | Movies.us@KPVMLD | - | NO_GUIDE_HIT |
| United States | MovieSphere CA | MovieSphere.us@CA | - | NO_GUIDE_HIT |
| United States | MovieSphere Gold WFXT | MovieSphereGold.us@WFXT | - | NO_GUIDE_HIT |
| United States | MTV (United States) | MTV.us@East | - | NO_GUIDE_HIT |
| United States | Paramount+ Picks | ParamountPlusPicks.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV A La Mexicana | PlutoTVALaMexicana.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Action (United States) | PlutoTVAction.us@US | - | NO_GUIDE_HIT |
| United States | Pluto TV Action Movies | PlutoTVActionMovies.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Bang Bang | PlutoTVBangBang.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Accion | PlutoTVCineAccion.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Clasico | PlutoTVCineClasico.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Classicos | PlutoTVCineClassicos.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Comedia (United States) | PlutoTVCineComedia.us@US | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Comedia (United States) BR | PlutoTVCineComedia.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Comedia (United States) LatAm | PlutoTVCineComedia.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Comedia Romantica | PlutoTVCineComediaRomantica.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Crime | PlutoTVCineCrime.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Drama | PlutoTVCineDrama.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Drama LatAm | PlutoTVCineDrama.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Estelar | PlutoTVCineEstelar.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Familia | PlutoTVCineFamilia.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Familia LatAm | PlutoTVCineFamilia.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Inspiracao | PlutoTVCineInspiracao.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Inspirador | PlutoTVCineInspirador.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Romance | PlutoTVCineRomance.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Romance LatAm | PlutoTVCineRomance.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Sucessos | PlutoTVCineSucessos.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Cine Suspenso | PlutoTVCineSuspenso.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Comedy Movies | PlutoTVComedyMovies.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Crime Drama | PlutoTVCrimeDrama.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Crime Drama CA | PlutoTVCrimeDrama.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Crime Movies | PlutoTVCrimeMovies.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Cult Films (United States) | PlutoTVCultFilms.us@US | - | NO_GUIDE_HIT |
| United States | Pluto TV Drama | PlutoTVDrama.us@US | - | NO_GUIDE_HIT |
| United States | Pluto TV Drama Movies | PlutoTVDramaMovies.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Estrellas de Accion | PlutoTVEstrellasdeAccion.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Ficcao Cientifica | PlutoTVFiccaoCientifica.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Filmes Acao | PlutoTVFilmesAcao.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Filmes Aventura | PlutoTVFilmesAventura.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Filmes de Luta | PlutoTVFilmesdeLuta.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Filmes Nacionais | PlutoTVFilmesNacionais.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Franchise Favorites | PlutoTVFranchiseFavorites.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Horror (United States) | PlutoTVHorror.us@US | - | NO_GUIDE_HIT |
| United States | Pluto TV Horror (United States) CA | PlutoTVHorror.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Icons | PlutoTVIcons.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Netmovies | PlutoTVNetmovies.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Nuestro Cine | PlutoTVNuestroCine.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Reaction | PlutoTVReaction.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Retro Action Movies | PlutoTVRetroActionMovies.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Romance | PlutoTVRomance.us@US | - | NO_GUIDE_HIT |
| United States | Pluto TV Sci-Fi (United States) | PlutoTVSciFi.us@US | - | NO_GUIDE_HIT |
| United States | Pluto TV Sci-Fi (United States) CA | PlutoTVSciFi.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Sci-Fi (United States) LatAm | PlutoTVSciFi.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Staff Picks | PlutoTVStaffPicks.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Terror | PlutoTVTerror.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Terror Trash | PlutoTVTerrorTrash.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Thrillers | PlutoTVThrillers.us@US | - | NO_GUIDE_HIT |
| United States | Pluto TV Trending Now | PlutoTVTrendingNow.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Westerns (United States) | PlutoTVWesterns.us@US | - | NO_GUIDE_HIT |
| United States | Pluto TV Westerns (United States) CA | PlutoTVWesterns.us@CA | - | NO_GUIDE_HIT |
| United States | Rawhide (United States) | Rawhide.us@SD | - | NO_GUIDE_HIT |
| United States | Rawhide (United States) CA | Rawhide.us@CA | - | NO_GUIDE_HIT |
| United States | RJTV | RJTV.us@SD | - | NO_GUIDE_HIT |
| United States | Runtime | Runtime.us@SD | - | NO_GUIDE_HIT |
| United States | Runtime Espanol | RuntimeEspanol.us@SD | - | NO_GUIDE_HIT |
| United States | Sony Canal Novelas | SonyCanalNovelas.us@SD | - | NO_GUIDE_HIT |
| United States | Sony Movies | sony.us | - | NO_GUIDE_HIT |
| United States | Sony Movies Latin America | SonyMoviesLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | Star Trek: Deep Space Nine | StarTrekDeepSpaceNine.us@SD | - | NO_GUIDE_HIT |
| United States | Star Trek: The Next Generation (United States) | StarTrekTheNextGeneration.us@SD | - | NO_GUIDE_HIT |
| United States | Star Trek: Voyager (United States) | StarTrekVoyager.us@SD | - | NO_GUIDE_HIT |
| United States | Starz Cinema | StarzCinema.us@East | - | NO_GUIDE_HIT |
| United States | Starz West | Starz.us@West | - | NO_GUIDE_HIT |
| United States | Stingray Greatest Holiday Hits | StingrayGreatestHolidayHits.us@SD | - | NO_GUIDE_HIT |
| United States | Stryk TV | StrykTV.us@HD | - | NO_GUIDE_HIT |
| United States | Summer of Movies | SummerofMovies.us@CA | - | NO_GUIDE_HIT |
| United States | TCM Latin America South | TCMLatinAmerica.us@South | - | NO_GUIDE_HIT |
| United States | TCM West [ ] | TCM.us@West | - | NO_GUIDE_HIT |
| United States | The Wild Wild West (United States) | TheWildWildWest.us@SD | - | NO_GUIDE_HIT |
| United States | TVS Classic Movies | TVSClassicMovies.us@SD | - | NO_GUIDE_HIT |
| United States | TVS Drive In Movie | TVSDriveInMovie.us@SD | - | NO_GUIDE_HIT |
| United States | TVS Film Noir Network | TVSFilmNoirNetwork.us@SD | - | NO_GUIDE_HIT |
| United States | TVS Music Network | TVSMusicNetwork.us@SD | - | NO_GUIDE_HIT |
| United States | TVS Nostalgia Movies | TVSNostalgiaMovies.us@SD | - | NO_GUIDE_HIT |
| United States | TVS Western Movie | TVSWesternMovie.us@SD | - | NO_GUIDE_HIT |
| United States | Universal Cinema | UniversalCinema.us@SD | - | NO_GUIDE_HIT |
| United States | Universal Comedy | UniversalComedy.us@SD | - | NO_GUIDE_HIT |
| United States | USA Network | USANetwork.us@East | - | NO_GUIDE_HIT |
| United States | Video Mix TV | VideoMixTV.us@SD | - | NO_GUIDE_HIT |
| United States | Watch it Scream! | WatchitScream.us@SD | - | NO_GUIDE_HIT |
| United States | Whiplash Cinema | WhiplashCinema.us | - | NO_GUIDE_HIT |
| United States | WVCU-LP | WVCULP.us@SD | - | NO_GUIDE_HIT |
| United States | Young Hollywood | YoungHollywood.us@SD | - | NO_GUIDE_HIT |
| Uzbekistan | BIZ Cinema | BIZCinema.uz@SD | - | NO_GUIDE_HIT |
| Uzbekistan | BIZ Music | BIZMusic.uz@SD | - | NO_GUIDE_HIT |
| Uzbekistan | FTV (Uzbekistan) | FTV.uz@SD | - | NO_GUIDE_HIT |
| Uzbekistan | Kinoteatr | Kinoteatr.uz@SD | - | NO_GUIDE_HIT |
| Uzbekistan | Muz TV Uzbekistan | MuzTVUzbekistan.uz@SD | - | NO_GUIDE_HIT |
| Vietnam | HTVC Movies | HTVCMovies.vn@SD | - | NO_GUIDE_HIT |
| Vietnam | ON Cine | ONCine.vn@SD | - | NO_GUIDE_HIT |
| Vietnam | ON Movies | ONMovies.vn@SD | - | NO_GUIDE_HIT |
| Vietnam | ON Music | ONMusic.vn@SD | - | NO_GUIDE_HIT |
| Vietnam | Vinh Long TV 3 | VinhLongTV3.vn@SD | - | NO_GUIDE_HIT |

## Published Guide Validation

- XMLTV channel IDs published: **1024**
- Active playlist IDs present in the published guide: **1024/2893 (35.4%)**
- Active playlist IDs with usable current/future programmes: **808/2893 (27.9%)**
- Active playlist IDs with usable programmes anywhere in the guide window (-6h/+7d): **813/2893 (28.1%)**
- Mapped playlist IDs present in the guide: **1024/1030 (99.4%)**
- Mapped playlist IDs with usable current/future programmes: **808/1030 (78.4%)**
- Mapped playlist IDs with usable programmes anywhere in the guide window: **813/1030 (78.9%)**
- Eligible programme rows published in the guide window: **100929**
- Mapped playlist IDs missing from the published XMLTV channel list: **6**
- Missing mapped playlist IDs: custom.24-7-xxx-metro, custom.24-7-xxx-reality-kings, custom.xxx-brazzers-europe, custom.xxx-ero-xxx, custom.xxx-hustler, custom.xxx-vivid-red
- Published mapped IDs without usable current/future programmes: **216**
- IDs without usable current/future programmes: 4SiDESTV.in@SD, 7XMusic.in@SD, ATNBanglaUK.uk, AXNMovies.es@SD, AaryaaTV.in, AaryaaTV.in@SD, AlQamarTV.ae, AlistiqamaTV.om, AmericanNinjaWarrior.us@SD, AnimalPlanet.cz@SD, ArenaSport1.sk@SD, ArenaSport2.sk@SD, AsharqDiscovery.sa@SD, AsharqDocumentary.sa@SD, AtfalMawahebTV.sa@SD, BBCDrama.uk, BSTV.pk@SD, BabyFirst.us@US, BanglaJagoTV.in, BravoKidsTV.hr@SD, CCTV9.cn@SD, CMT.us@East, Caillou.fr@SD, CampSpoopy.us@SD, ChinaTravel.cn@SD, CineFriki.es@SD, CineLatino.mx@SD, CineWestern.es@SD, CinemaxClassics.us@East, CinemaxHits.us@East, CrimeJustice.us, DMF.de@SD, DiscoveringChina.cn@SD, DiscoveryChannel.cz@SD, DisneyChannel.bg@SD, DisneyChannel.cz@SD, DisneyJr.us, DisneyJunior.cz@SD, DocumentaryPlus, DomkinoPremium.ru@HD, DuaChannel.sa, Dvojka.sk@SD, EKids.bg@SD, ESPNPremium.ar@HD, EkamraBharatOdia.in@SD, EkamraCinema.in, EkamraManoranjan.in, EkamraMusiq.in, EnterFilm.ua@SD, Enterr10 Bangla.in, EscapeTV.us, FILMBOXPlusComedy.pl@Poland, FILMBOXPlusEmotion.pl@Poland, FILMBOXPlusFestival.pl@SD, FILMBOXPlusHits.pl@Poland, FILMBOXPlusLoveCrime.pl@Czechia, FITE247.us@SD, FTFSports.us@SD, FalastiniTV.ps@SD, FashionOne.uk (and 156 more)

## Source / Published Schedule Reconciliation

- IDs with usable current/future source schedule data: **847/2893 (29.3%)**
- IDs with usable current/future schedules in published XMLTV at report time: **808/2893 (27.9%)**
- IDs with usable programmes in the published guide's common -6h/+7d window: **813/2893 (28.1%)**
- Current/future source IDs without any usable published programme in that common window: **43**
- Source-scheduled IDs without a usable published programme in the common window: 7X Music (`7XMusic.in@SD`), Aaryaa TV (`AaryaaTV.in`), Aaryaa TV (`AaryaaTV.in@SD`), American Ninja Warrior (`AmericanNinjaWarrior.us@SD`), BSTV (`BSTV.pk@SD`), Caillou (`Caillou.fr@SD`), Fast1 (`Fast1.in@SD`), Goldmines (`Goldmines.in@SD`), Goldmines Bollywood (`GoldminesBollywood.in@SD`), KTV Bangla (`KTVBangla.in@SD`), NTC TV (`NTCTV.in@SD`), Only Music (`Only.Music.in`), Qwest TV (`QwestTV.fr@SD`), Sangeet Marathi (`SangeetMarathi.in@SD`), Sonar Bangla (`SonarBangla.in@SD`), Spondon (`Spondon.in@SD`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray Easy Listening (`StingrayEasyListening.ca@SD`), Stingray Flashback 70's (`StingrayFlashback70s.ca@SD`), Stingray Hot Country (`StingrayHotCountry.ca@SD`), Stingray Jukebox Oldies (`StingrayJukeboxOldies.ca@SD`), Stingray Nothin' But 90s (`StingrayNothinBut90s.ca@SD`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray Romance Latino (`StingrayRomanceLatino.ca@SD`), Stingray Smooth Jazz (`StingraySmoothJazz.ca@SD`), Stingray The Spa (`StingrayTheSpa.ca`), Stingray The Spa (`StingrayTheSpa.ca@SD`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Stingray Today's K-Pop (`StingrayTodaysKPop.ca@SD`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca@SD`), Suriya TV (`SuriyaTV.in`), Suriya TV (`SuriyaTV.in@SD`), Teletubbies (`Teletubbies.uk@SD`), Ultimate TV (`UltimateTV.in@SD`), World Poker Tour (`WorldPokerTour.us@US`), Yu-Gi-Oh! (`YuGiOh.us@SD`), Metro (`custom.24-7-xxx-metro`), Reality Kings (`custom.24-7-xxx-reality-kings`), Brazzers Europe (`custom.xxx-brazzers-europe`), Ero Xxx (`custom.xxx-ero-xxx`), Hustler (`custom.xxx-hustler`), Vivid Red (`custom.xxx-vivid-red`)
- IDs with an in-window published programme but no current/future source match at the later scan: **9**
- In-window published IDs not counted source-current/future: CineLatino (`CineLatino.mx@SD`), Enter10 Bangla (`Enter10Bangla.in`), Escape TV (`EscapeTV.us`), Kalaignar Murasu (`KalaignarMurasu.in`), LoL TV (`LoLTV.in`), Odisha TV (`OdishaTV.in@SD`), PMC (`PMC.ae@SD`), Sarv Dharm Sangam (`SarvDharmSangam.in@SD`), Sony Entertainment TV (`SonyEntertainmentTelevision.in@SD`)
- Source-current/future IDs whose published programme is no longer current by report time: **43**
- Source-current/future IDs no longer current in the published guide: 7X Music (`7XMusic.in@SD`), Aaryaa TV (`AaryaaTV.in`), Aaryaa TV (`AaryaaTV.in@SD`), American Ninja Warrior (`AmericanNinjaWarrior.us@SD`), BSTV (`BSTV.pk@SD`), Caillou (`Caillou.fr@SD`), Fast1 (`Fast1.in@SD`), Goldmines (`Goldmines.in@SD`), Goldmines Bollywood (`GoldminesBollywood.in@SD`), KTV Bangla (`KTVBangla.in@SD`), NTC TV (`NTCTV.in@SD`), Only Music (`Only.Music.in`), Qwest TV (`QwestTV.fr@SD`), Sangeet Marathi (`SangeetMarathi.in@SD`), Sonar Bangla (`SonarBangla.in@SD`), Spondon (`Spondon.in@SD`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray Easy Listening (`StingrayEasyListening.ca@SD`), Stingray Flashback 70's (`StingrayFlashback70s.ca@SD`), Stingray Hot Country (`StingrayHotCountry.ca@SD`), Stingray Jukebox Oldies (`StingrayJukeboxOldies.ca@SD`), Stingray Nothin' But 90s (`StingrayNothinBut90s.ca@SD`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray Romance Latino (`StingrayRomanceLatino.ca@SD`), Stingray Smooth Jazz (`StingraySmoothJazz.ca@SD`), Stingray The Spa (`StingrayTheSpa.ca`), Stingray The Spa (`StingrayTheSpa.ca@SD`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Stingray Today's K-Pop (`StingrayTodaysKPop.ca@SD`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca@SD`), Suriya TV (`SuriyaTV.in`), Suriya TV (`SuriyaTV.in@SD`), Teletubbies (`Teletubbies.uk@SD`), Ultimate TV (`UltimateTV.in@SD`), World Poker Tour (`WorldPokerTour.us@US`), Yu-Gi-Oh! (`YuGiOh.us@SD`), Metro (`custom.24-7-xxx-metro`), Reality Kings (`custom.24-7-xxx-reality-kings`), Brazzers Europe (`custom.xxx-brazzers-europe`), Ero Xxx (`custom.xxx-ero-xxx`), Hustler (`custom.xxx-hustler`), Vivid Red (`custom.xxx-vivid-red`)
- Published current/future IDs not counted source-current/future: **4**
- Published current/future IDs not counted source-current/future: Enter10 Bangla (`Enter10Bangla.in`), Kalaignar Murasu (`KalaignarMurasu.in`), Odisha TV (`OdishaTV.in@SD`), Sony Entertainment TV (`SonyEntertainmentTelevision.in@SD`)


## Playlist EPG Headers

| Playlist | Header status |
|---|---|
| IPTV-Playlist.m3u | OK |
| BDIX-Playlist.m3u | OK |
| International-Playlist.m3u | OK |

## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **c2b21ff27a19db661d00c7ee96c9a884bbb4052f5541d1f1d110ceabb619790f**
- BDIX-Playlist.m3u SHA-256: **6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d**
- International-Playlist.m3u SHA-256: **359731d46ab6910e71335940aacfdeb1321d84c824fea6e120575031d128eff3**

