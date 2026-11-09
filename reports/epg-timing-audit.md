# EPG Timing Audit

Automatic corrections require four repeated title/duration matches, >=75% agreement, and corroboration from at least three distinct provider hosts. Separate country files or channel IDs on one host count as one vote; a host with conflicting times is excluded for that signature. Only plausible timezone displacements from 2 through 14 hours are applied; larger shifts are reported for manual review and left unchanged.

## Detected corrections

- **Alankar TV** (AlankarTV.in@SD): source ID Alankar.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Bihar** (DDBihar.in@SD): source ID DDBihar.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Goa** (DDGoa.in@SD): source ID DDGOA.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Kashir** (DDKashir.in@SD): source ID DDKashir.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Malayalam** (DDMalayalam.in@SD): source ID DDMalayalam.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Meghalaya** (DDMeghalaya.in@SD): source ID DDMEGHALAYA.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Mizoram** (DDMizoram.in): source ID DDMIZORAM.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Nagaland** (DDNagaland.in@SD): source ID DDNAGALAND.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Punjabi** (DDPunjabi.in@SD): source ID DDPunjabi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Saptagiri** (DDSaptagiri.in@SD): source ID DDSaptagiri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Tamil** (DDTamil.in@HD): source ID DDTAMIL.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Tamil** (DDTamil.in@SD): source ID DDTAMIL.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Yadagiri** (DDYadagiri.in@SD): source ID DDYadagiri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Fakt Marathi** (FaktMarathi.in@SD): source ID FaktMarathi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Pitaara** (Pitaara.in): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Pitaara TV** (Pitaara.in@SD): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Rang** (Rang.in@SD): source ID Rang.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Shemaroo Marathi Bana** (ShemarooMarathiBana.in@SD): source ID ShemarooMarathibana.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Siri Kannada** (SiriKannada.in@SD): source ID SiriKannada.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Star Movies Select** (StarMoviesSelect.in@HD): source ID StarMoviesSelect.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Tarang TV** (TarangTV.in@SD): source ID Tarang.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

## Feed-wide offset patterns

- **https://www.open-epg.com/files/india.xml.gz**: 21 channels were corrected by the same -5.5 hours. This looks like a feed-wide timezone problem; other channels from this feed without cross-source overlap may still be shifted and should be reviewed.

Detected source-ID corrections: **21**
