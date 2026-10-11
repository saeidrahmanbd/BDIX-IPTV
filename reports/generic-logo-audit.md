# Generic Channel Logo Audit — Three Playlists

Audit date: 2026-10-11 12:17 UTC  
Repository: https://github.com/saeidrahmanbd/BDIX-IPTV  
Method: scans current playlist metadata and checks referenced local SVG files for the generic CHANNEL MARK template.

## Summary

| Playlist | Entries | Unique generic placeholder assets |
|---|---:|---:|
| IPTV-Playlist.m3u | 1145 | 0 |
| BDIX-Playlist.m3u | 217 | 0 |
| NVisionBD-Playlist.m3u | 561 | 41 |

Current NVisionBD placeholder assets: **41 unique files**.

## Remaining affected NVisionBD channel labels

- 10 TV
- 88 Stereo [not 24/7]
- Abc Music Radio
- Adventure 4k
- Alistiqamah
- Asia Flix TV
- Aurora Media Flims
- Bangla Hits
- Banijoy Mr Been
- Blockbaster HD
- Cafe Film
- Cartoon Channel
- Digital Fashion
- Disney Channel Big City Greens
- Doyel Radio
- Dream Music Prime
- Espn5 HD
- Fashion 1
- Fight 24/7
- Flo Racing
- Global Panjab
- Htv Sport
- Kiev Sport HD
- Magical Blade FM
- Moner Radio
- Power Turk
- Radio Bangla Rock
- Radio Barakah
- Radio Janata
- Radio Ritmo On Line
- Radio Zenith FM
- Sagor FM
- Sine Plus
- Sport 1 HD
- Sport 2 HD
- Star Cinema
- Tapmad
- Wc Music
- Whiples Cinema
- Wifm 100.9
- Xrema Accion

## Scope and quality rules

- Only NVisionBD-Playlist.m3u is modified by the replacement workflow.
- A replacement must be a validated image, must not contain the CHANNEL MARK template, and must have a source recorded in the replacement-results report.
- If multiple channels share a name, or no trustworthy source is found, the placeholder is retained and listed for manual review.
- Old generic files are not deleted automatically, to avoid breaking any other reference.
