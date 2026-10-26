# EPG Coverage & Mapping Report

Generated: **2026-10-26T06:42:01+00:00**

This report audits active unique channel identities across the three maintained playlists configured in the automated EPG pipeline. A source mapping is not counted as usable current/future coverage unless it has a valid programme interval and valid non-empty multilingual title data within the generator's -6-hour/+7-day window; English titles rank first, then Bengali, then other valid languages.
The XMLTV guide is published at **epg/epg.xml**. The published guide uses the playlist's tvg-id as the XMLTV channel ID, not the upstream provider's source ID.

## Overall Coverage

- Active unique playlist channel IDs audited: **1878**
- IDs with an EPG source mapping: **678/1878 (36.1%)**
- IDs with usable current/future source schedules (nonblank multilingual titles (English preferred, then Bengali, then other valid languages)): **633/1878 (33.7%)**
- IDs with no EPG source mapping: **1200**

## Coverage by Playlist Group

| Group | Active IDs | Mapped IDs | Current/future | No mapping |
|---|---:|---:|---:|---:|
| Adult | 482 | 40 | 33 | 442 |
| Argentina | 13 | 0 | 0 | 13 |
| Backups | 24 | 16 | 16 | 8 |
| Bangladesh | 77 | 3 | 3 | 74 |
| Brazil | 5 | 0 | 0 | 5 |
| Canada | 2 | 2 | 2 | 0 |
| China | 10 | 0 | 0 | 10 |
| Documentary & Wildlife | 106 | 86 | 83 | 20 |
| France | 6 | 1 | 1 | 5 |
| Germany | 20 | 1 | 1 | 19 |
| Indian Bangla | 50 | 40 | 37 | 10 |
| Indian Entertainment | 224 | 179 | 166 | 45 |
| Indian Movies | 93 | 66 | 59 | 27 |
| Indian Music | 61 | 49 | 46 | 12 |
| International | 98 | 56 | 52 | 42 |
| International Movies | 165 | 14 | 14 | 151 |
| International Music | 90 | 5 | 5 | 85 |
| Kids | 51 | 33 | 32 | 18 |
| Pakistani | 41 | 6 | 6 | 35 |
| Poland | 5 | 1 | 1 | 4 |
| Religious | 32 | 10 | 9 | 22 |
| Romania | 5 | 3 | 3 | 2 |
| Russia | 10 | 0 | 0 | 10 |
| Spain | 5 | 2 | 1 | 3 |
| Sports | 38 | 29 | 27 | 9 |
| Sweden | 34 | 0 | 0 | 34 |
| United Kingdom | 13 | 4 | 4 | 9 |
| United States | 118 | 32 | 32 | 86 |

## Source Status

- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz — 1166 channel IDs; 713 IDs with usable current/future programmes; 96308 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz — 54 channel IDs; 11 IDs with usable current/future programmes; 101 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz — 557 channel IDs; 21 IDs with usable current/future programmes; 1991 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-in.xml.gz — 419 channel IDs; 419 IDs with usable current/future programmes; 17656 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/in.xml — 206 channel IDs; 202 IDs with usable current/future programmes; 2141 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/us.xml — 588 channel IDs; 587 IDs with usable current/future programmes; 4997 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epg.pw/xmltv/epg_IN.xml — 498 channel IDs; 21 IDs with usable current/future programmes; 2113 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epg.pw/api/epg.xml?channel_id=9374 — 1 channel IDs; 1 IDs with usable current/future programmes; 88 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epg.pw/api/epg.xml?channel_id=12504 — 1 channel IDs; 1 IDs with usable current/future programmes; 76 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml — 692 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **FAILED** — https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 403: Forbidden
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml — 763 channel IDs; 760 IDs with usable current/future programmes; 80773 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml — 1490 channel IDs; 1350 IDs with usable current/future programmes; 79606 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml — 282 channel IDs; 282 IDs with usable current/future programmes; 5232 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml — 119 channel IDs; 106 IDs with usable current/future programmes; 24034 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/epg.xml.gz — 2273 channel IDs; 898 IDs with usable current/future programmes; 23625 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/jioepg.xml.gz — 1226 channel IDs; 116 IDs with usable current/future programmes; 3506 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/tsepg.xml.gz — 717 channel IDs; 715 IDs with usable current/future programmes; 37978 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DISTROTV1.xml.gz — 90 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz — 690 channel IDs; 684 IDs with usable current/future programmes; 76268 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_RAKUTEN1.xml.gz — 1640 channel IDs; 1510 IDs with usable current/future programmes; 143722 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/nasimali/epg-auto/release/main-epg/epg_data/merged_epg.xml — 11 channel IDs; 10 IDs with usable current/future programmes; 1559 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz — 486 channel IDs; 387 IDs with usable current/future programmes; 32310 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.open-epg.com/files/unitedkingdom.xml.gz — 562 channel IDs; 529 IDs with usable current/future programmes; 24363 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz — 769 channel IDs; 754 IDs with usable current/future programmes; 63909 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-us.xml.gz — 13031 channel IDs; 13004 IDs with usable current/future programmes; 865920 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz — 912 channel IDs; 836 IDs with usable current/future programmes; 74238 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz — 345 channel IDs; 277 IDs with usable current/future programmes; 37184 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz — 696 channel IDs; 695 IDs with usable current/future programmes; 60752 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CH1.xml.gz — 751 channel IDs; 729 IDs with usable current/future programmes; 67286 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CZ1.xml.gz — 1087 channel IDs; 502 IDs with usable current/future programmes; 43058 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DE1.xml.gz — 266 channel IDs; 251 IDs with usable current/future programmes; 22209 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DO1.xml.gz — 56 channel IDs; 55 IDs with usable current/future programmes; 3719 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_ES1.xml.gz — 373 channel IDs; 339 IDs with usable current/future programmes; 17067 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_FR1.xml.gz — 574 channel IDs; 529 IDs with usable current/future programmes; 57561 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_GR1.xml.gz — 321 channel IDs; 306 IDs with usable current/future programmes; 21897 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz — 143 channel IDs; 133 IDs with usable current/future programmes; 10739 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HU1.xml.gz — 193 channel IDs; 167 IDs with usable current/future programmes; 16759 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IT1.xml.gz — 195 channel IDs; 155 IDs with usable current/future programmes; 15787 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz — 163 channel IDs; 131 IDs with usable current/future programmes; 10488 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MX1.xml.gz — 178 channel IDs; 167 IDs with usable current/future programmes; 13629 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_NL1.xml.gz — 159 channel IDs; 156 IDs with usable current/future programmes; 23213 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_PL1.xml.gz — 636 channel IDs; 585 IDs with usable current/future programmes; 89876 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_RO1.xml.gz — 370 channel IDs; 353 IDs with usable current/future programmes; 36782 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_SA2.xml.gz — 31 channel IDs; 30 IDs with usable current/future programmes; 3370 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_TR1.xml.gz — 178 channel IDs; 139 IDs with usable current/future programmes; 13560 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BEIN1.xml.gz — 80 channel IDs; 72 IDs with usable current/future programmes; 2184 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR1.xml.gz — 266 channel IDs; 97 IDs with usable current/future programmes; 12710 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR2.xml.gz — 97 channel IDs; 92 IDs with usable current/future programmes; 8840 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://hum.tv/schedule/ — 1 channel IDs; 1 IDs with usable current/future programmes; 21 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — M3U4U XMLTV (private Actions secret) — 201 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window

## Channels Requiring Attention

The table includes every active channel identity without usable current/future guide data, not only Indian channels. NO_GUIDE_HIT means no configured source could be matched; MAPPED_ID_ONLY means an identity was found but no usable schedule was available; MAPPED_NOT_CURRENTLY_FOUND means a retained mapping was not found in the currently configured feeds.

| Group | Channel | Playlist ID | EPG source ID | Status |
|---|---|---|---|---|
| Adult | 7 | custom.24-7-xxx-7 | Channel.7.uk | MAPPED_ID_ONLY |
| Adult | Babes TV | BabesTV.us | Babes.TV.cz | MAPPED_ID_ONLY |
| Adult | Babes Tv | custom.xxx-babes-tv | Babes.TV.cz | MAPPED_ID_ONLY |
| Adult | Dusk | custom.xxx-dusk | Dusk!.cz | MAPPED_ID_ONLY |
| Adult | LEO TV | LEOTV.cz | Leo.cz | MAPPED_ID_ONLY |
| Adult | Pure Babes | PureBabes.us | Pure.Babes.cz | MAPPED_ID_ONLY |
| Adult | True Amateurs | custom.xxx-true-amateurs | True.Amateurs.cz | MAPPED_ID_ONLY |
| Adult | 11 | custom.24-7-xxx-adult-11 | - | NO_GUIDE_HIT |
| Adult | 12 | custom.24-7-xxx-adult-12 | - | NO_GUIDE_HIT |
| Adult | 14 | custom.24-7-xxx-adult-14 | - | NO_GUIDE_HIT |
| Adult | 15 | custom.24-7-xxx-adult-15 | - | NO_GUIDE_HIT |
| Adult | 16 | custom.24-7-xxx-adult-16 | - | NO_GUIDE_HIT |
| Adult | 17 | custom.24-7-xxx-adult-17 | - | NO_GUIDE_HIT |
| Adult | 18 | custom.24-7-xxx-adult-18 | - | NO_GUIDE_HIT |
| Adult | 19 | custom.24-7-xxx-adult-19 | - | NO_GUIDE_HIT |
| Adult | 21 | custom.24-7-xxx-adult-21 | - | NO_GUIDE_HIT |
| Adult | 21 Sextury | custom.xxx-21-sextury | - | NO_GUIDE_HIT |
| Adult | 22 | custom.24-7-xxx-adult-22 | - | NO_GUIDE_HIT |
| Adult | 23 | custom.24-7-xxx-adult-23 | - | NO_GUIDE_HIT |
| Adult | 25 | custom.24-7-adult-xxx-25 | - | NO_GUIDE_HIT |
| Adult | 26 | custom.24-7-xxx-adult-26 | - | NO_GUIDE_HIT |
| Adult | 27 | custom.24-7-xxx-adult-27 | - | NO_GUIDE_HIT |
| Adult | 28 | custom.24-7-xxx-adult-28 | - | NO_GUIDE_HIT |
| Adult | 29 | custom.24-7-adult-xxx-29 | - | NO_GUIDE_HIT |
| Adult | 31 | custom.24-7-adult-xxx-31 | - | NO_GUIDE_HIT |
| Adult | 32 | custom.24-7-adult-xxx-32 | - | NO_GUIDE_HIT |
| Adult | 9 | custom.24-7-xxx-9 | - | NO_GUIDE_HIT |
| Adult | Abella Danger | custom.24-7-xxx-abella-danger | - | NO_GUIDE_HIT |
| Adult | AJ Applegate | custom.24-7-xxx-aj-applegate | - | NO_GUIDE_HIT |
| Adult | Alba 2 | custom.alba-2 | - | NO_GUIDE_HIT |
| Adult | Alba 3 | custom.alba-3 | - | NO_GUIDE_HIT |
| Adult | Alba 4 | custom.alba-4 | - | NO_GUIDE_HIT |
| Adult | Alba Xxx 1 | custom.xxx-alba-xxx-1 | - | NO_GUIDE_HIT |
| Adult | Alba Xxx 2 | custom.xxx-alba-xxx-2 | - | NO_GUIDE_HIT |
| Adult | Alba Xxx 3 | custom.xxx-alba-xxx-3 | - | NO_GUIDE_HIT |
| Adult | Alba Xxx 4 | custom.xxx-alba-xxx-4 | - | NO_GUIDE_HIT |
| Adult | Alba Xxx 5 | custom.xxx-alba-xxx-5 | - | NO_GUIDE_HIT |
| Adult | Alba Xxx 6 | custom.xxx-alba-xxx-6 | - | NO_GUIDE_HIT |
| Adult | Alba Xxx Hd1 | custom.xxx-alba-xxx-hd1 | - | NO_GUIDE_HIT |
| Adult | Alba Xxx Hd2 | custom.xxx-alba-xxx-hd2 | - | NO_GUIDE_HIT |
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
| Adult | Babes TV Russia | custom.babes-tv-russia | - | NO_GUIDE_HIT |
| Adult | Bang Bus | custom.xxx-bang-bus | - | NO_GUIDE_HIT |
| Adult | Bangbros | custom.xxx-bangbros | - | NO_GUIDE_HIT |
| Adult | Bangbus | custom.24-7-xxx-bangbus | - | NO_GUIDE_HIT |
| Adult | BBC Big Ass | custom.24-7-xxx-bbc-big-ass | - | NO_GUIDE_HIT |
| Adult | BBW | custom.24-7-xxx-bbw | - | NO_GUIDE_HIT |
| Adult | BDSM | custom.24-7-xxx-bdsm | - | NO_GUIDE_HIT |
| Adult | Big Ass | custom.24-7-xxx-big-ass | - | NO_GUIDE_HIT |
| Adult | Big Ass | custom.xxx-big-ass | - | NO_GUIDE_HIT |
| Adult | Big Dick | custom.xxx-big-dick | - | NO_GUIDE_HIT |
| Adult | Big Tits | custom.24-7-xxx-big-tits | - | NO_GUIDE_HIT |
| Adult | Big Tits | custom.xxx-big-tits | - | NO_GUIDE_HIT |
| Adult | Blacked | custom.xxx-blacked | - | NO_GUIDE_HIT |
| Adult | Blonde | custom.blonde | - | NO_GUIDE_HIT |
| Adult | Blonde | custom.xxx-blonde | - | NO_GUIDE_HIT |
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
| Adult | Brunette | custom.xxx-brunette | - | NO_GUIDE_HIT |
| Adult | Casting Couch | custom.24-7-xxx-casting-couch | - | NO_GUIDE_HIT |
| Adult | Cathy Heaven | custom.24-7-xxx-cathy-heaven | - | NO_GUIDE_HIT |
| Adult | Cento X Cento Tv | custom.xxx-cento-x-cento-tv | - | NO_GUIDE_HIT |
| Adult | Cherie Deville | custom.24-7-xxx-cherie-deville | - | NO_GUIDE_HIT |
| Adult | Compilation | custom.xxx-compilation | - | NO_GUIDE_HIT |
| Adult | Cuckold | custom.cuckold | - | NO_GUIDE_HIT |
| Adult | Cuckold | custom.xxx-cuckold | - | NO_GUIDE_HIT |
| Adult | Cum 4K UHD | custom.xxx-cum-4k-uhd | - | NO_GUIDE_HIT |
| Adult | Cum Perfection | custom.xxx-cum-perfection | - | NO_GUIDE_HIT |
| Adult | Daughter Swap | custom.xxx-daughter-swap | - | NO_GUIDE_HIT |
| Adult | Day With A Pornstar | custom.xxx-day-with-a-pornstar | - | NO_GUIDE_HIT |
| Adult | Ddf Network | custom.xxx-ddf-network | - | NO_GUIDE_HIT |
| Adult | Dee Williams | custom.24-7-xxx-dee-williams | - | NO_GUIDE_HIT |
| Adult | Dick Drainers | custom.24-7-xxx-dick-drainers | - | NO_GUIDE_HIT |
| Adult | Dorcel Club | custom.xxx-dorcel-club | - | NO_GUIDE_HIT |
| Adult | Ebony | custom.24-7-xxx-ebony | - | NO_GUIDE_HIT |
| Adult | Elsa Jean | custom.24-7-xxx-elsa-jean | - | NO_GUIDE_HIT |
| Adult | Ember Snow | custom.24-7-xxx-ember-snow | - | NO_GUIDE_HIT |
| Adult | Erox XXX HD | custom.xxx-erox-xxx-hd | - | NO_GUIDE_HIT |
| Adult | Euro Girls On Girls | custom.xxx-euro-girls-on-girls | - | NO_GUIDE_HIT |
| Adult | Evil Angel | custom.24-7-xxx-evil-angel | - | NO_GUIDE_HIT |
| Adult | Evil Angel | custom.evil-angel | - | NO_GUIDE_HIT |
| Adult | Evil Angel HD | custom.xxx-evil-angel-hd | - | NO_GUIDE_HIT |
| Adult | Evolved Fights | custom.xxx-evolved-fights | - | NO_GUIDE_HIT |
| Adult | Extasy - Leo Tv | custom.xxx-extasy-leo-tv | - | NO_GUIDE_HIT |
| Adult | Exxxotica TV | custom.exxxotica-tv | - | NO_GUIDE_HIT |
| Adult | Exxxotica Tv | custom.xxx-exxxotica-tv | - | NO_GUIDE_HIT |
| Adult | Fake Agent | custom.xxx-fake-agent | - | NO_GUIDE_HIT |
| Adult | Fake Taxi | custom.xxx-fake-taxi | - | NO_GUIDE_HIT |
| Adult | Fake Taxi 1 | custom.24-7-xxx-fake-taxi-1 | - | NO_GUIDE_HIT |
| Adult | Fake Taxi 2 | custom.24-7-xxx-fake-taxi-2 | - | NO_GUIDE_HIT |
| Adult | Fake Taxi 3 | custom.24-7-xxx-fake-taxi-3 | - | NO_GUIDE_HIT |
| Adult | Family Hookups | custom.xxx-family-hookups | - | NO_GUIDE_HIT |
| Adult | Family Strokes | custom.xxx-family-strokes | - | NO_GUIDE_HIT |
| Adult | Fap TV 6 | custom.fap-tv-6 | - | NO_GUIDE_HIT |
| Adult | Fetish | custom.xxx-fetish | - | NO_GUIDE_HIT |
| Adult | FM Therapy 1 | custom.24-7-xxx-fm-therapy-1 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 2 | custom.24-7-xxx-fm-therapy-2 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 3 | custom.24-7-xxx-fm-therapy-3 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 4 | custom.24-7-xxx-fm-therapy-4 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 5 | custom.24-7-xxx-fm-therapy-5 | - | NO_GUIDE_HIT |
| Adult | French Lover Europe | custom.xxx-french-lover-europe | - | NO_GUIDE_HIT |
| Adult | Gangbang | custom.xxx-gangbang | - | NO_GUIDE_HIT |
| Adult | Gay 2 | custom.24-7-xxx-gay-2 | - | NO_GUIDE_HIT |
| Adult | Gay 3 | custom.24-7-xxx-gay-3 | - | NO_GUIDE_HIT |
| Adult | Gay Adult Tv | custom.xxx-gay-adult-tv | - | NO_GUIDE_HIT |
| Adult | Gay Latin | custom.24-7-xxx-gay-latin | - | NO_GUIDE_HIT |
| Adult | Glory Hole | custom.xxx-glory-hole | - | NO_GUIDE_HIT |
| Adult | Gloryhole | custom.24-7-xxx-gloryhole | - | NO_GUIDE_HIT |
| Adult | Group | custom.24-7-xxx-group | - | NO_GUIDE_HIT |
| Adult | Group 2 | custom.24-7-xxx-group-2 | - | NO_GUIDE_HIT |
| Adult | Hardcore | custom.24-7-xxx-hardcore | - | NO_GUIDE_HIT |
| Adult | Hardcore | custom.xxx-hardcore | - | NO_GUIDE_HIT |
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
| Adult | Little Caprice | custom.xxx-little-caprice | - | NO_GUIDE_HIT |
| Adult | Live Cams | custom.live-cams | - | NO_GUIDE_HIT |
| Adult | Live Cams | custom.xxx-live-cams | - | NO_GUIDE_HIT |
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
| Adult | Mctv Anal | custom.xxx-mctv-anal | - | NO_GUIDE_HIT |
| Adult | Mctv Big Dick | custom.xxx-mctv-big-dick | - | NO_GUIDE_HIT |
| Adult | Mctv Big Tits | custom.xxx-mctv-big-tits | - | NO_GUIDE_HIT |
| Adult | Mctv Blonde | custom.xxx-mctv-blonde | - | NO_GUIDE_HIT |
| Adult | Mctv Blowjob | custom.xxx-mctv-blowjob | - | NO_GUIDE_HIT |
| Adult | Mctv Brunette | custom.xxx-mctv-brunette | - | NO_GUIDE_HIT |
| Adult | Mctv Compilation | custom.xxx-mctv-compilation | - | NO_GUIDE_HIT |
| Adult | Mctv Cuckold | custom.xxx-mctv-cuckold | - | NO_GUIDE_HIT |
| Adult | Mctv Fetish | custom.xxx-mctv-fetish | - | NO_GUIDE_HIT |
| Adult | Mctv Gangbang | custom.xxx-mctv-gangbang | - | NO_GUIDE_HIT |
| Adult | Mctv Gay | custom.xxx-mctv-gay | - | NO_GUIDE_HIT |
| Adult | Mctv Hardcore | custom.xxx-mctv-hardcore | - | NO_GUIDE_HIT |
| Adult | Mctv Milf | custom.xxx-mctv-milf | - | NO_GUIDE_HIT |
| Adult | Mctv Pornstar | custom.xxx-mctv-pornstar | - | NO_GUIDE_HIT |
| Adult | Mctv Rough | custom.xxx-mctv-rough | - | NO_GUIDE_HIT |
| Adult | Mctv Russian | custom.xxx-mctv-russian | - | NO_GUIDE_HIT |
| Adult | Mctv Threesome | custom.xxx-mctv-threesome | - | NO_GUIDE_HIT |
| Adult | Mctv Woman | custom.xxx-mctv-woman | - | NO_GUIDE_HIT |
| Adult | Mia Khalifa | custom.24-7-xxx-mia-khalifa | - | NO_GUIDE_HIT |
| Adult | Mia Khalifa | custom.xxx-mia-khalifa | - | NO_GUIDE_HIT |
| Adult | Miami Tv Jenny Live [Not 24/7] | custom.xxx-miami-tv-jenny-live-not-24-7 | - | NO_GUIDE_HIT |
| Adult | Milf | custom.adultm3u-com-milf | - | NO_GUIDE_HIT |
| Adult | Milf | custom.xxx-milf | - | NO_GUIDE_HIT |
| Adult | Milfs | custom.24-7-xxx-milfs | - | NO_GUIDE_HIT |
| Adult | Milfs Stepmom | custom.24-7-xxx-milfs-stepmom | - | NO_GUIDE_HIT |
| Adult | Mom Lovers | custom.24-7-xxx-mom-lovers | - | NO_GUIDE_HIT |
| Adult | My Daughter's Hot Friend | custom.xxx-my-daughter-s-hot-friend | - | NO_GUIDE_HIT |
| Adult | My Dirty Maid | custom.24-7-xxx-my-dirty-maid | - | NO_GUIDE_HIT |
| Adult | My FIrst Sex Teacher | custom.24-7-xxx-my-first-sex-teacher | - | NO_GUIDE_HIT |
| Adult | My Friends Hot Mom | custom.24-7-xxx-my-friends-hot-mom | - | NO_GUIDE_HIT |
| Adult | My Pervy Family | custom.xxx-my-pervy-family | - | NO_GUIDE_HIT |
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
| Adult | Penthouse Passion | custom.xxx-penthouse-passion | - | NO_GUIDE_HIT |
| Adult | Penthouse Quickies | custom.xxx-penthouse-quickies | - | NO_GUIDE_HIT |
| Adult | Penthouse Reality TV | PenthouseRealityTV.us | - | NO_GUIDE_HIT |
| Adult | Penthouse TV | custom.penthouse-tv | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 1 | custom.pink-erotic-1 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 1 | custom.xxx-pink-erotic-1 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 2 | custom.pink-erotic-2 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 2 | custom.xxx-pink-erotic-2 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 3 | custom.pink-erotic-3 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 3 | custom.xxx-pink-erotic-3 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 4 | custom.xxx-pink-erotic-4 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 5 | custom.pink-erotic-5 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 5 | custom.xxx-pink-erotic-5 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 6 | custom.xxx-pink-erotic-6 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 7 | custom.pink-erotic-7 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 7 | custom.xxx-pink-erotic-7 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 8 | custom.pink-erotic-8 | - | NO_GUIDE_HIT |
| Adult | Pink Erotic 8 | custom.xxx-pink-erotic-8 | - | NO_GUIDE_HIT |
| Adult | Pink O Tv | custom.xxx-pink-o-tv | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: BAEB | custom.pornbox-4k-baeb | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: BBC PIE | custom.pornbox-4k-bbc-pie | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: CUM 4K | custom.pornbox-4k-cum-4k | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: GIRL CUM | custom.pornbox-4k-girl-cum | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: JAYS POV | custom.pornbox-4k-jays-pov | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: LUBED PORN | custom.pornbox-4k-lubed-porn | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: NANNY SPY | custom.pornbox-4k-nanny-spy | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: SPANK MONSTER | custom.pornbox-4k-spank-monster | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: SPY FAM | custom.pornbox-4k-spy-fam | - | NO_GUIDE_HIT |
| Adult | PORNBOX 4K: TINY 4K | custom.pornbox-4k-tiny-4k | - | NO_GUIDE_HIT |
| Adult | PORNBOX GAY: BEEFCAKE HUNTER | custom.pornbox-gay-beefcake-hunter | - | NO_GUIDE_HIT |
| Adult | PORNBOX GAY: BOY FUN | custom.pornbox-gay-boy-fun | - | NO_GUIDE_HIT |
| Adult | PORNBOX GAY: MAN | custom.pornbox-gay-man | - | NO_GUIDE_HIT |
| Adult | PORNBOX: 1111 CUSTOMS | custom.pornbox-1111-customs | - | NO_GUIDE_HIT |
| Adult | PORNBOX: A GIRL KNOWS | custom.pornbox-a-girl-knows | - | NO_GUIDE_HIT |
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
| Adult | POV | custom.xxx-pov | - | NO_GUIDE_HIT |
| Adult | Princess Cum | custom.xxx-princess-cum | - | NO_GUIDE_HIT |
| Adult | Public Agent | custom.xxx-public-agent | - | NO_GUIDE_HIT |
| Adult | Pure Taboo | custom.24-7-xxx-pure-taboo | - | NO_GUIDE_HIT |
| Adult | Puretaboo | custom.xxx-puretaboo | - | NO_GUIDE_HIT |
| Adult | Rated | custom.24-7-xxx-rated | - | NO_GUIDE_HIT |
| Adult | Rated 3 | custom.24-7-xxx-rated-3 | - | NO_GUIDE_HIT |
| Adult | Real Wife Stories | custom.xxx-real-wife-stories | - | NO_GUIDE_HIT |
| Adult | Riley Reid | custom.24-7-xxx-riley-reid | - | NO_GUIDE_HIT |
| Adult | Rouge Tv | custom.xxx-rouge-tv | - | NO_GUIDE_HIT |
| Adult | Rough | custom.xxx-rough | - | NO_GUIDE_HIT |
| Adult | Russian | custom.xxx-russian | - | NO_GUIDE_HIT |
| Adult | Russian Night | custom.xxx-russian-night | - | NO_GUIDE_HIT |
| Adult | Sexto Senso | custom.xxx-sexto-senso | - | NO_GUIDE_HIT |
| Adult | Sexto Sento | custom.xxx-sexto-sento | - | NO_GUIDE_HIT |
| Adult | Sextreme | custom.xxx-sextreme | - | NO_GUIDE_HIT |
| Adult | Sexy Hot | custom.xxx-sexy-hot | - | NO_GUIDE_HIT |
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
| Adult | Taboo | custom.xxx-taboo | - | NO_GUIDE_HIT |
| Adult | Teen Red TV | custom.xxx-teen-red-tv | - | NO_GUIDE_HIT |
| Adult | Threesome | custom.xxx-threesome | - | NO_GUIDE_HIT |
| Adult | Tiny 4k | custom.xxx-tiny-4k | - | NO_GUIDE_HIT |
| Adult | Trans | custom.24-7-xxx-trans | - | NO_GUIDE_HIT |
| Adult | True Anal | custom.24-7-xxx-true-anal | - | NO_GUIDE_HIT |
| Adult | True Anal | custom.xxx-true-anal | - | NO_GUIDE_HIT |
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
| Adult | XXL | custom.xxx-xxl | - | NO_GUIDE_HIT |
| Adult | Xy Max | custom.xxx-xy-max | - | NO_GUIDE_HIT |
| Adult | XY Mix | custom.xxx-xy-mix | - | NO_GUIDE_HIT |
| Adult | XY Plus | custom.xxx-xy-plus | - | NO_GUIDE_HIT |
| Argentina | Disney Channel Latin America (1080p) | DisneyChannelLatinAmerica.ar@Panregional | - | NO_GUIDE_HIT |
| Argentina | Disney Channel Latin America Center (1080p) | DisneyChannelLatinAmerica.ar@Center | - | NO_GUIDE_HIT |
| Argentina | Disney Channel Latin America Mexico (720p) | DisneyChannelLatinAmerica.ar@Mexico | - | NO_GUIDE_HIT |
| Argentina | Disney Channel Latin America North (576p) | DisneyChannelLatinAmerica.ar@North | - | NO_GUIDE_HIT |
| Argentina | Disney Channel Latin America Panregional HD (1080p) | DisneyChannelLatinAmerica.ar@PanregionalHD | - | NO_GUIDE_HIT |
| Argentina | Disney Channel Latin America South | DisneyChannelLatinAmerica.ar@South | - | NO_GUIDE_HIT |
| Argentina | Disney Jr. Latin America (1080p) | DisneyJrLatinAmerica.ar@North | - | NO_GUIDE_HIT |
| Argentina | Disney Jr. Latin America North HD (1080p) | DisneyJrLatinAmerica.ar@NorthHD | - | NO_GUIDE_HIT |
| Argentina | Disney Jr. Latin America South (1080p) | DisneyJrLatinAmerica.ar@South | - | NO_GUIDE_HIT |
| Argentina | Garage TV Latin America | GarageTVLatinAmerica.ar@SD | - | NO_GUIDE_HIT |
| Argentina | LAMIL35 TV (720p) | LAMIL35TV.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Plim Plim (1080p) | PlimPlim.ar@SD | - | NO_GUIDE_HIT |
| Argentina | Xtrema Cartoons | XtremaCartoons.ar@SD | - | NO_GUIDE_HIT |
| Backups | Asian Sony Max 2 | custom.asian-sony-max-2 | - | NO_GUIDE_HIT |
| Backups | Nick Jr East | custom.nick-jr-east | - | NO_GUIDE_HIT |
| Backups | Peace TV | custom.peace-tv-tw8cm | - | NO_GUIDE_HIT |
| Backups | Quran | custom.quran-brqze | - | NO_GUIDE_HIT |
| Backups | Quran | custom.quran-w3y9b | - | NO_GUIDE_HIT |
| Backups | Sananda TV | custom.sananda-tv-16g2i | - | NO_GUIDE_HIT |
| Backups | Tiny 4K UHD | custom.xxx-tiny-4k-uhd | - | NO_GUIDE_HIT |
| Backups | Музыка 1 International | Kino1International.ru | - | NO_GUIDE_HIT |
| Bangladesh | Ananda TV | AnandaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ananda TV (480p) | AnandaTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | Asian TV | AsianTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | ATN Bangla | ATNBangla.bd | - | NO_GUIDE_HIT |
| Bangladesh | ATN Music (360p) | ATNMusic.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | ATN News | ATNNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bangla TV | BanglaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bangla Vision | BanglaVision.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bengali Beats | BengaliBeats.bd | - | NO_GUIDE_HIT |
| Bangladesh | Bijoy TV | BijoyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | BOISHAKHAI TV HD | custom.bdix.boishakhai | - | NO_GUIDE_HIT |
| Bangladesh | Boishakhi TV | BoishakhiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV Chattogram | BTVChattogram.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV CTG | custom.bdix.btvctg | - | NO_GUIDE_HIT |
| Bangladesh | BTV National | BTVNational.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV News | BTVNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | BTV News | custom.btv.news | - | NO_GUIDE_HIT |
| Bangladesh | Channel 1 | Channel1.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 1 | custom.channel.1 | - | NO_GUIDE_HIT |
| Bangladesh | Channel 16 | Channel16.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 24 | Channel24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 52 | Channel52.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel 9 | Channel9.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel I | ChannelI.bd | - | NO_GUIDE_HIT |
| Bangladesh | Channel S | ChannelS.uk | - | NO_GUIDE_HIT |
| Bangladesh | Channel S (Bangladesh) | ChannelS.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | DBC News | DBCNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Deepto TV | DeeptoTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Desh TV | DeshTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Deshe Bideshe | DesheBideshe.ca | - | NO_GUIDE_HIT |
| Bangladesh | Deshi TV | DeshiTV.ca@SD | - | NO_GUIDE_HIT |
| Bangladesh | Doyel TV | DoyelTV.ca@SD | - | NO_GUIDE_HIT |
| Bangladesh | Duronto TV | DurontoTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekattor TV | EkattorTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekhon TV | EkhonTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Ekushey TV | EkusheyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Enter TV | EnterTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | G Series Drama | GSeriesDrama.bd | - | NO_GUIDE_HIT |
| Bangladesh | G TV | GaziTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | GAZI TV HD | custom.bdix.gazi | - | NO_GUIDE_HIT |
| Bangladesh | Global TV | GlobalTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Green TV | GreenTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Green TV (1080p) | GreenTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | Independent TV | IndependentTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jago News 24 | JagoNews24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jalsha Bangla BD | JalshaBanglaBD.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jamuna TV | JamunaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jonmobhumi TV | JonmobhumiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Maasranga TV | MaasrangaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Matribhumi TV | MatribhumiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | ME TV | METV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Mohona TV | MohonaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Movie Bangla | MovieBangla.bd | - | NO_GUIDE_HIT |
| Bangladesh | Movie Bangla | MovieBangla.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | My TV | MyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Nagorik TV | NagorikTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | News 21 | News21BanglaTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | News 24 | News24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Nexus TV | NexusTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | NRB TV | NRBTV.ca | - | NO_GUIDE_HIT |
| Bangladesh | NTV | NTV-IN | - | NO_GUIDE_HIT |
| Bangladesh | NTV | NTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Rajdhani TV | RajdhaniTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | RTV | RTV.bd | - | NO_GUIDE_HIT |
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
| Brazil | AWTV (1080p) [Geo-blocked] | AWTV.br@HD | - | NO_GUIDE_HIT |
| Brazil | Geekdot (720p) | Geekdot.br@SD | - | NO_GUIDE_HIT |
| Brazil | Laboral TV (360p) | LaboralTV.br@SD | - | NO_GUIDE_HIT |
| Brazil | NickOnline Bob Esponja (720p) [Not 24/7] | NickOnlineBobEsponja.br@HD | - | NO_GUIDE_HIT |
| Brazil | NickOnline HD (720p) | NickOnline.br@HD | - | NO_GUIDE_HIT |
| China | CCTV-11 | CCTV11.cn | - | NO_GUIDE_HIT |
| China | CCTV-2 (720p) | CCTV2.cn@SD | - | NO_GUIDE_HIT |
| China | CGTN Global Biz (1080p) | CGTNGlobalBiz.cn@SD | - | NO_GUIDE_HIT |
| China | Golden Eagle Cartoon (576p) | GoldenEagleCartoon.cn@SD | - | NO_GUIDE_HIT |
| China | Guangxi Variety & Travel Channel | GuangxiVarietyTravelChannel.cn | - | NO_GUIDE_HIT |
| China | Jiangxi Children's Channel | JiangxiChildrensChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Jiangxi Economy & Life Channel | JiangxiEconomyLifeChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Xi'an Business Information Channel (180p) [Not 24/7] | XianBusinessInformationChannel.cn@SD | - | NO_GUIDE_HIT |
| China | Xuzhou Economic Life Channel (1080p) | XuzhouEconomicLifeChannel.cn@SD | - | NO_GUIDE_HIT |
| China | You Man Cartoon Channel (576p) | YouManCartoonChannel.cn@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | 4K Travel | Travel.us | 4K.TRAVEL.TV.distro | MAPPED_ID_ONLY |
| Documentary & Wildlife | National Geographic (India) (576p) [Geo-blocked] | NationalGeographic.in@SD | NATIONAL.GEOGRAPHIC.in | MAPPED_ID_ONLY |
| Documentary & Wildlife | National Geographic (India) HD (1080p) | NationalGeographic.in@HD | NATIONAL.GEOGRAPHIC.in | MAPPED_ID_ONLY |
| Documentary & Wildlife | Adventure Earth | AdventureEarth.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Alone | Alone.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Amazing Discoveries TV | AmazingDiscoveriesTV.in | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic Adventure Earth | AutenticAdventureEarth.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic History | AutenticHistory.de | - | NO_GUIDE_HIT |
| Documentary & Wildlife | DISCOVERY BANGLA | custom.bdix.discoverybangla | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Velocity | discoveryvelocity.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | DocuBay TV (1080p) | DocuBayTV.in@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Documentary+ 2 | Documentary2.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Epic Crimes (1080p) | EpicCrimes.in@SD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Inside Crime | InsideCrime.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Mystery TV | MysteryTV.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | National Geographic Wild (India) HD (1080p) | NationalGeographicWild.in@HD | - | NO_GUIDE_HIT |
| Documentary & Wildlife | PBS Arts | PBSArts.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | RT Documentary | RTDocumentary.ru | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Tochka.rf | Tochkarf.ru | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Travel Channel East | travel.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Watch Mojo | WatchMojo.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | WaterBear | WaterBear.ch | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Wild Planet | WildPlanet.us | - | NO_GUIDE_HIT |
| France | Gong (1080p) | Gong.fr@SD | - | NO_GUIDE_HIT |
| France | P2M TV | P2MTV.fr | - | NO_GUIDE_HIT |
| France | Sony One Favoris | SonyOneFavoris.fr | - | NO_GUIDE_HIT |
| France | Sony One Hits Action | SonyOneHitsAction.fr | - | NO_GUIDE_HIT |
| France | Sony One Hits Comedie | SonyOneHitsComedie.fr | - | NO_GUIDE_HIT |
| Germany | Avatar (Germany) | Avatar.de@GB | - | NO_GUIDE_HIT |
| Germany | Cin Cin | CinCin.de@IT | - | NO_GUIDE_HIT |
| Germany | Pluto TV Adult Animation | PlutoTVAdultAnimation.de@DACH | - | NO_GUIDE_HIT |
| Germany | Pluto TV Animation | PlutoTVAnimation.de@GB | - | NO_GUIDE_HIT |
| Germany | Pluto TV Motor (Germany) | PlutoTVMotor.de@ES | - | NO_GUIDE_HIT |
| Germany | Pluto TV Retro Toons | PlutoTVRetroToons.de@FR | - | NO_GUIDE_HIT |
| Germany | Pluto TV Retro Toons GB | PlutoTVRetroToons.de@GB | - | NO_GUIDE_HIT |
| Germany | Pluto TV Star Trek: Animation | PlutoTVStarTrekAnimation.de@DACH | - | NO_GUIDE_HIT |
| Germany | South Park (Germany) | SouthPark.de@ES | - | NO_GUIDE_HIT |
| Germany | South Park (Germany) GB | SouthPark.de@GB | - | NO_GUIDE_HIT |
| Germany | South Park (Germany) IT | SouthPark.de@IT | - | NO_GUIDE_HIT |
| Germany | South Park Version Original | SouthParkVersionOriginal.de@ES | - | NO_GUIDE_HIT |
| Germany | South Park: Butters Collection (Germany) | SouthParkButtersCollection.de@DACH | - | NO_GUIDE_HIT |
| Germany | South Park: Cartman Collection (Germany) | SouthParkCartmanCollection.de@DACH | - | NO_GUIDE_HIT |
| Germany | South Park: Kenny Collection (Germany) | SouthParkKennyCollection.de@DACH | - | NO_GUIDE_HIT |
| Germany | South Park: Kyle Collection (Germany) | SouthParkKyleCollection.de@DACH | - | NO_GUIDE_HIT |
| Germany | South Park: Original Version | SouthParkOriginalVersion.de@DACH | - | NO_GUIDE_HIT |
| Germany | South Park: Stan Collection (Germany) | SouthParkStanCollection.de@DACH | - | NO_GUIDE_HIT |
| Germany | Teenage Mutant Ninja Turtles (720p) | TeenageMutantNinjaTurtles.de@IT | - | NO_GUIDE_HIT |
| Indian Bangla | BANGLA JAGO | custom.bdix.banglajago | Bangla.Jago.in | MAPPED_ID_ONLY |
| Indian Bangla | Bangla Jago TV | BanglaJagoTV.in | Bangla.Jago.in | MAPPED_ID_ONLY |
| Indian Bangla | Tara TV | TaraTV.in | Tara.TV.in | MAPPED_ID_ONLY |
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
| Indian Entertainment | Colors Super (396p) | ColorsSuper.in@SD | Colors.Super.in | MAPPED_ID_ONLY |
| Indian Entertainment | Darshana TV | DarshanaTV.in@SD | DARSHANA.in | MAPPED_ID_ONLY |
| Indian Entertainment | ETV Comedy (1080p) | ETVComedy.in@HD | ETVComedy.in | MAPPED_ID_ONLY |
| Indian Entertainment | Global Punjab | GlobalPunjab.in | Global.Punjab.in | MAPPED_ID_ONLY |
| Indian Entertainment | Kalaignar Murasu | KalaignarMurasu.in | MURASU.in | MAPPED_ID_ONLY |
| Indian Entertainment | Manoranjan Grand | ManoranjanGrand.in | Manoranjan.Grand.in | MAPPED_ID_ONLY |
| Indian Entertainment | Manoranjan Prime | ManoranjanPrime.in@SD | 154892 | MAPPED_ID_ONLY |
| Indian Entertainment | One Paschima | OnePaschima.in@SD | One.Paschima.in | MAPPED_ID_ONLY |
| Indian Entertainment | Prarthana TV | PrarthanaTV.in@SD | Prarthana.TV.in | MAPPED_ID_ONLY |
| Indian Entertainment | Sony Entertainment TV | SonyEntertainmentTelevision.in@SD | Sony.Entertainment.Television.in | MAPPED_ID_ONLY |
| Indian Entertainment | Super Hungama (576p) | SuperHungama.in@SD | Super.Hungama.in | MAPPED_ID_ONLY |
| Indian Entertainment | Suriyan TV | SuriyanTV.in@SD | ts1384 | MAPPED_ID_ONLY |
| Indian Entertainment | Odisha TV | OdishaTV.in@SD | OdishaTV.in|OdishaTV.in@SD | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Asianet Middle East (576p) | AsianetMiddleEast.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Baiscope TV | BaiscopeTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | BT TV (720p) | BTTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | CCV | CCV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors MENA | ColorsMENA.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors MENA HD (720p) | ColorsMENA.in@HD | - | NO_GUIDE_HIT |
| Indian Entertainment | DD Mizoram (504p) | DDMizoram.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | E-Vidya 10 (576p) | EVidya10.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | E-Vidya 11 (576p) | EVidya11.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | E-Vidya 12 (576p) | EVidya12.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | E-Vidya 4 (576p) | EVidya4.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | E-Vidya 5 (576p) | EVidya5.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | E-Vidya 6 (576p) | EVidya6.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | E-Vidya 7 (576p) | EVidya7.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | E-Vidya 8 (576p) | EVidya8.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | E-Vidya 9 (576p) | EVidya9.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Epic Bharat Digital (1080p) | EpicBharat.in@Digital | - | NO_GUIDE_HIT |
| Indian Entertainment | Flowers US | Flowers.us | - | NO_GUIDE_HIT |
| Indian Entertainment | JTBS Classic | JTBSClassic.in@Main | - | NO_GUIDE_HIT |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | - | NO_GUIDE_HIT |
| Indian Entertainment | KCL TV | KCLTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Kerala Vision | KeralaVision.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Maha Punjabi | MahaPunjabi.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | MediBizTV (720p) | MediBizTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | MH One Prime | Mh1Prime.in | - | NO_GUIDE_HIT |
| Indian Entertainment | MNTV (Tamil) | MarutamTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | NKR TV Kannada | NKRTVKannada.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Oli TV | OliTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Pankh | Pankh.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Pardesi TV | PardesiTV.ca | - | NO_GUIDE_HIT |
| Indian Entertainment | Pravasi Channel | PravasiChannel.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Pulari TV | PulariTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Punjabi TV | PunjabiTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Q TV | QTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Rajdhani | custom.rajdhani | - | NO_GUIDE_HIT |
| Indian Entertainment | SADA TV | SADATV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Sanskar TV (1080p) | SanskarTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Sooriyan TV | SooriyanTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Starnet | Starnet.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Thendral TV | ThendralTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | UTV Palakkad | UTVPalakkad.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Vyas Channel (576p) | VyasChannel.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Zee Cine Classic (1080p) | ZeeCineClassic.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Zee Comedy Nation (1080p) | ZeeComedyNation.in@HD | - | NO_GUIDE_HIT |
| Indian Movies | Ekamra Cinema | EkamraCinema.in | Ekamra.Cinema.in | MAPPED_ID_ONLY |
| Indian Movies | Jalsha Movies HD (1080p) | JalshaMovies.in@HD | JALSHA.MOVIES.in | MAPPED_ID_ONLY |
| Indian Movies | Manoranjan Grand (720p) | ManoranjanGrand.in@SD | Manoranjan.Grand.in | MAPPED_ID_ONLY |
| Indian Movies | Manoranjan Movies | ManoranjanMovies.in@SD | Manoranjan.Movies.in2 | MAPPED_ID_ONLY |
| Indian Movies | MH One Dil Se | MHOneDilSe.in@SD | 143536 | MAPPED_ID_ONLY |
| Indian Movies | Sony Pix HD (1080p) | SonyPix.in@HD | SONY.PIX.in | MAPPED_ID_ONLY |
| Indian Movies | Star Movies (India) HD (1080p) | StarMovies.in@HD | Star.Movies.in | MAPPED_ID_ONLY |
| Indian Movies | &TV International (1080p) | AndTV.in@International | - | NO_GUIDE_HIT |
| Indian Movies | B4U Bhojpuri Plus (1080p) | B4UBhojpuri.in@Plus | - | NO_GUIDE_HIT |
| Indian Movies | Chhaya Chitram Telugu | ChhayaChitramTelugu.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Goldmines 2 | Goldmines2.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Goldmines Action | GoldminesAction.in | - | NO_GUIDE_HIT |
| Indian Movies | Goldmines Action (576p) | GoldminesAction.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Hindi Movie Classic 24 | new.hindi.movie.classic.24 | - | NO_GUIDE_HIT |
| Indian Movies | India Talkies | IndiaTalkies.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Indywood TV | IndywoodTV.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | K Cine | KCine.in | - | NO_GUIDE_HIT |
| Indian Movies | Maha Movie | MahaMovie.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Mango | Mango.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | MH One Movies | MHOneMovies.in | - | NO_GUIDE_HIT |
| Indian Movies | MH One Movies (576p) | MHOneMovies.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Movie Punjab | MoviePunjab.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | NH BollyFlix (1080p) | NHBollyFlix.in@HD | - | NO_GUIDE_HIT |
| Indian Movies | NH BollyGold (1080p) | NHBollyGold.in@HD | - | NO_GUIDE_HIT |
| Indian Movies | NH Tamil Gold (1080p) | NHTamilGold.in@HD | - | NO_GUIDE_HIT |
| Indian Movies | Punjabi Shorts (1080p) | PunjabiShorts.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Shemaroo Filmi Gaane (1080p) | ShemarooFilmiGaane.in@HD | - | NO_GUIDE_HIT |
| Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | - | NO_GUIDE_HIT |
| Indian Movies | Soneri Cinema | SoneriCinema.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | South Movies | SouthMovies.in | - | NO_GUIDE_HIT |
| Indian Movies | Thalaa TV (1080p) | ThalaaTV.in@HD | - | NO_GUIDE_HIT |
| Indian Movies | Tolly TV (1080p) | TollyTV.in@HD | - | NO_GUIDE_HIT |
| Indian Movies | Zee Cinema APAC (720p) | ZeeCinema.in@APAC | - | NO_GUIDE_HIT |
| Indian Movies | Zee South Flix (1080p) | ZeeSouthFlix.in@HD | - | NO_GUIDE_HIT |
| Indian Music | Ekamra Musiq | EkamraMusiq.in | Ekamra.Musiq.in | MAPPED_ID_ONLY |
| Indian Music | Mastiii | Mastiii.in@SD | Mastiii.in | MAPPED_ID_ONLY |
| Indian Music | Steelbird Music | SteelbirdMusic.in@SD | Steelbird.Music.in | MAPPED_ID_ONLY |
| Indian Music | 7X Punjabi | 7XPunjabi.in | - | NO_GUIDE_HIT |
| Indian Music | Andy Haryana | AndyHaryana.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Deewana | DeewanaHD.in | - | NO_GUIDE_HIT |
| Indian Music | Deewana HD (540p) | DeewanaHD.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Dhamaal (576p) [Geo-blocked] | Dhamaal.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Hindi Hits | HindiHits.in | - | NO_GUIDE_HIT |
| Indian Music | Kalika TV | KalikaTV.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Punjabi Beats | PunjabiBeatsHD.in@HD | - | NO_GUIDE_HIT |
| Indian Music | Punjabi Music | PunjabiMusicHD.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Rang Rangoli | RangRangoli.in | - | NO_GUIDE_HIT |
| Indian Music | Superhitz | Superhitz.in@SD | - | NO_GUIDE_HIT |
| Indian Music | YRF Music Nepal | YRFMusic.in@Nepal | - | NO_GUIDE_HIT |
| International | BBC Drama | BBCDrama.uk | BBCDrama.au | MAPPED_ID_ONLY |
| International | CNN INTERNATIONLA | custom.bdix.cnninternationla | 157679 | MAPPED_ID_ONLY |
| International | Fashion One | FashionOne.uk | Fashion.One.cz | MAPPED_ID_ONLY |
| International | Shanson TV | ShansonTV.ru | Shanson.TV.cz | MAPPED_ID_ONLY |
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
| International Movies | +MaisUm (720p) | PlusMaisUm.br@HD | - | NO_GUIDE_HIT |
| International Movies | 00s Replay | 00sReplay.us@SD | - | NO_GUIDE_HIT |
| International Movies | 30A TV Classic Movies (720p) | 30ATVClassicMovies.us@SD | - | NO_GUIDE_HIT |
| International Movies | 312 Kino (406p) | 312Kino.kg@SD | - | NO_GUIDE_HIT |
| International Movies | 4ever Cinema (1080p) | 4everCinema.ua@SD | - | NO_GUIDE_HIT |
| International Movies | 70s Cinema | 70sCinema.us@SD | - | NO_GUIDE_HIT |
| International Movies | 80s Rewind | 80sRewind.us@SD | - | NO_GUIDE_HIT |
| International Movies | 90s Throwback | 90sThrowback.us@SD | - | NO_GUIDE_HIT |
| International Movies | Adrenalina Pura TV (720p) | AdrenalinaPuraTV.us@SD | - | NO_GUIDE_HIT |
| International Movies | Adrenalina Pura TV Brazil | AdrenalinaPuraTV.us@Brazil | - | NO_GUIDE_HIT |
| International Movies | Afghan Nobel Movies (720p) | AfghanNobelMovies.ca@SD | - | NO_GUIDE_HIT |
| International Movies | Aflam | custom.aflam | - | NO_GUIDE_HIT |
| International Movies | Afra Film | AfraFilm.ir@SD | - | NO_GUIDE_HIT |
| International Movies | Allo Cine (1080p) | AlloCine.cm@SD | - | NO_GUIDE_HIT |
| International Movies | alpha Cinema (1080p) | alphaCinema.ru@HD | - | NO_GUIDE_HIT |
| International Movies | AlternaTV (720p) [Not 24/7] | AlternaTV.ar@SD | - | NO_GUIDE_HIT |
| International Movies | AMC (United States) (720p) | AMC.us@EastHD | - | NO_GUIDE_HIT |
| International Movies | AMC Europe Bulgary (576p) | AMCEurope.uk@Bulgary | - | NO_GUIDE_HIT |
| International Movies | AMC Europe Czech Republic | AMCEurope.uk@CzechRepublic | - | NO_GUIDE_HIT |
| International Movies | AMC Europe Hungary | AMCEurope.uk@Hungary | - | NO_GUIDE_HIT |
| International Movies | AMC Europe Romania | AMCEurope.uk@Romania | - | NO_GUIDE_HIT |
| International Movies | AMC Latin America (1080p) | AMCLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| International Movies | AMC Latin America Brazil (720p) | AMCLatinAmerica.us@Brazil | - | NO_GUIDE_HIT |
| International Movies | Amedia Hit (1080p) | AmediaHit.ru@SD | - | NO_GUIDE_HIT |
| International Movies | Amedia Premium (720p) | AmediaPremium.ru@SD | - | NO_GUIDE_HIT |
| International Movies | American Horrors (480p) | AmericanHorrors.us@SD | - | NO_GUIDE_HIT |
| International Movies | Aneflix Live (720p) | AneflixLive.us@HD | - | NO_GUIDE_HIT |
| International Movies | Armenia Premium (720p) | ArmeniaPremium.am@SD | - | NO_GUIDE_HIT |
| International Movies | Aurora Media Films (720p) | AuroraMediaFilms.gt@SD | - | NO_GUIDE_HIT |
| International Movies | AVI Rewind (1080p) | AVIRewind.us@SD | - | NO_GUIDE_HIT |
| International Movies | AXN (Portugal) (1080p) | AXN.pt@SD | - | NO_GUIDE_HIT |
| International Movies | AXN Adria | AXNAdria.us@SD | - | NO_GUIDE_HIT |
| International Movies | AXN Asia Taiwan (1080p) | AXNAsia.sg@Taiwan | - | NO_GUIDE_HIT |
| International Movies | AXN Black (United States) (576p) | AXNBlack.us@Bulgary | - | NO_GUIDE_HIT |
| International Movies | AXN Black (United States) Czech Republic | AXNBlack.us@CzechRepublic | - | NO_GUIDE_HIT |
| International Movies | AXN Black (United States) Hungary (576p) | AXNBlack.us@Hungary | - | NO_GUIDE_HIT |
| International Movies | AXN Black (United States) Romania | AXNBlack.us@Romania | - | NO_GUIDE_HIT |
| International Movies | AXN CEE | AXNCEE.es@Hungary | - | NO_GUIDE_HIT |
| International Movies | AXN CEE Bulgary | AXNCEE.es@Bulgary | - | NO_GUIDE_HIT |
| International Movies | AXN CEE Czech Republic | AXNCEE.es@CzechRepublic | - | NO_GUIDE_HIT |
| International Movies | AXN CEE Romania | AXNCEE.es@Romania | - | NO_GUIDE_HIT |
| International Movies | AXN Crime | AXNCrime.us@SD | - | NO_GUIDE_HIT |
| International Movies | AXN Latin America Andes (1080p) | AXNLatinAmerica.us@Andes | - | NO_GUIDE_HIT |
| International Movies | AXN Latin America Mexico | AXNLatinAmerica.us@Mexico | - | NO_GUIDE_HIT |
| International Movies | AXN Latin America South | AXNLatinAmerica.us@South | - | NO_GUIDE_HIT |
| International Movies | AXN Movies (Portugal) (720p) | AXNMovies.pt@SD | - | NO_GUIDE_HIT |
| International Movies | AXN Poland (1080p) | AXNPoland.pl@SD | - | NO_GUIDE_HIT |
| International Movies | Az Cinema (1080p) | AzCinema.mx@SD | - | NO_GUIDE_HIT |
| International Movies | Battlestar Galactica | BattlestarGalactica.us@SD | - | NO_GUIDE_HIT |
| International Movies | beIN Box Office 1 | beINBoxOffice1.tr@SD | - | NO_GUIDE_HIT |
| International Movies | beIN Box Office 2 | beINBoxOffice2.tr@SD | - | NO_GUIDE_HIT |
| International Movies | beIN Box Office 3 | beINBoxOffice3.tr@SD | - | NO_GUIDE_HIT |
| International Movies | beIN Movies Stars | beINMoviesStars.tr@SD | - | NO_GUIDE_HIT |
| International Movies | beIN Movies Turk | beINMoviesTurk.tr@SD | - | NO_GUIDE_HIT |
| International Movies | BET Cinema | BETCinema.us@SD | - | NO_GUIDE_HIT |
| International Movies | BET Comedy Movies | BETComedyMovies.us@SD | - | NO_GUIDE_HIT |
| International Movies | BET Visionaries | BETVisionaries.us@SD | - | NO_GUIDE_HIT |
| International Movies | BIZ Cinema (1080p) | BIZCinema.uz@SD | - | NO_GUIDE_HIT |
| International Movies | Blokbaster HD (1080p) | Blokbaster.ru@HD | - | NO_GUIDE_HIT |
| International Movies | Bollywood HD (576p) | Bollywood.ru@HD | - | NO_GUIDE_HIT |
| International Movies | Bollywood HD Russia (576p) | BollywoodHD.ro@Russia | - | NO_GUIDE_HIT |
| International Movies | Bolt (Russia) (576p) | Bolt.ru@SD | - | NO_GUIDE_HIT |
| International Movies | Bolt (Ukraine) (1080p) | Bolt.ua@SD | - | NO_GUIDE_HIT |
| International Movies | Bonanza | Bonanza.us@SD | - | NO_GUIDE_HIT |
| International Movies | Bonanza CA | Bonanza.us@CA | - | NO_GUIDE_HIT |
| International Movies | Boreal (720p) [Not 24/7] | Boreal.do@SD | - | NO_GUIDE_HIT |
| International Movies | Bravo Farsi TV (360p) | BravoFarsiTV.ir@SD | - | NO_GUIDE_HIT |
| International Movies | bTV Action | bTVAction.bg@SD | - | NO_GUIDE_HIT |
| International Movies | bTV Cinema | bTVCinema.bg@SD | - | NO_GUIDE_HIT |
| International Movies | bTV Lady | bTVLady.bg@SD | - | NO_GUIDE_HIT |
| International Movies | Cafe Film | CafeFilm.ir@SD | - | NO_GUIDE_HIT |
| International Movies | Canal Cine Dios | CanalCineDios.co@SD | - | NO_GUIDE_HIT |
| International Movies | Canal+ Action Europe (360p) | CanalPlusActionEurope.nl@Netherlands | - | NO_GUIDE_HIT |
| International Movies | Canal+ Action Europe Czechia | CanalPlusActionEurope.nl@Czechia | - | NO_GUIDE_HIT |
| International Movies | Canal+ Action Europe Slovakia (720p) | CanalPlusActionEurope.nl@Slovakia | - | NO_GUIDE_HIT |
| International Movies | Canal+ Cinemas (720p) | CanalPlusCinemas.fr@SD | - | NO_GUIDE_HIT |
| International Movies | CCTV-6 [Geo-blocked] | CCTV6.cn@SD | - | NO_GUIDE_HIT |
| International Movies | CCTV-6 HD (1080p) | CCTV6.cn@HD | - | NO_GUIDE_HIT |
| International Movies | Celestial Movies (576i) | CelestialMovies.hk@SD | - | NO_GUIDE_HIT |
| International Movies | CHC Action (1080p) | CHCAction.cn@SD | - | NO_GUIDE_HIT |
| International Movies | CINDIE TV (1080p) | CINDIETV.br@HD | - | NO_GUIDE_HIT |
| International Movies | Cine 666 by Pluto TV | Cine666byPlutoTV.de@FR | - | NO_GUIDE_HIT |
| International Movies | Cine Action by Pluto TV | CineActionbyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| International Movies | Cine Adrenalina | CineAdrenalina.us@SD | - | NO_GUIDE_HIT |
| International Movies | Cine Amor | CineAmor.us@SD | - | NO_GUIDE_HIT |
| International Movies | Cine by Pluto TV | CinebyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| International Movies | Cine Catastrophe by Pluto TV | CineCatastrophebyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| International Movies | Cine d'Asie by Pluto TV | CinedAsiebyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| International Movies | Cine Familiar (1080p) | CineFamiliar.us@SD | - | NO_GUIDE_HIT |
| International Movies | Cine Hispano (1080p) | CineHispano.us@SD | - | NO_GUIDE_HIT |
| International Movies | Cine Horreur by Pluto TV | CineHorreurbyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| International Movies | Cine Nanar (1080p) | CineNanar.fr@SD | - | NO_GUIDE_HIT |
| International Movies | Cine Premiere | CinePremiere.us@SD | - | NO_GUIDE_HIT |
| International Movies | Cine Premium (1080p) | CinePremium.us@SD | - | NO_GUIDE_HIT |
| International Movies | Cine Retro by Pluto TV | CineRetrobyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| International Movies | Cine Romance by Pluto TV | CineRomancebyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| International Movies | Cine Romantico (720p) | CineRomantico.us@SD | - | NO_GUIDE_HIT |
| International Movies | Cine Sci-Fi by Pluto TV | CineSciFibyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| International Movies | Cine Terror | CineTerror.us@US | - | NO_GUIDE_HIT |
| International Movies | Cine Terror BR | CineTerror.us@BR | - | NO_GUIDE_HIT |
| International Movies | Cine Terror LatAm | CineTerror.us@LatAm | - | NO_GUIDE_HIT |
| International Movies | Cine Thrillers by Pluto TV | CineThrillersbyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| International Movies | Cine Western (France) (1080p) | CineWestern.fr@SD | - | NO_GUIDE_HIT |
| International Movies | Cine Western by Pluto TV | CineWesternbyPlutoTV.de@FR | - | NO_GUIDE_HIT |
| International Movies | Cine+ | CinePlus.ua@SD | - | NO_GUIDE_HIT |
| International Movies | Cine+ Classic | CinePlusClassic.fr@SD | - | NO_GUIDE_HIT |
| International Movies | Cine+ Frisson (1080p) | CinePlusFrisson.fr@SD | - | NO_GUIDE_HIT |
| International Movies | Cine+ Hit | CinePlusHit.ua@SD | - | NO_GUIDE_HIT |
| International Movies | Cine+ Legend | CinePlusLegend.ua@SD | - | NO_GUIDE_HIT |
| International Movies | cine.box | cinebox.bg@SD | - | NO_GUIDE_HIT |
| International Movies | Cinecanal (1080p) | Cinecanal.us@Panregional | - | NO_GUIDE_HIT |
| International Movies | Cinecanal Pacific (1080p) | Cinecanal.us@Pacific | - | NO_GUIDE_HIT |
| International Movies | Cinecanal South | Cinecanal.us@South | - | NO_GUIDE_HIT |
| International Movies | CineLatino (720p) | CineLatino.mx@SD | - | NO_GUIDE_HIT |
| International Movies | Cinema (Mongolia) (1080p) | Cinema.mn@SD | - | NO_GUIDE_HIT |
| International Movies | Cinema (Russia) (576p) | Cinema.ru@SD | - | NO_GUIDE_HIT |
| International Movies | Cinemaraton Plus (1080i) | CinemaratonPlus.ro@HD | - | NO_GUIDE_HIT |
| International Movies | CinemaWorld (720p) | CinemaWorld.my@SD | - | NO_GUIDE_HIT |
| International Movies | Cinemax (Czech Republic) | Cinemax.cz@Czechia | - | NO_GUIDE_HIT |
| International Movies | Cinemax (United States) West (720p) | Cinemax.us@West | - | NO_GUIDE_HIT |
| International Movies | Cinemax Asia (720p) [Geo-blocked] | CinemaxAsia.sg@SD | - | NO_GUIDE_HIT |
| International Movies | Cinemax Asia HD (1080p) | CinemaxAsia.sg@HD | - | NO_GUIDE_HIT |
| International Movies | Cinemax Classics (1080p) | CinemaxClassics.us@East | - | NO_GUIDE_HIT |
| International Movies | Cinemax Hits (1080p) | CinemaxHits.us@East | - | NO_GUIDE_HIT |
| International Movies | Cinemax Latin America (720p) | CinemaxLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| International Movies | CineStar 1 Bulgaria | CineStar1Bulgaria.bg@SD | - | NO_GUIDE_HIT |
| International Movies | Cinevault 80s (720p) | Cinevault80s.us@SD | - | NO_GUIDE_HIT |
| International Movies | CineWow | CineWow.ro@SD | - | NO_GUIDE_HIT |
| International Movies | City Eden KinoAction [Not 24/7] | CityEdenKinoAction.ru@HD | - | NO_GUIDE_HIT |
| International Movies | City Eden KinoArt [Not 24/7] | CityEdenKinoArt.ru@HD | - | NO_GUIDE_HIT |
| International Movies | City Eden KinoAsia [Not 24/7] | CityEdenKinoAsia.ru@HD | - | NO_GUIDE_HIT |
| International Movies | City Eden KinoDetektiv [Not 24/7] | CityEdenKinoDetektiv.ru@HD | - | NO_GUIDE_HIT |
| International Movies | City Eden KinoDrama [Not 24/7] | CityEdenKinoDrama.ru@HD | - | NO_GUIDE_HIT |
| International Movies | City Eden KinoFantastika [Not 24/7] | CityEdenKinoFantastika.ru@HD | - | NO_GUIDE_HIT |
| International Movies | City Eden KinoKlassika [Not 24/7] | CityEdenKinoKlassika.ru@HD | - | NO_GUIDE_HIT |
| International Movies | City Eden KinoKomediya [Not 24/7] | CityEdenKinoKomediya.ru@HD | - | NO_GUIDE_HIT |
| International Movies | City Eden KinoMistika [Not 24/7] | CityEdenKinoMistika.ru@HD | - | NO_GUIDE_HIT |
| International Movies | City Eden KinoSemya [Not 24/7] | CityEdenKinoSemya.ru@HD | - | NO_GUIDE_HIT |
| International Movies | Claro Cinema (1080p) | ClaroCinema.mx@SD | - | NO_GUIDE_HIT |
| International Movies | CND Film Discovery Channel (576p) | CNDFilmDiscoveryChannel.cn@SD | - | NO_GUIDE_HIT |
| International Movies | Pluto TV Comedy Movies | PlutoTVComedyMovies.us@CA | - | NO_GUIDE_HIT |
| International Movies | Pluto TV Retro Action Movies | PlutoTVRetroActionMovies.us@CA | - | NO_GUIDE_HIT |
| International Movies | Rakuten TV Family Movies (1080p) | RakutenTVFamilyMovies.es@Spain | - | NO_GUIDE_HIT |
| International Movies | Rakuten TV Family Movies Austria (720p) | RakutenTVFamilyMovies.es@Austria | - | NO_GUIDE_HIT |
| International Movies | Rakuten TV Family Movies Finland (1080p) | RakutenTVFamilyMovies.es@Finland | - | NO_GUIDE_HIT |
| International Movies | Rakuten TV Family Movies Germany (1080p) | RakutenTVFamilyMovies.es@Germany | - | NO_GUIDE_HIT |
| International Movies | Rakuten TV Family Movies Italy (1080p) | RakutenTVFamilyMovies.es@Italy | - | NO_GUIDE_HIT |
| International Movies | Rakuten TV Family Movies Switzerland (720p) | RakutenTVFamilyMovies.es@Switzerland | - | NO_GUIDE_HIT |
| International Movies | TVS Classic Movies (288p) | TVSClassicMovies.us@SD | - | NO_GUIDE_HIT |
| International Movies | TVS Nostalgia Movies (480p) | TVSNostalgiaMovies.us@SD | - | NO_GUIDE_HIT |
| International Movies | TVS Western Movie (270p) | TVSWesternMovie.us@SD | - | NO_GUIDE_HIT |
| International Music | 13 Festival (1080p) | 13Festival.cl@SD | - | NO_GUIDE_HIT |
| International Music | 2TV (1080p) | 2TV.lt@SD | - | NO_GUIDE_HIT |
| International Music | 360TuneBox (1080p) | 360TuneBox.nl@SD | - | NO_GUIDE_HIT |
| International Music | 4 Music | 4Music.fr@SD | - | NO_GUIDE_HIT |
| International Music | 4ever Music (1080p) | 4everMusic.ua@SD | - | NO_GUIDE_HIT |
| International Music | 4Kurd | 4Kurd.fr@SD | - | NO_GUIDE_HIT |
| International Music | 7 RadioVisione (720p) | 7RadioVisione.it@HD | - | NO_GUIDE_HIT |
| International Music | 70-80 TV | 7080TV.it@SD | - | NO_GUIDE_HIT |
| International Music | 88 Stereo (720p) [Not 24/7] | 88Stereo.cr@SD | - | NO_GUIDE_HIT |
| International Music | 98.1 Pearl FM (720p) | 981PearlFM.sx@SD | - | NO_GUIDE_HIT |
| International Music | A2i Music (720p) [Not 24/7] | A2iMusic.sn@SD | - | NO_GUIDE_HIT |
| International Music | Abdulmajeed Abdullah (1080p) | AbdulmajeedAbdullah.sa@SD | - | NO_GUIDE_HIT |
| International Music | ACW UG TV (480p) | ACWUGTV.ug@SD | - | NO_GUIDE_HIT |
| International Music | AFN TV | AFNTV.ir@SD | - | NO_GUIDE_HIT |
| International Music | Aghani Aghani TV (1080p) | AghaniAghaniTV.lb@SD | - | NO_GUIDE_HIT |
| International Music | AlbKanale Music TV HD (1080p) | AlbKanaleMusicTV.al@HD | - | NO_GUIDE_HIT |
| International Music | Alcance FM PLAY TV | AlcanceFMPLAYTV.py@SD | - | NO_GUIDE_HIT |
| International Music | Alegria TV (720p) | AlegriaTV.bo@SD | - | NO_GUIDE_HIT |
| International Music | Allegro HD (1080p) | AllegroHD.ar@SD | - | NO_GUIDE_HIT |
| International Music | AMC (Afghanistan) (1080p) | AMC.af@SD | - | NO_GUIDE_HIT |
| International Music | AMusic Channel (720p) | AMusicChannel.ng@SD | - | NO_GUIDE_HIT |
| International Music | Andina RTV (720p) | AndinaRTV.pe@SD | - | NO_GUIDE_HIT |
| International Music | Antenne Kaernten (720p) | AntenneKaernten.at@SD | - | NO_GUIDE_HIT |
| International Music | Antenne Steiermark (720p) | AntenneSteiermark.at@SD | - | NO_GUIDE_HIT |
| International Music | Antenne Vorarlberg (720p) [Not 24/7] | AntenneVorarlberg.at@SD | - | NO_GUIDE_HIT |
| International Music | Arabica TV | custom.arabica-tv | - | NO_GUIDE_HIT |
| International Music | Atomic Academy TV (480p) | AtomicAcademyTV.ro@SD | - | NO_GUIDE_HIT |
| International Music | Atomic TV (360p) | AtomicTV.ro@SD | - | NO_GUIDE_HIT |
| International Music | Audiokiss (1080p) | Audiokiss.bo@SD | - | NO_GUIDE_HIT |
| International Music | Azahares Radiovisual Multimedia (720p) | AzaharesRadiovisualMultimedia.ar@SD | - | NO_GUIDE_HIT |
| International Music | Bandamax (1080p) | Bandamax.mx@SD | - | NO_GUIDE_HIT |
| International Music | Baraza TV (1080p) | BarazaTV.gr@SD | - | NO_GUIDE_HIT |
| International Music | Baraza TV Deep House (720p) | BarazaTVDeepHouse.gr@SD | - | NO_GUIDE_HIT |
| International Music | Baraza TV Relaxing (720p) | BarazaTVRelaxing.gr@SD | - | NO_GUIDE_HIT |
| International Music | BEATTV (1080p) | BEATTV.nl@SD | - | NO_GUIDE_HIT |
| International Music | Bel RTL (1080p) | BelRTL.be@SD | - | NO_GUIDE_HIT |
| International Music | Best of Dance TV (1080p) | BestofDanceTV.ee@SD | - | NO_GUIDE_HIT |
| International Music | BIZ Music (1080p) | BIZMusic.uz@SD | - | NO_GUIDE_HIT |
| International Music | Black (1080p) | Black.ua@SD | - | NO_GUIDE_HIT |
| International Music | BOKTV (720p) [Not 24/7] | BOKTV.za@SD | - | NO_GUIDE_HIT |
| International Music | Boom TV (1080p) | BoomTV.ro@HD | - | NO_GUIDE_HIT |
| International Music | BOX TV | BOXTV.bg@SD | - | NO_GUIDE_HIT |
| International Music | BTA TV (720p) | BTATV.ve@SD | - | NO_GUIDE_HIT |
| International Music | Canal 3 KMK TV (720p) | Canal3KMKTV.cr@SD | - | NO_GUIDE_HIT |
| International Music | CCTV-15 (720p) | CCTV15.cn@SD | - | NO_GUIDE_HIT |
| International Music | CEACOM TV (1080p) [Not 24/7] | CEACOMTV.bo@SD | - | NO_GUIDE_HIT |
| International Music | Chamame TV | ChamameTV.ar@SD | - | NO_GUIDE_HIT |
| International Music | Chocolate FM (720p) | ChocolateFM.cl@SD | - | NO_GUIDE_HIT |
| International Music | City TV (Bulgaria) (576p) [Not 24/7] | CityTV.bg@SD | - | NO_GUIDE_HIT |
| International Music | CKNO-FM (616p) | CKNOFM.ca@SD | - | NO_GUIDE_HIT |
| International Music | Claro Musica TV (1080p) | ClaroMusicaTV.co@SD | - | NO_GUIDE_HIT |
| International Music | Company TV (720p) | CompanyTV.it@SD | - | NO_GUIDE_HIT |
| International Music | Conecta TV (720p) | ConectaTV.mx@SD | - | NO_GUIDE_HIT |
| International Music | Cool FM 98.9 (720p) | CoolFM989.aw@SD | - | NO_GUIDE_HIT |
| International Music | Corazon TV | CorazonTV.pa@SD | - | NO_GUIDE_HIT |
| International Music | Couleur 3 (720p) | Couleur3.ch@SD | - | NO_GUIDE_HIT |
| International Music | Cumbia Mix (720p) | CumbiaMix.ar@HD | - | NO_GUIDE_HIT |
| International Music | D Music (1280p) [Not 24/7] | DMusic.kh@SD | - | NO_GUIDE_HIT |
| International Music | Dance FM (720p) | DanceFM.cl@SD | - | NO_GUIDE_HIT |
| International Music | Dance TV [Geo-blocked] | DanceTV.ar@SD | - | NO_GUIDE_HIT |
| International Music | DanceTV Algorhythm (1080p) | DanceTVAlgorhythm.ee@SD | - | NO_GUIDE_HIT |
| International Music | DanceTV Deep House District (1080p) | DanceTVDeepHouseDistrict.ee@SD | - | NO_GUIDE_HIT |
| International Music | DanceTV EDM Mainstage (1080p) | DanceTVEDMMainstage.ee@SD | - | NO_GUIDE_HIT |
| International Music | DanceTV House Floor (1080p) | DanceTVHouseFloor.ee@SD | - | NO_GUIDE_HIT |
| International Music | DanceTV Minimal Tech (1080p) | DanceTVMinimalTech.ee@SD | - | NO_GUIDE_HIT |
| International Music | DanceTV Techno Warehouse (1080p) | DanceTVTechnoWarehouse.ee@SD | - | NO_GUIDE_HIT |
| International Music | DBM TV (1080p) | DBMTV.fr@SD | - | NO_GUIDE_HIT |
| International Music | Deep House District (1080p) | DeepHouseDistrict.nl@SD | - | NO_GUIDE_HIT |
| International Music | Disco Mix (576p) | DiscoMix.ro@SD | - | NO_GUIDE_HIT |
| International Music | DM Sat (576p) | DMSat.rs@SD | - | NO_GUIDE_HIT |
| International Music | Dream Turk (720p) | DreamTurk.tr@SD | - | NO_GUIDE_HIT |
| International Music | DSTV (Bulgaria) (614p) [Not 24/7] | DSTV.bg@SD | - | NO_GUIDE_HIT |
| International Music | E40 (1080p) | E40.py@SD | - | NO_GUIDE_HIT |
| International Music | El Sol Network TV (1080p) | ElSolNetworkTV.ec@SD | - | NO_GUIDE_HIT |
| International Music | Ellinikos FM (720p) | EllinikosFM.gr@SD | - | NO_GUIDE_HIT |
| International Music | Epic Music Digital | custom.epic-music-digital | - | NO_GUIDE_HIT |
| International Music | EU Music | EUMusic.ua | - | NO_GUIDE_HIT |
| International Music | Euro Indie Music Chart TV (360p) | EuroIndieMusicChartTV.it@SD | - | NO_GUIDE_HIT |
| International Music | Exa TV | ExaTV.mx@SD | - | NO_GUIDE_HIT |
| International Music | Fabulosa Estereo 100.5 FM (720p) | FabulosaEstereo1005FM.pa@SD | - | NO_GUIDE_HIT |
| International Music | Live Music | LiveMusic.us@SD | - | NO_GUIDE_HIT |
| International Music | Trace Urban (Australia) | custom.trace-urban-australia | - | NO_GUIDE_HIT |
| International Music | Ua Music | custom.ua-music | - | NO_GUIDE_HIT |
| International Music | V2BEAT | custom.v2beat | - | NO_GUIDE_HIT |
| International Music | ¡Viva Latino! (1080p) | VivaLatino.ua@SD | - | NO_GUIDE_HIT |
| Kids | Disney Channel India | DisneyChannel.in@HD | DISNEY.CHANNEL.in | MAPPED_ID_ONLY |
| Kids | ADN TV+ | ADNTVPlus.fr | - | NO_GUIDE_HIT |
| Kids | Afarin TV | AfarinTV.iq | - | NO_GUIDE_HIT |
| Kids | Bantul the Great | BantulTheGreat.us | - | NO_GUIDE_HIT |
| Kids | Doraemon TV | DoraemonTV.us | - | NO_GUIDE_HIT |
| Kids | Epic Kids Digital | EpicKidsDigital.us | - | NO_GUIDE_HIT |
| Kids | Extrema Kids TV [Not 24/7] | ExtremaKidsTV.cr@HD | - | NO_GUIDE_HIT |
| Kids | Lego Channel | LegoChannel.us@SD | - | NO_GUIDE_HIT |
| Kids | MAX Anime (1080p) | MAXAnime.ve@SD | - | NO_GUIDE_HIT |
| Kids | Moonbug Kids | MoonbugKids.uk | - | NO_GUIDE_HIT |
| Kids | Nick Bangla | NickBangla.bd | - | NO_GUIDE_HIT |
| Kids | Powerkids Kartoon Channel | PowerkidsKartoonChannel.us | - | NO_GUIDE_HIT |
| Kids | Smurf TV | SmurfTV.us | - | NO_GUIDE_HIT |
| Kids | Tom and Jerry | TomAndJerry.do | - | NO_GUIDE_HIT |
| Kids | Tooku | Tooku.ru | - | NO_GUIDE_HIT |
| Kids | Toon Goggles Junior | ToonGogglesJunior.us | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Hindi | WOWKidz.in@Hindi | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Tamil | WOWKidzTamil.in | - | NO_GUIDE_HIT |
| Kids | WOW Kidz Telugu | WOWKidz.in@Telugu | - | NO_GUIDE_HIT |
| Pakistani | 8XM | 8XM.pk@HD | - | NO_GUIDE_HIT |
| Pakistani | 8XM | 8XM.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | A-Plus TV (576p) | APlusTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Aaj Entertainment (1080p) | AajEntertainment.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | ARY Family | custom.ary-family | - | NO_GUIDE_HIT |
| Pakistani | ARY Music | custom.ary-music-tumyo | - | NO_GUIDE_HIT |
| Pakistani | ARY Musik (1080p) | ARYMusik.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | ATV (Pakistan) (1080p) | ATV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | aur LIFE | aurLIFE.pk | - | NO_GUIDE_HIT |
| Pakistani | AVT Khyber (1080p) | AVTKhyber.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Awaz TV | custom.awaz-tv | - | NO_GUIDE_HIT |
| Pakistani | Bol Entertainment HD | BolEntertainment.pk@HD | - | NO_GUIDE_HIT |
| Pakistani | Cartoon Network (Pakistan) | CartoonNetwork.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Discover Pakistan | custom.discover-pikstan | - | NO_GUIDE_HIT |
| Pakistani | Express Entertainment (1080p) | ExpressEntertainment.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Falak TV | FalakTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Filmax (576p) | Filmax.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Filmazia (576p) | Filmazia.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | HarPal Geo (360p) | HarPalGeo.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | HUM Sitaray | HUMSitaray.pk | - | NO_GUIDE_HIT |
| Pakistani | Hum Sitaray World | custom.hum-sitery-world | - | NO_GUIDE_HIT |
| Pakistani | Jalwa TV | JalwaTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Joo Music | JooMusic.pk | - | NO_GUIDE_HIT |
| Pakistani | LTN Family SD (576p) | LTNFamily.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Masala TV (576p) | MasalaTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Mehran TV (576p) | MehranTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Paighan TV | PaighanTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Pashto 1 (1080p) | Pashto1.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Play Entertainment (576p) | PlayEntertainment.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | SAB TV (1080p) | SABTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | See TV | SeeTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Tag TV | TagTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Waseb TV | WasebTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Waseeb TV | custom.waseeb-tv | - | NO_GUIDE_HIT |
| Poland | AXN Black Poland | custom.axn-black-poland | - | NO_GUIDE_HIT |
| Poland | Teletoon+ HD (1080i) | TeletoonPlus.pl@HD | - | NO_GUIDE_HIT |
| Poland | Telewizja Biznesowa (1080p) | TelewizjaBiznesowa.pl@SD | - | NO_GUIDE_HIT |
| Poland | wedotv Auta (480p) | wedotvAuta.pl@FAST | - | NO_GUIDE_HIT |
| Religious | Makkah TV | MakkahTV.sa | Makkah.TV.ae | MAPPED_ID_ONLY |
| Religious | Al Quran Al Kareem TV | AlQuranAlKareemTV.sa | - | NO_GUIDE_HIT |
| Religious | Al Quran Radio | custom.al-quran-radio | - | NO_GUIDE_HIT |
| Religious | Al Sunnah TV | custom.al-sunnah-tv | - | NO_GUIDE_HIT |
| Religious | Al-Zahra TV Turkic | AlZahraTVTurkic.sa | - | NO_GUIDE_HIT |
| Religious | ARY Q TV | ARYQTV.pk | - | NO_GUIDE_HIT |
| Religious | Bahrain Quran | BahrainQuran.bh | - | NO_GUIDE_HIT |
| Religious | Islam TV Urdu | custom.islam-tv-urdu | - | NO_GUIDE_HIT |
| Religious | Islamic TV | IslamicTV.sa | - | NO_GUIDE_HIT |
| Religious | Madani Channel | custom.madani-channel | - | NO_GUIDE_HIT |
| Religious | Madani TV | MadaniTV.sa | - | NO_GUIDE_HIT |
| Religious | MADANI TV BANGLA | custom.bdix.madanibangla | - | NO_GUIDE_HIT |
| Religious | MADINA LIVE | custom.bdix.madinalive | - | NO_GUIDE_HIT |
| Religious | Makkah Live | MakkahLive.sa | - | NO_GUIDE_HIT |
| Religious | Makkah Live | custom.makkah.live | - | NO_GUIDE_HIT |
| Religious | Medina Live | MedinaLive.bd | - | NO_GUIDE_HIT |
| Religious | Peace TV Bangla | PeaceTVBangla.ae | - | NO_GUIDE_HIT |
| Religious | Peace TV English | PeaceTVEnglish.ae | - | NO_GUIDE_HIT |
| Religious | Peace TV Urdu | PeaceTVUrdu.pk | - | NO_GUIDE_HIT |
| Religious | Quran | custom.quran | - | NO_GUIDE_HIT |
| Religious | Quran TV | QuranTV.iq | - | NO_GUIDE_HIT |
| Religious | Sunnah TV | custom.sunnah-tv | - | NO_GUIDE_HIT |
| Religious | Zainabia Channel | ZainabiaChannel.sa | - | NO_GUIDE_HIT |
| Romania | Aleph Business (1280p) | AlephBusiness.ro@SD | - | NO_GUIDE_HIT |
| Romania | Bollywood Classic Romania (576p) | BollywoodClassic.ro@Romania | - | NO_GUIDE_HIT |
| Russia | Auto Plus (576p) | AutoPlus.ru@SD | - | NO_GUIDE_HIT |
| Russia | Avto24 (576p) | Avto24.ru@SD | - | NO_GUIDE_HIT |
| Russia | BRIDGE Classic (576p) | BRIDGEClassic.ru@SD | - | NO_GUIDE_HIT |
| Russia | City Eden AutoGid [Not 24/7] | CityEdenAutoGid.ru@HD | - | NO_GUIDE_HIT |
| Russia | Detvora+ (1080p) | DetvoraPlus.ru@HD | - | NO_GUIDE_HIT |
| Russia | Drive (576i) | Drive.ru@SD | - | NO_GUIDE_HIT |
| Russia | FAN (1080p) | FAN.ru@SD | - | NO_GUIDE_HIT |
| Russia | Pro Business (720p) | ProBusiness.ru@SD | - | NO_GUIDE_HIT |
| Russia | RBK-TV (576p) | RBKTV.ru@SD | - | NO_GUIDE_HIT |
| Russia | Solnce (576p) | Solnce.ru@SD | - | NO_GUIDE_HIT |
| Spain | SX3 (1080p) [Geo-blocked] | SX3.es@SD | SX3.es | MAPPED_ID_ONLY |
| Spain | 3Cat Plats bruts (1080p) | 3CatPlatsbruts.es@SD | - | NO_GUIDE_HIT |
| Spain | Anime Vision (1080p) | AnimeVision.es@SD | - | NO_GUIDE_HIT |
| Spain | Anime Vision Classics (1080p) | AnimeVisionClassics.es@SD | - | NO_GUIDE_HIT |
| Sports | Sky Sports Cricket | SkySportsCricket.ie | SkySportsCricket.ie | MAPPED_ID_ONLY |
| Sports | IN: -HINDI- STAR SPORTS 1 HD | Star Sports 1 Hindi HD.in | StarSports1HindiHD.in | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | A Sports | ASports.pk | - | NO_GUIDE_HIT |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | - | NO_GUIDE_HIT |
| Sports | eSports Max TV | eSportsMaxTV.ve@SD | - | NO_GUIDE_HIT |
| Sports | Goal TV | GoalTV.in | - | NO_GUIDE_HIT |
| Sports | PK Sports | PKSports.pk@SD | - | NO_GUIDE_HIT |
| Sports | PK: GEO SUPER | custom.bdix.geosuper | - | NO_GUIDE_HIT |
| Sports | PTV Sports | PTVSports.pk | - | NO_GUIDE_HIT |
| Sports | T Sports | TSports.bd | - | NO_GUIDE_HIT |
| Sports | Ten Sports | TenSports.pk | - | NO_GUIDE_HIT |
| Sweden | Avatar (Sweden) | Avatar.se@DK | - | NO_GUIDE_HIT |
| Sweden | Becker (Sweden) | Becker.se@SE | - | NO_GUIDE_HIT |
| Sweden | Becker (Sweden) DK | Becker.se@DK | - | NO_GUIDE_HIT |
| Sweden | Becker (Sweden) NO | Becker.se@NO | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Motor (Sweden) | PlutoTVMotor.se@SE | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Motor (Sweden) DK | PlutoTVMotor.se@DK | - | NO_GUIDE_HIT |
| Sweden | Pluto TV Motor (Sweden) NO | PlutoTVMotor.se@NO | - | NO_GUIDE_HIT |
| Sweden | South Park (Sweden) | SouthPark.se@SE | - | NO_GUIDE_HIT |
| Sweden | South Park (Sweden) DK | SouthPark.se@DK | - | NO_GUIDE_HIT |
| Sweden | South Park (Sweden) NO | SouthPark.se@NO | - | NO_GUIDE_HIT |
| Sweden | South Park Armageddon | SouthParkArmageddon.se@SE | - | NO_GUIDE_HIT |
| Sweden | South Park Armageddon DK | SouthParkArmageddon.se@DK | - | NO_GUIDE_HIT |
| Sweden | South Park Armageddon NO | SouthParkArmageddon.se@NO | - | NO_GUIDE_HIT |
| Sweden | South Park Rockin' Out | SouthParkRockinOut.se@SE | - | NO_GUIDE_HIT |
| Sweden | South Park Rockin' Out DK | SouthParkRockinOut.se@DK | - | NO_GUIDE_HIT |
| Sweden | South Park Rockin' Out NO | SouthParkRockinOut.se@NO | - | NO_GUIDE_HIT |
| Sweden | South Park: Butters Collection (Sweden) | SouthParkButtersCollection.se@SE | - | NO_GUIDE_HIT |
| Sweden | South Park: Butters Collection (Sweden) DK | SouthParkButtersCollection.se@DK | - | NO_GUIDE_HIT |
| Sweden | South Park: Butters Collection (Sweden) NO | SouthParkButtersCollection.se@NO | - | NO_GUIDE_HIT |
| Sweden | South Park: Cartman Collection (Sweden) | SouthParkCartmanCollection.se@SE | - | NO_GUIDE_HIT |
| Sweden | South Park: Cartman Collection (Sweden) DK | SouthParkCartmanCollection.se@DK | - | NO_GUIDE_HIT |
| Sweden | South Park: Cartman Collection (Sweden) NO | SouthParkCartmanCollection.se@NO | - | NO_GUIDE_HIT |
| Sweden | South Park: Into the Stars | SouthParkIntotheStars.se@SE | - | NO_GUIDE_HIT |
| Sweden | South Park: Into the Stars DK | SouthParkIntotheStars.se@DK | - | NO_GUIDE_HIT |
| Sweden | South Park: Into the Stars NO | SouthParkIntotheStars.se@NO | - | NO_GUIDE_HIT |
| Sweden | South Park: Kenny Collection (Sweden) | SouthParkKennyCollection.se@SE | - | NO_GUIDE_HIT |
| Sweden | South Park: Kenny Collection (Sweden) DK | SouthParkKennyCollection.se@DK | - | NO_GUIDE_HIT |
| Sweden | South Park: Kenny Collection (Sweden) NO | SouthParkKennyCollection.se@NO | - | NO_GUIDE_HIT |
| Sweden | South Park: Kyle Collection (Sweden) | SouthParkKyleCollection.se@SE | - | NO_GUIDE_HIT |
| Sweden | South Park: Kyle Collection (Sweden) DK | SouthParkKyleCollection.se@DK | - | NO_GUIDE_HIT |
| Sweden | South Park: Kyle Collection (Sweden) NO | SouthParkKyleCollection.se@NO | - | NO_GUIDE_HIT |
| Sweden | South Park: Stan Collection (Sweden) | SouthParkStanCollection.se@SE | - | NO_GUIDE_HIT |
| Sweden | South Park: Stan Collection (Sweden) DK | SouthParkStanCollection.se@DK | - | NO_GUIDE_HIT |
| Sweden | South Park: Stan Collection (Sweden) NO | SouthParkStanCollection.se@NO | - | NO_GUIDE_HIT |
| United Kingdom | Cartoon Network CEE Czech Republic | CartoonNetworkCEE.uk@CzechRepublic | - | NO_GUIDE_HIT |
| United Kingdom | Cartoon Network CEE Poland | CartoonNetworkCEE.uk@Poland | - | NO_GUIDE_HIT |
| United Kingdom | Cartoon Network CEE Ukraine (576p) | CartoonNetworkCEE.uk@Ukraine | - | NO_GUIDE_HIT |
| United Kingdom | MovieSphere UK | custom.moviesphere-uk | - | NO_GUIDE_HIT |
| United Kingdom | Mr Bean Animated ES (1080p) | MrBeanAnimated.uk@ES | - | NO_GUIDE_HIT |
| United Kingdom | Mr Bean Animated FR (1080p) | MrBeanAnimated.uk@FR | - | NO_GUIDE_HIT |
| United Kingdom | Top Gear (720p) | TopGear.uk@SD | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic 80s | Totalmusic80s.uk | - | NO_GUIDE_HIT |
| United Kingdom | Totalmusic Concerts | TotalmusicConcerts.uk | - | NO_GUIDE_HIT |
| United States | 30A Investment Pitch (720p) | 30AInvestmentPitch.us@SD | - | NO_GUIDE_HIT |
| United States | 30A We Love Cars (720p) | 30AWeLoveCars.us@SD | - | NO_GUIDE_HIT |
| United States | Ameritrade (1080p) [Not 24/7] | Ameritrade.us@SD | - | NO_GUIDE_HIT |
| United States | Animation+ (1080p) [Geo-blocked] | AnimationPlus.us@SD | - | NO_GUIDE_HIT |
| United States | ARTFLIX Movie Classics (720p) | ARTFLIXMovieClassics.us@SD | - | NO_GUIDE_HIT |
| United States | AXN Latin America | AXNLatinAmerica.us | - | NO_GUIDE_HIT |
| United States | Beverly Hillbillies | BeverlyHillbillies.us@US | - | NO_GUIDE_HIT |
| United States | Botflix TV (1080p) | BotflixTV.us@HD | - | NO_GUIDE_HIT |
| United States | Business Rockstars (720p) | BusinessRockstars.us@SD | - | NO_GUIDE_HIT |
| United States | California Music Channel | CaliforniaMusicChannel.us | - | NO_GUIDE_HIT |
| United States | Cartoon Network (United States) (720p) | CartoonNetwork.us@East | - | NO_GUIDE_HIT |
| United States | Cartoon Network Latin America | CartoonNetworkLatinAmerica.us@SouthAtlanticHD | - | NO_GUIDE_HIT |
| United States | Cartoon Network Latin America Brazil (720p) | CartoonNetworkLatinAmerica.us@Brazil | - | NO_GUIDE_HIT |
| United States | Cartoon Network Latin America North Atlantic (1080p) | CartoonNetworkLatinAmerica.us@NorthAtlantic | - | NO_GUIDE_HIT |
| United States | Cartoon Network Latin America South Atlantic (1080p) | CartoonNetworkLatinAmerica.us@SouthAtlantic | - | NO_GUIDE_HIT |
| United States | Cartoon Network Latin America South Pacific (576p) | CartoonNetworkLatinAmerica.us@SouthPacific | - | NO_GUIDE_HIT |
| United States | Cartoonito Latin America (1080p) | CartoonitoLatinAmerica.us@SD | - | NO_GUIDE_HIT |
| United States | CBS TV | CBSTV.us | - | NO_GUIDE_HIT |
| United States | Classic TV Crime Drama | ClassicTVCrimeDrama.us@SD | - | NO_GUIDE_HIT |
| United States | Classic TV Drama | ClassicTVDrama.us@SD | - | NO_GUIDE_HIT |
| United States | Classic TV: Families | ClassicTVFamilies.us@US | - | NO_GUIDE_HIT |
| United States | Comedy Central South Park | ComedyCentralSouthPark.us@BR | - | NO_GUIDE_HIT |
| United States | Comedy Central South Park LatAm | ComedyCentralSouthPark.us@LatAm | - | NO_GUIDE_HIT |
| United States | Detective Conan | DetectiveConan.us@Spain | - | NO_GUIDE_HIT |
| United States | Detective Conan France (720p) | DetectiveConan.us@France | - | NO_GUIDE_HIT |
| United States | Discovery Turbo Latin America (1080p) | DiscoveryTurboLatinAmerica.us@Panregional | - | NO_GUIDE_HIT |
| United States | DreamWorks Channel Asia (1080p) | DreamWorksChannelAsia.us@SD | - | NO_GUIDE_HIT |
| United States | EntrepreneurTV (720p) | EntrepreneurTV.us@SD | - | NO_GUIDE_HIT |
| United States | Epix | epix.us | - | NO_GUIDE_HIT |
| United States | Epix Hits | epixhits.us | - | NO_GUIDE_HIT |
| United States | Fierro a Fondo TV (1080p) | FierroaFondoTV.us@SD | - | NO_GUIDE_HIT |
| United States | Fox Business Network (576p) | FoxBusinessNetwork.us@SD | - | NO_GUIDE_HIT |
| United States | Fun Roads (720p) | FunRoads.us@SD | - | NO_GUIDE_HIT |
| United States | FXM | fxm.us | - | NO_GUIDE_HIT |
| United States | KidOO (1080p) [Geo-blocked] | KidOO.us@SD | - | NO_GUIDE_HIT |
| United States | Las Tortugas Ninja (720p) | LasTortugasNinja.us@LatAm | - | NO_GUIDE_HIT |
| United States | Lifetime Movies | lifetimemovies.us | - | NO_GUIDE_HIT |
| United States | MCN6 Music Channel (1080p) [Not 24/7] | MCN6MusicChannel.us@SD | - | NO_GUIDE_HIT |
| United States | Naruto (1080p) | Naruto.us@US | - | NO_GUIDE_HIT |
| United States | Naruto Brazil | Naruto.us@Brazil | - | NO_GUIDE_HIT |
| United States | Naruto en espanol | Narutoenespanol.us@SD | - | NO_GUIDE_HIT |
| United States | Naruto Germany (720p) | Naruto.us@Germany | - | NO_GUIDE_HIT |
| United States | Naruto Shippuden | NarutoShippuden.us@LatAm | - | NO_GUIDE_HIT |
| United States | Nickelodeon Pluto TV (720p) | NickelodeonPlutoTV.us@SD | - | NO_GUIDE_HIT |
| United States | One Piece | OnePiece.us@US | - | NO_GUIDE_HIT |
| United States | One Piece BR | OnePiece.us@BR | - | NO_GUIDE_HIT |
| United States | One Piece CA | OnePiece.us@CA | - | NO_GUIDE_HIT |
| United States | One Piece FR | OnePiece.us@FR | - | NO_GUIDE_HIT |
| United States | One Piece LatAm | OnePiece.us@LatAm | - | NO_GUIDE_HIT |
| United States | One Piece Spain | OnePiece.us@Spain | - | NO_GUIDE_HIT |
| United States | Placid (1080p) [Not 24/7] | Placid.us@EastHD | - | NO_GUIDE_HIT |
| United States | Pluto TV Anime | PlutoTVAnime.us@US | - | NO_GUIDE_HIT |
| United States | Pluto TV Anime Acao | PlutoTVAnimeAcao.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Anime BR | PlutoTVAnime.us@BR | - | NO_GUIDE_HIT |
| United States | Pluto TV Anime CA | PlutoTVAnime.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Anime LatAm | PlutoTVAnime.us@LatAm | - | NO_GUIDE_HIT |
| United States | Pluto TV Anime Movies | PlutoTVAnimeMovies.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Cars | PlutoTVCars.us@SD | - | NO_GUIDE_HIT |
| United States | Pluto TV Cars CA | PlutoTVCars.us@CA | - | NO_GUIDE_HIT |
| United States | Pluto TV Turbo | PlutoTVTurbo.us@BR | - | NO_GUIDE_HIT |
| United States | PowerNation TV (1080p) | PowerNationTV.us@SD | - | NO_GUIDE_HIT |
| United States | REV'N Action (720p) [Geo-blocked] | REVNAction.us@SD | - | NO_GUIDE_HIT |
| United States | Schwab Network (1080p) | SchwabNetwork.us@SD | - | NO_GUIDE_HIT |
| United States | Sonic TV (720p) | SonicTV.us@SD | - | NO_GUIDE_HIT |
| United States | Sony Movies | sony.us | - | NO_GUIDE_HIT |
| United States | South Park (United States) | SouthPark.us@CA | - | NO_GUIDE_HIT |
| United States | South Park En Francais | SouthParkEnFrancais.us@CA | - | NO_GUIDE_HIT |
| United States | South Park: Cartman Collection (United States) | SouthParkCartmanCollection.us@CA | - | NO_GUIDE_HIT |
| United States | South Park: Colecao Cartman | SouthParkColecaoCartman.us@BR | - | NO_GUIDE_HIT |
| United States | South Park: Colecao Kenny | SouthParkColecaoKenny.us@BR | - | NO_GUIDE_HIT |
| United States | South Park: Colecao Kyle | SouthParkColecaoKyle.us@BR | - | NO_GUIDE_HIT |
| United States | South Park: Colecao Stan | SouthParkColecaoStan.us@BR | - | NO_GUIDE_HIT |
| United States | South Park: Coleccion Cartman | SouthParkColeccionCartman.us@LatAm | - | NO_GUIDE_HIT |
| United States | South Park: Coleccion Kenny | SouthParkColeccionKenny.us@LatAm | - | NO_GUIDE_HIT |
| United States | South Park: Coleccion Kyle | SouthParkColeccionKyle.us@LatAm | - | NO_GUIDE_HIT |
| United States | South Park: Coleccion Stan | SouthParkColeccionStan.us@LatAm | - | NO_GUIDE_HIT |
| United States | South Park: Kenny Collection (United States) | SouthParkKennyCollection.us@CA | - | NO_GUIDE_HIT |
| United States | South Park: Kyle Collection (United States) | SouthParkKyleCollection.us@CA | - | NO_GUIDE_HIT |
| United States | South Park: Stan Collection (United States) | SouthParkStanCollection.us@CA | - | NO_GUIDE_HIT |
| United States | South Park: Welcome to Canada! | SouthParkWelcometoCanada.us@CA | - | NO_GUIDE_HIT |
| United States | Tokusato | Tokusato.us@Brazil | - | NO_GUIDE_HIT |
| United States | Toonami Aftermath West (480p) | ToonamiAftermath.us@West | - | NO_GUIDE_HIT |
| United States | Tooncast (1080p) | Tooncast.us@SD | - | NO_GUIDE_HIT |
| United States | Tooncast SouthAmerica (480p) | Tooncast.us@SouthAmerica | - | NO_GUIDE_HIT |
| United States | Whiplash Cinema | WhiplashCinema.us | - | NO_GUIDE_HIT |
| United States | Yu-Gi-Oh! (1080p) | YuGiOh.us@SD | - | NO_GUIDE_HIT |

## Published Guide Validation

- XMLTV channel IDs published: **678**
- Active playlist IDs present in the published guide: **678/1878 (36.1%)**
- Active playlist IDs with usable current/future programmes: **590/1878 (31.4%)**
- Active playlist IDs with usable programmes anywhere in the guide window (-6h/+7d): **590/1878 (31.4%)**
- Mapped playlist IDs present in the guide: **678/678 (100.0%)**
- Mapped playlist IDs with usable current/future programmes: **590/678 (87.0%)**
- Mapped playlist IDs with usable programmes anywhere in the guide window: **590/678 (87.0%)**
- Eligible programme rows published in the guide window: **51487**
- Mapped playlist IDs missing from the published XMLTV channel list: **0**
- Missing mapped playlist IDs: none
- Published mapped IDs without usable current/future programmes: **88**
- IDs without usable current/future programmes: 7XMusic.in@SD, AaryaaTV.in, B4UBhojpuri.in@SD, B4UKadak.in@SD, B4UMovies.in@India, BBCDrama.uk, BabesTV.us, BanglaJagoTV.in, BhojpuriCinema.in@SD, Captain.in@SD, ColorsSuper.in@SD, DarshanaTV.in@SD, DhoomMusic.in@SD, DishaTV.in@SD, DisneyChannel.in@HD, ETVCinema.in, ETVCinema.in@HD, ETVCinema.in@SD, ETVComedy.in@HD, EkamraCinema.in, EkamraMusiq.in, EpicMusic.in@SD, FashionOne.uk, Fast1.in@SD, GlobalPunjab.in, Goldmines.in@SD, GoldminesBollywood.in@SD, GoldminesMovies.in@SD, HosannaTV.in@Tamil, IsaiAruvi.in@SD, JalshaMovies.in@HD, KTVBangla.in@SD, KalaignarMurasu.in, LEOTV.cz, MHOneDilSe.in@SD, MakkahTV.sa, ManoranjanGrand.in, ManoranjanGrand.in@SD, ManoranjanMovies.in@SD, ManoranjanPrime.in@SD, Mastiii.in@SD, MetroTV.in@SD, NTCTV.in@SD, NationalGeographic.in@HD, NationalGeographic.in@SD, OnePaschima.in@SD, Only.Music.in, OscarMoviesBhojpuri.in@SD, PTCMusic.in@SD, PTCPunjabiGold.in@SD, PearTV.in@SD, PrarthanaTV.in@SD, PureBabes.us, RaftaarMedia.in@SD, SX3.es@SD, SangeetMarathi.in@SD, ShansonTV.ru, ShemarooUmang.in@SD, SiriKannadaAllTime.in, SkySportsCricket.ie (and 28 more)

## Source / Published Schedule Reconciliation

- IDs with usable current/future source schedule data: **633/1878 (33.7%)**
- IDs with usable current/future schedules in published XMLTV at report time: **590/1878 (31.4%)**
- IDs with usable programmes in the published guide's common -6h/+7d window: **590/1878 (31.4%)**
- Current/future source IDs without any usable published programme in that common window: **46**
- Source-scheduled IDs without a usable published programme in the common window: 7X Music (360p) (`7XMusic.in@SD`), Aaryaa TV (`AaryaaTV.in`), B4U Bhojpuri (1080p) (`B4UBhojpuri.in@SD`), B4U Kadak (`B4UKadak.in@SD`), B4U Movies (`B4UMovies.in@India`), Bhojpuri Cinema (`BhojpuriCinema.in@SD`), Captain (576p) (`Captain.in@SD`), Dhoom Music Bangla (`DhoomMusic.in@SD`), Disha TV (`DishaTV.in@SD`), ETV Cinema (`ETVCinema.in`), ETV Cinema HD (1080p) (`ETVCinema.in@HD`), ETV Cinema (396p) (`ETVCinema.in@SD`), Epic Music (`EpicMusic.in@SD`), Fast1 (`Fast1.in@SD`), Goldmines (`Goldmines.in@SD`), Goldmines Bollywood (`GoldminesBollywood.in@SD`), Goldmines Movies (`GoldminesMovies.in@SD`), Hosanna TV (`HosannaTV.in@Tamil`), Isai Aruvi (`IsaiAruvi.in@SD`), KTV Bangla (`KTVBangla.in@SD`), Metro TV (`MetroTV.in@SD`), NTC TV (`NTCTV.in@SD`), Only Music (`Only.Music.in`), Oscar Movies Bhojpuri (`OscarMoviesBhojpuri.in@SD`), PTC Music (`PTCMusic.in@SD`), PTC Punjabi Gold (`PTCPunjabiGold.in@SD`), Pear TV (`PearTV.in@SD`), Raftaar Media (`RaftaarMedia.in@SD`), Sangeet Marathi (`SangeetMarathi.in@SD`), Shemaroo Umang (`ShemarooUmang.in@SD`), Siri Kannada All Time (`SiriKannadaAllTime.in`), Sonar Bangla (`SonarBangla.in@SD`), Spondon (`Spondon.in@SD`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray Hit List (`StingrayHitList.ca`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray The Spa (`StingrayTheSpa.ca`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca`), Suriya TV (`SuriyaTV.in`), Tabbar Hits (`TabbarHits.in`), Ultimate TV (`UltimateTV.in@SD`), WildEarth (`WildEarth.za`), ZB Cinema (`ZBCinema.in`), Zee Cinema (`ZeeCinema.in@HD`), Zee Cinema (576p) (`ZeeCinema.in@SD`)
- IDs with an in-window published programme but no current/future source match at the later scan: **3**
- In-window published IDs not counted source-current/future: Odisha TV (`OdishaTV.in@SD`), Sony Entertainment TV (`SonyEntertainmentTelevision.in@SD`), IN: -HINDI- STAR SPORTS 1 HD (`Star Sports 1 Hindi HD.in`)
- Source-current/future IDs whose published programme is no longer current by report time: **46**
- Source-current/future IDs no longer current in the published guide: 7X Music (360p) (`7XMusic.in@SD`), Aaryaa TV (`AaryaaTV.in`), B4U Bhojpuri (1080p) (`B4UBhojpuri.in@SD`), B4U Kadak (`B4UKadak.in@SD`), B4U Movies (`B4UMovies.in@India`), Bhojpuri Cinema (`BhojpuriCinema.in@SD`), Captain (576p) (`Captain.in@SD`), Dhoom Music Bangla (`DhoomMusic.in@SD`), Disha TV (`DishaTV.in@SD`), ETV Cinema (`ETVCinema.in`), ETV Cinema HD (1080p) (`ETVCinema.in@HD`), ETV Cinema (396p) (`ETVCinema.in@SD`), Epic Music (`EpicMusic.in@SD`), Fast1 (`Fast1.in@SD`), Goldmines (`Goldmines.in@SD`), Goldmines Bollywood (`GoldminesBollywood.in@SD`), Goldmines Movies (`GoldminesMovies.in@SD`), Hosanna TV (`HosannaTV.in@Tamil`), Isai Aruvi (`IsaiAruvi.in@SD`), KTV Bangla (`KTVBangla.in@SD`), Metro TV (`MetroTV.in@SD`), NTC TV (`NTCTV.in@SD`), Only Music (`Only.Music.in`), Oscar Movies Bhojpuri (`OscarMoviesBhojpuri.in@SD`), PTC Music (`PTCMusic.in@SD`), PTC Punjabi Gold (`PTCPunjabiGold.in@SD`), Pear TV (`PearTV.in@SD`), Raftaar Media (`RaftaarMedia.in@SD`), Sangeet Marathi (`SangeetMarathi.in@SD`), Shemaroo Umang (`ShemarooUmang.in@SD`), Siri Kannada All Time (`SiriKannadaAllTime.in`), Sonar Bangla (`SonarBangla.in@SD`), Spondon (`Spondon.in@SD`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray Hit List (`StingrayHitList.ca`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray The Spa (`StingrayTheSpa.ca`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca`), Suriya TV (`SuriyaTV.in`), Tabbar Hits (`TabbarHits.in`), Ultimate TV (`UltimateTV.in@SD`), WildEarth (`WildEarth.za`), ZB Cinema (`ZBCinema.in`), Zee Cinema (`ZeeCinema.in@HD`), Zee Cinema (576p) (`ZeeCinema.in@SD`)
- Published current/future IDs not counted source-current/future: **3**
- Published current/future IDs not counted source-current/future: Odisha TV (`OdishaTV.in@SD`), Sony Entertainment TV (`SonyEntertainmentTelevision.in@SD`), IN: -HINDI- STAR SPORTS 1 HD (`Star Sports 1 Hindi HD.in`)


## Playlist EPG Headers

| Playlist | Header status |
|---|---|
| IPTV-Playlist.m3u | OK |
| BDIX-Playlist.m3u | OK |
| International-Playlist.m3u | OK |

## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **f61c38a3e13388833cf721031d0214366fb87b3a98a555d00da52100ddc58955**
- BDIX-Playlist.m3u SHA-256: **9cc2eaa4f9209e4d1a2576f9953f47240c176f15a929c41c94b9394f62323d81**
- International-Playlist.m3u SHA-256: **c816bf5276e62bc79a85429f23827cebe89bfd4f3fff34a67573ba9859f172aa**

