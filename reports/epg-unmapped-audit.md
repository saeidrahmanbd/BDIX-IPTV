# Strict Unmapped EPG Audit

Generated: **2026-10-14T07:53:43+00:00**

This audit compares every unmapped active playlist identity against display names from the configured XMLTV feeds. Candidates have current/future schedule records, but name similarity is not proof of identity.
No candidate in this report is automatically applied to the mapping CSV. Any match must be verified against the source channel identity, territory/variant, and current programme data first.

- Unmapped channel identities reviewed: **235**
- Unmapped identities with at least one review candidate: **161**
- Candidate rows: **661**
- Unmapped identities with no review candidate: **74**

## Candidate matches for manual review

| Group | Playlist channel | Playlist tvg-id | Candidate source name normalized | Candidate EPG ID | Similarity | Usable programme rows | Source feed(s) | Decision |
|---|---|---|---|---|---:|---:|---|---|
| Bangladesh | Ananda TV | AnandaTV.bd | anand | jtv3294 | 0.909 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Ananda TV | AnandaTV.bd | alnada | Al.Nada.TV.ae | 0.833 | 114 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Ananda TV | AnandaTV.bd | abpananda | 142518 | 0.800 | 152 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Ananda TV | AnandaTV.bd | abpananda | LIVETV_LIVETVCHANNEL_ABP_ANANDA | 0.800 | 165 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Ananda TV | AnandaTV.bd | abpananda | jtv672 | 0.800 | 97 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Asian TV | AsianTV.bd | asiandrama | plex.tv.Asian.Drama.plex | 1.000 | 113 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Asian TV | AsianTV.bd | asianet | 142668 | 0.833 | 85 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Asian TV | AsianTV.bd | asianet | ASIANET.in | 0.833 | 139 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz<br>https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Asian TV | AsianTV.bd | asianet | LIVETV_LIVETVCHANNEL_ASIANET | 0.833 | 89 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Asian TV | AsianTV.bd | asianet | LIVETV_LIVETVCHANNEL_ASIANET_HD | 0.833 | 89 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | ATN Bangla | ATNBangla.bd | nkbangla | jtv2933 | 0.824 | 77 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | ATN Bangla | ATNBangla.bd | raatdinbangla | jtv2027 | 0.818 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | ATN Bangla | ATNBangla.bd | tv9bangla | 0-9-378 | 0.778 | 240 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | ATN Bangla | ATNBangla.bd | tv9bangla | LIVETV_LIVETVCHANNEL_TV9_BANGLA | 0.778 | 127 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | ATN Bangla | ATNBangla.bd | tv9bangla | SWIFTTV_LIVECHANNEL_31 | 0.778 | 128 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | ATN News | ATNNews.bd | tnpnews | 158792 | 0.857 | 128 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | ATN News | ATNNews.bd | apnnews | 6433 | 0.857 | 205 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | ATN News | ATNNews.bd | anbnews | LIVETV_LIVETVCHANNEL_ANB_NEWS | 0.857 | 99 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | ATN News | ATNNews.bd | tnpnews | LIVETV_LIVETVCHANNEL_TNP_NEWS | 0.857 | 132 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | ATN News | ATNNews.bd | apnnews | ts286 | 0.857 | 376 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Bangla TV | BanglaTV.bd | rbangla | 143697 | 0.923 | 130 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Bangla TV | BanglaTV.bd | rbangla | R..Bangla.in | 0.923 | 49 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Bangla TV | BanglaTV.bd | ubangla | jtv2184 | 0.923 | 71 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Bangla TV | BanglaTV.bd | rbangla | jtv2780 | 0.923 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Bangla TV | BanglaTV.bd | ubangla | ts1080 | 0.923 | 34 | https://avkb.short.gy/epg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Bangla Vision | BanglaVision.bd | dangervision | 6589 | 0.750 | 28 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Bangla Vision | BanglaVision.bd | usalmavision | Almavision.us | 0.750 | 27 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Bangla Vision | BanglaVision.bd | usgalavision | Galavision.us | 0.750 | 195 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Bangla Vision | BanglaVision.bd | usgalavisionwest | GalavisionPacific.us | 0.750 | 201 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Bangla Vision | BanglaVision.bd | toonavision | Toon-A-Vision.ca2 | 0.696 | 123 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Bengali Beats | custom.bengali.beats | bengali | Bengali.ae | 0.737 | 52 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Boishakhi TV | BoishakhiTV.bd | lokshahi | LIVETV_LIVETVCHANNEL_LOKSHAHI | 0.706 | 145 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Boishakhi TV | BoishakhiTV.bd | lokshahi | LOKSHAHI.in | 0.706 | 49 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Boishakhi TV | BoishakhiTV.bd | rbhakthi | jtv3300 | 0.706 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV National | BTVNational.bd | tv7national | 7257 | 0.909 | 45 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV National | BTVNational.bd | tv7national | jtv3609 | 0.909 | 69 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV National | BTVNational.bd | matvnational | MATV.National.uk | 0.870 | 70 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV National | BTVNational.bd | matvnationaluk | MATVNational.uk | 0.870 | 34 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV National | BTVNational.bd | nationalindia | jtv3105 | 0.842 | 71 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV News | custom.btv.news | wbtvnews | US700004OA | 0.933 | 10 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV News | custom.btv.news | ctvnews | CTV.News.Channel.HD.ca2 | 0.857 | 143 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV News | custom.btv.news | ctvnews | CTV.News.Channel.ca2 | 0.857 | 102 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV News | custom.btv.news | tvcnews | TVC.News.uk | 0.857 | 139 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV News | custom.btv.news | vtvnews | ts497 | 0.857 | 82 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV World | custom.btvworld | ndtvworlduk | NDTVWorld.uk | 0.824 | 64 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV World | custom.btvworld | tvriworld | ts1290 | 0.824 | 82 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV World | custom.btvworld | world | WORLD.Channel.us2 | 0.769 | 96 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV World | custom.btvworld | trtworld | TRT.World.HD.uk | 0.750 | 130 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | BTV World | custom.btvworld | trtworld | TRT.World.ae | 0.750 | 130 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | DBC News | DBCNews.bd | bbcnews | 158142 | 0.857 | 166 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | DBC News | DBCNews.bd | bbcnews | BBC.News.HD.my | 0.857 | 164 | https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | DBC News | DBCNews.bd | bbcnews | BBC.News.ch | 0.857 | 160 | https://epgshare01.online/epgshare01/epg_ripper_CH1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | DBC News | DBCNews.bd | bbcnews | BBCNews.au | 0.857 | 330 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | DBC News | DBCNews.bd | bbcnews | LIVETV_LIVETVCHANNEL_BBC_NEWS | 0.857 | 159 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Deshi TV | DeshiTV.ca@SD | usdesi | DesiChannel.us | 0.727 | 321 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Doyel TV | DoyelTV.ca@SD | dorcel | DORCEL.TV.ca2 | 0.727 | 2 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Doyel TV | DoyelTV.ca@SD | dorcelcanada | Dorcel.TV.Canada.ca2 | 0.727 | 55 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Enter TV | custom.enter.tv | bether | BET.Her.us2 | 0.727 | 93 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Enter TV | custom.enter.tv | hunter | plex.tv.Hunter.plex | 0.727 | 96 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | G Series Drama | custom.gseriesdrama | geniekdrama | US2000012KX | 0.783 | 6 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | G Series Drama | custom.gseriesdrama | usa3series | ATRESseries.us | 0.706 | 119 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | G Series Drama | custom.gseriesdrama | atreseries | Atreseries.us2 | 0.706 | 3 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Global TV | GlobalTV.bd | globalindia | jtv1959 | 1.000 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Global TV | GlobalTV.bd | globalindia | ts1044 | 1.000 | 44 | https://avkb.short.gy/epg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Global TV | GlobalTV.bd | globalbc | Global.BC.HD.ca2 | 0.857 | 113 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Global TV | GlobalTV.bd | globalbc | Global.BC.ca2 | 0.857 | 92 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Global TV | GlobalTV.bd | toiglobal | jtv3440 | 0.800 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Green TV | GreenTV.bd | greengold | 6963 | 0.714 | 49 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Green TV | GreenTV.bd | greengoldindia | 7120 | 0.714 | 49 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Green TV | GreenTV.bd | greengold | IN4000625P | 0.714 | 11 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Green TV | GreenTV.bd | greengold | SWIFTTV_LIVECHANNEL_310 | 0.714 | 13 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Green TV | GreenTV.bd | greengold | jtv3467 | 0.714 | 70 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Jago News 24 | JagoNews24.bd | news24 | 90009 | 0.750 | 130 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Jago News 24 | JagoNews24.bd | news24 | LIVETV_LIVETVCHANNEL_NEWS24 | 0.750 | 144 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Jago News 24 | JagoNews24.bd | news24 | News24.au | 0.750 | 125 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Jago News 24 | JagoNews24.bd | news24 | jtv501 | 0.750 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Jago News 24 | JagoNews24.bd | news24 | ts209 | 0.750 | 82 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Jamuna TV | JamunaTV.bd | janam | 143221 | 0.727 | 84 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Jamuna TV | JamunaTV.bd | janam | LIVETV_LIVETVCHANNEL_JANAM_TV | 0.727 | 87 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Jamuna TV | JamunaTV.bd | janta | LIVETV_LIVETVCHANNEL_JANTA_TV | 0.727 | 141 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Jamuna TV | JamunaTV.bd | janta | jtv880 | 0.727 | 71 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Jamuna TV | JamunaTV.bd | janta | ts371 | 0.727 | 71 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Maasranga TV | MaasrangaTV.bd | amarbangla | jtv1962 | 0.737 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Matribhumi TV | MatribhumiTV.bd | mathrubhuminews | 1309 | 0.720 | 52 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Matribhumi TV | MatribhumiTV.bd | mathrubhuminews | 143309 | 0.720 | 104 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Matribhumi TV | MatribhumiTV.bd | mathrubhuminews | LIVETV_LIVETVCHANNEL_MATHRUBHUMI_NEWS | 0.720 | 120 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Matribhumi TV | MatribhumiTV.bd | mathrubhuminews | jtv780 | 0.720 | 65 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Matribhumi TV | MatribhumiTV.bd | mathrubhuminews | ts394 | 0.720 | 65 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Mohona TV | MohonaTV.bd | mhone | 143539 | 0.727 | 39 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Mohona TV | MohonaTV.bd | mhone | MH.ONE.in | 0.727 | 15 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Mohona TV | MohonaTV.bd | mhone | Mh.One.in2 | 0.727 | 56 | https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Mohona TV | MohonaTV.bd | mhone | ts399 | 0.727 | 25 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Movie Bangla | MovieBangla.bd | monbangla | jtv3298 | 0.800 | 11 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Movie Bangla | MovieBangla.bd | inzeebangla | ZEEBANGLA.in | 0.727 | 249 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Movie Bangla | MovieBangla.bd | sonicbangla | jtv1345 | 0.727 | 26 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Movie Bangla | MovieBangla.bd | zeebangla | 0-9-9z5383484 | 0.700 | 249 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Movie Bangla | MovieBangla.bd | zeebangla | 0-9-zeebangla | 0.700 | 250 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | News 21 | News21BanglaTV.bd@SD | news21 | jtv2008 | 1.000 | 17 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | News 21 | News21BanglaTV.bd@SD | news21 | ts1380 | 1.000 | 41 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | News 21 | News21BanglaTV.bd@SD | news1india | LIVETV_LIVETVCHANNEL_NEWS_1_INDIA | 0.909 | 132 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | News 21 | News21BanglaTV.bd@SD | news1india | jtv936 | 0.909 | 80 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | News 21 | News21BanglaTV.bd@SD | news1india | ts414 | 0.909 | 80 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | News 24 | News24.bd | news24 | 90009 | 1.000 | 130 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | News 24 | News24.bd | news24 | LIVETV_LIVETVCHANNEL_NEWS24 | 1.000 | 144 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | News 24 | News24.bd | news24 | News24.au | 1.000 | 125 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | News 24 | News24.bd | news24 | jtv501 | 1.000 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | News 24 | News24.bd | news24 | ts209 | 1.000 | 82 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | NRB TV | NRBTV.ca | usnrb | NRBTV.us | 0.750 | 253 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | NTV | NTV.bd | inetv | ETV.in | 0.750 | 182 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | NTV | NTV.bd | inntvtelugu | NTVTelugu.in | 0.750 | 72 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | NTV | NTV.bd | onetv | ONETV.ca2 | 0.750 | 129 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | NTV | NTV.bd | intv9telugu | TV9Telugu.in | 0.750 | 273 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | NTV | NTV.bd | inutv | UTV.in | 0.750 | 72 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | NTV Europe | NTVEurope.bd | wrneurope | WRN.Europe.uk | 0.778 | 98 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | NTV Europe | NTVEurope.bd | wrneuropeuk | WRNEurope.uk | 0.778 | 45 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Rajdhani TV | RajdhaniTV.bd | aradhana | jtv777 | 0.750 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Rajdhani TV | RajdhaniTV.bd | madaniuk | MadaniChannel.uk | 0.714 | 40 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | RTV | RTV.bd | trutv | truTV.HD.us2 | 0.750 | 99 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Star News | custom.star.news | abstarnews | jtv1553 | 0.889 | 17 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Star News | custom.star.news | abstarnews | ts1332 | 0.889 | 34 | https://avkb.short.gy/epg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Star News | custom.star.news | taranews | ts866 | 0.875 | 21 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Star News | custom.star.news | vistaarnews | LIVETV_LIVETVCHANNEL_VISTAAR_NEWS | 0.842 | 130 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Star News | custom.star.news | vistaarnews | jtv3070 | 0.842 | 68 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Bangladesh | Time Television | TimeTelevision.us | outsidetelevision | Outside.Television.HD.us2 | 0.839 | 107 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Time Television | TimeTelevision.us | iontelevision | ION.Television.HD.us2 | 0.815 | 89 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Time Television | TimeTelevision.us | televisionxuk | TelevisionX.uk | 0.800 | 33 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Time Television | TimeTelevision.us | usoutsidetelevision | OutsideTelevision.us | 0.788 | 250 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Bangladesh | Time Television | TimeTelevision.us | tamilantelevision | jtv2958 | 0.774 | 47 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Adventure Earth | custom.adventure.earth | skyadventurehd | SkyAdventureHD.uk | 0.714 | 41 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Adventure Earth | custom.adventure.earth | usadventuresports | AdventureSportsTV.us | 0.710 | 72 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Adventure Earth | custom.adventure.earth | skyadventure | Sky.Adventure.uk | 0.692 | 41 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Autentic History | AutenticHistory.de | ustruehistory | TrueHistoryChannel.us | 0.714 | 114 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Autentic History | AutenticHistory.de | dischistory | Disc.History.uk | 0.692 | 76 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Autentic History | AutenticHistory.de | truehistory | plex.tv.True.History.plex | 0.692 | 113 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Autentic History | AutenticHistory.de | axmenbyhistory | plex.tv.Ax.Men.by.History.plex | 0.690 | 108 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | DISCOVERY BANGLA | custom.bdix.discoverybangla | discoverybengali | jtv3428 | 0.839 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | DISCOVERY BANGLA | custom.bdix.discoverybangla | discoverybengali | jtv573 | 0.839 | 54 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | DISCOVERY BANGLA | custom.bdix.discoverybangla | discoveryasia | Discovery.Asia.HD.my | 0.786 | 96 | https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | DISCOVERY BANGLA | custom.bdix.discoverybangla | discoveryasia | Discovery.Asia.hk | 0.786 | 90 | https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | DISCOVERY BANGLA | custom.bdix.discoverybangla | discoveryenglish | jtv242 | 0.774 | 54 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ 2 | custom.documentary.2 | documentarycanada | Documentary.Canada.ca2 | 0.957 | 20 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ 2 | custom.documentary.2 | documentary | SWIFTTV_LIVECHANNEL_288 | 0.957 | 52 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ 2 | custom.documentary.2 | documentary | USAJ3504701A | 0.957 | 8 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ 2 | custom.documentary.2 | documentary | documentary.HD.ca2 | 0.957 | 25 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ 2 | custom.documentary.2 | documentary | plex.tv.Documentary+.plex | 0.957 | 72 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ International | DocumentaryPlus | documentarycanada | Documentary.Canada.ca2 | 1.000 | 20 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ International | DocumentaryPlus | documentary | SWIFTTV_LIVECHANNEL_288 | 1.000 | 52 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ International | DocumentaryPlus | documentary | USAJ3504701A | 1.000 | 8 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ International | DocumentaryPlus | documentary | documentary.HD.ca2 | 1.000 | 25 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ International | DocumentaryPlus | documentary | plex.tv.Documentary+.plex | 1.000 | 72 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ USA | custom.documentary.usa | documentarycanada | Documentary.Canada.ca2 | 1.000 | 20 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ USA | custom.documentary.usa | documentary | SWIFTTV_LIVECHANNEL_288 | 1.000 | 52 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ USA | custom.documentary.usa | documentary | USAJ3504701A | 1.000 | 8 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ USA | custom.documentary.usa | documentary | documentary.HD.ca2 | 1.000 | 25 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Documentary+ USA | custom.documentary.usa | documentary | plex.tv.Documentary+.plex | 1.000 | 72 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Mystery TV | MysteryTV.us | ionmystery | ION.Mystery.us2 | 0.824 | 47 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Mystery TV | MysteryTV.us | ionmystery | USBC24000223S | 0.824 | 7 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Mystery TV | MysteryTV.us | ionmystery | plex.tv.Ion.Mystery.plex | 0.824 | 94 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Mystery TV | MysteryTV.us | mysteria | plex.tv.Mysteria.plex | 0.800 | 132 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Mystery TV | MysteryTV.us | usionmystery | IonMystery.us | 0.737 | 161 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | RT Documentary | RTDocumentary.ru | documentarycanada | Documentary.Canada.ca2 | 0.917 | 20 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | RT Documentary | RTDocumentary.ru | documentary | SWIFTTV_LIVECHANNEL_288 | 0.917 | 52 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | RT Documentary | RTDocumentary.ru | documentary | USAJ3504701A | 0.917 | 8 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | RT Documentary | RTDocumentary.ru | documentary | documentary.HD.ca2 | 0.917 | 25 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | RT Documentary | RTDocumentary.ru | documentary | plex.tv.Documentary+.plex | 0.917 | 72 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Travelxp English | custom.travelxp.english | travelxp | 144014 | 1.000 | 136 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Travelxp English | custom.travelxp.english | travelxp | LIVETV_LIVETVCHANNEL_TRAVELXP | 1.000 | 149 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Travelxp English | custom.travelxp.english | travelxp | Travelxp.HD.in | 1.000 | 182 | https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Travelxp English | custom.travelxp.english | travelxp | Travelxp.uk | 1.000 | 138 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz<br>https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Travelxp English | custom.travelxp.english | travelxp | travelxp.ch | 1.000 | 150 | https://epgshare01.online/epgshare01/epg_ripper_CH1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Wild Flix Hindi | custom.wild.flix.hindi | wildflix | IN460000585 | 1.000 | 8 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Wild Flix Hindi | custom.wild.flix.hindi | wildfire | US1900013Z7 | 0.750 | 8 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Wild Flix Hindi | custom.wild.flix.hindi | kidsflix | plex.tv.KidsFlix.plex | 0.750 | 79 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Wild Planet | custom.wild.planet | animalplanetenglish | Animal.Planet.English.in | 0.727 | 107 | https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Wild Planet | custom.wild.planet | animalplanet | Animal.Planet.uk | 0.727 | 80 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Wild Planet | custom.wild.planet | animalplanet | AnimalPlanet.au | 0.727 | 118 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Wild Planet | custom.wild.planet | animalplanet | LIVETV_LIVETVCHANNEL_ANIMAL_PLANET | 0.727 | 85 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | Wild Planet | custom.wild.planet | animalplanet | LIVETV_LIVETVCHANNEL_ANIMAL_PLANET_WORLD_HD | 0.727 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | World War TV | custom.world.war.tv | worldwaruk | WorldWarTV.uk | 1.000 | 34 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | World War TV | custom.world.war.tv | world | WORLD.Channel.us2 | 0.769 | 96 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | XXTreme Jobs Hindi | custom.xxtreme.jobs.hindi | xxtremejobs | IN46000011Q | 1.000 | 8 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| Documentary & Wildlife | XXTreme Jobs Hindi | custom.xxtreme.jobs.hindi | extremejobs | plex.tv.Extreme.Jobs.plex | 0.909 | 105 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Aamar Bangla | AamarBangla.in@SD | amarbangla | jtv1962 | 0.952 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Aamar Bangla | AamarBangla.in@SD | rbangla | 143697 | 0.778 | 130 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Aamar Bangla | AamarBangla.in@SD | rbangla | INBD2500016OR | 0.778 | 13 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Aamar Bangla | AamarBangla.in@SD | rbangla | R..Bangla.in | 0.778 | 49 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Aamar Bangla | AamarBangla.in@SD | rbangla | jtv2780 | 0.778 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Amar Bangla Digital | custom.amar.bangla.digital | amardigital | jtv3297 | 0.786 | 14 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Amar Bangla Digital | custom.amar.bangla.digital | amarbangla | jtv1962 | 0.741 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Bangla Cinema | custom.banglacinema | zeebanglacinema | ZEE.BANGLA.CINEMA.in | 0.889 | 12 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Bangla Cinema | custom.banglacinema | zeebanglacinema | jtv685 | 0.889 | 20 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Bangla Cinema | custom.banglacinema | alfacinema | Alfa.Cinema.ae | 0.818 | 62 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Bangla Cinema | custom.banglacinema | airtelbanglacinema | LIVETV_LIVETVCHANNEL_AIRTEL_BANGLA_CINEMA | 0.800 | 371 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Bangla Cinema | custom.banglacinema | colorsbanglacinema | LIVETV_LIVETVCHANNEL_COLORS_BANGLA_CINEMA | 0.800 | 31 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Bangla Plus | BanglaPlus.in | rbangla | 143697 | 0.800 | 130 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Bangla Plus | BanglaPlus.in | rbangla | R..Bangla.in | 0.800 | 49 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Bangla Plus | BanglaPlus.in | ubangla | jtv2184 | 0.800 | 71 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Bangla Plus | BanglaPlus.in | rbangla | jtv2780 | 0.800 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Bangla Plus | BanglaPlus.in | ubangla | ts1080 | 0.800 | 34 | https://avkb.short.gy/epg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Jhankar TV | JhankarTV.ca | sanskar | 143713 | 0.714 | 84 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Jhankar TV | JhankarTV.ca | sanskar | LIVETV_LIVETVCHANNEL_SANSKAR | 0.714 | 113 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Jhankar TV | JhankarTV.ca | sanskar | Sanskar.uk | 0.714 | 97 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz<br>https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Jhankar TV | JhankarTV.ca | sanskar | jtv288 | 0.714 | 51 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Jhankar TV | JhankarTV.ca | sanskar | ts43 | 0.714 | 51 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | JTV Bangla | JTVBangla.in@SD | tv9bangla | 0-9-378 | 0.889 | 240 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | JTV Bangla | JTVBangla.in@SD | tv9bangla | 144026 | 0.889 | 116 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | JTV Bangla | JTVBangla.in@SD | tv9bangla | LIVETV_LIVETVCHANNEL_TV9_BANGLA | 0.889 | 127 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | JTV Bangla | JTVBangla.in@SD | tv9bangla | SWIFTTV_LIVECHANNEL_31 | 0.889 | 128 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | JTV Bangla | JTVBangla.in@SD | stvbangla | jtv3331 | 0.889 | 78 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Jtv Classic | custom.jtv.classic | mtvclassic | MTV.Classic.us2 | 0.900 | 76 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Jtv Classic | custom.jtv.classic | tvbclassic | TVB.Classic.HD.my | 0.900 | 98 | https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Jtv Classic | custom.jtv.classic | usmtvclassic | MTVClassic.us | 0.818 | 161 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Jtv Classic | custom.jtv.classic | usmtvclassicwest | MTVClassicPacific.us | 0.818 | 161 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Jtv Classic | custom.jtv.classic | classics | Classics.au | 0.778 | 145 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Orange Bangla TV | OrangeBanglaTV.in@SD | sangeetbangla | 143756 | 0.800 | 65 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Orange Bangla TV | OrangeBanglaTV.in@SD | sangeetbangla | LIVETV_LIVETVCHANNEL_SANGEET_BANGLA | 0.800 | 72 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Orange Bangla TV | OrangeBanglaTV.in@SD | sangeetbangla | SANGEET.BANGLA.in | 0.800 | 25 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Orange Bangla TV | OrangeBanglaTV.in@SD | sangeetbangla | jtv740 | 0.800 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Orange Bangla TV | OrangeBanglaTV.in@SD | sangeetbangla | ts215 | 0.800 | 41 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Sananda | SanandaTV.in | anand | jtv3294 | 0.833 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Sananda | SanandaTV.in | alnada | Al.Nada.TV.ae | 0.769 | 114 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Sananda | SanandaTV.in | sansad | jtv520 | 0.769 | 107 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Sananda | SanandaTV.in | sansad | jtv522 | 0.769 | 88 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Sananda | SanandaTV.in | abpananda | LIVETV_LIVETVCHANNEL_ABP_ANANDA | 0.750 | 165 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | SNB Cinema | custom.snb.cinema | zbcinema | jtv3322 | 0.824 | 12 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | SNB Cinema | custom.snb.cinema | uscinemax | CineMAX.us | 0.778 | 88 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | SNB Cinema | custom.snb.cinema | uscinemaxwest | CineMAXPacific.us | 0.778 | 89 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | SNB Cinema | custom.snb.cinema | uscinemaxaction | CinemaxAction.us | 0.778 | 88 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | SNB Cinema | custom.snb.cinema | skycinemacomedy | Sky.Cinema.Comedy.uk | 0.778 | 42 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Star Bangla | custom.starbangla | sonarbangla | jtv3602 | 0.857 | 12 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Star Bangla | custom.starbangla | stvbangla | jtv3331 | 0.842 | 78 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Star Bangla | custom.starbangla | rbangla | 143697 | 0.824 | 130 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Bangla | Star Bangla | custom.starbangla | rbangla | R..Bangla.in | 0.824 | 49 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Bangla | Star Bangla | custom.starbangla | rbangla | jtv2780 | 0.824 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | nickmalayalam | jtv1340 | 0.870 | 34 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | ddmalayalam | 142791 | 0.857 | 114 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | ddmalayalam | LIVETV_LIVETVCHANNEL_DD_MALAYALAM | 0.857 | 143 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | ddmalayalam | jtv699 | 0.857 | 70 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | C Malayalam TV | CMalayalamTV.ca@SD | ddmalayalam | ts328 | 0.857 | 70 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Colors MENA | custom.colors.mena | colors | 158149 | 1.000 | 95 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Colors MENA | custom.colors.mena | colors | COLORS.HD.uk | 1.000 | 120 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Colors MENA | custom.colors.mena | colors | COLORS.hk | 1.000 | 114 | https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Colors MENA | custom.colors.mena | colors | Colors.in | 1.000 | 168 | https://iptv-epg.org/files/epg-in.xml.gz<br>https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Colors MENA | custom.colors.mena | colors | LIVETV_LIVETVCHANNEL_COLORS_HD | 1.000 | 97 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Flowers US | custom.flowers.us | flowers | 143065 | 1.000 | 84 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Flowers US | custom.flowers.us | flowers | FLOWERS.in | 1.000 | 41 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Flowers US | custom.flowers.us | flowers | LIVETV_LIVETVCHANNEL_FLOWERS_TV | 1.000 | 84 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Flowers US | custom.flowers.us | flowers | ts10 | 1.000 | 59 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Flowers US | custom.flowers.us | flower | jtv634 | 0.923 | 59 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | kairali | 143247 | 1.000 | 36 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | kairali | KAIRALI.in | 1.000 | 16 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | kairali | LIVETV_LIVETVCHANNEL_KAIRALI_TV | 1.000 | 37 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | kairali | jtv710 | 1.000 | 27 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kairali Arabia | KairaliArabia.in | kairali | ts25 | 1.000 | 26 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kalika TV | KalikaTV.in@SD | kalinga | 143250 | 0.769 | 160 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kalika TV | KalikaTV.in@SD | kalinga | 6382 | 0.769 | 62 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kalika TV | KalikaTV.in@SD | kalinga | LIVETV_LIVETVCHANNEL_KALINGA_TV | 0.769 | 167 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kalika TV | KalikaTV.in@SD | kalinga | jtv781 | 0.769 | 102 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kalika TV | KalikaTV.in@SD | kalinga | ts375 | 0.769 | 102 | https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kerala Vision | KeralaVision.in@SD | usalmavision | Almavision.us | 0.750 | 27 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kerala Vision | KeralaVision.in@SD | usgalavision | Galavision.us | 0.750 | 195 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kerala Vision | KeralaVision.in@SD | usgalavisionwest | GalavisionPacific.us | 0.750 | 201 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kerala Vision | KeralaVision.in@SD | powervision | 143670 | 0.696 | 130 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Kerala Vision | KeralaVision.in@SD | tamilvisioncanada | Tamil.Vision.(Canada).ca2 | 0.696 | 121 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | MH One Prime | Mh1Prime.in | mhonedilse | 143536 | 0.700 | 33 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | MNTV (Tamil) | MarutamTV.in | indtamil | DTamil.in | 0.706 | 72 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | NKR TV Kannada | NKRTVKannada.in | rkannada | 142883 | 0.889 | 131 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | NKR TV Kannada | NKRTVKannada.in | rkannada | R.KANNADA.in | 0.889 | 49 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | NKR TV Kannada | NKRTVKannada.in | rkannada | jtv923 | 0.889 | 84 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | NKR TV Kannada | NKRTVKannada.in | rkannada | ts342 | 0.889 | 83 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | NKR TV Kannada | NKRTVKannada.in | nickkannada | jtv1244 | 0.857 | 34 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | NTV (Malyalam) | custom.ntv.malayalam | newsmalayalam | 7138 | 0.750 | 38 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | NTV (Malyalam) | custom.ntv.malayalam | inddmalayalam | DDMalayalam.in | 0.750 | 260 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | NTV (Malyalam) | custom.ntv.malayalam | nickmalayalam | jtv1340 | 0.750 | 34 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | NTV (Malyalam) | custom.ntv.malayalam | newsmalayalam | jtv3184 | 0.750 | 43 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | NTV (Malyalam) | custom.ntv.malayalam | ddmalayalam | LIVETV_LIVETVCHANNEL_DD_MALAYALAM | 0.727 | 143 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | SADA TV | SADATV.in | sadhna | jtv593 | 0.800 | 47 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | SADA TV | SADATV.in | sadhna | ts447 | 0.800 | 47 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Sooriyan TV | SooriyanTV.ca@SD | suriya | jtv3394 | 0.714 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Starnet | Starnet.in@SD | barnetuk | EFLBarnet.uk | 0.769 | 9 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Starnet | Starnet.in@SD | startnetwork | Start.TV.Network.us2 | 0.737 | 82 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Starnet | Starnet.in@SD | asianet | LIVETV_LIVETVCHANNEL_ASIANET | 0.714 | 89 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Starnet | Starnet.in@SD | asianet | LIVETV_LIVETVCHANNEL_ASIANET_HD | 0.714 | 89 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Starnet | Starnet.in@SD | usstart | StartTV.us | 0.714 | 173 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Swantham | Swantham.in@SD | sathiyam | 143765 | 0.750 | 116 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Swantham | Swantham.in@SD | sathiyam | LIVETV_LIVETVCHANNEL_SATHIYAM_TV | 0.750 | 129 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Swantham | Swantham.in@SD | sathiyam | SATHIYAM.TV.in | 0.750 | 44 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Swantham | Swantham.in@SD | sathiyam | jtv671 | 0.750 | 74 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Entertainment | Swantham | Swantham.in@SD | sathiyam | ts455 | 0.750 | 74 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Epic Bhojpuri Digital | custom.epic.bhojpuri.digital | epicbhojpuri | 157803 | 0.774 | 22 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Epic Bhojpuri Digital | custom.epic.bhojpuri.digital | epicbhojpuri | IN800020ZZ | 0.774 | 4 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Epic Bhojpuri Digital | custom.epic.bhojpuri.digital | epicbhojpuri | LIVETV_LIVETVCHANNEL_FILAMCHI_BHOJPURI | 0.774 | 32 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Epic Bhojpuri Digital | custom.epic.bhojpuri.digital | epicbhojpuri | jtv3384 | 0.774 | 18 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Epic Bhojpuri Digital | custom.epic.bhojpuri.digital | epicbhojpuri | ts830 | 0.774 | 14 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Goldmines 2 | Goldmines2.in@SD | goldminesmovies | 142881 | 0.947 | 22 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Goldmines 2 | Goldmines2.in@SD | goldmines | 143087 | 0.947 | 22 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Goldmines 2 | Goldmines2.in@SD | goldmines | LIVETV_LIVETVCHANNEL_GOLDMINES | 0.947 | 1 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Goldmines 2 | Goldmines2.in@SD | goldminesmovies | ts1499 | 0.947 | 14 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Goldmines 2 | Goldmines2.in@SD | goldmines | ts823 | 0.947 | 14 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Goldmines Action | GoldminesAction.in | goldminesmovies | 142881 | 1.000 | 22 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Goldmines Action | GoldminesAction.in | goldmines | 143087 | 1.000 | 22 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Goldmines Action | GoldminesAction.in | goldmines | LIVETV_LIVETVCHANNEL_GOLDMINES | 1.000 | 1 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Goldmines Action | GoldminesAction.in | goldminesmovies | ts1499 | 1.000 | 14 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Goldmines Action | GoldminesAction.in | goldmines | ts823 | 1.000 | 14 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Hindi Movie Classic 24 | new.hindi.movie.classic.24 | familymovieclassics | Family.Movie.Classics.us2 | 0.684 | 54 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Hindi Movies | custom.hindi.movies | india | 143199 | 0.800 | 96 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Hindi Movies | custom.hindi.movies | injmovies | JMovies.in | 0.800 | 72 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Hindi Movies | custom.hindi.movies | india | LIVETV_LIVETVCHANNEL_INDIA_TV | 0.800 | 108 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Hindi Movies | custom.hindi.movies | india | jtv235 | 0.800 | 61 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Hindi Movies | custom.hindi.movies | india | ts104 | 0.800 | 60 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | MH One Movies | MHOneMovies.in | mhone | 143539 | 1.000 | 39 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | MH One Movies | MHOneMovies.in | mhone | MH.ONE.in | 1.000 | 15 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | MH One Movies | MHOneMovies.in | mhone | Mh.One.in2 | 1.000 | 56 | https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | MH One Movies | MHOneMovies.in | mhone | ts399 | 1.000 | 25 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | MH One Movies | MHOneMovies.in | onemovies | One.Movies.ae | 0.900 | 62 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | surfcinema | plex.tv.Surf.Cinema.plex | 0.762 | 120 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | zbcinema | jtv3322 | 0.737 | 12 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | alshashacinema | Al.Shasha.Cinema.ae | 0.720 | 62 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | uscinemax | CineMAX.us | 0.700 | 88 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Shubh Cinema TV | ShubhCinemaTV.in | uscinemaxwest | CineMAXPacific.us | 0.700 | 89 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Sony Max 2 [US] | custom.sony.max.2 | sonymax2 | 143801 | 1.000 | 23 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Sony Max 2 [US] | custom.sony.max.2 | sonymax2 | LIVETV_LIVETVCHANNEL_SONY_MAX_2 | 1.000 | 26 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | Sony Max 2 [US] | custom.sony.max.2 | sonymax2 | SONY.MAX.2.uk | 1.000 | 34 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Sony Max 2 [US] | custom.sony.max.2 | sonymax2uk | SonyMax2.uk | 1.000 | 16 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | Sony Max 2 [US] | custom.sony.max.2 | sonymax2 | jtv483 | 1.000 | 16 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | South Movies | custom.south.movies | shoutmovies | plex.tv.Shout!.Movies.plex | 0.909 | 46 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | South Movies | custom.south.movies | usshoutmovies | ShoutMovies.us | 0.833 | 78 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | South Movies | custom.south.movies | shout | USBD1200021JM | 0.800 | 13 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Indian Movies | South Movies | custom.south.movies | shout | plex.tv.Shout!.TV.plex | 0.800 | 148 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Movies | South Movies | custom.south.movies | usthemovie | TheMovieChannel.us | 0.762 | 90 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Music | 7X Punjabi | custom.7x.punjabi | ddpunjabi | 142800 | 0.778 | 129 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Music | 7X Punjabi | custom.7x.punjabi | ddpunjabi | DD.PUNJABI.in | 0.778 | 53 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Music | 7X Punjabi | custom.7x.punjabi | ddpunjabi | LIVETV_LIVETVCHANNEL_DD_PUNJABI | 0.778 | 155 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Music | 7X Punjabi | custom.7x.punjabi | ddpunjabi | jtv715 | 0.778 | 83 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Music | 7X Punjabi | custom.7x.punjabi | ddpunjabi | ts335 | 0.778 | 83 | https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Music | YRF Music Nepal | YRFMusic.in@Nepal | yrfmusic | jtv2753 | 0.762 | 38 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Music | Zoom Music | custom.zoommusic | dhoommusic | 142882 | 0.842 | 109 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Indian Music | Zoom Music | custom.zoommusic | dhoommusic | DHOOM.MUSIC.in | 0.842 | 42 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Indian Music | Zoom Music | custom.zoommusic | dhoommusic | LIVETV_LIVETVCHANNEL_DHOOM_MUSIC | 0.842 | 135 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Indian Music | Zoom Music | custom.zoommusic | zbmusic | jtv3319 | 0.750 | 28 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Indian Music | Zoom Music | custom.zoommusic | musicindia | 143563 | 0.714 | 38 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| International | 4ever Cinema | 4everCinema.ua | zeecinemausa | 0-9-179 | 0.800 | 73 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| International | 4ever Cinema | 4everCinema.ua | zeecinema | 0-9-zeecinema | 0.800 | 54 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| International | 4ever Cinema | 4everCinema.ua | zeecinema | 0-9-zeecinemahd | 0.800 | 52 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| International | 4ever Cinema | 4everCinema.ua | zeecinemauk | 0-9-zeecinemauk | 0.800 | 51 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| International | 4ever Cinema | 4everCinema.ua | zeecinemausa | Zee.Cinema.USA.in | 0.800 | 51 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| International | 4ever Drama | 4everDrama.ua | 4seven | 4Seven.ch | 0.727 | 79 | https://epgshare01.online/epgshare01/epg_ripper_CH1.xml.gz | MANUAL_REVIEW_ONLY |
| International | 4ever Drama | 4everDrama.ua | 4sevenuk | 4Seven.uk | 0.727 | 32 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| International | 4ever Drama | 4everDrama.ua | 4seven | 4seven.uk | 0.727 | 73 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | 4ever Music | 4everMusic.ua | etvmusic | 143023 | 0.778 | 52 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| International | 4ever Music | 4everMusic.ua | etvmusic | LIVETV_LIVETVCHANNEL_ETV_ABHIRUCHI | 0.778 | 57 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| International | 4ever Music | 4everMusic.ua | etvmusic | jtv3559 | 0.778 | 11 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | 4ever Music | 4everMusic.ua | etvmusic | ts358 | 0.778 | 33 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| International | 4ever Music | 4everMusic.ua | fevamusic | DISTROTV_LIVETVCHANNEL_4595 | 0.737 | 1 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| International | American Idol | custom.american.idol | meritcanada | Merit.TV.Canada.ca2 | 0.696 | 133 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | American Idol | custom.american.idol | americancrimes | American.Crimes.us2 | 0.692 | 91 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | American Idol | custom.american.idol | americanheroescanada | American.Heroes.Channel.-.Canada.ca2 | 0.692 | 76 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | American Idol | custom.american.idol | usamericanhero | AmericanHeroesChannel.us | 0.692 | 163 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | American Idol | custom.american.idol | americancrimes | plex.tv.American.Crimes.plex | 0.692 | 111 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | AXN Black Czech Republic | AXNBlack.us@CzechRepublic | starzinblack | Starz.in.Black.HD.us2 | 0.700 | 52 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | AXN Black Poland | AXNBlack.us@Poland | starzinblack | Starz.in.Black.HD.us2 | 0.700 | 52 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | AXN Black Poland | AXNBlack.us@Poland | blackpooluk | EFLBlackpool.uk | 0.696 | 9 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| International | Baraza Music TV | BarazaMusicTV.gr | starmaamusic | 143828 | 0.783 | 76 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| International | Baraza Music TV | BarazaMusicTV.gr | starmaamusic | LIVETV_LIVETVCHANNEL_STAR_MAA_MUSIC | 0.783 | 84 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| International | Baraza Music TV | BarazaMusicTV.gr | starmaamusic | STAR.MAA.MUSIC.in | 0.783 | 29 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| International | Baraza Music TV | BarazaMusicTV.gr | starmaamusic | Star.Maa.Music.in | 0.783 | 48 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | Baraza Music TV | BarazaMusicTV.gr | starmaamusic | ts389 | 0.783 | 20 | https://avkb.short.gy/epg.xml.gz | MANUAL_REVIEW_ONLY |
| International | CANADA ONE | custom.bdix.canadaone | uscanalonce | CanalOnce.us | 0.700 | 208 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | CNN INTERNATIONLA | custom.bdix.cnninternationla | cnninternational | 157679 | 0.938 | 80 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| International | CNN INTERNATIONLA | custom.bdix.cnninternationla | cnninternational | CNN.International.ae | 0.938 | 346 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| International | CNN INTERNATIONLA | custom.bdix.cnninternationla | cnninternational | CNN.International.ca2 | 0.938 | 90 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | CNN INTERNATIONLA | custom.bdix.cnninternationla | cnninternational | CNN.International.hk | 0.938 | 81 | https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | CNN INTERNATIONLA | custom.bdix.cnninternationla | cnninternational | CNN.International.us2 | 0.938 | 90 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | EBS Cinema | EBSCinema.us | zbcinema | jtv3322 | 0.824 | 12 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | EBS Cinema | EBSCinema.us | zeecinemausa | 0-9-179 | 0.778 | 73 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| International | EBS Cinema | EBSCinema.us | uscinemax | CineMAX.us | 0.778 | 88 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | EBS Cinema | EBSCinema.us | uscinemaxwest | CineMAXPacific.us | 0.778 | 89 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | EBS Cinema | EBSCinema.us | uscinemaxaction | CinemaxAction.us | 0.778 | 88 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | EU Music | EUMusic.ua | musicindia | 143563 | 0.833 | 38 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| International | EU Music | EUMusic.ua | musicindia | INBD4700015M0 | 0.833 | 5 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| International | EU Music | EUMusic.ua | musicindia | jtv250 | 0.833 | 24 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | EU Music | EUMusic.ua | b4umusic | B4U.Music.uk | 0.800 | 102 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | EU Music | EUMusic.ua | sunmusic | LIVETV_LIVETVCHANNEL_SUN_MUSIC | 0.800 | 66 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| International | FON Music | custom.fon.music | onlymusic | jtv903 | 0.824 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | FON Music | custom.fon.music | musicindia | 143563 | 0.769 | 38 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| International | FON Music | custom.fon.music | musicindia | INBD4700015M0 | 0.769 | 5 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| International | FON Music | custom.fon.music | musicindia | jtv250 | 0.769 | 24 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | FON Music | custom.fon.music | sunmusic | LIVETV_LIVETVCHANNEL_SUN_MUSIC | 0.750 | 66 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| International | iFilm English | iFilmEnglish.ir | film4 | Film4.HD.uk | 0.800 | 32 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | iFilm English | iFilmEnglish.ir | film4uk | Film4.uk | 0.800 | 14 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| International | iFilm English | iFilmEnglish.ir | english | 6616 | 0.737 | 50 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml | MANUAL_REVIEW_ONLY |
| International | iFilm English | iFilmEnglish.ir | tlcenglish | TLC.English.in | 0.727 | 105 | https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz | MANUAL_REVIEW_ONLY |
| International | iFilm English | iFilmEnglish.ir | tlcenglish | jtv479 | 0.727 | 47 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | MBC Drama USA | MBCDramaUSA.us | mbcdrama | MBC.Drama.ae | 1.000 | 70 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| International | MBC Drama USA | MBCDramaUSA.us | usmbcdrama | MBCDrama.us | 0.889 | 161 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | MBC Drama USA | MBCDramaUSA.us | cbcdrama | CBC.Drama.ae | 0.875 | 68 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| International | MBC Drama USA | MBCDramaUSA.us | dmcdrama | DMC.Drama.ae | 0.875 | 62 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| International | MBC Drama USA | MBCDramaUSA.us | mbcmasrdrama | MBC.Masr.Drama.HD.ae | 0.800 | 87 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Megogo Music | MegogoMusic.ua | megamusiq | 143532 | 0.700 | 60 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| International | Megogo Music | MegogoMusic.ua | megamusiq | LIVETV_LIVETVCHANNEL_MEGA_MUSIQ | 0.700 | 64 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| International | Megogo Music | MegogoMusic.ua | megamusiq | MEGA.MUSIQ.in | 0.700 | 22 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| International | Megogo Music | MegogoMusic.ua | megamusiq | ts400 | 0.700 | 39 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| International | Mei Ah Movie Channel | MeiAhMovieChannel.hk | mahamovies | jtv809 | 0.800 | 2 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | Mei Ah Movie Channel | MeiAhMovieChannel.hk | maamovies | LIVETV_LIVETVCHANNEL_STAR_MAA_MOVIES | 0.737 | 29 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| International | Mei Ah Movie Channel | MeiAhMovieChannel.hk | maamovies | jtv1111 | 0.737 | 16 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | Mei Ah Movie Channel | MeiAhMovieChannel.hk | maamovies | jtv760 | 0.737 | 16 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | Mei Ah Movie Channel | MeiAhMovieChannel.hk | miramaxmovie | plex.tv.Miramax.Movie.Channel.plex | 0.727 | 44 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Movies Thriller | MoviesThriller.sa@SD | moviesphere | Moviesphere.au | 0.720 | 78 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Movies Thriller | MoviesThriller.sa@SD | skythriller | Sky.Thriller.HD.uk | 0.720 | 35 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Movies Thriller | MoviesThriller.sa@SD | moviesphere | USBD17000117B | 0.720 | 4 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | Movies Thriller | MoviesThriller.sa@SD | moviesphere | plex.tv.MOVIESPHERE.plex | 0.720 | 45 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Movies Thriller | MoviesThriller.sa@SD | crimethrillher | plex.tv.Crime.ThrillHer.plex | 0.714 | 82 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | MovieSphere AU | MovieSphere.us@AU | moviesphere | Moviesphere.au | 1.000 | 78 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| International | MovieSphere AU | MovieSphere.us@AU | moviesphere | USBD17000117B | 1.000 | 4 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | MovieSphere AU | MovieSphere.us@AU | moviesphere | plex.tv.MOVIESPHERE.plex | 1.000 | 45 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | MovieSphere AU | MovieSphere.us@AU | usmoviesphere | MOVIESPHERE.us | 0.917 | 77 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | MovieSphere AU | MovieSphere.us@AU | moviespheregold | MovieSphere.Gold.us2 | 0.846 | 47 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | MovieSphere UK | MovieSphere.us@UK | moviesphere | Moviesphere.au | 1.000 | 78 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| International | MovieSphere UK | MovieSphere.us@UK | moviesphere | USBD17000117B | 1.000 | 4 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | MovieSphere UK | MovieSphere.us@UK | moviesphere | plex.tv.MOVIESPHERE.plex | 1.000 | 45 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | MovieSphere UK | MovieSphere.us@UK | usmoviesphere | MOVIESPHERE.us | 0.917 | 77 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | MovieSphere UK | MovieSphere.us@UK | moviespheregold | MovieSphere.Gold.us2 | 0.846 | 47 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | My Cinema | MyCinema.us | skycinemacomedy | Sky.Cinema.Comedy.uk | 0.824 | 42 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | My Cinema | MyCinema.us | cinemax | CINEMAX.hk | 0.800 | 39 | https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | My Cinema | MyCinema.us | cinemaxaction | Cinemax.Action.us2 | 0.800 | 43 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | My Cinema | MyCinema.us | cinemax | Cinemax.HD.us2 | 0.800 | 41 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | My Cinema | MyCinema.us | zbcinema | jtv3322 | 0.750 | 12 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | My Cinema Europe | MyCinemaEurope.ch | skycinemacomedy | Sky.Cinema.Comedy.uk | 0.824 | 42 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | My Cinema Europe | MyCinemaEurope.ch | cinemax | CINEMAX.hk | 0.800 | 39 | https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | My Cinema Europe | MyCinemaEurope.ch | cinemaxaction | Cinemax.Action.us2 | 0.800 | 43 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | My Cinema Europe | MyCinemaEurope.ch | cinemax | Cinemax.HD.us2 | 0.800 | 41 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | My Cinema Europe | MyCinemaEurope.ch | zbcinema | jtv3322 | 0.750 | 12 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | Mytime Movie | MyTimeMovieNetwork.uk@SD | moviemovie | MOVIE.MOVIE.hk | 0.762 | 33 | https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Mytime Movie | MyTimeMovieNetwork.uk@SD | mytimemovienetwork | USBC3900018K6 | 0.759 | 6 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | Mytime Movie | MyTimeMovieNetwork.uk@SD | mytimemovienetwork | plex.tv.MyTime.Movie.Network.plex | 0.759 | 60 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Mytime Movie | MyTimeMovieNetwork.uk@SD | alltimemovies | 160750 | 0.750 | 23 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| International | Mytime Movie | MyTimeMovieNetwork.uk@SD | alltimemovies | All.Time.Movies.Tv.in2 | 0.750 | 18 | https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz | MANUAL_REVIEW_ONLY |
| International | MyTime Movie Network BR | MyTimeMovieNetwork.br@SD | mytimemovienetwork | USBC3900018K6 | 1.000 | 6 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | MyTime Movie Network BR | MyTimeMovieNetwork.br@SD | mytimemovienetwork | plex.tv.MyTime.Movie.Network.plex | 1.000 | 60 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | MyTime Movie Network BR | MyTimeMovieNetwork.br@SD | usmytimemovienetwork | MyTimeMovieNetwork.us | 0.947 | 98 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | MyTime Movie Network BR | MyTimeMovieNetwork.br@SD | uslifetimemovienetworkwest | LifetimeMovieNetworkPacific.us | 0.800 | 102 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | MyTime Movie Network BR | MyTimeMovieNetwork.br@SD | uslifetimemoviesnetwork | LifetimeMoviesNetwork.us | 0.780 | 102 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | MyTime Movie Network East | MyTimeMovieNetworkEast.us | mytimemovienetwork | USBC3900018K6 | 1.000 | 6 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | MyTime Movie Network East | MyTimeMovieNetworkEast.us | mytimemovienetwork | plex.tv.MyTime.Movie.Network.plex | 1.000 | 60 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | MyTime Movie Network East | MyTimeMovieNetworkEast.us | usmytimemovienetwork | MyTimeMovieNetwork.us | 0.947 | 98 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | MyTime Movie Network East | MyTimeMovieNetworkEast.us | uslifetimemovienetworkwest | LifetimeMovieNetworkPacific.us | 0.800 | 102 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | MyTime Movie Network East | MyTimeMovieNetworkEast.us | uslifetimemoviesnetwork | LifetimeMoviesNetwork.us | 0.780 | 102 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | NASHE Music | NASHEMusic.ua | 7smusic | LIVETV_LIVETVCHANNEL_7S_MUSIC | 0.706 | 144 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| International | NASHE Music | NASHEMusic.ua | peacemusic | jtv1103 | 0.700 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | Pardesi TV | PardesiTV.ca | parvasi | 4908 | 0.714 | 49 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml | MANUAL_REVIEW_ONLY |
| International | POP World TV | POPWorldTV.es | world | WORLD.Channel.us2 | 0.769 | 96 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | POP World TV | POPWorldTV.es | loveworld | LoveWorld.HD.uk | 0.706 | 107 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | POP World TV | POPWorldTV.es | loveworlduk | LoveWorld.uk | 0.706 | 50 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| International | POP World TV | POPWorldTV.es | loveworld | jtv3313 | 0.706 | 43 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | POP World TV | POPWorldTV.es | plutopixelworld | USAJ3504531A | 0.696 | 8 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | PowerTürk TV | PowerTurkTV.tr | power | 143669 | 0.769 | 130 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| International | PowerTürk TV | PowerTurkTV.tr | power | LIVETV_LIVETVCHANNEL_POWER_TV | 0.769 | 142 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| International | PowerTürk TV | PowerTurkTV.tr | power | POWER.TV.in | 0.769 | 49 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| International | PowerTürk TV | PowerTurkTV.tr | power | jtv2743 | 0.769 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | PowerTürk TV | PowerTurkTV.tr | power | ts824 | 0.769 | 82 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| International | Rakuten Movies | RakutenMovies | atnmovies | ATN.Movies.us2 | 0.818 | 29 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Rakuten Movies | RakutenMovies | rakutenviki | plex.tv.Rakuten.Viki.plex | 0.778 | 113 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Rakuten Movies | RakutenMovies | enmoviesaction | EN:.Movies.Action.sa | 0.762 | 36 | https://epgshare01.online/epgshare01/epg_ripper_SA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Rakuten Movies | RakutenMovies | greatmovies | 0-9-9z5910243 | 0.750 | 108 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| International | Rakuten Movies | RakutenMovies | greatmovies | GREAT!.movies.uk | 0.750 | 90 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Rakuten TV Comedy Movies UK | RakutenTVComedyMovies.es@UK | plutobetcomedymovies | BETComedyMovies.pluto | 0.769 | 12 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | Sony Movies | SonyMovies.in | sonymovie | Sony.Movie.Channel.HD.us2 | 0.947 | 43 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Sony Movies | SonyMovies.in | ussonymovie | SonyMovieChannel.us | 0.857 | 92 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | Sony Movies | SonyMovies.in | onemovies | One.Movies.ae | 0.842 | 62 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Sony Movies | SonyMovies.in | enmoviesaction | EN:.Movies.Action.sa | 0.778 | 36 | https://epgshare01.online/epgshare01/epg_ripper_SA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Sony Movies | SonyMovies.in | usmovies | Movies!.us | 0.778 | 84 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | Sony One Favoris | SonyOneFavoris.fr@HD | sonycine | Sony.Cine.us2 | 0.800 | 47 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Sony One Favoris | SonyOneFavoris.fr@HD | skyone | Sky.One.HD.uk | 0.769 | 89 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Sony One Favoris | SonyOneFavoris.fr@HD | skyoneuk | SkyOne.uk | 0.769 | 41 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| International | Sony One Favoris | SonyOneFavoris.fr@HD | sonymovie | Sony.Movie.Channel.HD.us2 | 0.750 | 43 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Sony One Favoris | SonyOneFavoris.fr@HD | spondon | jtv2435 | 0.714 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | Sparkle Movies | GBAJ400042T1 | starmovies | 140069 | 0.783 | 22 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| International | Sparkle Movies | GBAJ400042T1 | starmovies | 143829 | 0.783 | 22 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| International | Sparkle Movies | GBAJ400042T1 | starmovies | LIVETV_LIVETVCHANNEL_STAR_MOVIES | 0.783 | 29 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| International | Sparkle Movies | GBAJ400042T1 | starmovies | LIVETV_LIVETVCHANNEL_STAR_MOVIES_HD | 0.783 | 29 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| International | Sparkle Movies | GBAJ400042T1 | starmovies | jtv1104 | 0.783 | 19 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | Stingray Rock Alternative | StingrayRockAlternative.ca | stingrayalternative | Stingray.Alternative.ca2 | 0.905 | 25 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Rock Alternative | StingrayRockAlternative.ca | usstingrayalternative | StingrayAlternative.us | 0.864 | 41 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Rock Alternative | StingrayRockAlternative.ca | stingrayadultalternative | Stingray.Adult.Alternative.ca2 | 0.809 | 25 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Rock Alternative | StingrayRockAlternative.ca | usstingrayadultalternative | StingrayAdultAlternative.us | 0.776 | 41 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Rock Alternative | StingrayRockAlternative.ca | stingrayrock | Stingray.Rock.ca2 | 0.686 | 25 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Stream 101 | custom.recovered.stingray.101 | stingrayclassicastream | plex.tv.Stingray.Classica.Stream.plex | 0.718 | 71 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Stream 101 | custom.recovered.stingray.101 | stingrayspa | USBD3500013DG | 0.714 | 4 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | Stingray Stream 101 | custom.recovered.stingray.101 | stingraynature | Stingray.Nature.ca2 | 0.710 | 25 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Stream 101 | custom.recovered.stingray.101 | stingraysoulstorm | plex.tv.Stingray.Soul.Storm.plex | 0.706 | 71 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Stream 101 | custom.recovered.stingray.101 | stingrayjammin | Stingray.Jammin’.ca2 | 0.690 | 25 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Stream 137 | custom.recovered.stingray.137 | stingrayclassicastream | plex.tv.Stingray.Classica.Stream.plex | 0.718 | 71 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Stream 137 | custom.recovered.stingray.137 | stingrayspa | USBD3500013DG | 0.714 | 4 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | Stingray Stream 137 | custom.recovered.stingray.137 | stingraynature | Stingray.Nature.ca2 | 0.710 | 25 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Stream 137 | custom.recovered.stingray.137 | stingraysoulstorm | plex.tv.Stingray.Soul.Storm.plex | 0.706 | 71 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Stingray Stream 137 | custom.recovered.stingray.137 | stingrayjammin | Stingray.Jammin’.ca2 | 0.690 | 25 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Totalmusic | Totalmusic.uk | rotanamusic | Rotana.Music.ae | 0.762 | 178 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Totalmusic | Totalmusic.uk | onlymusic | jtv903 | 0.737 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | Totalmusic | Totalmusic.uk | usrotanamusic | RotanaMusic.us | 0.696 | 96 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | Totalmusic | Totalmusic.uk | tataplaymusic | ts737 | 0.696 | 17 | https://avkb.short.gy/epg.xml.gz | MANUAL_REVIEW_ONLY |
| International | Trace UK | TraceUK.uk | grace | Grace.TV.in | 0.800 | 89 | https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Trace UK | TraceUK.uk | grace | jtv2775 | 0.800 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| International | Trace UK | TraceUK.uk | travel | IN400053KM | 0.727 | 6 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| International | Trace UK | TraceUK.uk | travel | TravelChannel.au | 0.727 | 244 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Trace UK | TraceUK.uk | artrace01 | RACE01.art | 0.714 | 45 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | Vevo Hip Hop & R&B | GBBD2300001C0 | vevohiphop | USBC3600002EK | 0.909 | 7 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | Vevo Hip Hop & R&B | GBBD2300001C0 | vevohiphop | Vevo.Hip-Hop.us2 | 0.909 | 75 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | Vevo Hip Hop & R&B | GBBD2300001C0 | hiphoprb | plex.tv.Hip-Hop/R&B.plex | 0.800 | 71 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | Vevo Hip Hop & R&B | GBBD2300001C0 | vevopop | USBC3600008WY | 0.737 | 6 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | Vevo Hip Hop & R&B | GBBD2300001C0 | vevopop | Vevo.Pop.us2 | 0.737 | 57 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| International | XITE Hits UK | XITEHits.nl@UK | xitehits | USBD3300004RH | 1.000 | 3 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| International | XITE Hits UK | XITEHits.nl@UK | xitehits | plex.tv.XITE.Hits.plex | 1.000 | 31 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| International | XITE Hits UK | XITEHits.nl@UK | usxitehits | XITEHits.us | 0.889 | 63 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| International | XITE Hits UK | XITEHits.nl@UK | thatsuk | ThatsTV.uk | 0.706 | 46 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | ADN TV+ | ADNTVPlus.fr | accdn | plex.tv.ACCDN.plex | 0.750 | 45 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | Afarin TV | AfarinTV.iq | safari | 143739 | 0.833 | 130 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Kids | Afarin TV | AfarinTV.iq | safari | LIVETV_LIVETVCHANNEL_SAFARI_TV | 0.833 | 144 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Kids | Afarin TV | AfarinTV.iq | safari | SAFARI.TV.in | 0.833 | 49 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | Afarin TV | AfarinTV.iq | safari | jtv1666 | 0.833 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Kids | Afarin TV | AfarinTV.iq | safari | ts436 | 0.833 | 82 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | Dios Te Ve Kids | custom.dios.te.ve.kids | discoverykids | 159011 | 0.720 | 261 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Kids | Dios Te Ve Kids | custom.dios.te.ve.kids | discoverykids | Discovery.Kids.in | 0.720 | 166 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Kids | Dios Te Ve Kids | custom.dios.te.ve.kids | discoverykids | LIVETV_LIVETVCHANNEL_DISCOVERY_KIDS | 0.720 | 297 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Kids | Dios Te Ve Kids | custom.dios.te.ve.kids | discoverykidstelugu | jtv3447 | 0.720 | 166 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Kids | Dios Te Ve Kids | custom.dios.te.ve.kids | discoverykidsmalayalam | jtv3448 | 0.720 | 166 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Kids | Doraemon TV | custom.doraemon.tv | dramon | USAJ3000002OC | 0.857 | 8 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Kids | Doraemon TV | custom.doraemon.tv | dragon | Dragon.TV.hk | 0.714 | 9 | https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | Epic Kids Digital | custom.epic.kids.digital | epickids | 159014 | 0.696 | 127 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Kids | Epic Kids Digital | custom.epic.kids.digital | epickids | IN800021X7 | 0.696 | 7 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| Kids | Epic Kids Digital | custom.epic.kids.digital | epickids | LIVETV_LIVETVCHANNEL_GUBBARE | 0.696 | 54 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Kids | Epic Kids Digital | custom.epic.kids.digital | epickids | jtv3385 | 0.696 | 39 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Kids | Epic Kids Digital | custom.epic.kids.digital | epickids | ts867 | 0.696 | 80 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | Lego Channel | LegoChannel.us@SD | thelego | USBA2300001S8 | 0.727 | 17 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Kids | Moonbug Kids | MoonbugKids.uk | moonbug | Moonbug.au | 0.778 | 282 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | Moonbug Kids | MoonbugKids.uk | moonbug | Moonbug.my | 0.778 | 135 | https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | Moonbug Kids | MoonbugKids.uk | moonbug | USBB11000015Q | 0.778 | 14 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Kids | Powerkids Kartoon Channel | custom.powerkids.kartoon.channel | powerkids | IN2500003JW | 0.720 | 28 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| Kids | Powerkids Kartoon Channel | custom.powerkids.kartoon.channel | powerkids | SWIFTTV_LIVECHANNEL_78 | 0.720 | 360 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Kids | Powerkids Kartoon Channel | custom.powerkids.kartoon.channel | powerkids | jtv2774 | 0.720 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Kids | Smurf TV | SmurfTV.us | surfer | USBB10000058A | 0.727 | 7 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Kids | Smurf TV | SmurfTV.us | surfer | plex.tv.Surfer.TV.plex | 0.727 | 91 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | Toon Goggles Junior | custom.toon.goggles.junior | toongoggles | INBA4900026FJ | 0.786 | 16 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| Kids | Toon Goggles Junior | custom.toon.goggles.junior | toongoggles | USBB1900004J9 | 0.786 | 6 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Kids | Toon Goggles Junior | custom.toon.goggles.junior | toongoggles | plex.tv.Toon.Goggles.plex | 0.786 | 138 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | Toon Goggles Junior | custom.toon.goggles.junior | ustoongoggles | ToonGoggles.us | 0.733 | 41 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | Toonami Aftermath East | custom.toonami.aftermath.east | ustoonamiaftermath | ToonamiAftermath.us | 0.941 | 55 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Kids | WOW Kidz Tamil | custom.wow.kidz.tamil | indtamil | DTamil.in | 0.700 | 72 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | aur LIFE | aurLIFE.pk | sunlife | 143873 | 0.714 | 50 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Pakistani | aur LIFE | aurLIFE.pk | gmalife | GMA.Life.TV.hk | 0.714 | 69 | https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | aur LIFE | aurLIFE.pk | gmalife | GMA.Life.TV.us2 | 0.714 | 83 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | aur LIFE | aurLIFE.pk | sunlife | LIVETV_LIVETVCHANNEL_SUN_LIFE | 0.714 | 58 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Pakistani | aur LIFE | aurLIFE.pk | sunlife | Sun.Life.my | 0.714 | 43 | https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | discoverykidstamil | jtv550 | 0.765 | 166 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | discoverykids | 159011 | 0.759 | 261 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | discoverykids | Discovery.Kids.in | 0.759 | 166 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | discoverykids | LIVETV_LIVETVCHANNEL_DISCOVERY_KIDS | 0.759 | 297 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Discover Pakistan | DiscoverPakistan.pk@SD | discoverykidstelugu | jtv3447 | 0.759 | 166 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Grace Network | GraceNetwork.pk@SD | racernetwork | RACER.Network.HD.us2 | 0.917 | 118 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | Grace Network | GraceNetwork.pk@SD | usracernetwork | RacerNetwork.us | 0.846 | 237 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | Grace Network | GraceNetwork.pk@SD | accnetwork | ACC.Network.us2 | 0.818 | 55 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | Grace Network | GraceNetwork.pk@SD | usaenetwork | AandENetwork.us | 0.783 | 227 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | Grace Network | GraceNetwork.pk@SD | usaenetworkwest | AandENetworkPacific.us | 0.783 | 227 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | Jalwa TV | JalwaTV.pk@SD | 9xjalwa | INBC2800013L6 | 0.833 | 3 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Jalwa TV | JalwaTV.pk@SD | 9xjalwa | LIVETV_LIVETVCHANNEL_9X_JALWA | 0.833 | 141 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Jalwa TV | JalwaTV.pk@SD | 9xjalwa | jtv440 | 0.833 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Jalwa TV | JalwaTV.pk@SD | alawla | Alawla.ae | 0.727 | 70 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | Jalwa TV | JalwaTV.pk@SD | jalshamovies | LIVETV_LIVETVCHANNEL_JALSHA_MOVIES_HD | 0.727 | 31 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Joo Music | JooMusic.pk | dhoommusic | 142882 | 0.778 | 109 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Joo Music | JooMusic.pk | dhoommusic | DHOOM.MUSIC.in | 0.778 | 42 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | Joo Music | JooMusic.pk | dhoommusic | LIVETV_LIVETVCHANNEL_DHOOM_MUSIC | 0.778 | 135 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Joo Music | JooMusic.pk | musicindia | 143563 | 0.769 | 38 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Pakistani | Joo Music | JooMusic.pk | musicindia | jtv250 | 0.769 | 24 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Pakistani | King TV | KingTV.pk@SD | alkingdrama | Alking.Drama.TV.ae | 0.800 | 62 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | King TV | KingTV.pk@SD | kingdt | KING-DT.ca2 | 0.800 | 92 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | King TV | KingTV.pk@SD | kalinga | 143250 | 0.727 | 160 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Pakistani | King TV | KingTV.pk@SD | cooking | Cooking.Channel.HD.us2 | 0.727 | 124 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Pakistani | King TV | KingTV.pk@SD | kalinga | LIVETV_LIVETVCHANNEL_KALINGA_TV | 0.727 | 167 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Religious | Al Quran Al Kareem TV | AlQuranAlKareemTV.sa | alquranalkarem | Al.Quran.Al.Karem.ae | 0.966 | 52 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Al Quran Al Kareem TV | AlQuranAlKareemTV.sa | qurankareem | Quran.Kareem.ae | 0.846 | 52 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Al Quran Al Kareem TV | AlQuranAlKareemTV.sa | misrqurankareem | Misr.Quran.Kareem.ae | 0.733 | 114 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Al Quran Al Kareem TV | AlQuranAlKareemTV.sa | alrayyanalqadeem | Al.Rayyan.Al.Qadeem.HD.ae | 0.710 | 69 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Al Quran Al Kareem TV | AlQuranAlKareemTV.sa | qurankareemjordan | Quran.Kareem.Jordan.ae | 0.688 | 52 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Islamic TV | IslamicTV.bd | islam | Islam.Channel.uk | 0.833 | 169 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Islamic TV | IslamicTV.bd | islam | Islam.TV.uk | 0.833 | 106 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Islamic TV | IslamicTV.bd | islamuk | IslamChannel.uk | 0.833 | 74 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Islamic TV | IslamicTV.bd | islamuk | IslamTV.uk | 0.833 | 49 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Madani TV | custom.madani.tv | madaniuk | MadaniChannel.uk | 1.000 | 40 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Madani TV | custom.madani.tv | madanichnl | Madani.Chnl.uk | 0.750 | 88 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Madani TV | custom.madani.tv | madha | 143287 | 0.727 | 131 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Religious | Madani TV | custom.madani.tv | madha | LIVETV_LIVETVCHANNEL_MADHA_TV | 0.727 | 147 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Religious | Madani TV | custom.madani.tv | madha | jtv1655 | 0.727 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Religious | MADANI TV BANGLA | custom.bdix.madanibangla | monbangla | jtv3298 | 0.762 | 11 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Religious | MADANI TV BANGLA | custom.bdix.madanibangla | madanichnl | Madani.Chnl.uk | 0.727 | 88 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | MADANI TV BANGLA | custom.bdix.madanibangla | nickbangla | jtv1341 | 0.727 | 34 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Religious | MADANI TV BANGLA | custom.bdix.madanibangla | amarbangla | jtv1962 | 0.727 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Religious | MADANI TV BANGLA | custom.bdix.madanibangla | raatdinbangla | jtv2027 | 0.720 | 82 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Religious | MADINA LIVE | custom.bdix.madinalive | amazonlive | US4900004KP | 0.700 | 13 | https://i.mjh.nz/SamsungTVPlus/us.xml | MANUAL_REVIEW_ONLY |
| Religious | MADINA LIVE | custom.bdix.madinalive | mrbeanliveaction | plex.tv.Mr..Bean.Live.Action.plex | 0.700 | 186 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | MADINA LIVE | custom.bdix.madinalive | yaadeinactive | 209090 | 0.696 | 65 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Religious | MADINA LIVE | custom.bdix.madinalive | mangalmaylive | jtv1794 | 0.696 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Religious | Makkah Live | custom.makkah.live | makkal | 143296 | 0.750 | 153 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml | MANUAL_REVIEW_ONLY |
| Religious | Makkah Live | custom.makkah.live | makkal | 708 | 0.750 | 40 | https://avkb.short.gy/jioepg.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Makkah Live | custom.makkah.live | makkal | LIVETV_LIVETVCHANNEL_MAKKAL_TV | 0.750 | 171 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml | MANUAL_REVIEW_ONLY |
| Religious | Makkah Live | custom.makkah.live | makkal | jtv708 | 0.750 | 97 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Religious | Makkah Live | custom.makkah.live | makkal | ts392 | 0.750 | 97 | https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz<br>https://avkb.short.gy/epg.xml.gz<br>https://avkb.short.gy/tsepg.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Medina Live | MedinaLive.bd | entlive | IN400000830 | 0.706 | 9 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| Religious | Medina Live | MedinaLive.bd | mrbeanliveaction | plex.tv.Mr..Bean.Live.Action.plex | 0.700 | 186 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Peace TV Bangla | PeaceTVBangla.ae | zeebanglainternational | 0-9-366 | 0.800 | 215 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| Religious | Peace TV Bangla | custom.peacetvbangla | zeebanglainternational | 0-9-366 | 0.800 | 215 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| Religious | Peace TV Bangla | PeaceTVBangla.ae | zeebangla | 0-9-9z5383484 | 0.800 | 249 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| Religious | Peace TV Bangla | custom.peacetvbangla | zeebangla | 0-9-9z5383484 | 0.800 | 249 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| Religious | Peace TV Bangla | PeaceTVBangla.ae | zeebangla | 0-9-zeebangla | 0.800 | 250 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| Religious | Peace TV Bangla | custom.peacetvbangla | zeebangla | 0-9-zeebangla | 0.800 | 250 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml | MANUAL_REVIEW_ONLY |
| Religious | Peace TV Bangla | PeaceTVBangla.ae | zeebangla | Zee.Bangla.HD.in | 0.800 | 161 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Peace TV Bangla | custom.peacetvbangla | zeebangla | Zee.Bangla.HD.in | 0.800 | 161 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Peace TV Bangla | PeaceTVBangla.ae | zeebanglainternational | Zee.Bangla.International.in | 0.800 | 161 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Peace TV Bangla | custom.peacetvbangla | zeebanglainternational | Zee.Bangla.International.in | 0.800 | 161 | https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz | MANUAL_REVIEW_ONLY |
| Religious | Quran TV | QuranTV.iq | urbanaction | 6602 | 0.800 | 30 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml | MANUAL_REVIEW_ONLY |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | beinsports2 | beIN.SPORTS.2.hk | 0.800 | 55 | https://epgshare01.online/epgshare01/epg_ripper_HK1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | beinsports2 | beIN.SPORTS.2.my | 0.800 | 55 | https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | beinsports2 | beINSports2.au | 0.800 | 96 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | dubaisports2 | Dubai.Sports.2.ae | 0.769 | 31 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Bahrain Sports 2 | BahrainSports2.bh@SD | beinsportsusa | beIN.Sports.USA.HD.us2 | 0.750 | 84 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | beIN SPORTS 7 | beINSports7.qa | beinsportscanada | beIN.Sports.HD.(Canada).ca2 | 0.952 | 83 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | beIN SPORTS 7 | beINSports7.qa | beinsports | beIN.Sports.HD.ae | 0.952 | 37 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | beIN SPORTS 7 | beINSports7.qa | beinsportsusa | beIN.Sports.USA.HD.us2 | 0.952 | 84 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | beIN SPORTS 7 | beINSports7.qa | usbeinsports7 | beINSPORTS7.us | 0.917 | 47 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | beIN SPORTS 7 | beINSports7.qa | beinsports3 | beINSports3.au | 0.909 | 127 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | FOX Cricket 501 | foxsports501hd.au | foxcricket | FoxCricket.au | 0.870 | 130 | https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Goal TV | GoalTV.in | globalindia | jtv1959 | 0.800 | 41 | https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml | MANUAL_REVIEW_ONLY |
| Sports | Goal TV | GoalTV.in | globalindia | ts1044 | 0.800 | 44 | https://avkb.short.gy/epg.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | IN: -HINDI- STAR SPORTS 1 HD | Star Sports 1 Hindi HD.in | instarsports1 | StarSports1.in | 0.839 | 276 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | IN: -HINDI- STAR SPORTS 1 HD | Star Sports 1 Hindi HD.in | instarsports1hindi | StarSports1Hindi.in | 0.839 | 321 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | IN: -HINDI- STAR SPORTS 1 HD | Star Sports 1 Hindi HD.in | instarsports1tamil | StarSports1Tamil.in | 0.839 | 350 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | IN: -HINDI- STAR SPORTS 1 HD | Star Sports 1 Hindi HD.in | instarsports1telugu | StarSports1Telugu.in | 0.839 | 300 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | IN: -HINDI- STAR SPORTS 1 HD | Star Sports 1 Hindi HD.in | instarsports3 | StarSports3.in | 0.774 | 310 | https://iptv-epg.org/files/epg-in.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | PK Sports | PKSports.pk@SD | ppvsports | PPV.Sports.ca2 | 0.824 | 20 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | PK Sports | PKSports.pk@SD | skysportsuk | SkySportsPlus.uk | 0.824 | 37 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | PK Sports | PKSports.pk@SD | ksasports1 | KSA.sports.1.ae | 0.778 | 106 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | PK Sports | PKSports.pk@SD | ksasports2 | KSA.sports.2.HD.ae | 0.778 | 106 | https://epgshare01.online/epgshare01/epg_ripper_AE1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | PK Sports | PKSports.pk@SD | uspxsports | PXSports.us | 0.778 | 198 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | PTV Sports | PTVSports.pk | ppvsports | PPV.Sports.ca2 | 0.889 | 20 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | PTV Sports | PTVSports.pk | tvasports2 | TVA.Sports.2.HD.ca2 | 0.842 | 4 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | PTV Sports | PTVSports.pk | ftfsports | plex.tv.FTF.Sports.plex | 0.778 | 72 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | PTV Sports | PTVSports.pk | wedotvsports | IN2100015RL | 0.762 | 13 | https://i.mjh.nz/SamsungTVPlus/in.xml | MANUAL_REVIEW_ONLY |
| Sports | PTV Sports | PTVSports.pk | prmtvflosports0 | FloSports0.prmtv | 0.750 | 45 | https://iptv-epg.org/files/epg-us.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Sky Sports Cricket | SkySportsCricket.ie | skysportscricketuk | SkySportsCricket.uk | 1.000 | 31 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Sky Sports Cricket | SkySportsCricket.ie | skyspcricket | SkySp.Cricket.uk | 0.857 | 68 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Sky Sports Cricket | SkySportsCricket.ie | skyspcricket | SkySpCricket.HD.uk | 0.857 | 68 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Sky Sports Cricket | SkySportsCricket.ie | skysportsuk | SkySportsPlus.uk | 0.741 | 37 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Sky Sports Cricket | SkySportsCricket.ie | skysportsmixuk | SkySportsMix.uk | 0.733 | 34 | https://www.open-epg.com/files/unitedkingdom.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | T Sports | TSports.bd | ftfsports | plex.tv.FTF.Sports.plex | 0.875 | 72 | https://epgshare01.online/epgshare01/epg_ripper_PLEX1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | T Sports | TSports.bd | tntsports1 | TNT.Sports.1.HD.uk | 0.824 | 62 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | T Sports | TSports.bd | tntsports2 | TNT.Sports.2.HD.uk | 0.824 | 79 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | T Sports | TSports.bd | tntsports3 | TNT.Sports.3.HD.uk | 0.824 | 100 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | T Sports | TSports.bd | tntsports4 | TNT.Sports.4.HD.uk | 0.824 | 78 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Ten Sports | TenSports.pk | tntsports2 | TNT.Sports.2.HD.uk | 0.842 | 79 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Ten Sports | TenSports.pk | tntsports3 | TNT.Sports.3.HD.uk | 0.842 | 100 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Ten Sports | TenSports.pk | tntsports4 | TNT.Sports.4.HD.uk | 0.842 | 78 | https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Ten Sports | TenSports.pk | beinsportscanada | beIN.Sports.HD.(Canada).ca2 | 0.842 | 83 | https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz | MANUAL_REVIEW_ONLY |
| Sports | Ten Sports | TenSports.pk | beinsportsusa | beIN.Sports.USA.HD.us2 | 0.842 | 84 | https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz | MANUAL_REVIEW_ONLY |

## Unmapped identities without a schedule-backed candidate

| Group | Channel | Playlist tvg-id | Status | Reason |
|---|---|---|---|---|
| Bangladesh | Bijoy TV | BijoyTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | BOISHAKHAI TV HD | custom.bdix.boishakhai | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | BTV Chattogram | BTVChattogram.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | BTV CTG | custom.bdix.btvctg | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Channel 1 | custom.channel.1 | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Channel 24 | Channel24.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Channel 9 | Channel9.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Channel I | ChannelI.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Channel S | ChannelS.uk | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Deepto TV | DeeptoTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Desh TV | DeshTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Deshe Bideshe | custom.deshe.bideshe | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Duronto TV | DurontoTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Ekattor TV | EkattorTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Ekhon TV | EkhonTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Ekushey TV | EkusheyTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | G TV | GaziTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | GAZI TV HD | custom.bdix.gazi | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Independent TV | IndependentTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Jonmobhumi TV | custom.jonmobhumitv | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | ME TV | METV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | My TV | MyTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Nagorik TV | NagorikTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Nexus TV | NexusTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Probashi TV | custom.probashitv | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | SA TV | SATV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | SATV HD | custom.bdix.satv | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Somoy TV | SomoyNewsTV.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | SRK | custom.srk | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Bangladesh | Thikana | ThikanaTV.us | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Documentary & Wildlife | Autentic Adventure Earth | custom.autentic.adventure.earth | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Documentary & Wildlife | Inside Crime | InsideCrime.us | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Documentary & Wildlife | Terra Mater WILD English | custom.terra.mater.wild.english | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Bangla | Channel 52 | staging.channel.52 | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Bangla | Jalsha Bangla BD | custom.jalsha.bangla.bd | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Entertainment | Baiscope TV | custom.baiscope.tv | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Entertainment | Mei Alai TV | MeiAlaiTV.in | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Entertainment | Oli TV | OliTV.in@SD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Entertainment | Pulari TV | PulariTV.in@SD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Entertainment | Q TV | QTV.in | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Entertainment | UTV Palakkad | UTVPalakkad.in@SD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Movies | Mango | Mango.in@SD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Music | Deewana | DeewanaHD.in | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Music | Hindi Hits | HindiHits.in | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Indian Music | Rang Rangoli | custom.rang.rangoli | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | AXN CEE | AXNCEE.es@Hungary | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | CBN TV USA | custom.cbn.tv.usa | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | CMC-USA | CMCUSACountryMusicChannel.us@SD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | EBS Musika | EBSMusika.us | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | EPIX TV | custom.epix.tv | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | FilmUA Live | FilmUALive.ua | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | Metro TV (Honduras) | MetroTV.hn | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | Rakuten TV Action Movies UK | RakutenTVActionMovies.es@UK | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | Rakuten TV Drama Movies UK | RakutenTVDramaMovies.es@UK | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | Rakuten TV Family Movies UK | RakutenTVFamilyMovies.es@UK | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | Sony One Hits Action | SonyOneHitsAction.fr@HD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | Sony One Hits Comedie | SonyOneHitsComedie.fr@HD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | Totalmusic 80s | Totalmusic80s.uk | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | Totalmusic Concerts | TotalmusicConcerts.uk | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| International | Totalmusic Dance | TotalmusicDance.uk | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Kids | Bantul the Great | custom.bantul.the.great | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Kids | Motu Patlu | custom.motu.patlu | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Kids | Tom and Jerry | TomAndJerry.do | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Kids | Tooku | Tooku.ru | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Kids | WOW Kidz Hindi | WOWKidz.in@Hindi | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Kids | WOW Kidz Telugu | WOWKidz.in@Telugu | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Pakistani | 8XM | 8XM.pk@SD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Pakistani | Falak TV | FalakTV.pk@SD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Pakistani | HUM Sitaray | custom.humsitaray | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Pakistani | Jeremiah TV | JeremiahTV.pk@SD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Pakistani | Joshua TV | JoshuaTV.pk@SD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Pakistani | Paighan TV | PaighanTV.pk@SD | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Religious | ARY Q TV | custom.ary.q.tv | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |
| Sports | PK: GEO SUPER | custom.bdix.geosuper | NO_GUIDE_HIT | No name-similar source ID with current/future programme rows in configured feeds |

## Bangladesh-specific review

Bangladesh-group identities are never automatically fuzzy-matched. Candidate rows are research leads only; only an exact tvg-id or a specifically verified alias may be promoted. The official BTV site publishes daily and weekly programme schedule pages, but the latest indexed daily and weekly schedule pages found in this audit were last updated in August 2025 and are not a current reliable automated schedule feed. No stale or fabricated schedules are inserted.

