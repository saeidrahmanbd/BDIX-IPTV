# EPG Timing Audit

Automatic corrections require repeated cross-source title and duration matches, at least four consistent matches, >=75% agreement, at least three source IDs, and a displacement of two hours or more.

## Detected corrections

- **Alankar TV** (AlankarTV.in@SD): source ID Alankar.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **CNN** (CNN.us): source ID CNN.ro from https://iptv-epg.org/files/epg-ro.xml.gz shifted by +48 hours after repeated cross-source agreement.
- **DD Girnar** (DDGirnar.in@SD): source ID DDGirnar.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Goa** (DDGoa.in@SD): source ID DDGOA.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Haryana** (DDHaryana.in@SD): source ID DDHaryana.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Kashir** (DDKashir.in@SD): source ID DDKashir.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Malayalam** (DDMalayalam.in@SD): source ID DDMalayalam.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Meghalaya** (DDMeghalaya.in@SD): source ID DDMEGHALAYA.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Mizoram** (DDMizoram.in): source ID DDMIZORAM.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Nagaland** (DDNagaland.in@SD): source ID DDNAGALAND.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Punjabi** (DDPunjabi.in@SD): source ID DDPunjabi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Saptagiri** (DDSaptagiri.in@SD): source ID DDSaptagiri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Yadagiri** (DDYadagiri.in@SD): source ID DDYadagiri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Enter10 Bangla** (Enter10Bangla.in): source ID Enterr10Bangla.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Fakt Marathi** (FaktMarathi.in@SD): source ID FaktMarathi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Love Nature** (LoveNature.us): source ID LoveNature.au from https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz shifted by +3 hours after repeated cross-source agreement.
- **Nepal 1** (Nepal1.in@SD): source ID Nepal1.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Pitaara** (Pitaara.in): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Pitaara TV** (Pitaara.in@SD): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Shemaroo TV** (ShemarooTV.in@SD): source ID ShemarooTV.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Shubh TV** (ShubhTV.in@SD): source ID ShubhTV.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Siri Kannada** (SiriKannada.in@SD): source ID SiriKannada.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Stingray Classica** (StingrayClassica.ca@SD): source ID StingrayClassica.ca from https://iptv-epg.org/files/epg-ca.xml.gz shifted by -6 hours after repeated cross-source agreement.
- **Sun Bangla** (SunBangla.in@SD): source ID SunBangla.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Sun TV** (SunTV.in@HD): source ID SUN.TV.HD.my from https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz shifted by +2.5 hours after repeated cross-source agreement.
- **TV9 Bangla** (TV9Bangla.in): source ID SWIFTTV_LIVECHANNEL_31 from https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml shifted by -5.5 hours after repeated cross-source agreement.
- **Tarang TV** (TarangTV.in@SD): source ID Tarang.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Unique TV** (UniqueTV.in@SD): source ID UniqueTV.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Love Nature** (custom.love-natural): source ID LoveNature.au from https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz shifted by +3 hours after repeated cross-source agreement.
- **Sun Bangla** (custom.sun-bangla-k1d4w): source ID SunBangla.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

## Feed-wide offset patterns

- **https://www.open-epg.com/files/india.xml.gz**: 24 channels were corrected by the same -5.5 hours. This looks like a feed-wide timezone problem; other channels from this feed without cross-source overlap may still be shifted and should be reviewed.

Detected source-ID corrections: **30**
