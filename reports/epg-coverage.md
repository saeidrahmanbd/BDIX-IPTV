# EPG Coverage & Mapping Report

Generated: **2026-10-23T08:52:49+00:00**

This report audits active unique channel identities across the playlist files in the repository. A source mapping is not counted as usable current/future coverage unless it has a valid programme interval and valid non-empty multilingual title data within the generator's -6-hour/+7-day window; English titles rank first, then Bengali, then other valid languages.
The XMLTV guide is published at **epg/epg.xml**. The published guide uses the playlist's tvg-id as the XMLTV channel ID, not the upstream provider's source ID.

## Overall Coverage

- Active unique playlist channel IDs audited: **1568**
- IDs with an EPG source mapping: **746/1568 (47.6%)**
- IDs with usable current/future source schedules (nonblank multilingual titles (English preferred, then Bengali, then other valid languages)): **701/1568 (44.7%)**
- IDs with no EPG source mapping: **822**

## Coverage by Playlist Group

| Group | Active IDs | Mapped IDs | Current/future | No mapping |
|---|---:|---:|---:|---:|
| Adult | 519 | 49 | 39 | 470 |
| Bangladesh | 71 | 3 | 3 | 68 |
| Documentary & Wildlife | 107 | 87 | 86 | 20 |
| Indian Bangla | 48 | 38 | 37 | 10 |
| Indian Entertainment | 166 | 146 | 138 | 20 |
| Indian Movies | 72 | 61 | 59 | 11 |
| Indian Music | 56 | 49 | 46 | 7 |
| International | 166 | 97 | 93 | 69 |
| Kids | 47 | 31 | 30 | 16 |
| New Backup | 59 | 44 | 43 | 15 |
| New Channels | 120 | 85 | 80 | 35 |
| Pakistani | 46 | 8 | 7 | 38 |
| Religious | 51 | 17 | 12 | 34 |
| Sports | 40 | 31 | 28 | 9 |

## Source Status

- **FAILED** — https://free-epg.de/api/epg/bd.xml.gz — 0 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window; HTTP Error 404: Not Found
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz — 1166 channel IDs; 766 IDs with usable current/future programmes; 43529 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz — 54 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz — 557 channel IDs; 21 IDs with usable current/future programmes; 1143 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-in.xml.gz — 415 channel IDs; 415 IDs with usable current/future programmes; 45282 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/in.xml — 206 channel IDs; 203 IDs with usable current/future programmes; 2221 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://i.mjh.nz/SamsungTVPlus/us.xml — 587 channel IDs; 585 IDs with usable current/future programmes; 5068 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epg.pw/xmltv/epg_IN.xml — 528 channel IDs; 21 IDs with usable current/future programmes; 1384 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epg.pw/api/epg.xml?channel_id=9374 — 1 channel IDs; 1 IDs with usable current/future programmes; 38 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epg.pw/api/epg.xml?channel_id=12504 — 1 channel IDs; 1 IDs with usable current/future programmes; 61 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml — 692 channel IDs; 638 IDs with usable current/future programmes; 36555 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz — 717 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml — 762 channel IDs; 759 IDs with usable current/future programmes; 80674 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml — 1490 channel IDs; 1413 IDs with usable current/future programmes; 76276 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml — 282 channel IDs; 282 IDs with usable current/future programmes; 13954 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml — 113 channel IDs; 100 IDs with usable current/future programmes; 22745 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/epg.xml.gz — 2273 channel IDs; 987 IDs with usable current/future programmes; 22303 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/jioepg.xml.gz — 1269 channel IDs; 210 IDs with usable current/future programmes; 4736 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://avkb.short.gy/tsepg.xml.gz — 717 channel IDs; 717 IDs with usable current/future programmes; 41000 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DISTROTV1.xml.gz — 90 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz — 690 channel IDs; 685 IDs with usable current/future programmes; 35466 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_RAKUTEN1.xml.gz — 1640 channel IDs; 1510 IDs with usable current/future programmes; 58084 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://raw.githubusercontent.com/nasimali/epg-auto/release/main-epg/epg_data/merged_epg.xml — 11 channel IDs; 10 IDs with usable current/future programmes; 1505 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz — 486 channel IDs; 385 IDs with usable current/future programmes; 9510 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://www.open-epg.com/files/unitedkingdom.xml.gz — 562 channel IDs; 532 IDs with usable current/future programmes; 20591 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz — 769 channel IDs; 730 IDs with usable current/future programmes; 21422 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://iptv-epg.org/files/epg-us.xml.gz — 12991 channel IDs; 12796 IDs with usable current/future programmes; 853044 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz — 804 channel IDs; 610 IDs with usable current/future programmes; 16092 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz — 345 channel IDs; 280 IDs with usable current/future programmes; 26572 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz — 696 channel IDs; 695 IDs with usable current/future programmes; 28198 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CH1.xml.gz — 751 channel IDs; 730 IDs with usable current/future programmes; 23413 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_CZ1.xml.gz — 1087 channel IDs; 521 IDs with usable current/future programmes; 13125 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DE1.xml.gz — 266 channel IDs; 248 IDs with usable current/future programmes; 13163 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_DO1.xml.gz — 56 channel IDs; 13 IDs with usable current/future programmes; 431 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_ES1.xml.gz — 373 channel IDs; 334 IDs with usable current/future programmes; 7716 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_FR1.xml.gz — 574 channel IDs; 516 IDs with usable current/future programmes; 20124 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_GR1.xml.gz — 321 channel IDs; 304 IDs with usable current/future programmes; 9374 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz — 143 channel IDs; 133 IDs with usable current/future programmes; 6432 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_HU1.xml.gz — 193 channel IDs; 164 IDs with usable current/future programmes; 11150 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_IT1.xml.gz — 195 channel IDs; 152 IDs with usable current/future programmes; 5203 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz — 163 channel IDs; 131 IDs with usable current/future programmes; 3160 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_MX1.xml.gz — 178 channel IDs; 159 IDs with usable current/future programmes; 4548 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_NL1.xml.gz — 159 channel IDs; 158 IDs with usable current/future programmes; 11158 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_PL1.xml.gz — 636 channel IDs; 584 IDs with usable current/future programmes; 64048 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_RO1.xml.gz — 370 channel IDs; 339 IDs with usable current/future programmes; 12130 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_SA2.xml.gz — 31 channel IDs; 30 IDs with usable current/future programmes; 2065 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_TR1.xml.gz — 178 channel IDs; 140 IDs with usable current/future programmes; 4140 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BEIN1.xml.gz — 80 channel IDs; 46 IDs with usable current/future programmes; 913 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR1.xml.gz — 266 channel IDs; 108 IDs with usable current/future programmes; 8711 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://epgshare01.online/epgshare01/epg_ripper_BR2.xml.gz — 97 channel IDs; 92 IDs with usable current/future programmes; 2922 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — https://hum.tv/schedule/ — 1 channel IDs; 1 IDs with usable current/future programmes; 21 eligible programme rows with valid non-empty titles in any language in the guide window
- **OK** — M3U4U XMLTV (private Actions secret) — 201 channel IDs; 0 IDs with usable current/future programmes; 0 eligible programme rows with valid non-empty titles in any language in the guide window

## Channels Requiring Attention

The table includes every active channel identity without usable current/future guide data, not only Indian channels. NO_GUIDE_HIT means no configured source could be matched; MAPPED_ID_ONLY means an identity was found but no usable schedule was available; MAPPED_NOT_CURRENTLY_FOUND means a retained mapping was not found in the currently configured feeds.

| Group | Channel | Playlist ID | EPG source ID | Status |
|---|---|---|---|---|
| Adult | 7 | custom.24-7-xxx-7 | Channel.7.uk | MAPPED_ID_ONLY |
| Adult | Babes TV | BabesTV.us | Babes.TV.cz | MAPPED_ID_ONLY |
| Adult | Babes Tv | custom.xxx-babes-tv | Babes.TV.cz | MAPPED_ID_ONLY |
| Adult | Dusk | custom.dusk | Dusk!.cz | MAPPED_ID_ONLY |
| Adult | Dusk | custom.xxx-dusk | Dusk!.cz | MAPPED_ID_ONLY |
| Adult | LEO TV | LEOTV.cz | Leo.cz | MAPPED_ID_ONLY |
| Adult | Prive Tv | custom.xxx-prive-tv | 142639 | MAPPED_ID_ONLY |
| Adult | Pure Babes | PureBabes.us | Pure.Babes.cz | MAPPED_ID_ONLY |
| Adult | True Amateurs | custom.xxx-true-amateurs | True.Amateurs.cz | MAPPED_ID_ONLY |
| Adult | Venus | custom.xxx-venus | Venus.TV.uk | MAPPED_ID_ONLY |
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
| Adult | Alba XXX HD 2 | AlbaXXXHD2.ru | - | NO_GUIDE_HIT |
| Adult | Alba Xxx Hd1 | custom.xxx-alba-xxx-hd1 | - | NO_GUIDE_HIT |
| Adult | Alba Xxx Hd2 | custom.xxx-alba-xxx-hd2 | - | NO_GUIDE_HIT |
| Adult | Alexis Texas | custom.24-7-xxx-alexis-texas | - | NO_GUIDE_HIT |
| Adult | Alura Jenson | custom.24-7-xxx-alura-jenson | - | NO_GUIDE_HIT |
| Adult | Amateur | custom.24-7-xxx-amateur | - | NO_GUIDE_HIT |
| Adult | Anal | custom.anal | - | NO_GUIDE_HIT |
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
| Adult | Compilation | custom.compilation | - | NO_GUIDE_HIT |
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
| Adult | Erotic 1 La2 | custom.erotic-1-la2 | - | NO_GUIDE_HIT |
| Adult | Erotic 2 La4 | custom.erotic-2-la4 | - | NO_GUIDE_HIT |
| Adult | Erotic 2 La6 | custom.erotic-2-la6 | - | NO_GUIDE_HIT |
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
| Adult | Fap TV 5 | custom.fap-tv-5 | - | NO_GUIDE_HIT |
| Adult | Fap TV 6 | custom.fap-tv-6 | - | NO_GUIDE_HIT |
| Adult | Fetish | custom.xxx-fetish | - | NO_GUIDE_HIT |
| Adult | FM Therapy 1 | custom.24-7-xxx-fm-therapy-1 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 2 | custom.24-7-xxx-fm-therapy-2 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 3 | custom.24-7-xxx-fm-therapy-3 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 4 | custom.24-7-xxx-fm-therapy-4 | - | NO_GUIDE_HIT |
| Adult | FM Therapy 5 | custom.24-7-xxx-fm-therapy-5 | - | NO_GUIDE_HIT |
| Adult | French Lover Europe | custom.xxx-french-lover-europe | - | NO_GUIDE_HIT |
| Adult | Gangbang | custom.gangbang | - | NO_GUIDE_HIT |
| Adult | Gangbang | custom.xxx-gangbang | - | NO_GUIDE_HIT |
| Adult | Gay 2 | custom.24-7-xxx-gay-2 | - | NO_GUIDE_HIT |
| Adult | Gay 3 | custom.24-7-xxx-gay-3 | - | NO_GUIDE_HIT |
| Adult | Gay Adult Tv | custom.xxx-gay-adult-tv | - | NO_GUIDE_HIT |
| Adult | Gay Latin | custom.24-7-xxx-gay-latin | - | NO_GUIDE_HIT |
| Adult | Glory Hole | custom.xxx-glory-hole | - | NO_GUIDE_HIT |
| Adult | Gloryhole | custom.24-7-xxx-gloryhole | - | NO_GUIDE_HIT |
| Adult | Gotmylf | custom.gotmylf | - | NO_GUIDE_HIT |
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
| Adult | Jasmin TV | JasminTV.lu | - | NO_GUIDE_HIT |
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
| Adult | m3u.Com Milf | custom.adultm3u-com-milf | - | NO_GUIDE_HIT |
| Adult | m3u.Com Pornstar | custom.adultm3u-com-pornstar | - | NO_GUIDE_HIT |
| Adult | m3u.Com Pov | custom.adultm3u-com-pov | - | NO_GUIDE_HIT |
| Adult | m3u.Com Rough | custom.adultm3u-com-rough | - | NO_GUIDE_HIT |
| Adult | m3u.Com Russian | custom.adultm3u-com-russian | - | NO_GUIDE_HIT |
| Adult | m3u.Com Threesome | custom.adultm3u-com-threesome | - | NO_GUIDE_HIT |
| Adult | Mature | custom.24-7-xxx-mature | - | NO_GUIDE_HIT |
| Adult | Mctv Anal | custom.xxx-mctv-anal | - | NO_GUIDE_HIT |
| Adult | Mctv Big Ass | custom.xxx-mctv-big-ass | - | NO_GUIDE_HIT |
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
| Adult | Mctv Latina | custom.xxx-mctv-latina | - | NO_GUIDE_HIT |
| Adult | Mctv Milf | custom.xxx-mctv-milf | - | NO_GUIDE_HIT |
| Adult | Mctv Pornstar | custom.xxx-mctv-pornstar | - | NO_GUIDE_HIT |
| Adult | Mctv Rough | custom.xxx-mctv-rough | - | NO_GUIDE_HIT |
| Adult | Mctv Russian | custom.xxx-mctv-russian | - | NO_GUIDE_HIT |
| Adult | Mctv Threesome | custom.xxx-mctv-threesome | - | NO_GUIDE_HIT |
| Adult | Mctv Woman | custom.xxx-mctv-woman | - | NO_GUIDE_HIT |
| Adult | Mia Khalifa | custom.24-7-xxx-mia-khalifa | - | NO_GUIDE_HIT |
| Adult | Mia Khalifa | custom.xxx-mia-khalifa | - | NO_GUIDE_HIT |
| Adult | Miami Tv Jenny Live [Not 24/7] | custom.xxx-miami-tv-jenny-live-not-24-7 | - | NO_GUIDE_HIT |
| Adult | Milf | custom.milf | - | NO_GUIDE_HIT |
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
| Adult | N1 Play Adult Club Seventeen 1 | custom.n1-play-adult-club-seventeen-1 | - | NO_GUIDE_HIT |
| Adult | N1 Play Adult Czech Bitch | custom.n1-play-adult-czech-bitch | - | NO_GUIDE_HIT |
| Adult | N1 Play Adult Dancing Bear | custom.n1-play-adult-dancing-bear | - | NO_GUIDE_HIT |
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
| Adult | Pornhub Cuckold | custom.pornhub-cuckold | - | NO_GUIDE_HIT |
| Adult | Pornstar | custom.xxx-pornstar | - | NO_GUIDE_HIT |
| Adult | POV | custom.24-7-xxx-pov | - | NO_GUIDE_HIT |
| Adult | Pov | custom.xxx-pov | - | NO_GUIDE_HIT |
| Adult | Princess Cum | custom.xxx-princess-cum | - | NO_GUIDE_HIT |
| Adult | Private La4 | custom.private-la4 | - | NO_GUIDE_HIT |
| Adult | Public Agent | custom.xxx-public-agent | - | NO_GUIDE_HIT |
| Adult | Pure Taboo | custom.24-7-xxx-pure-taboo | - | NO_GUIDE_HIT |
| Adult | Puretaboo | custom.xxx-puretaboo | - | NO_GUIDE_HIT |
| Adult | Rated | custom.24-7-xxx-rated | - | NO_GUIDE_HIT |
| Adult | Rated 3 | custom.24-7-xxx-rated-3 | - | NO_GUIDE_HIT |
| Adult | Real Girls Gone Bad | custom.xxx-real-girls-gone-bad | - | NO_GUIDE_HIT |
| Adult | Real Wife Stories | custom.xxx-real-wife-stories | - | NO_GUIDE_HIT |
| Adult | Reality Kings 2 | custom.24-7-xxx-reality-kings-2 | - | NO_GUIDE_HIT |
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
| Adult | Tiny4k 1 | custom.adult-tiny4k-1 | - | NO_GUIDE_HIT |
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
| Adult | Vip 21 Sextury | custom.vip-21-sextury | - | NO_GUIDE_HIT |
| Adult | Vip Live Cams Adult TV | custom.vip-live-cams-adult-tv | - | NO_GUIDE_HIT |
| Adult | Vip Mycamtv Squirt | custom.vip-mycamtv-squirt | - | NO_GUIDE_HIT |
| Adult | Vip Pink Erotic 3 | custom.vip-pink-erotic-3 | - | NO_GUIDE_HIT |
| Adult | Vip Pov | custom.vip-pov | - | NO_GUIDE_HIT |
| Adult | Visit-X | custom.visit-x | - | NO_GUIDE_HIT |
| Adult | Vivid TV Europe | VividTVEurope.uk | - | NO_GUIDE_HIT |
| Adult | Vividred Xxx | custom.xxx-vividred-xxx | - | NO_GUIDE_HIT |
| Adult | Vixen | custom.vixen | - | NO_GUIDE_HIT |
| Adult | Wank It Now | custom.xxx-wank-it-now | - | NO_GUIDE_HIT |
| Adult | Xxl | custom.xxx-xxl | - | NO_GUIDE_HIT |
| Adult | Xy Max | custom.xxx-xy-max | - | NO_GUIDE_HIT |
| Adult | Xy Mix | custom.xxx-xy-mix | - | NO_GUIDE_HIT |
| Adult | Xy Plus | custom.xxx-xy-plus | - | NO_GUIDE_HIT |
| Bangladesh | Ananda TV | AnandaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Asian TV | AsianTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | ATN Bangla | ATNBangla.bd | - | NO_GUIDE_HIT |
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
| Bangladesh | Independent TV | IndependentTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jago News 24 | JagoNews24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jamuna TV | JamunaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Jonmobhumi TV | JonmobhumiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Maasranga TV | MaasrangaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Matribhumi TV | MatribhumiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | ME TV | METV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Mohona TV | MohonaTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Movie Bangla | MovieBangla.bd | - | NO_GUIDE_HIT |
| Bangladesh | My TV | MyTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Nagorik TV | NagorikTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | News 21 | News21BanglaTV.bd@SD | - | NO_GUIDE_HIT |
| Bangladesh | News 24 | News24.bd | - | NO_GUIDE_HIT |
| Bangladesh | Nexus TV | NexusTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | NRB TV | NRBTV.ca | - | NO_GUIDE_HIT |
| Bangladesh | NTV | NTV-IN | - | NO_GUIDE_HIT |
| Bangladesh | NTV | NTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Probashi TV | ProbashiTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | Rajdhani TV | RajdhaniTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | RTV | RTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | SA TV | SATV.bd | - | NO_GUIDE_HIT |
| Bangladesh | SATV HD | custom.bdix.satv | - | NO_GUIDE_HIT |
| Bangladesh | Somoy TV | SomoyNewsTV.bd | - | NO_GUIDE_HIT |
| Bangladesh | SRK | SRK.bd | - | NO_GUIDE_HIT |
| Bangladesh | Star News | StarNews.bd | - | NO_GUIDE_HIT |
| Bangladesh | Star News | custom.star.news | - | NO_GUIDE_HIT |
| Bangladesh | TBN24 | TBN24.us | - | NO_GUIDE_HIT |
| Bangladesh | Thikana | ThikanaTV.us | - | NO_GUIDE_HIT |
| Bangladesh | Time Television | TimeTelevision.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | 4K Travel | Travel.us | 4K.TRAVEL.TV.distro | MAPPED_ID_ONLY |
| Documentary & Wildlife | Adventure Earth | AdventureEarth.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Alone | Alone.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Amazing Discoveries TV | AmazingDiscoveriesTV.in | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Animal Planet Gujarati | custom.animal-planet-gujarati | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic Adventure Earth | AutenticAdventureEarth.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Autentic History | AutenticHistory.de | - | NO_GUIDE_HIT |
| Documentary & Wildlife | DISCOVERY BANGLA | custom.bdix.discoverybangla | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Discovery Velocity | discoveryvelocity.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Documentary+ 2 | Documentary2.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Inside Crime | InsideCrime.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Mystery TV | MysteryTV.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Nat Geo Wild Telugu | custom.nat-geo-wild-telugu | - | NO_GUIDE_HIT |
| Documentary & Wildlife | PBS Arts | PBSArts.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | RT Documentary | RTDocumentary.ru | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Terra Mater WILD English | TerraMaterWILDEnglish.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Tochka.rf | Tochkarf.ru | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Travel Channel East | travel.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Watch Mojo (EU) | WatchMojo.us | - | NO_GUIDE_HIT |
| Documentary & Wildlife | WaterBear | WaterBear.ch | - | NO_GUIDE_HIT |
| Documentary & Wildlife | Wild Planet | WildPlanet.us | - | NO_GUIDE_HIT |
| Indian Bangla | Tara TV | TaraTV.in | Tara.TV.in | MAPPED_ID_ONLY |
| Indian Bangla | Bangla Plus | BanglaPlus.in | - | NO_GUIDE_HIT |
| Indian Bangla | Jalsha Bangla BD | JalshaBanglaBD.bd | - | NO_GUIDE_HIT |
| Indian Bangla | Jhankar TV | JhankarTV.ca | - | NO_GUIDE_HIT |
| Indian Bangla | JTV Bangla | JTVBangla.in@SD | - | NO_GUIDE_HIT |
| Indian Bangla | JTV Classic | JTVClassic.in | - | NO_GUIDE_HIT |
| Indian Bangla | Orange Bangla TV | OrangeBanglaTV.in@SD | - | NO_GUIDE_HIT |
| Indian Bangla | Sananda | SanandaTV.in | - | NO_GUIDE_HIT |
| Indian Bangla | Sananda TV | custom.sananda-tv | - | NO_GUIDE_HIT |
| Indian Bangla | SNB Cinema | SNBCinema.in | - | NO_GUIDE_HIT |
| Indian Bangla | Star Bangla | StarBangla.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Global Punjab | GlobalPunjab.in | Global.Punjab.in | MAPPED_ID_ONLY |
| Indian Entertainment | Kalaignar Murasu | KalaignarMurasu.in | MURASU.in | MAPPED_ID_ONLY |
| Indian Entertainment | Manoranjan Prime | ManoranjanPrime.in@SD | 154892 | MAPPED_ID_ONLY |
| Indian Entertainment | One Paschima | OnePaschima.in@SD | One.Paschima.in | MAPPED_ID_ONLY |
| Indian Entertainment | Prarthana TV | PrarthanaTV.in@SD | Prarthana.TV.in | MAPPED_ID_ONLY |
| Indian Entertainment | Sony Entertainment TV | SonyEntertainmentTelevision.in@SD | Sony.Entertainment.Television.in | MAPPED_ID_ONLY |
| Indian Entertainment | Suriyan TV | SuriyanTV.in@SD | ts1384 | MAPPED_ID_ONLY |
| Indian Entertainment | Odisha TV | OdishaTV.in@SD | OdishaTV.in | MAPPED_NOT_CURRENTLY_FOUND |
| Indian Entertainment | Baiscope TV | BaiscopeTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Colors MENA | ColorsMENA.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Flowers US | Flowers.us | - | NO_GUIDE_HIT |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Kerala Vision | KeralaVision.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Mei Alai TV | MeiAlaiTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | MH One Prime | Mh1Prime.in | - | NO_GUIDE_HIT |
| Indian Entertainment | MNTV (Tamil) | MarutamTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | NKR TV Kannada | NKRTVKannada.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Oli TV | OliTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Pardesi TV | PardesiTV.ca | - | NO_GUIDE_HIT |
| Indian Entertainment | Pulari TV | PulariTV.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Q TV | QTV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Rajdhani | custom.rajdhani | - | NO_GUIDE_HIT |
| Indian Entertainment | SADA TV | SADATV.in | - | NO_GUIDE_HIT |
| Indian Entertainment | Sooriyan TV | SooriyanTV.ca@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Starnet | Starnet.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | Swantham | Swantham.in@SD | - | NO_GUIDE_HIT |
| Indian Entertainment | UTV Palakkad | UTVPalakkad.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Colors Kannada Movies | custom.colors-kannada-movies-lqp30 | COLORS.KANNADA.MOVIES.in | MAPPED_ID_ONLY |
| Indian Movies | Ekamra Cinema | EkamraCinema.in | Ekamra.Cinema.in | MAPPED_ID_ONLY |
| Indian Movies | Bangla Cinema | BanglaCinema.in | - | NO_GUIDE_HIT |
| Indian Movies | Goldmines 2 | Goldmines2.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Goldmines Action | GoldminesAction.in | - | NO_GUIDE_HIT |
| Indian Movies | Hindi Movie Classic 24 | new.hindi.movie.classic.24 | - | NO_GUIDE_HIT |
| Indian Movies | Indywood TV | IndywoodTV.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | K Cine | KCine.in | - | NO_GUIDE_HIT |
| Indian Movies | Maha Movie | MahaMovie.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | Mango | Mango.in@SD | - | NO_GUIDE_HIT |
| Indian Movies | MH One Movies | MHOneMovies.in | - | NO_GUIDE_HIT |
| Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | - | NO_GUIDE_HIT |
| Indian Movies | South Movies | SouthMovies.in | - | NO_GUIDE_HIT |
| Indian Music | Ekamra Musiq | EkamraMusiq.in | Ekamra.Musiq.in | MAPPED_ID_ONLY |
| Indian Music | Mastiii | Mastiii.in@SD | Mastiii.in | MAPPED_ID_ONLY |
| Indian Music | Steelbird Music | SteelbirdMusic.in@SD | Steelbird.Music.in | MAPPED_ID_ONLY |
| Indian Music | 7X Punjabi | 7XPunjabi.in | - | NO_GUIDE_HIT |
| Indian Music | Andy Haryana | AndyHaryana.in@SD | - | NO_GUIDE_HIT |
| Indian Music | Deewana | DeewanaHD.in | - | NO_GUIDE_HIT |
| Indian Music | Hindi Hits | HindiHits.in | - | NO_GUIDE_HIT |
| Indian Music | Raj Music | custom.raj-music-lpiaw | - | NO_GUIDE_HIT |
| Indian Music | Rang Rangoli | RangRangoli.in | - | NO_GUIDE_HIT |
| Indian Music | YRF Music Nepal | YRFMusic.in@Nepal | - | NO_GUIDE_HIT |
| International | LAFF TV | LAFFTV.us | Laff.us2 | MAPPED_ENDED |
| International | BBC Drama | BBCDrama.uk | BBCDrama.au | MAPPED_ID_ONLY |
| International | Fashion One | FashionOne.uk | Fashion.One.cz | MAPPED_ID_ONLY |
| International | Shanson TV | ShansonTV.ru | Shanson.TV.cz | MAPPED_ID_ONLY |
| International | 1Mus | 1Mus.us | - | NO_GUIDE_HIT |
| International | Aflam | custom.aflam | - | NO_GUIDE_HIT |
| International | Afrobeats | Afrobeats.us | - | NO_GUIDE_HIT |
| International | AMC Latin America Brazil | custom.amc-latin-america-brazil | - | NO_GUIDE_HIT |
| International | AMG TV Classic | AMGTVClassic.us | - | NO_GUIDE_HIT |
| International | Arabica TV | ArabicaTV.us | - | NO_GUIDE_HIT |
| International | Arabica TV | custom.arabica-tv | - | NO_GUIDE_HIT |
| International | AVA FAMILY | AVAFAMILY.us | - | NO_GUIDE_HIT |
| International | AVA SERIES | AVASERIES.us | - | NO_GUIDE_HIT |
| International | AXN Asia Taiwan | custom.axn-asia-taiwan | - | NO_GUIDE_HIT |
| International | AXN Black Poland | custom.axn-black-poland | - | NO_GUIDE_HIT |
| International | AXN Latin America | AXNLatinAmerica.us | - | NO_GUIDE_HIT |
| International | California Music Channel | CaliforniaMusicChannel.us | - | NO_GUIDE_HIT |
| International | CANADA ONE | custom.bdix.canadaone | - | NO_GUIDE_HIT |
| International | CBS TV | CBSTV.us | - | NO_GUIDE_HIT |
| International | CCTV-11 | CCTV11.cn | - | NO_GUIDE_HIT |
| International | Classic Movies | ClassicMovies.us | - | NO_GUIDE_HIT |
| International | Dance TV | DanceTV.us | - | NO_GUIDE_HIT |
| International | Digital Fashion | DigitalFashion.us | - | NO_GUIDE_HIT |
| International | DW News | DWNews.de | - | NO_GUIDE_HIT |
| International | Epic Music Digital | custom.epic-music-digital | - | NO_GUIDE_HIT |
| International | Epix | epix.us | - | NO_GUIDE_HIT |
| International | Epix Hits | epixhits.us | - | NO_GUIDE_HIT |
| International | EU Music | EUMusic.ua | - | NO_GUIDE_HIT |
| International | FON Music | FONMusic.us | - | NO_GUIDE_HIT |
| International | FXM | fxm.us | - | NO_GUIDE_HIT |
| International | Guangxi Variety & Travel Channel | GuangxiVarietyTravelChannel.cn | - | NO_GUIDE_HIT |
| International | iFilm English | iFilmEnglish.ir | - | NO_GUIDE_HIT |
| International | Kronehit | Kronehit.at | - | NO_GUIDE_HIT |
| International | Lifetime Movies | lifetimemovies.us | - | NO_GUIDE_HIT |
| International | M20 Music | M20Music.us | - | NO_GUIDE_HIT |
| International | MBC Drama USA | MBCDramaUSA.us | - | NO_GUIDE_HIT |
| International | Mei Ah Movie Channel | MeiAhMovieChannel.hk | - | NO_GUIDE_HIT |
| International | Movie Dome Family | MovieDomeFamily.us | - | NO_GUIDE_HIT |
| International | Movies Thriller | MoviesThriller.sa@SD | - | NO_GUIDE_HIT |
| International | MovieSphere AU | custom.moviesphere-au | - | NO_GUIDE_HIT |
| International | MovieSphere UK | custom.moviesphere-uk | - | NO_GUIDE_HIT |
| International | My Cinema | MyCinema.us | - | NO_GUIDE_HIT |
| International | MyTime Movie | MyTimeMovieNetwork.uk@SD | - | NO_GUIDE_HIT |
| International | MyTime Movie Network East | MyTimeMovieNetworkEast.us | - | NO_GUIDE_HIT |
| International | Oxygen Music | OxygenMusic.us | - | NO_GUIDE_HIT |
| International | P2M TV | P2MTV.fr | - | NO_GUIDE_HIT |
| International | POP World TV | POPWorldTV.es | - | NO_GUIDE_HIT |
| International | PowerTürk TV | PowerTurkTV.tr | - | NO_GUIDE_HIT |
| International | Rakuten Movies | RakutenMovies | - | NO_GUIDE_HIT |
| International | Rakuten TV Action Movies UK | RakutenTVActionMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Comedy Movies UK | RakutenTVComedyMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Drama Movies UK | RakutenTVDramaMovies.es@UK | - | NO_GUIDE_HIT |
| International | Rakuten TV Family Movies UK | RakutenTVFamilyMovies.es@UK | - | NO_GUIDE_HIT |
| International | Sony Movies | SonyMovies.in | - | NO_GUIDE_HIT |
| International | Sony Movies | sony.us | - | NO_GUIDE_HIT |
| International | Sony One Favoris | SonyOneFavoris.fr | - | NO_GUIDE_HIT |
| International | Sony One Hits Action | SonyOneHitsAction.fr | - | NO_GUIDE_HIT |
| International | Sony One Hits Comedie | SonyOneHitsComedie.fr | - | NO_GUIDE_HIT |
| International | Sparkle Movies | GBAJ400042T1 | - | NO_GUIDE_HIT |
| International | Stingray Rock Alternative | StingrayRockAlternative.ca | - | NO_GUIDE_HIT |
| International | Totalmusic | Totalmusic.uk | - | NO_GUIDE_HIT |
| International | Totalmusic 80s | Totalmusic80s.uk | - | NO_GUIDE_HIT |
| International | Totalmusic Concerts | TotalmusicConcerts.uk | - | NO_GUIDE_HIT |
| International | Trace UK | TraceUK.uk | - | NO_GUIDE_HIT |
| International | Trace Urban (Australia) | custom.trace-urban-australia | - | NO_GUIDE_HIT |
| International | Ua Music | custom.ua-music | - | NO_GUIDE_HIT |
| International | V2BEAT | custom.v2beat | - | NO_GUIDE_HIT |
| International | Vevo '70s & '80s | Vevo70s80s.us | - | NO_GUIDE_HIT |
| International | Vevo '90s & '00s | Vevo90s00s.us | - | NO_GUIDE_HIT |
| International | Vevo Hip Hop & R&B | GBBD2300001C0 | - | NO_GUIDE_HIT |
| International | Whiplash Cinema | WhiplashCinema.us | - | NO_GUIDE_HIT |
| International | XITE Hits UK | XITEHits.nl@UK | - | NO_GUIDE_HIT |
| International | Young Hollywood | YoungHollywood.us | - | NO_GUIDE_HIT |
| Kids | Disney Channel India | DisneyChannel.in@HD | DISNEY.CHANNEL.in | MAPPED_ID_ONLY |
| Kids | ADN TV+ | ADNTVPlus.fr | - | NO_GUIDE_HIT |
| Kids | Afarin TV | AfarinTV.iq | - | NO_GUIDE_HIT |
| Kids | Bantul the Great | BantulTheGreat.us | - | NO_GUIDE_HIT |
| Kids | Doraemon TV | DoraemonTV.us | - | NO_GUIDE_HIT |
| Kids | Epic Kids Digital | EpicKidsDigital.us | - | NO_GUIDE_HIT |
| Kids | Lego Channel | LegoChannel.us@SD | - | NO_GUIDE_HIT |
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
| New Backup | Star Movies (India) | StarMovies.in@HD | Star.Movies.in | MAPPED_ID_ONLY |
| New Backup | Ananda TV | AnandaTV.bd@SD | - | NO_GUIDE_HIT |
| New Backup | DBC News | DBCNews.bd@SD | - | NO_GUIDE_HIT |
| New Backup | Ekhon TV | EkhonTV.bd@SD | - | NO_GUIDE_HIT |
| New Backup | Epic Bharat Digital | EpicBharat.in@Digital | - | NO_GUIDE_HIT |
| New Backup | Gazi TV | GaziTV.bd@SD | - | NO_GUIDE_HIT |
| New Backup | Green TV | GreenTV.bd@SD | - | NO_GUIDE_HIT |
| New Backup | Hosanna TV Global | HosannaTV.in@Global | - | NO_GUIDE_HIT |
| New Backup | Hosanna TV Hindi | HosannaTV.in@Hindi | - | NO_GUIDE_HIT |
| New Backup | Maasranga TV | MaasrangaTV.bd@SD | - | NO_GUIDE_HIT |
| New Backup | National Geographic Wild (India) | NationalGeographicWild.in@HD | - | NO_GUIDE_HIT |
| New Backup | Nickelodeon (India) | Nickelodeon.in@SD | - | NO_GUIDE_HIT |
| New Backup | Rajdhani TV | RajdhaniTV.bd@SD | - | NO_GUIDE_HIT |
| New Backup | T Sports | TSports.bd@SD | - | NO_GUIDE_HIT |
| New Backup | Travelxp 4K HDR (2160p) [Geo-blocked] | Travelxp.in@4KHDR | - | NO_GUIDE_HIT |
| New Backup | Zoom (India) Nepal | Zoom.in@Nepal | - | NO_GUIDE_HIT |
| New Channels | Aastha Tamil | AasthaTamil.in@SD | Aastha.Tamil.in | MAPPED_ID_ONLY |
| New Channels | Ananda Barta | AnandaBarta.in@SD | Ananda.Barta.in | MAPPED_ID_ONLY |
| New Channels | Ashwaveega News 24x7 | AshwaveegaNews24x7.in@SD | jtv3371 | MAPPED_ID_ONLY |
| New Channels | Disney Junior (India) | DisneyJunior.in@SD | Disney.Junior.in | MAPPED_ID_ONLY |
| New Channels | Friends TV | FriendsTV.in@SD | Friends.TV.in | MAPPED_ID_ONLY |
| New Channels | Aastha Prime 1 | AasthaPrime1.in@SD | - | NO_GUIDE_HIT |
| New Channels | ABN Andhra Jyoti | ABNAndhraJyoti.in@SD | - | NO_GUIDE_HIT |
| New Channels | Adhyatm TV | AdhyatmTV.in@SD | - | NO_GUIDE_HIT |
| New Channels | AKD Calcutta News | AKDCalcuttaNews.in@SD | - | NO_GUIDE_HIT |
| New Channels | Amrit Gurbani | AmritGurbani.in@SD | - | NO_GUIDE_HIT |
| New Channels | Anandpur Live | AnandpurLive.in@HD | - | NO_GUIDE_HIT |
| New Channels | APN | APN.in@SD | - | NO_GUIDE_HIT |
| New Channels | Arputhar Yesu TV | ArputharYesuTV.in@SD | - | NO_GUIDE_HIT |
| New Channels | ATN Music | ATNMusic.bd@SD | - | NO_GUIDE_HIT |
| New Channels | Awaaz India TV (720p) [Not 24/7] | AwaazIndiaTV.in@SD | - | NO_GUIDE_HIT |
| New Channels | Bhakthi TV | BhakthiTV.in@SD | - | NO_GUIDE_HIT |
| New Channels | BT TV | BTTV.in@SD | - | NO_GUIDE_HIT |
| New Channels | CCV | CCV.in@SD | - | NO_GUIDE_HIT |
| New Channels | Chardikla Gurbaani TV | ChardiklaGurbaaniTV.in@SD | - | NO_GUIDE_HIT |
| New Channels | Chardikla Time TV North America | ChardiklaTimeTVNorthAmerica.in@SD | - | NO_GUIDE_HIT |
| New Channels | Chhaya Chitram Telugu | ChhayaChitramTelugu.in@SD | - | NO_GUIDE_HIT |
| New Channels | Dhamaal (576p) [Geo-blocked] | Dhamaal.in@SD | - | NO_GUIDE_HIT |
| New Channels | E-Vidya 10 | EVidya10.in@SD | - | NO_GUIDE_HIT |
| New Channels | E-Vidya 11 | EVidya11.in@SD | - | NO_GUIDE_HIT |
| New Channels | E-Vidya 12 | EVidya12.in@SD | - | NO_GUIDE_HIT |
| New Channels | E-Vidya 4 | EVidya4.in@SD | - | NO_GUIDE_HIT |
| New Channels | E-Vidya 5 | EVidya5.in@SD | - | NO_GUIDE_HIT |
| New Channels | E-Vidya 6 | EVidya6.in@SD | - | NO_GUIDE_HIT |
| New Channels | E-Vidya 7 | EVidya7.in@SD | - | NO_GUIDE_HIT |
| New Channels | E-Vidya 8 | EVidya8.in@SD | - | NO_GUIDE_HIT |
| New Channels | E-Vidya 9 | EVidya9.in@SD | - | NO_GUIDE_HIT |
| New Channels | Epic TV Digital | EpicTV.in@Digital | - | NO_GUIDE_HIT |
| New Channels | HSTV | HSTV.in@SD | - | NO_GUIDE_HIT |
| New Channels | India Talkies | IndiaTalkies.in@SD | - | NO_GUIDE_HIT |
| New Channels | Kalika TV | KalikaTV.in@SD | - | NO_GUIDE_HIT |
| New Channels | KCL TV | KCLTV.in@SD | - | NO_GUIDE_HIT |
| New Channels | Madani Channel Bangla | MadaniChannelBangla.bd@SD | - | NO_GUIDE_HIT |
| New Channels | NAN TV | NANTV.bd@SD | - | NO_GUIDE_HIT |
| New Channels | Rupashi Bangla TV | RupashiBanglaTV.bd@SD | - | NO_GUIDE_HIT |
| New Channels | Vokta TV | VoktaTV.bd@SD | - | NO_GUIDE_HIT |
| Pakistani | PTV Global | PTVGlobal.pk | PTV.Global.uk | MAPPED_ID_ONLY |
| Pakistani | 5AAB TV | 5AABTV.ca | - | NO_GUIDE_HIT |
| Pakistani | 8XM | 8XM.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | A Plus | custom.a-plus | - | NO_GUIDE_HIT |
| Pakistani | Aaj Entertainment | AajEntertainment.pk | - | NO_GUIDE_HIT |
| Pakistani | Apna Channel | ApnaChannel.pk | - | NO_GUIDE_HIT |
| Pakistani | ARY Family | custom.ary-family | - | NO_GUIDE_HIT |
| Pakistani | ARY Music | custom.ary-music-tumyo | - | NO_GUIDE_HIT |
| Pakistani | ATV Entertainment | custom.atv-entertainment | - | NO_GUIDE_HIT |
| Pakistani | aur LIFE | aurLIFE.pk | - | NO_GUIDE_HIT |
| Pakistani | AVT Khyber | AVTKhyber.pk | - | NO_GUIDE_HIT |
| Pakistani | Avt Khyber TV | custom.avt-khyber-tv | - | NO_GUIDE_HIT |
| Pakistani | Awaz TV | custom.awaz-tv | - | NO_GUIDE_HIT |
| Pakistani | Bol Entertainment | BolEntertainment.pk | - | NO_GUIDE_HIT |
| Pakistani | City 42 | City42.pk | - | NO_GUIDE_HIT |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Discover Pakistan | custom.discover-pikstan | - | NO_GUIDE_HIT |
| Pakistani | Express Entertainment | ExpressEntertainment.pk | - | NO_GUIDE_HIT |
| Pakistani | Falak TV | FalakTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Geo Entertainment | custom.geo-entertainment | - | NO_GUIDE_HIT |
| Pakistani | Geo Kahani | GeoKahani.pk | - | NO_GUIDE_HIT |
| Pakistani | Geo Super | GeoSuper.pk | - | NO_GUIDE_HIT |
| Pakistani | Geo Tezz | GeoTez.pk | - | NO_GUIDE_HIT |
| Pakistani | Green Entertainment | custom.green-ent | - | NO_GUIDE_HIT |
| Pakistani | HUM Sitaray | HUMSitaray.pk | - | NO_GUIDE_HIT |
| Pakistani | Hum Sitaray World | custom.hum-sitery-world | - | NO_GUIDE_HIT |
| Pakistani | Jalwa Music | custom.jalwa-music | - | NO_GUIDE_HIT |
| Pakistani | Jalwa TV | JalwaTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | Joo Music | JooMusic.pk | - | NO_GUIDE_HIT |
| Pakistani | Kay 2 | custom.kay-2 | - | NO_GUIDE_HIT |
| Pakistani | Lahore Rang | LahoreRang.pk | - | NO_GUIDE_HIT |
| Pakistani | Paighan TV | PaighanTV.pk@SD | - | NO_GUIDE_HIT |
| Pakistani | PTV Home | ptvhome.pk | - | NO_GUIDE_HIT |
| Pakistani | PTV World | ptvworld.pk | - | NO_GUIDE_HIT |
| Pakistani | See TV | SeeTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Tag TV | TagTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Urdu 1 | urdu1.pk | - | NO_GUIDE_HIT |
| Pakistani | Waseb TV | WasebTV.pk | - | NO_GUIDE_HIT |
| Pakistani | Waseeb TV | custom.waseeb-tv | - | NO_GUIDE_HIT |
| Religious | Ahlulbayt TV | AhlulbaytTV.uk | Ahlulbayt.TV.uk | MAPPED_ID_ONLY |
| Religious | Al Qamar | AlQamarTV.ae | Al.Qamar.TV.ae | MAPPED_ID_ONLY |
| Religious | Dua Channel | DuaChannel.sa | Dua.Channel.ae | MAPPED_ID_ONLY |
| Religious | Hidayat TV | HidayatTV.uk | Hidayat.TV.uk | MAPPED_ID_ONLY |
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
| Religious | Mecca TV | custom.mecca-tv | - | NO_GUIDE_HIT |
| Religious | Medina Live | MedinaLive.bd | - | NO_GUIDE_HIT |
| Religious | Peace TV | custom.peace-tv | - | NO_GUIDE_HIT |
| Religious | Peace TV Bangla | PeaceTVBangla.ae | - | NO_GUIDE_HIT |
| Religious | Peace TV English | PeaceTVEnglish.ae | - | NO_GUIDE_HIT |
| Religious | Peace TV Urdu | PeaceTVUrdu.pk | - | NO_GUIDE_HIT |
| Religious | Peace TV Urdu | custom.peace.tv.urdu | - | NO_GUIDE_HIT |
| Religious | Quran | custom.quran | - | NO_GUIDE_HIT |
| Religious | Quran - أحمد علي العجمي Ahmad Bin Ali Al-Ajmi | custom.quran-ahmad-bin-ali-al-ajmi | - | NO_GUIDE_HIT |
| Religious | Quran - سعد الغامدي Saad Al-Ghamdi | custom.quran-saad-al-ghamdi | - | NO_GUIDE_HIT |
| Religious | Quran - سعود الشريم Saud Al Shuraim | custom.quran-saud-al-shuraim | - | NO_GUIDE_HIT |
| Religious | Quran - عبد الرحمان السديس Abdul Rahman Al-Sudais | custom.quran-abdul-rahman-al-sudais | - | NO_GUIDE_HIT |
| Religious | Quran - علي الحذيفي Ali Al Huthaify | custom.quran-ali-al-huthaify | - | NO_GUIDE_HIT |
| Religious | Quran - علي جابر Ali Jaber | custom.quran-ali-jaber | - | NO_GUIDE_HIT |
| Religious | Quran - ماهر المعيقلي Maher Al Meaqli | custom.quran-maher-al-meaqli | - | NO_GUIDE_HIT |
| Religious | Quran - مشاري العفاسي Mishary Alafasi | custom.quran-mishary-alafasi | - | NO_GUIDE_HIT |
| Religious | Quran - ياسر الدوسري Yasser Al-Dosari | custom.quran-yasser-al-dosari | - | NO_GUIDE_HIT |
| Religious | Quran TV | QuranTV.iq | - | NO_GUIDE_HIT |
| Religious | Sunnah TV | custom.sunnah-tv | - | NO_GUIDE_HIT |
| Religious | Zainabia Channel | ZainabiaChannel.sa | - | NO_GUIDE_HIT |
| Sports | FITE 24/7 | FITE247.us@SD | FITE247.us | MAPPED_ID_ONLY |
| Sports | Sky Sports Cricket | SkySportsCricket.ie | SkySportsCricket.ie | MAPPED_ID_ONLY |
| Sports | IN: -HINDI- STAR SPORTS 1 HD | Star Sports 1 Hindi HD.in | StarSports1HindiHD.in | MAPPED_NOT_CURRENTLY_FOUND |
| Sports | A Sports | ASports.pk | - | NO_GUIDE_HIT |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | - | NO_GUIDE_HIT |
| Sports | Goal TV | GoalTV.in | - | NO_GUIDE_HIT |
| Sports | PK Sports | PKSports.pk@SD | - | NO_GUIDE_HIT |
| Sports | PK: GEO SUPER | custom.bdix.geosuper | - | NO_GUIDE_HIT |
| Sports | PTV Sports | PTVSports.pk | - | NO_GUIDE_HIT |
| Sports | T Sports | TSports.bd | - | NO_GUIDE_HIT |
| Sports | Ten Sports | TenSports.pk | - | NO_GUIDE_HIT |
| Sports | Willow TV | WillowTV.us | - | NO_GUIDE_HIT |

## Published Guide Validation

- XMLTV channel IDs published: **460**
- Active playlist IDs present in the published guide: **361/1568 (23.0%)**
- Active playlist IDs with usable current/future programmes: **191/1568 (12.2%)**
- Active playlist IDs with usable programmes anywhere in the guide window (-6h/+7d): **191/1568 (12.2%)**
- Mapped playlist IDs present in the guide: **361/746 (48.4%)**
- Mapped playlist IDs with usable current/future programmes: **191/746 (25.6%)**
- Mapped playlist IDs with usable programmes anywhere in the guide window: **191/746 (25.6%)**
- Eligible programme rows published in the guide window: **13368**
- Mapped playlist IDs missing from the published XMLTV channel list: **385**
- Missing mapped playlist IDs: 10TV.in@SD, 22ScopeNews.in@SD, 24News.in@SD, 4SiDESTV.in@SD, 4TVNews.in@SD, 99TV.in@SD, 9PlusNews.in@SD, ABPAnanda.in@SD, ABPAsmita.in@SD, ABPGanga.in@SD, ABPMajha.in@SD, ABPNews.in@SD, AMCThrillers.us, ANBNews.in@SD, ARYDigital.pk, AXS.us, AXSTV.us, AadinathTV.in@SD, AagaazTimes.in@SD, AajKiKhabar.in@SD, AajTak.in, AajTak.in@HD, AajTak.in@SD, AaseervathamTV.in@SD, Aastha.in@HD, AasthaGujarati.in@SD, AasthaKannada.in@SD, AasthaTamil.in@SD, AasthaTelugu.in@SD, AhlulbaytTV.uk, AkhonKolkata.in@SD, AlJazeera.qa, AllTimeMovies.in@SD, AmarBanglaDigital.in, AmarUjala.in@SD, AnandWariTV.in@SD, AnandaBarta.in@SD, AndTV.in@HD, Andflix.in, Andpictures.in, AngelTV.in@India, AnimalPlanet.in@HD, AnmolTV.in@SD, AradanaTV.in@SD, ArgusNews.in@SD, Arirang.kr, AryanTVNational.in@SD, AshwaveegaNews24x7.in@SD, AsianNews.in@SD, Asianet.in, AsianetMovies.in@SD, AsianetNews.in@SD, AsianetSuvarnaNews.in@SD, AsomLive24.in@SD, AssamTalks.in, AssamTalks.in@SD, AwakeningTV.in@SD, AxMen.us, AyushTV.in@SD, B4UBhojpuri.in@SD (and 325 more)
- Published mapped IDs without usable current/future programmes: **170**
- IDs without usable current/future programmes: AlQamarTV.ae, AlankarTV.in@SD, AmritaTV.in@SD, AndTV.in@SD, AnimalPlanet.in@SD, B4UKadak.in@SD, B4UMovies.in@India, BBCDrama.uk, BBCEarth.ca, BBCNews.uk, BabySharkTV.us, BangBangTV, BhojpuriCinema.in@SD, Bollygold.in@HD, CartoonNetwork.uk, CinevaultWesterns.us, Circle.us, Colors.Bangla.in, Colors.in, ColorsCineplex.in@SD, ColorsCineplexSuperhits.in@SD, ColorsGujarati.in@SD, ColorsRishteyAmericas.in, ColorsSuper.in, ColorsTamil.in@SD, CricketGold.au@SD, DDChandana.in@SD, DDNational.in@SD, DDOdia.in@SD, DDRajasthan.in@SD, DDSahyadri.in@SD, DDSports.in@SD, DDTamil.in@SD, DDUttarakhand.in@SD, DDYadagiri.in@SD, Dangal2.in@SD, DangalTV.in@SD, DarshanaTV.in@SD, DiscoveryChannel.in@SD, DiscoveryKids.au, Disney Junior.in, DisneyChannel.in@HD, DocuBayTV.in, ETVBeats.in@HD, ETVCinema.in, ETVComedy.in, ETVJosh.in, EkamraBharatOdia.in@SD, Enterr10 Bangla.in, EpicBharat.in@SD, EpicBhojpuri.in@SD, EpicCrimes.in, EpicMusic.in@SD, FITE247.us@SD, FashionOne.uk, GlobalPunjab.in, GravitasMovies.us, HistoryWarfareNow.us, Hungama.in@SD, INFAST.nl (and 110 more)

## Source / Published Schedule Reconciliation

- IDs with usable current/future source schedule data: **701/1568 (44.7%)**
- IDs with usable current/future schedules in published XMLTV at report time: **191/1568 (12.2%)**
- IDs with usable programmes in the published guide's common -6h/+7d window: **191/1568 (12.2%)**
- Current/future source IDs without any usable published programme in that common window: **510**
- Source-scheduled IDs without a usable published programme in the common window: 10 TV (`10TV.in@SD`), 22Scope News (`22ScopeNews.in@SD`), 24 News (`24News.in@SD`), 4 SiDES TV (`4SiDESTV.in@SD`), 4TV News (`4TVNews.in@SD`), 99TV (`99TV.in@SD`), 9 Plus News (`9PlusNews.in@SD`), ABP Ananda (`ABPAnanda.in@SD`), ABP Asmita (`ABPAsmita.in@SD`), ABP Ganga (`ABPGanga.in@SD`), ABP Majha (`ABPMajha.in@SD`), ABP News (`ABPNews.in@SD`), AMC Thrillers (`AMCThrillers.us`), ANB News (`ANBNews.in@SD`), ARY Digital (`ARYDigital.pk`), AXS (`AXS.us`), AXS TV (`AXSTV.us`), Aadinath TV (`AadinathTV.in@SD`), Aagaaz Times (`AagaazTimes.in@SD`), Aaj Ki Khabar (`AajKiKhabar.in@SD`), Aaj Tak (`AajTak.in`), Aaj Tak (`AajTak.in@HD`), Aaj Tak (`AajTak.in@SD`), Aaseervatham TV (`AaseervathamTV.in@SD`), Aastha (`Aastha.in@HD`), Aastha Gujarati (`AasthaGujarati.in@SD`), Aastha Kannada (`AasthaKannada.in@SD`), Aastha Telugu (`AasthaTelugu.in@SD`), Akhon Kolkata (`AkhonKolkata.in@SD`), Al Jazeera (`AlJazeera.qa`), Alankar TV (`AlankarTV.in@SD`), All Time Movies (`AllTimeMovies.in@SD`), Amar Bangla Digital (`AmarBanglaDigital.in`), AmarUjala (`AmarUjala.in@SD`), Amrita TV (`AmritaTV.in@SD`), Anand Wari TV (`AnandWariTV.in@SD`), &TV (`AndTV.in@HD`), &TV (`AndTV.in@SD`), &flix (`Andflix.in`), &pictures (`Andpictures.in`), Angel TV (`AngelTV.in@India`), Animal Planet (India) (`AnimalPlanet.in@HD`), Animal Planet (`AnimalPlanet.in@SD`), Anmol TV (`AnmolTV.in@SD`), Aradana TV (`AradanaTV.in@SD`), Argus News (`ArgusNews.in@SD`), Arirang (`Arirang.kr`), Aryan TV National (`AryanTVNational.in@SD`), Asian News (`AsianNews.in@SD`), Asianet (`Asianet.in`), Asianet Movies (`AsianetMovies.in@SD`), Asianet News (`AsianetNews.in@SD`), Asianet Suvarna News (1080p) [Not 24/7] (`AsianetSuvarnaNews.in@SD`), Asom Live 24 (`AsomLive24.in@SD`), Assam Talks (`AssamTalks.in`), Assam Talks (`AssamTalks.in@SD`), Awakening TV (`AwakeningTV.in@SD`), Ax Men (`AxMen.us`), Ayush TV (`AyushTV.in@SD`), B4U Bhojpuri (`B4UBhojpuri.in@SD`), B4U Kadak (`B4UKadak.in@SD`), B4U Movies (`B4UMovies.in@India`), BBC Earth (`BBCEarth.ca`), BBC News (`BBCNews.uk`), BIG TV (`BIGTV.in@SD`), BRK News (`BRKNews.in@SD`), BVG (`BVG.in@SD`), Baby Shark TV (`BabySharkTV.us`), Bada Khabar (`BadaKhabar.in@SD`), Bang Bang TV (`BangBangTV`), Bang U (`BangU.us`), Bangla Jago TV (`BanglaJagoTV.in`), Bansal News (`BansalNews.in@SD`), Bhagyam TV (`BhagyamTV.in@SD`), Bhakthi Siri (`BhakthiSiri.in@SD`), Bhakti Dhara (`BhaktiDhara.in@SD`), Bhakti Sagar (`BhaktiSagar.in@SD`), Bharat24 (`Bharat24.in@SD`), Bharat Express (`BharatExpress.in@SD`), Bharat Samachar (`BharatSamachar.in@SD`), Bharat Update (`BharatUpdate.in@SD`), Bhojpuri Cinema (`BhojpuriCinema.in@SD`), Big TV 24x7 (`BigTV24x7.in@SD`), Bloomberg TV (`BloombergTV.us`), Bollygold (`Bollygold.in@HD`), Bon Voyage (`BonVoyage.us`), CMC TV (`CMCTV.hr`), CNBC Awaaz (`CNBCAwaaz.in@SD`), CNBC Bajar (`CNBCBajar.in@SD`), CNBC TV (`CNBCTV.us`), CNBC TV18 (`CNBCTV18.in@SD`), CNBC TV18 Prime (`CNBCTV18PrimeHD.in@SD`), CNN (`CNN.us`), CVR Health (`CVRHealth.in@SD`), Calvary TV (`CalvaryTV.in@SD`), Captain (`Captain.in@SD`), Cartoon Network UK (`CartoonNetwork.uk`), Cartoon Network (`CartoonNetwork.us`), Channel Divya (`ChannelDivya.in@SD`), Channel S UK (`ChannelS.uk@679aa9`), Channel WIN (`ChannelWIN.in@SD`), Chardikla Time TV (`ChardiklaTimeTV.in@SD`), Chithiram (`Chithiram.in@SD`), Cinevault Westerns (`CinevaultWesterns.us`), Circle (`Circle.us`), Colors Bangla (`Colors.Bangla.in`), Colors (`Colors.in`), Colors (`Colors.in@HD`), Colors Bangla (`ColorsBangla.in@HD`), Colors Cineplex (`ColorsCineplex.in@HD`), Colors Cineplex (`ColorsCineplex.in@SD`), Colors Cineplex [UK] (`ColorsCineplex.uk`), Colors Cineplex Superhits (`ColorsCineplexSuperhits.in@SD`), Colors Gujarati (`ColorsGujarati.in@SD`), Colors Infinity (`ColorsInfinity.in`), Colors Rishtey (`ColorsRishtey.in`), Colors Rishtey (`ColorsRishteyAmericas.in`), Colors Super (`ColorsSuper.in`), Colors Tamil (`ColorsTamil.in@SD`), Comedy Central (`ComedyCentral.us`), Cook & Bake (`CookBake.us`), Cooking Channel (`CookingChannel.us`), Cricket Gold (`CricketGold.au@SD`), Crime & Justice (`CrimeJustice.us`), Crime Scene TV (`CrimeSceneTV.us`), DD Bihar (`DDBihar.in@SD`), DD Chandana (`DDChandana.in@SD`), DD Kisan (`DDKisan.in@SD`), DD Mizoram (`DDMizoram.in`), DD National (`DDNational.in@SD`), DD News (`DDNews.in@HD`), DD News (`DDNews.in@SD`), DD Odia (`DDOdia.in@SD`), DD Rajasthan (`DDRajasthan.in@SD`), DD Sahyadri (`DDSahyadri.in@SD`), DD Sports (`DDSports.in@HD`), DD Sports (`DDSports.in@SD`), DD Tamil (`DDTamil.in@HD`), DD Tamil (`DDTamil.in@SD`), DD Uttarakhand (`DDUttarakhand.in@SD`), DD Yadagiri (`DDYadagiri.in@SD`), Dangal 2 (`Dangal2.in@SD`), Dangal (`DangalTV.in@SD`), Darshana TV (`DarshanaTV.in@SD`), Discovery (`Discovery.us`), Discovery (`DiscoveryChannel.in@SD`), Discovery Channel (`DiscoveryChannel.us`), Discovery Family (`DiscoveryFamily.us`), Discovery Kids (`DiscoveryKids.au`), Discovery Science (`DiscoveryScience.in@SD`), Discovery Science (`DiscoveryScience.us`), Discovery Turbo (India) (`DiscoveryTurbo.in@SD`), Discovery Turbo (`DiscoveryTurbo.us`), Discovery World (`DiscoveryWorld.us`), Disha TV (`DishaTV.in@SD`), DISNEY JUNIOR (`Disney Junior.in`), Disney International (`DisneyInternationalHD.in@SD`), Disney Jr (`DisneyJr.us`), DocuBay TV (`DocuBayTV.in`), Documentary+ USA (`Documentary.us`), Duck TV (`DuckTV.us`), ETV Bal Bharat (`ETVBalBharat.in@SD`), ETV Beats (`ETVBeats.in@HD`), ETV Cinema (`ETVCinema.in`), ETV Cinema (`ETVCinema.in@HD`), ETV Comedy (`ETVComedy.in`), ETV Josh (`ETVJosh.in`), ETV Life (`ETVLife.in@SD`), ETV Music (`ETVMusic.in@SD`), ETV Plus (`ETVPlus.in@HD`), ETV Telugu (`ETVTelugu.in@HD`), Ekamra Bharat Odia (`EkamraBharatOdia.in@SD`), Ekamra Manoranjan (`EkamraManoranjan.in`), Enter10 Bangla (`Enter10Bangla.in`), ENTER 10 BANGLA (`Enterr10 Bangla.in`), Epic Bharat (`EpicBharat.in@SD`), Epic Bhojpuri (`EpicBhojpuri.in@SD`), Epic Bhojpuri Digital (`EpicBhojpuriDigital.in`), Epic Crimes (`EpicCrimes.in`), Epic Music (`EpicMusic.in@SD`), Epic Parivar (`EpicParivar.in@SD`), Escape TV (`EscapeTV.us`), Fashion TV (`FashionTV.us`), Fast1 (`Fast1.in@SD`), Flowers TV (`FlowersTV.in`), Food Network (`FoodNetwork.us`), Fox News (`FoxNews.us`), GNT (`GNT.in`), GTC Punjabi (`GTCPunjabi.in@SD`), Gemini Movies (`GeminiMovies.in`), Gemini Music (`GeminiMusic.in`), Geo TV (`GeoTV.pk`), Gravitas Movies (`GravitasMovies.us`), Gyandarshan (`Gyandarshan.in@HD`), Gyandarshan (`Gyandarshan.in@SD`), HBO (`HBO.us`), HBO 2 (`HBO2.us`), HGTV (`HGTV.us`), HISTORY TV (`HISTORYTV.us`), HUM Masala (`HUMMasala.pk`), Hallmark Movies & More (`HallmarkMoviesMore.us`), History Channel (`History.hu`), History & Warfare Now (`HistoryWarfareNow.us`), Hosanna TV (`HosannaTV.in@Tamil`), House of Crime (`HouseOfCrime.us`), Huda TV (`HudaTV.eg`), Hungama (`Hungama.in@SD`), Hungama TV (`HungamaTV.in@SD`), InFast (`INFAST.nl`), InWild (`INWILD.nl`), iON TV UK (`IONTV.us`), InWonder (`InWonder.nl`), Isai Aruvi (`IsaiAruvi.in@SD`), Islam Channel (`IslamChannel.uk`), Islam TV (`IslamTV.sa`), Jaihind TV (`JaihindTV.in@SD`), Jalsha Movies (`JalshaMovies.in@HD`), Jan TV (`JanTV.in@SD`), Jaya Plus (`JayaPlus.in@SD`), KTV Bangla (`KTVBangla.in@SD`), Kairali TV (`KairaliTV.in@SD`), Kartoon Channel! (`KartoonChannel.us`), Kaumudy TV (`KaumudyTV.in@SD`), KidDo MATIX (`KidDoMATIX.us`), Kite Victers (720p) [Not 24/7] (`KiteVicters.in@SD`), Kolkata TV (`KolkataTV.in`), Life+Style (`LifeStyle.us`), Lifetime (`Lifetime.us`), LoL TV (`LoLTV.in`), Love Nature (`LoveNature.us`), Love the Planet (`LoveThePlanet.us`), MBC 1 (`MBC1.sa`), MBC 4 (`MBC4.sa`), MSNBC (`MSNBC.us`), MTV (`MTV.in`), Manoranjan Grand (`ManoranjanGrand.in`), Marquee Sports Network (`MarqueeSportsNetwork.us`), Mayday: Air Disaster (`MaydayAirDisaster.us`), Mazhavil Manorama (`MazhavilManorama.in@SD`), MovieSphere (`MovieSphere.us`), Movies Now (`MoviesNow.in@SD`), Mr Bean Animated (`MrBeanAnimated.uk`), MyTime Movie Network (`MyTimeMovieNetwork.br`), NFL Network (`NFLNetwork.us`), NH BollyFlix (`NHBollyFlix.in`), NH BollyRaga (`NHBollyRaga.in`), NH Tamil Gold (`NHTamilGold.in`), NOW 70s (`NOW70s.us`), NOW 80s (`NOW80s.us`), Nat Geo TV (`NatGeoTV.us`), Nat Geo (`NationalGeographic.uk`), Nat Geo Wild (`NationalGeographicWild.in@SD`), Nature Time (`NatureTime.us`), News 24 (India) (`News24.in@SD`), Nick Jr (`NickJr.in@SD`), OuterSphere (`OuterSphere.us`), PBS Kids (`PBSKids.us@SD`), PGA Tour (`PGATour.us@SD`), Paramount Network (`ParamountNetwork.us`), Passie XXX (`PassieXXX.nl`), Penthouse Gold (`PenthouseGold.us`), & Picture (`Picture.in`), Pitaara (`Pitaara.in`), Pogo (`Pogo.in@SD`), Popular Science (`PopularScience.us`), Private TV (`PrivateTV.nl`), Punjabi Shorts (`PunjabiShorts.in`), Qello Concerts by Stingray (`QelloConcertsbyStingray.ca@SD`), Raj Musix Kannada (`RajMusixKannada.in@SD`), Raj Musix Malayalam (`RajMusixMalayalam.in@SD`), Raj Musix Tamil (`RajMusixTamil.in@SD`), Raj Musix Telugu (`RajMusixTelugu.in@SD`), Rang (`Rang.in@SD`), Rengoni (`Rengoni.in@SD`), RetroCrush (`RetroCrush.us`), Robot Wars by Mech+ (`RobotWarsByMech.us`), Roja Movies (`RojaMovies.in@SD`), Romedy Now (`RomedyNow.in`), Ruposhi Bangla (`RupasiBangla.in@SD`), IN: SONY SPORTS TEN 1 HD (`SONY SPORTS TEN 1 HD.in`), IN: SONY SPORTS TEN 2 HD (`SONY SPORTS TEN 2 HD.in`), Saga Music Haryanvi (`SagaMusicHaryanvi.in`), Sana Plus (`SanaPlus.in@SD`), Sana TV (`SanaTV.in@SD`), Sansad TV 2 (`SansadTV2.in@HD`), Sansad TV 2 (`SansadTV2.in@SD`), Saudi TV (`SaudiTV.sa`), Shemaroo TV (`ShemarooTV.in@SD`), Siri Kannada All Time (`SiriKannadaAllTime.in`), Sony Aath (`Sony.Aath.in`), Sony Aath (`SonyAath.in@SD`), Sony Max (`SonyMax.in@HD`), Sony Max (`SonyMax.in@SD`), Sony PAL (`SonyPal.in@SD`), Sony PIX (`SonyPix.in`), Sony SAB (`SonySAB.in@HD`), Sony Sports Ten 1 (`SonySportsTen1.in@HD`), Sony Sports Ten 1 (`SonySportsTen1.in@SD`), Sony Sports Ten 3 (`SonySportsTen3.in`), Sony WAH (`SonyWah.in@SD`), Sony Yay (`SonyYay.in@SD`), South Station (`SouthStation.in`), Sports First TV (`SportsFirstTV.us`), STAR GOLD ROMANCE (`Star Gold Romance.in`), Jalsha Movies HD (`Star.Jalsha.Movies.HD.in`), Jalsha Movies (`Star.Jalsha.Movies.in`), Star Jalsha (`Star.Jalsha.in`), Star Bharat (`StarBharat.in`), Star Gold (`StarGold.in`), Star Gold (`StarGold.in@HD`), Star Gold 2 (`StarGold2.in@HD`), Star Gold Select (`StarGoldSelect.in`), Star Jalsha (`StarJalsha.in@HD`), Star Jalsha (`StarJalsha.in@SD`), Star Maa (`StarMaa.in@SD`), Star Maa Movies (`StarMaaMovies.in@SD`), Star Movies (`StarMovies.in`), Star Movies (`StarMovies.in@SD`), Star Movies Select (`StarMoviesSelect.in@HD`), StarPlus (India) HD (1080i) (`StarPlus.in@HD`), Star Plus (`StarPlus.in@SD`), Star Pravah (`StarPravah.in@HD`), Star Sports 1 (`StarSports1.in`), Star Sports 1 (`StarSports1.in@HD`), Star Sports 1 Hindi (`StarSports1Hindi.in@HD`), Star Sports 2 (`StarSports2.in`), Star Sports 2 (`StarSports2.in@HD`), Star Sports 2 (`StarSports2.in@SD`), Star Sports 3 (`StarSports3.in@SD`), Star Sports Select 1 (`StarSportsSelect1.in@HD`), Star Sports Select 1 (`StarSportsSelect1.in@SD`), Star Sports Select 2 (`StarSportsSelect2.in`), Star Sports Select 2 (`StarSportsSelect2.in@HD`), Star Suvarna (`StarSuvarna.in`), Star Utsav (`StarUtsav.in`), Star Utsav Movies (`StarUtsavMovies.in`), Star Vijay (`StarVijay.in`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray DJAZZ (`StingrayDJAZZ.ca@SD`), Stingray Naturescape (`StingrayNaturescape.ca`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca`), Strawberry Shortcake (`StrawberryShortcake.us`), Sun Bangla (`SunBangla.in`), Udaya Movies (`SunUdayaMovies.in`), Survivor (`Survivor.us`), TBS (`TBS.us`), TLC (India) (`TLC.in@SD`), TLC (`TLC.us`), TRT Müzik (`TRTMuzik.tr`), TV9 Bangla (`TV9Bangla.in`), TV9 Bangla (`TV9Bangla.in@SD`), Tarang Music (`TarangMusic.in@SD`), Tarang TV (`TarangTV.in@SD`), Teen Nick (`TeenNick.us`), Teleritmo (`Teleritmo.us`), Teletubbies (`Teletubbies.uk`), Thalaa TV (`ThalaaTV.in`), The Movie Club (`TheMovieClub.in@HD`), The Movie Club +2 (`TheMovieClub.in@Plus2`), Times Now Navbharat (`TimesNowNavbharat.in@HD`), Times Now Navbharat (`TimesNowNavbharat.in@SD`), Tolly TV (`TollyTV.in`), Toon Goggles (`ToonGoggles.us`), Toonami Aftermath East (`ToonamiAftermathEast.us`), Trace Latina (`TraceLatina.us`), Trace Urban (`TraceUrban.fr`), Travel Channel (`TravelChannel.us`), Travelxp (`Travelxp.in@HD`), Travelxp English (`TravelxpEnglish.us`), True Crime UK (`TrueCrime.uk`), Mysteries Xplored (`USBB5200028MM`), Unidentified (`Unidentified.us`), Vevo Pop (`VevoPop.us`), Wheel World (`WheelWorld.us`), Wild Flix Hindi (`WildFlixHindi.in`), Willow (`Willow.us`), Witness to Justice (`WitnessToJustice.us`), Wonder (`Wonder.us`), World War TV (`WorldWarTV.us`), XITE 90's Throwback (`XITE90sThrowback.us`), XITE Hits (`XITEHits.nl`), XITE Rock x Metal (`XITERockxMetal.nl`), XXTreme Jobs Hindi (`XXTremeJobsHindi.in`), YTV (`YTV.us`), ZB Cinema (`ZBCinema.in`), Zee Action (`ZeeAction.in`), Zee Bangla (`ZeeBangla.in@HD`), Zee Bangla (`ZeeBangla.in@SD`), Zee Bangla Sonar (`ZeeBanglaSonar.in@SD`), Zee Bollywood (`ZeeBollywood.in@SD`), Zee Cinema (`ZeeCinema.in@HD`), Zee Cinema (`ZeeCinema.in@SD`), Zee Cinemalu (`ZeeCinemalu.in`), Zee Kannada (`ZeeKannada.in@SD`), Zee Marathi (`ZeeMarathi.in@HD`), Zee TV (`ZeeTV.in@SD`), Zee Tamil (`ZeeTamil.in@HD`), Zee Tamil (`ZeeTamil.in@SD`), Zee Telugu (`ZeeTelugu.in`), Zing (`Zing.in@SD`), Zoo Moo (`ZooMoo.sg`), American Heroes Channel (`americanheroeschannel.us`), Asianet Movies (`asianetmovies.in`), Asianet Plus (`asianetplus.in`), beIN SPORTS XTRA (`beINSPORTSXTRA.us`), Big Magic (`bigmagic.in`), Blaze (`blaze.uk`), CMT (`cmt.us`), 30 (`custom.24-7-adult-xxx-30`), 33 (`custom.24-7-adult-xxx-33`), 1 (`custom.24-7-xxx-1`), 10 (`custom.24-7-xxx-10`), 2 (`custom.24-7-xxx-2`), 3 (`custom.24-7-xxx-3`), 4 (`custom.24-7-xxx-4`), 5 (`custom.24-7-xxx-5`), 6 (`custom.24-7-xxx-6`), 8 (`custom.24-7-xxx-8`), 13 (`custom.24-7-xxx-adult-13`), 20 (`custom.24-7-xxx-adult-20`), 24 (`custom.24-7-xxx-adult-24`), Metro (`custom.24-7-xxx-metro`), Reality Kings (`custom.24-7-xxx-reality-kings`), 24 Hour Free Movies (`custom.24-hour-free-movies`), AMC TV (`custom.amc-tv`), and Xplor (`custom.and-xplor`), Animal Planet Telugu (`custom.animal-planet-telugu`), Asianet (`custom.asianet-2s7ex`), AAKASH AATH (`custom.bdix.aakashaath`), TRACE Sport Stars HD (`custom.bdix.tracesportstars`), CGTN Documentary (`custom.cgtn-docment`), Colors Rishtey TV (`custom.colors-rishtey-tv`), Discovery (`custom.discovery`), Discovery Turbo (`custom.discovery-turbo-fiqpt`), ETV (`custom.etv`), Food Network (`custom.food-network-bd0w6`), FX TV (`custom.fx-tv`), HBO (`custom.hbo-4dc4i`), HGTV (`custom.hgtv-xvgvy`), History (`custom.history`), Hum Masala TV (`custom.hum-masala-tv`), Id Investigation Discovery (`custom.id-investigation-discovery`), Iqra TV (`custom.iqra-tv`), Iqra TV UK (`custom.iqra-tv-uk`), Jungle Book (`custom.jungle-book`), Love Nature (`custom.love-natural`), MBC TV (`custom.mbc-tv`), MTV Live (`custom.mtv-live`), Noor TV (`custom.noor-tv`), Raj Musix (`custom.raj-musix-ltc82`), Redlight (`custom.redlight`), Rengoni TV (`custom.rengoni-tv`), Saudi Quran (`custom.saudi-quran`), Shemaroo Bollywood (`custom.sheemaroo-bollywood`), Star Channel (`custom.star-channel`), Star Gold (`custom.star.gold`), Star Movies (`custom.star.movies`), Star Utsav (`custom.starutsav`), Sun Bangla (`custom.sun-bangla-k1d4w`), Sun TV (`custom.sun-tv`), Syfy (`custom.syfy`), Beate Uhse.Tv (`custom.xxx-beate-uhse-tv`), Blue Hustler (`custom.xxx-blue-hustler`), Brazzers (`custom.xxx-brazzers`), Brazzers Europe (`custom.xxx-brazzers-europe`), Dorcel HD (`custom.xxx-dorcel-hd`), Dorcel Tv (`custom.xxx-dorcel-tv`), Dorcel Xxx (`custom.xxx-dorcel-xxx`), ERO X (`custom.xxx-ero-x`), Ero Xxx (`custom.xxx-ero-xxx`), Hustler (`custom.xxx-hustler`), Meiden Van Holland Hard (`custom.xxx-meiden-van-holland-hard`), Passie Xxx (`custom.xxx-passie-xxx`), Penthouse Gold (`custom.xxx-penthouse-gold`), Playboy (`custom.xxx-playboy`), Reality Kings (`custom.xxx-reality-kings`), Redlight (`custom.xxx-redlight`), Secret Circle Tv (`custom.xxx-secret-circle-tv`), Super One (`custom.xxx-super-one`), Vivid Red (`custom.xxx-vivid-red`), Destination America (`destinationamerica.us`), Discovery Life (`discoverylife.us`), Discovery Science (`discoveryscience.us`), Disney Channel East (`disneychannel.us`), Epic (`epic.in`), Film 4 (`film4.uk`), Fuse (`fusetv.us`), HBO Signature (`hbosignature.us`), HBO Zone (`hbozone.us`), IFC (`independentfilmchannel.us`), Investigation Discovery (`investigationdiscovery.uk`), Jalsha Movies (`jalshamovieshd.in`), Jaya TV (`jaya.in`), Jaya Max (`jayamax.in`), J Movies (`jmovie.in`), Kappa TV (`kappatv.in`), Law & Crime (`lawandcrime.us`), Military History (`militaryhistory.us`), Motortrend (`motortrend.us`), Movieplex (`movieplex.us`), MTV Classic (`mtv.classic.gb`), Smithsonian Channel (`smithsonianchannel.us`), Sony BBC Earth (`sonybbcearthhd.in`), True Crime Network (`truecrimenetwork.us`), Turner Classic Movies (`turnerclassicmovies.us`), TV One (`tvone.us`), World Fishing Network (`worldfishingnetwork.us`), Zee Anmol Cinema (`zeeanmolcinema.in`)
- IDs with an in-window published programme but no current/future source match at the later scan: **0**
- In-window published IDs not counted source-current/future: none
- Source-current/future IDs whose published programme is no longer current by report time: **510**
- Source-current/future IDs no longer current in the published guide: 10 TV (`10TV.in@SD`), 22Scope News (`22ScopeNews.in@SD`), 24 News (`24News.in@SD`), 4 SiDES TV (`4SiDESTV.in@SD`), 4TV News (`4TVNews.in@SD`), 99TV (`99TV.in@SD`), 9 Plus News (`9PlusNews.in@SD`), ABP Ananda (`ABPAnanda.in@SD`), ABP Asmita (`ABPAsmita.in@SD`), ABP Ganga (`ABPGanga.in@SD`), ABP Majha (`ABPMajha.in@SD`), ABP News (`ABPNews.in@SD`), AMC Thrillers (`AMCThrillers.us`), ANB News (`ANBNews.in@SD`), ARY Digital (`ARYDigital.pk`), AXS (`AXS.us`), AXS TV (`AXSTV.us`), Aadinath TV (`AadinathTV.in@SD`), Aagaaz Times (`AagaazTimes.in@SD`), Aaj Ki Khabar (`AajKiKhabar.in@SD`), Aaj Tak (`AajTak.in`), Aaj Tak (`AajTak.in@HD`), Aaj Tak (`AajTak.in@SD`), Aaseervatham TV (`AaseervathamTV.in@SD`), Aastha (`Aastha.in@HD`), Aastha Gujarati (`AasthaGujarati.in@SD`), Aastha Kannada (`AasthaKannada.in@SD`), Aastha Telugu (`AasthaTelugu.in@SD`), Akhon Kolkata (`AkhonKolkata.in@SD`), Al Jazeera (`AlJazeera.qa`), Alankar TV (`AlankarTV.in@SD`), All Time Movies (`AllTimeMovies.in@SD`), Amar Bangla Digital (`AmarBanglaDigital.in`), AmarUjala (`AmarUjala.in@SD`), Amrita TV (`AmritaTV.in@SD`), Anand Wari TV (`AnandWariTV.in@SD`), &TV (`AndTV.in@HD`), &TV (`AndTV.in@SD`), &flix (`Andflix.in`), &pictures (`Andpictures.in`), Angel TV (`AngelTV.in@India`), Animal Planet (India) (`AnimalPlanet.in@HD`), Animal Planet (`AnimalPlanet.in@SD`), Anmol TV (`AnmolTV.in@SD`), Aradana TV (`AradanaTV.in@SD`), Argus News (`ArgusNews.in@SD`), Arirang (`Arirang.kr`), Aryan TV National (`AryanTVNational.in@SD`), Asian News (`AsianNews.in@SD`), Asianet (`Asianet.in`), Asianet Movies (`AsianetMovies.in@SD`), Asianet News (`AsianetNews.in@SD`), Asianet Suvarna News (1080p) [Not 24/7] (`AsianetSuvarnaNews.in@SD`), Asom Live 24 (`AsomLive24.in@SD`), Assam Talks (`AssamTalks.in`), Assam Talks (`AssamTalks.in@SD`), Awakening TV (`AwakeningTV.in@SD`), Ax Men (`AxMen.us`), Ayush TV (`AyushTV.in@SD`), B4U Bhojpuri (`B4UBhojpuri.in@SD`), B4U Kadak (`B4UKadak.in@SD`), B4U Movies (`B4UMovies.in@India`), BBC Earth (`BBCEarth.ca`), BBC News (`BBCNews.uk`), BIG TV (`BIGTV.in@SD`), BRK News (`BRKNews.in@SD`), BVG (`BVG.in@SD`), Baby Shark TV (`BabySharkTV.us`), Bada Khabar (`BadaKhabar.in@SD`), Bang Bang TV (`BangBangTV`), Bang U (`BangU.us`), Bangla Jago TV (`BanglaJagoTV.in`), Bansal News (`BansalNews.in@SD`), Bhagyam TV (`BhagyamTV.in@SD`), Bhakthi Siri (`BhakthiSiri.in@SD`), Bhakti Dhara (`BhaktiDhara.in@SD`), Bhakti Sagar (`BhaktiSagar.in@SD`), Bharat24 (`Bharat24.in@SD`), Bharat Express (`BharatExpress.in@SD`), Bharat Samachar (`BharatSamachar.in@SD`), Bharat Update (`BharatUpdate.in@SD`), Bhojpuri Cinema (`BhojpuriCinema.in@SD`), Big TV 24x7 (`BigTV24x7.in@SD`), Bloomberg TV (`BloombergTV.us`), Bollygold (`Bollygold.in@HD`), Bon Voyage (`BonVoyage.us`), CMC TV (`CMCTV.hr`), CNBC Awaaz (`CNBCAwaaz.in@SD`), CNBC Bajar (`CNBCBajar.in@SD`), CNBC TV (`CNBCTV.us`), CNBC TV18 (`CNBCTV18.in@SD`), CNBC TV18 Prime (`CNBCTV18PrimeHD.in@SD`), CNN (`CNN.us`), CVR Health (`CVRHealth.in@SD`), Calvary TV (`CalvaryTV.in@SD`), Captain (`Captain.in@SD`), Cartoon Network UK (`CartoonNetwork.uk`), Cartoon Network (`CartoonNetwork.us`), Channel Divya (`ChannelDivya.in@SD`), Channel S UK (`ChannelS.uk@679aa9`), Channel WIN (`ChannelWIN.in@SD`), Chardikla Time TV (`ChardiklaTimeTV.in@SD`), Chithiram (`Chithiram.in@SD`), Cinevault Westerns (`CinevaultWesterns.us`), Circle (`Circle.us`), Colors Bangla (`Colors.Bangla.in`), Colors (`Colors.in`), Colors (`Colors.in@HD`), Colors Bangla (`ColorsBangla.in@HD`), Colors Cineplex (`ColorsCineplex.in@HD`), Colors Cineplex (`ColorsCineplex.in@SD`), Colors Cineplex [UK] (`ColorsCineplex.uk`), Colors Cineplex Superhits (`ColorsCineplexSuperhits.in@SD`), Colors Gujarati (`ColorsGujarati.in@SD`), Colors Infinity (`ColorsInfinity.in`), Colors Rishtey (`ColorsRishtey.in`), Colors Rishtey (`ColorsRishteyAmericas.in`), Colors Super (`ColorsSuper.in`), Colors Tamil (`ColorsTamil.in@SD`), Comedy Central (`ComedyCentral.us`), Cook & Bake (`CookBake.us`), Cooking Channel (`CookingChannel.us`), Cricket Gold (`CricketGold.au@SD`), Crime & Justice (`CrimeJustice.us`), Crime Scene TV (`CrimeSceneTV.us`), DD Bihar (`DDBihar.in@SD`), DD Chandana (`DDChandana.in@SD`), DD Kisan (`DDKisan.in@SD`), DD Mizoram (`DDMizoram.in`), DD National (`DDNational.in@SD`), DD News (`DDNews.in@HD`), DD News (`DDNews.in@SD`), DD Odia (`DDOdia.in@SD`), DD Rajasthan (`DDRajasthan.in@SD`), DD Sahyadri (`DDSahyadri.in@SD`), DD Sports (`DDSports.in@HD`), DD Sports (`DDSports.in@SD`), DD Tamil (`DDTamil.in@HD`), DD Tamil (`DDTamil.in@SD`), DD Uttarakhand (`DDUttarakhand.in@SD`), DD Yadagiri (`DDYadagiri.in@SD`), Dangal 2 (`Dangal2.in@SD`), Dangal (`DangalTV.in@SD`), Darshana TV (`DarshanaTV.in@SD`), Discovery (`Discovery.us`), Discovery (`DiscoveryChannel.in@SD`), Discovery Channel (`DiscoveryChannel.us`), Discovery Family (`DiscoveryFamily.us`), Discovery Kids (`DiscoveryKids.au`), Discovery Science (`DiscoveryScience.in@SD`), Discovery Science (`DiscoveryScience.us`), Discovery Turbo (India) (`DiscoveryTurbo.in@SD`), Discovery Turbo (`DiscoveryTurbo.us`), Discovery World (`DiscoveryWorld.us`), Disha TV (`DishaTV.in@SD`), DISNEY JUNIOR (`Disney Junior.in`), Disney International (`DisneyInternationalHD.in@SD`), Disney Jr (`DisneyJr.us`), DocuBay TV (`DocuBayTV.in`), Documentary+ USA (`Documentary.us`), Duck TV (`DuckTV.us`), ETV Bal Bharat (`ETVBalBharat.in@SD`), ETV Beats (`ETVBeats.in@HD`), ETV Cinema (`ETVCinema.in`), ETV Cinema (`ETVCinema.in@HD`), ETV Comedy (`ETVComedy.in`), ETV Josh (`ETVJosh.in`), ETV Life (`ETVLife.in@SD`), ETV Music (`ETVMusic.in@SD`), ETV Plus (`ETVPlus.in@HD`), ETV Telugu (`ETVTelugu.in@HD`), Ekamra Bharat Odia (`EkamraBharatOdia.in@SD`), Ekamra Manoranjan (`EkamraManoranjan.in`), Enter10 Bangla (`Enter10Bangla.in`), ENTER 10 BANGLA (`Enterr10 Bangla.in`), Epic Bharat (`EpicBharat.in@SD`), Epic Bhojpuri (`EpicBhojpuri.in@SD`), Epic Bhojpuri Digital (`EpicBhojpuriDigital.in`), Epic Crimes (`EpicCrimes.in`), Epic Music (`EpicMusic.in@SD`), Epic Parivar (`EpicParivar.in@SD`), Escape TV (`EscapeTV.us`), Fashion TV (`FashionTV.us`), Fast1 (`Fast1.in@SD`), Flowers TV (`FlowersTV.in`), Food Network (`FoodNetwork.us`), Fox News (`FoxNews.us`), GNT (`GNT.in`), GTC Punjabi (`GTCPunjabi.in@SD`), Gemini Movies (`GeminiMovies.in`), Gemini Music (`GeminiMusic.in`), Geo TV (`GeoTV.pk`), Gravitas Movies (`GravitasMovies.us`), Gyandarshan (`Gyandarshan.in@HD`), Gyandarshan (`Gyandarshan.in@SD`), HBO (`HBO.us`), HBO 2 (`HBO2.us`), HGTV (`HGTV.us`), HISTORY TV (`HISTORYTV.us`), HUM Masala (`HUMMasala.pk`), Hallmark Movies & More (`HallmarkMoviesMore.us`), History Channel (`History.hu`), History & Warfare Now (`HistoryWarfareNow.us`), Hosanna TV (`HosannaTV.in@Tamil`), House of Crime (`HouseOfCrime.us`), Huda TV (`HudaTV.eg`), Hungama (`Hungama.in@SD`), Hungama TV (`HungamaTV.in@SD`), InFast (`INFAST.nl`), InWild (`INWILD.nl`), iON TV UK (`IONTV.us`), InWonder (`InWonder.nl`), Isai Aruvi (`IsaiAruvi.in@SD`), Islam Channel (`IslamChannel.uk`), Islam TV (`IslamTV.sa`), Jaihind TV (`JaihindTV.in@SD`), Jalsha Movies (`JalshaMovies.in@HD`), Jan TV (`JanTV.in@SD`), Jaya Plus (`JayaPlus.in@SD`), KTV Bangla (`KTVBangla.in@SD`), Kairali TV (`KairaliTV.in@SD`), Kartoon Channel! (`KartoonChannel.us`), Kaumudy TV (`KaumudyTV.in@SD`), KidDo MATIX (`KidDoMATIX.us`), Kite Victers (720p) [Not 24/7] (`KiteVicters.in@SD`), Kolkata TV (`KolkataTV.in`), Life+Style (`LifeStyle.us`), Lifetime (`Lifetime.us`), LoL TV (`LoLTV.in`), Love Nature (`LoveNature.us`), Love the Planet (`LoveThePlanet.us`), MBC 1 (`MBC1.sa`), MBC 4 (`MBC4.sa`), MSNBC (`MSNBC.us`), MTV (`MTV.in`), Manoranjan Grand (`ManoranjanGrand.in`), Marquee Sports Network (`MarqueeSportsNetwork.us`), Mayday: Air Disaster (`MaydayAirDisaster.us`), Mazhavil Manorama (`MazhavilManorama.in@SD`), MovieSphere (`MovieSphere.us`), Movies Now (`MoviesNow.in@SD`), Mr Bean Animated (`MrBeanAnimated.uk`), MyTime Movie Network (`MyTimeMovieNetwork.br`), NFL Network (`NFLNetwork.us`), NH BollyFlix (`NHBollyFlix.in`), NH BollyRaga (`NHBollyRaga.in`), NH Tamil Gold (`NHTamilGold.in`), NOW 70s (`NOW70s.us`), NOW 80s (`NOW80s.us`), Nat Geo TV (`NatGeoTV.us`), Nat Geo (`NationalGeographic.uk`), Nat Geo Wild (`NationalGeographicWild.in@SD`), Nature Time (`NatureTime.us`), News 24 (India) (`News24.in@SD`), Nick Jr (`NickJr.in@SD`), OuterSphere (`OuterSphere.us`), PBS Kids (`PBSKids.us@SD`), PGA Tour (`PGATour.us@SD`), Paramount Network (`ParamountNetwork.us`), Passie XXX (`PassieXXX.nl`), Penthouse Gold (`PenthouseGold.us`), & Picture (`Picture.in`), Pitaara (`Pitaara.in`), Pogo (`Pogo.in@SD`), Popular Science (`PopularScience.us`), Private TV (`PrivateTV.nl`), Punjabi Shorts (`PunjabiShorts.in`), Qello Concerts by Stingray (`QelloConcertsbyStingray.ca@SD`), Raj Musix Kannada (`RajMusixKannada.in@SD`), Raj Musix Malayalam (`RajMusixMalayalam.in@SD`), Raj Musix Tamil (`RajMusixTamil.in@SD`), Raj Musix Telugu (`RajMusixTelugu.in@SD`), Rang (`Rang.in@SD`), Rengoni (`Rengoni.in@SD`), RetroCrush (`RetroCrush.us`), Robot Wars by Mech+ (`RobotWarsByMech.us`), Roja Movies (`RojaMovies.in@SD`), Romedy Now (`RomedyNow.in`), Ruposhi Bangla (`RupasiBangla.in@SD`), IN: SONY SPORTS TEN 1 HD (`SONY SPORTS TEN 1 HD.in`), IN: SONY SPORTS TEN 2 HD (`SONY SPORTS TEN 2 HD.in`), Saga Music Haryanvi (`SagaMusicHaryanvi.in`), Sana Plus (`SanaPlus.in@SD`), Sana TV (`SanaTV.in@SD`), Sansad TV 2 (`SansadTV2.in@HD`), Sansad TV 2 (`SansadTV2.in@SD`), Saudi TV (`SaudiTV.sa`), Shemaroo TV (`ShemarooTV.in@SD`), Siri Kannada All Time (`SiriKannadaAllTime.in`), Sony Aath (`Sony.Aath.in`), Sony Aath (`SonyAath.in@SD`), Sony Max (`SonyMax.in@HD`), Sony Max (`SonyMax.in@SD`), Sony PAL (`SonyPal.in@SD`), Sony PIX (`SonyPix.in`), Sony SAB (`SonySAB.in@HD`), Sony Sports Ten 1 (`SonySportsTen1.in@HD`), Sony Sports Ten 1 (`SonySportsTen1.in@SD`), Sony Sports Ten 3 (`SonySportsTen3.in`), Sony WAH (`SonyWah.in@SD`), Sony Yay (`SonyYay.in@SD`), South Station (`SouthStation.in`), Sports First TV (`SportsFirstTV.us`), STAR GOLD ROMANCE (`Star Gold Romance.in`), Jalsha Movies HD (`Star.Jalsha.Movies.HD.in`), Jalsha Movies (`Star.Jalsha.Movies.in`), Star Jalsha (`Star.Jalsha.in`), Star Bharat (`StarBharat.in`), Star Gold (`StarGold.in`), Star Gold (`StarGold.in@HD`), Star Gold 2 (`StarGold2.in@HD`), Star Gold Select (`StarGoldSelect.in`), Star Jalsha (`StarJalsha.in@HD`), Star Jalsha (`StarJalsha.in@SD`), Star Maa (`StarMaa.in@SD`), Star Maa Movies (`StarMaaMovies.in@SD`), Star Movies (`StarMovies.in`), Star Movies (`StarMovies.in@SD`), Star Movies Select (`StarMoviesSelect.in@HD`), StarPlus (India) HD (1080i) (`StarPlus.in@HD`), Star Plus (`StarPlus.in@SD`), Star Pravah (`StarPravah.in@HD`), Star Sports 1 (`StarSports1.in`), Star Sports 1 (`StarSports1.in@HD`), Star Sports 1 Hindi (`StarSports1Hindi.in@HD`), Star Sports 2 (`StarSports2.in`), Star Sports 2 (`StarSports2.in@HD`), Star Sports 2 (`StarSports2.in@SD`), Star Sports 3 (`StarSports3.in@SD`), Star Sports Select 1 (`StarSportsSelect1.in@HD`), Star Sports Select 1 (`StarSportsSelect1.in@SD`), Star Sports Select 2 (`StarSportsSelect2.in`), Star Sports Select 2 (`StarSportsSelect2.in@HD`), Star Suvarna (`StarSuvarna.in`), Star Utsav (`StarUtsav.in`), Star Utsav Movies (`StarUtsavMovies.in`), Star Vijay (`StarVijay.in`), Stingray Classic Rock (`StingrayClassicRock.ca`), Stingray DJAZZ (`StingrayDJAZZ.ca@SD`), Stingray Naturescape (`StingrayNaturescape.ca`), Stingray Remember the 80s (`StingrayRememberthe80s.ca`), Stingray Today's KPOP (`StingrayTodaySKPOP.us`), Stingray Today's Latin Pop (`StingrayTodaysLatinPop.ca`), Strawberry Shortcake (`StrawberryShortcake.us`), Sun Bangla (`SunBangla.in`), Udaya Movies (`SunUdayaMovies.in`), Survivor (`Survivor.us`), TBS (`TBS.us`), TLC (India) (`TLC.in@SD`), TLC (`TLC.us`), TRT Müzik (`TRTMuzik.tr`), TV9 Bangla (`TV9Bangla.in`), TV9 Bangla (`TV9Bangla.in@SD`), Tarang Music (`TarangMusic.in@SD`), Tarang TV (`TarangTV.in@SD`), Teen Nick (`TeenNick.us`), Teleritmo (`Teleritmo.us`), Teletubbies (`Teletubbies.uk`), Thalaa TV (`ThalaaTV.in`), The Movie Club (`TheMovieClub.in@HD`), The Movie Club +2 (`TheMovieClub.in@Plus2`), Times Now Navbharat (`TimesNowNavbharat.in@HD`), Times Now Navbharat (`TimesNowNavbharat.in@SD`), Tolly TV (`TollyTV.in`), Toon Goggles (`ToonGoggles.us`), Toonami Aftermath East (`ToonamiAftermathEast.us`), Trace Latina (`TraceLatina.us`), Trace Urban (`TraceUrban.fr`), Travel Channel (`TravelChannel.us`), Travelxp (`Travelxp.in@HD`), Travelxp English (`TravelxpEnglish.us`), True Crime UK (`TrueCrime.uk`), Mysteries Xplored (`USBB5200028MM`), Unidentified (`Unidentified.us`), Vevo Pop (`VevoPop.us`), Wheel World (`WheelWorld.us`), Wild Flix Hindi (`WildFlixHindi.in`), Willow (`Willow.us`), Witness to Justice (`WitnessToJustice.us`), Wonder (`Wonder.us`), World War TV (`WorldWarTV.us`), XITE 90's Throwback (`XITE90sThrowback.us`), XITE Hits (`XITEHits.nl`), XITE Rock x Metal (`XITERockxMetal.nl`), XXTreme Jobs Hindi (`XXTremeJobsHindi.in`), YTV (`YTV.us`), ZB Cinema (`ZBCinema.in`), Zee Action (`ZeeAction.in`), Zee Bangla (`ZeeBangla.in@HD`), Zee Bangla (`ZeeBangla.in@SD`), Zee Bangla Sonar (`ZeeBanglaSonar.in@SD`), Zee Bollywood (`ZeeBollywood.in@SD`), Zee Cinema (`ZeeCinema.in@HD`), Zee Cinema (`ZeeCinema.in@SD`), Zee Cinemalu (`ZeeCinemalu.in`), Zee Kannada (`ZeeKannada.in@SD`), Zee Marathi (`ZeeMarathi.in@HD`), Zee TV (`ZeeTV.in@SD`), Zee Tamil (`ZeeTamil.in@HD`), Zee Tamil (`ZeeTamil.in@SD`), Zee Telugu (`ZeeTelugu.in`), Zing (`Zing.in@SD`), Zoo Moo (`ZooMoo.sg`), American Heroes Channel (`americanheroeschannel.us`), Asianet Movies (`asianetmovies.in`), Asianet Plus (`asianetplus.in`), beIN SPORTS XTRA (`beINSPORTSXTRA.us`), Big Magic (`bigmagic.in`), Blaze (`blaze.uk`), CMT (`cmt.us`), 30 (`custom.24-7-adult-xxx-30`), 33 (`custom.24-7-adult-xxx-33`), 1 (`custom.24-7-xxx-1`), 10 (`custom.24-7-xxx-10`), 2 (`custom.24-7-xxx-2`), 3 (`custom.24-7-xxx-3`), 4 (`custom.24-7-xxx-4`), 5 (`custom.24-7-xxx-5`), 6 (`custom.24-7-xxx-6`), 8 (`custom.24-7-xxx-8`), 13 (`custom.24-7-xxx-adult-13`), 20 (`custom.24-7-xxx-adult-20`), 24 (`custom.24-7-xxx-adult-24`), Metro (`custom.24-7-xxx-metro`), Reality Kings (`custom.24-7-xxx-reality-kings`), 24 Hour Free Movies (`custom.24-hour-free-movies`), AMC TV (`custom.amc-tv`), and Xplor (`custom.and-xplor`), Animal Planet Telugu (`custom.animal-planet-telugu`), Asianet (`custom.asianet-2s7ex`), AAKASH AATH (`custom.bdix.aakashaath`), TRACE Sport Stars HD (`custom.bdix.tracesportstars`), CGTN Documentary (`custom.cgtn-docment`), Colors Rishtey TV (`custom.colors-rishtey-tv`), Discovery (`custom.discovery`), Discovery Turbo (`custom.discovery-turbo-fiqpt`), ETV (`custom.etv`), Food Network (`custom.food-network-bd0w6`), FX TV (`custom.fx-tv`), HBO (`custom.hbo-4dc4i`), HGTV (`custom.hgtv-xvgvy`), History (`custom.history`), Hum Masala TV (`custom.hum-masala-tv`), Id Investigation Discovery (`custom.id-investigation-discovery`), Iqra TV (`custom.iqra-tv`), Iqra TV UK (`custom.iqra-tv-uk`), Jungle Book (`custom.jungle-book`), Love Nature (`custom.love-natural`), MBC TV (`custom.mbc-tv`), MTV Live (`custom.mtv-live`), Noor TV (`custom.noor-tv`), Raj Musix (`custom.raj-musix-ltc82`), Redlight (`custom.redlight`), Rengoni TV (`custom.rengoni-tv`), Saudi Quran (`custom.saudi-quran`), Shemaroo Bollywood (`custom.sheemaroo-bollywood`), Star Channel (`custom.star-channel`), Star Gold (`custom.star.gold`), Star Movies (`custom.star.movies`), Star Utsav (`custom.starutsav`), Sun Bangla (`custom.sun-bangla-k1d4w`), Sun TV (`custom.sun-tv`), Syfy (`custom.syfy`), Beate Uhse.Tv (`custom.xxx-beate-uhse-tv`), Blue Hustler (`custom.xxx-blue-hustler`), Brazzers (`custom.xxx-brazzers`), Brazzers Europe (`custom.xxx-brazzers-europe`), Dorcel HD (`custom.xxx-dorcel-hd`), Dorcel Tv (`custom.xxx-dorcel-tv`), Dorcel Xxx (`custom.xxx-dorcel-xxx`), ERO X (`custom.xxx-ero-x`), Ero Xxx (`custom.xxx-ero-xxx`), Hustler (`custom.xxx-hustler`), Meiden Van Holland Hard (`custom.xxx-meiden-van-holland-hard`), Passie Xxx (`custom.xxx-passie-xxx`), Penthouse Gold (`custom.xxx-penthouse-gold`), Playboy (`custom.xxx-playboy`), Reality Kings (`custom.xxx-reality-kings`), Redlight (`custom.xxx-redlight`), Secret Circle Tv (`custom.xxx-secret-circle-tv`), Super One (`custom.xxx-super-one`), Vivid Red (`custom.xxx-vivid-red`), Destination America (`destinationamerica.us`), Discovery Life (`discoverylife.us`), Discovery Science (`discoveryscience.us`), Disney Channel East (`disneychannel.us`), Epic (`epic.in`), Film 4 (`film4.uk`), Fuse (`fusetv.us`), HBO Signature (`hbosignature.us`), HBO Zone (`hbozone.us`), IFC (`independentfilmchannel.us`), Investigation Discovery (`investigationdiscovery.uk`), Jalsha Movies (`jalshamovieshd.in`), Jaya TV (`jaya.in`), Jaya Max (`jayamax.in`), J Movies (`jmovie.in`), Kappa TV (`kappatv.in`), Law & Crime (`lawandcrime.us`), Military History (`militaryhistory.us`), Motortrend (`motortrend.us`), Movieplex (`movieplex.us`), MTV Classic (`mtv.classic.gb`), Smithsonian Channel (`smithsonianchannel.us`), Sony BBC Earth (`sonybbcearthhd.in`), True Crime Network (`truecrimenetwork.us`), Turner Classic Movies (`turnerclassicmovies.us`), TV One (`tvone.us`), World Fishing Network (`worldfishingnetwork.us`), Zee Anmol Cinema (`zeeanmolcinema.in`)
- Published current/future IDs not counted source-current/future: **0**
- Published current/future IDs not counted source-current/future: none


## Playlist EPG Headers

| Playlist | Header status |
|---|---|
| IPTV-Playlist.m3u | OK |
| BDIX-Playlist.m3u | OK |
| International-Playlist.m3u | OK |

## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **0ce6e1a9799733fae3febaa075d00c8c19a71f5ec225525a6559bbdcdc7ad3d5**
- BDIX-Playlist.m3u SHA-256: **9cc2eaa4f9209e4d1a2576f9953f47240c176f15a929c41c94b9394f62323d81**
- International-Playlist.m3u SHA-256: **dedc725ba5eccdb5619232a12750cd1b3397122ca4627d5c7a1da58c18c3537c**

