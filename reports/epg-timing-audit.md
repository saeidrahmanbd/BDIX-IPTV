# EPG Timing Audit

Automatic corrections require repeated cross-source title and duration matches, at least four consistent matches, >=75% agreement, at least three source IDs, and a displacement of two hours or more.

## Detected corrections

- **Alankar TV** (AlankarTV.in@SD): source ID Alankar.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **BBC Earth** (BBCEarth.ca): source ID BBCEarth.ro from https://iptv-epg.org/files/epg-ro.xml.gz shifted by -24 hours after repeated cross-source agreement.
- **DD Bangla** (DDBangla.in@SD): source ID DDBangla.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Girnar** (DDGirnar.in@SD): source ID DDGirnar.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Goa** (DDGoa.in@SD): source ID DDGOA.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Kashir** (DDKashir.in@SD): source ID DDKashir.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Malayalam** (DDMalayalam.in@SD): source ID DDMalayalam.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Meghalaya** (DDMeghalaya.in@SD): source ID DDMEGHALAYA.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Mizoram** (DDMizoram.in): source ID DDMIZORAM.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Nagaland** (DDNagaland.in@SD): source ID DDNAGALAND.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Odia** (DDOdia.in@SD): source ID ts333 from https://avkb.short.gy/tsepg.xml.gz shifted by -24 hours after repeated cross-source agreement.
- **DD Punjabi** (DDPunjabi.in@SD): source ID DDPunjabi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Saptagiri** (DDSaptagiri.in@SD): source ID DDSaptagiri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Yadagiri** (DDYadagiri.in@SD): source ID DDYadagiri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Discovery Kids** (DiscoveryKids.au): source ID ts119 from https://avkb.short.gy/tsepg.xml.gz shifted by -24 hours after repeated cross-source agreement.
- **Fakt Marathi** (FaktMarathi.in@SD): source ID FaktMarathi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **HBO 2** (HBO2.cz@SD): source ID HBO2.ro from https://iptv-epg.org/files/epg-ro.xml.gz shifted by -24 hours after repeated cross-source agreement.
- **HBO 3** (HBO3.cz@SD): source ID HBO3.ro from https://iptv-epg.org/files/epg-ro.xml.gz shifted by -24 hours after repeated cross-source agreement.
- **History Channel** (History.hu): source ID History.ro from https://iptv-epg.org/files/epg-ro.xml.gz shifted by -24 hours after repeated cross-source agreement.
- **M4 Sport** (M4Sport.hu@SD): source ID M4Sport.ro from https://iptv-epg.org/files/epg-ro.xml.gz shifted by -24 hours after repeated cross-source agreement.
- **MBC TV** (MBCTV.in@SD): source ID MBCTV.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Mazhavil Manorama** (MazhavilManorama.in@SD): source ID ts31 from https://avkb.short.gy/tsepg.xml.gz shifted by -24 hours after repeated cross-source agreement.
- **Muzsika TV** (MuzsikaTV.hu@SD): source ID MuzsikaTV.ro from https://iptv-epg.org/files/epg-ro.xml.gz shifted by -24 hours after repeated cross-source agreement.
- **Pitaara** (Pitaara.in): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Pitaara TV** (Pitaara.in@SD): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Shubh TV** (ShubhTV.in@SD): source ID ShubhTV.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Siri Kannada** (SiriKannada.in@SD): source ID SiriKannada.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Stingray Classica** (StingrayClassica.ca@SD): source ID StingrayClassica.ca from https://iptv-epg.org/files/epg-ca.xml.gz shifted by -6 hours after repeated cross-source agreement.
- **Stingray Classica** (StingrayClassica.ca@SD): source ID StingrayClassica.ro from https://iptv-epg.org/files/epg-ro.xml.gz shifted by -25 hours after repeated cross-source agreement.
- **Stingray DJAZZ** (StingrayDJAZZ.ca@SD): source ID StingrayDjazz.ro from https://iptv-epg.org/files/epg-ro.xml.gz shifted by -23 hours after repeated cross-source agreement.
- **HBO** (custom.hbo): source ID HBO.ro from https://iptv-epg.org/files/epg-ro.xml.gz shifted by -24 hours after repeated cross-source agreement.
- **History** (custom.history): source ID History.ro from https://iptv-epg.org/files/epg-ro.xml.gz shifted by -24 hours after repeated cross-source agreement.

## Feed-wide offset patterns

- **https://www.open-epg.com/files/india.xml.gz**: 18 channels were corrected by the same -5.5 hours. This looks like a feed-wide timezone problem; other channels from this feed without cross-source overlap may still be shifted and should be reviewed.
- **https://iptv-epg.org/files/epg-ro.xml.gz**: 8 channels were corrected by the same -24 hours. This looks like a feed-wide timezone problem; other channels from this feed without cross-source overlap may still be shifted and should be reviewed.

Detected source-ID corrections: **32**
