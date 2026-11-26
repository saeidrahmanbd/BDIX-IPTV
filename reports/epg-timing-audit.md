# EPG Timing Audit

Automatic corrections require four repeated title/duration matches, >=75% agreement, and corroboration from at least three distinct provider hosts. Separate country files or channel IDs on one host count as one vote; a host with conflicting times is excluded for that signature. Only plausible timezone displacements from 2 through 14 hours are applied; larger shifts are reported for manual review and left unchanged.

## Detected corrections

- **&xplor** (AndxplorHD.in@HD): source ID LIVETV_LIVETVCHANNEL_SYMANDXPLOR_HD from https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml shifted by -5.5 hours after repeated cross-source agreement.

### Large source-offset proposals — manual review only

- **M6 Music** (M6Music.fr@SD): source ID M6Music.fr has a proposed -24-hour displacement from 6/6 independent programme signatures. This exceeds the plausible ±14-hour timezone limit; timestamps were **not changed**.

Detected source-ID corrections: **1**
