# EPG Timing Audit

Automatic corrections require four repeated title/duration matches, >=75% agreement, and corroboration from at least three distinct provider hosts. Separate country files or channel IDs on one host count as one vote; a host with conflicting times is excluded for that signature. Only plausible timezone displacements from 2 through 14 hours are applied; larger shifts are reported for manual review and left unchanged.

## Detected corrections

- **Animal Planet** (AnimalPlanet.in@SD): source ID AnimalPlanetHD.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Colors Bangla Cinema** (ColorsBanglaCinema.in@SD): source ID ColorsBanglaCinema.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Colors Bangla Cinema** (ColorsBanglaCinema.in@SD@colors.bangla.cinema): source ID ColorsBanglaCinema.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Girnar** (DDGirnar.in@SD): source ID DDGirnar.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Kashir** (DDKashir.in@SD): source ID DDKashir.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Malayalam** (DDMalayalam.in@SD): source ID DDMalayalam.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **DD Odia** (DDOdia.in@SD): source ID DD.ODIA.in has a proposed -24-hour displacement from 5/5 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **DD Punjabi** (DDPunjabi.in@SD): source ID DDPunjabi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Rajasthan** (DDRajasthan.in@SD): source ID DDRajasthan.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **DD Rajasthan** (DDRajasthan.in@SD): source ID DD.RAJASTHAN.in has a proposed -24-hour displacement from 6/6 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **DD Saptagiri** (DDSaptagiri.in@SD): source ID DDSaptagiri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **DD Tamil** (DDTamil.in@HD): source ID DD.TAMIL.in has a proposed -24-hour displacement from 10/10 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.

### Large source-offset proposals — manual review only

- **DD Tamil** (DDTamil.in@SD): source ID DD.TAMIL.in has a proposed -24-hour displacement from 10/10 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **DD Yadagiri** (DDYadagiri.in@SD): source ID DDYadagiri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Enter10 Bangla** (Enter10Bangla.in): source ID Enterr10Bangla.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Fakt Marathi** (FaktMarathi.in@SD): source ID FaktMarathi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **Isai Aruvi** (IsaiAruvi.in@SD): source ID ISAI.ARUVI.in has a proposed -24-hour displacement from 4/4 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.

### Large source-offset proposals — manual review only

- **Kalaignar TV** (KalaignarTV.in@SD): source ID KALAIGNAR.in has a proposed -24-hour displacement from 4/4 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **Nepal 1** (Nepal1.in@SD): source ID Nepal1.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **Nepal 1** (Nepal1.in@SD): source ID NEPAL.1.in has a proposed -24-hour displacement from 6/6 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **Pitaara** (Pitaara.in): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Pitaara TV** (Pitaara.in@SD): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Pitaara** (Pitaara.in@SD@pitaara): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **Polimer TV** (PolimerTV.in@SD): source ID POLIMER.in has a proposed -24-hour displacement from 5/5 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **Shemaroo TV** (ShemarooTV.in@SD): source ID ShemarooTV.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **Sun TV** (SunTV.in@HD): source ID SUN.TV.in has a proposed -24-hour displacement from 4/4 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.

### Large source-offset proposals — manual review only

- **Vissa TV** (VissaTV.in@SD): source ID VISSA.TV.in has a proposed -24-hour displacement from 5/5 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.

## Feed-wide offset patterns

- **https://www.open-epg.com/files/india.xml.gz**: 17 channels were corrected by the same -5.5 hours. This looks like a feed-wide timezone problem; other channels from this feed without cross-source overlap may still be shifted and should be reviewed.

Detected source-ID corrections: **17**
