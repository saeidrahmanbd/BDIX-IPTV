# Generic Channel Logo Audit — Three Playlists

Audit date: 2026-10-11 12:14 UTC  
Repository: https://github.com/saeidrahmanbd/BDIX-IPTV  
Method: scans current playlist metadata and checks referenced local SVG files for the generic CHANNEL MARK template.

## Summary

| Playlist | Entries | Unique generic placeholder assets |
|---|---:|---:|
| IPTV-Playlist.m3u | 1145 | 0 |
| BDIX-Playlist.m3u | 217 | 0 |
| NVisionBD-Playlist.m3u | 561 | 67 |

Current NVisionBD placeholder assets: **67 unique files**.

## Remaining affected NVisionBD channel labels

- &xplorer HD
- 10 TV
- 88 Stereo [not 24/7]
- Abc Music Radio
- Adt FM
- Adventure 4k
- Alistiqamah
- Asean Cup 2026
- Asia Flix TV
- Aurora Media Flims
- Bangla Big Boss 24x7
- Bangla Hits
- Banijoy Mr Been
- Bd Radio FM
- Blockbaster HD
- Cafe Film
- Cartoon Channel
- Cooking TV
- Digital Fashion
- Disney Channel Big City Greens
- Doyel Radio
- Dream Music Prime
- English Premier League 2
- Espn5 HD
- Fashion 1
- Fight 24/7
- Flo Racing
- Global Panjab
- Hindi Big Boss 24x7 2026
- Htv Sport
- Ind Unite8 Sports 1 HD
- Kiev Sport HD
- Laliga Live 1
- Laliga Live 2
- Magical Blade FM
- Moner Radio
- Nat Geo Bangla
- Niki Jr Kids
- Palki FM
- Pk Ten Cricket
- Power Turk
- Radio Adamya
- Radio Bangla Rock
- Radio Bangladesh Co
- Radio Barakah
- Radio Janata
- Radio Ritmo On Line
- Radio Sonali Dingulo
- Radio Zenith FM
- Rick Astley
- Sagor FM
- Sine Plus
- Sky Sports Laliga
- Sport 1 HD
- Sport 2 HD
- Sports Digital Fsbl
- Sports Fishing TV
- Star Cinema
- TNT Sport 1
- Tapmad
- Utbd FM
- Valobasar Rupali Sur
- Wc Music
- Whiples Cinema
- Wifm 100.9
- Xrema Accion
- Xtrem Sports

## Scope and quality rules

- Only NVisionBD-Playlist.m3u is modified by the replacement workflow.
- A replacement must be a validated image, must not contain the CHANNEL MARK template, and must have a source recorded in the replacement-results report.
- If multiple channels share a name, or no trustworthy source is found, the placeholder is retained and listed for manual review.
- Old generic files are not deleted automatically, to avoid breaking any other reference.
