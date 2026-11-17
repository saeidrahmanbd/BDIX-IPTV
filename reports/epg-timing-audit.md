# EPG Timing Audit

Automatic corrections require four repeated title/duration matches, >=75% agreement, and corroboration from at least three distinct provider hosts. Separate country files or channel IDs on one host count as one vote; a host with conflicting times is excluded for that signature. Only plausible timezone displacements from 2 through 14 hours are applied; larger shifts are reported for manual review and left unchanged.

## Detected corrections

- **DD Bangla** (DDBangla.in@SD): source ID DDBangla.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Bihar** (DDBihar.in@SD): source ID DDBihar.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Girnar** (DDGirnar.in@SD): source ID DDGirnar.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Kashir** (DDKashir.in@SD): source ID DDKashir.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Punjabi** (DDPunjabi.in@SD): source ID DDPunjabi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **DD Sahyadri** (DDSahyadri.in@SD): source ID DDSahyadri.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Fakt Marathi** (FaktMarathi.in@SD): source ID FaktMarathi.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Nepal 1** (Nepal1.in@SD): source ID Nepal1.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Pitaara** (Pitaara.in): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.
- **Pitaara** (Pitaara.in@SD): source ID Pitaara.in from https://www.open-epg.com/files/india.xml.gz shifted by -5.5 hours after repeated cross-source agreement.

## Feed-wide offset patterns

- **https://www.open-epg.com/files/india.xml.gz**: 10 channels were corrected by the same -5.5 hours. This looks like a feed-wide timezone problem; other channels from this feed without cross-source overlap may still be shifted and should be reviewed.

Detected source-ID corrections: **10**
