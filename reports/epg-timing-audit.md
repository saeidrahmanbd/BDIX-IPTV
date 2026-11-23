# EPG Timing Audit

Automatic corrections require four repeated title/duration matches, >=75% agreement, and corroboration from at least three distinct provider hosts. Separate country files or channel IDs on one host count as one vote; a host with conflicting times is excluded for that signature. Only plausible timezone displacements from 2 through 14 hours are applied; larger shifts are reported for manual review and left unchanged.

## Detected corrections

- **All Time Movies** (AllTimeMovies.in@SD): source ID AllTimeMovies.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **&xplor HD** (AndxplorHD.in@HD): source ID LIVETV_LIVETVCHANNEL_SYMANDXPLOR_HD from https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **DD Bihar** (DDBihar.in@SD): source ID DD.BIHAR.in has a proposed -24-hour displacement from 4/5 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **DD Kashir** (DDKashir.in@SD): source ID DDKashir.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Malayalam** (DDMalayalam.in@SD): source ID DDMalayalam.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Punjabi** (DDPunjabi.in@SD): source ID DDPunjabi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Rajasthan** (DDRajasthan.in@SD): source ID DDRajasthan.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **DD Rajasthan** (DDRajasthan.in@SD): source ID DD.RAJASTHAN.in has a proposed -24-hour displacement from 4/4 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **DD Saptagiri** (DDSaptagiri.in@SD): source ID DDSaptagiri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **DD Tamil** (DDTamil.in@HD): source ID DD.TAMIL.in has a proposed -24-hour displacement from 8/8 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.

### Large source-offset proposals — manual review only

- **DD Tamil** (DDTamil.in@SD): source ID DD.TAMIL.in has a proposed -24-hour displacement from 8/8 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **DD Yadagiri** (DDYadagiri.in@SD): source ID DDYadagiri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Fakt Marathi** (FaktMarathi.in@SD): source ID FaktMarathi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **Kalaignar TV** (KalaignarTV.in@SD): source ID KALAIGNAR.in has a proposed -24-hour displacement from 4/4 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **MNX** (MNX.in@SD): source ID MNX.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **Nepal 1** (Nepal1.in@SD): source ID NEPAL.1.in has a proposed -24-hour displacement from 5/5 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **Pitaara** (Pitaara.in): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Pitaara** (Pitaara.in@SD): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Shemaroo TV** (ShemarooTV.in@SD): source ID ShemarooTV.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Sony Pix HD** (SonyPix.in@HD): source ID SONYPIX.in from https://www.open-epg.com/files/india.xml.gz shifted by -8 hours after repeated cross-source agreement.
- **Star Gold Select HD** (StarGoldSelect.in@HD): source ID StarGoldSelect.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Star Movies (India) HD** (StarMovies.in@HD): source ID StarMovies.in from https://www.open-epg.com/files/india.xml.gz shifted by -8 hours after repeated cross-source agreement.
- **Star Movies Select HD** (StarMoviesSelect.in@HD): source ID StarMoviesSelect.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **Vissa TV** (VissaTV.in@SD): source ID VISSA.TV.in has a proposed -24-hour displacement from 4/4 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.
- **Zee Classic** (ZeeClassic.in@SD): source ID ZeeClassic.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

## Feed-wide offset patterns

- **https://www.open-epg.com/files/india.xml.gz**: 15 channels were corrected by the same -5.5 hours. This looks like a feed-wide timezone problem; other channels from this feed without cross-source overlap may still be shifted and should be reviewed.

Detected source-ID corrections: **18**
