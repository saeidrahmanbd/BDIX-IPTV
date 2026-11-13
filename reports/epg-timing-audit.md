# EPG Timing Audit

Automatic corrections require four repeated title/duration matches, >=75% agreement, and corroboration from at least three distinct provider hosts. Separate country files or channel IDs on one host count as one vote; a host with conflicting times is excluded for that signature. Only plausible timezone displacements from 2 through 14 hours are applied; larger shifts are reported for manual review and left unchanged.

## Detected corrections

- **Cine Jomjomat** (CineJomjomat.in@SD): source ID IN2100007QM from https://i.mjh.nz/SamsungTVPlus/in.xml shifted by -5.5 hours after repeated cross-source agreement.
- **DD Girnar** (DDGirnar.in@SD): source ID DDGirnar.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Haryana** (DDHaryana.in@SD): source ID DDHaryana.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Kashir** (DDKashir.in@SD): source ID DDKashir.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Malayalam** (DDMalayalam.in@SD): source ID DDMalayalam.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Punjabi** (DDPunjabi.in@SD): source ID DDPunjabi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **DD Rajasthan** (DDRajasthan.in@SD): source ID ts332 has a proposed -24-hour displacement from 6/8 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **DD Sahyadri** (DDSahyadri.in@SD): source ID DDSahyadri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Yadagiri** (DDYadagiri.in@SD): source ID DDYadagiri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Fakt Marathi** (FaktMarathi.in@SD): source ID FaktMarathi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **GTC Punjabi** (GTCPunjabi.in@SD): source ID ts1836 has a proposed -24-hour displacement from 5/5 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.

### Large source-offset proposals — manual review only

- **MH One** (MHOne.in@SD): source ID ts399 has a proposed -24-hour displacement from 7/7 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **Manoranjan TV** (ManoranjanTV.in@SD): source ID ManoranjanTV.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Nepal 1** (Nepal1.in@SD): source ID Nepal1.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **PTC Punjabi** (PTCPunjabi.in@HD): source ID ts122 has a proposed -24-hour displacement from 6/6 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.

### Large source-offset proposals — manual review only

- **PTC Punjabi** (PTCPunjabi.in@SD): source ID ts122 has a proposed -24-hour displacement from 6/6 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.

### Large source-offset proposals — manual review only

- **PTC Punjabi Gold** (PTCPunjabiGold.in@SD): source ID ts794 has a proposed -24-hour displacement from 6/6 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **Pitaara** (Pitaara.in): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Pitaara** (Pitaara.in@SD): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

## Feed-wide offset patterns

- **https://www.open-epg.com/files/india.xml.gz**: 12 channels were corrected by the same -5.5 hours. This looks like a feed-wide timezone problem; other channels from this feed without cross-source overlap may still be shifted and should be reviewed.

Detected source-ID corrections: **13**
