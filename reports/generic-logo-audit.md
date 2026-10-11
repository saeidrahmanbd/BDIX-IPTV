# Generic Channel Logo Audit — Three Playlists

Audit date: 2026-10-11 11:54 UTC  
Repository: https://github.com/saeidrahmanbd/BDIX-IPTV  
Method: scans current playlist metadata and checks referenced local SVG files for the generic CHANNEL MARK template.

## Summary

| Playlist | Entries | Unique generic placeholder assets |
|---|---:|---:|
| IPTV-Playlist.m3u | 1145 | 0 |
| BDIX-Playlist.m3u | 217 | 0 |
| NVisionBD-Playlist.m3u | 561 | 92 |

Current NVisionBD placeholder assets: **92 unique files**.

## Remaining affected NVisionBD channel labels

- &xplorer HD
- 10 TV
- 51 Radio TV [geo-blocked]
- 88 Stereo [not 24/7]
- Abc Music Radio
- Adt FM
- Adventure 4k
- Afra Film
- Alistiqamah
- Amar Ujala
- Asean Cup 2026
- Asia Flix TV
- Aurora Media Flims
- Bangla Big Boss 24x7
- Bangla Hits
- Banijoy Mr Been
- Bd Radio FM
- Be.joy Kids
- Blockbaster HD
- Cafe Film
- Cartoon Channel
- Cooking TV
- Cricbuzz
- Dhaka FM 90.4
- Digital Fashion
- Disney Channel Big City Greens
- Doyel Radio
- Dream Music Prime
- ETV
- English Premier League 2
- Espn5 HD
- Fail Army
- Fashion 1
- Fight 24/7
- Filmua Drama
- Flo Racing
- Fuel TV Apac
- Fuel TV Europe
- Global Panjab
- Hindi Big Boss 24x7 2026
- Htv Sport
- Ind Unite8 Sports 1 HD
- Kiev Sport HD
- Laliga Live 1
- Laliga Live 2
- Love Gold Bangla
- Madani TV Bangla
- Madina Live
- Magical Blade FM
- Moner Radio
- Nat Geo Bangla
- News 18 Assam
- Nexus Television
- Niki Jr Kids
- Oman Sports
- Palki FM
- Persiana Travel
- Pk Geo Super
- Pk Ten Cricket
- Power Turk
- Radio Adamya
- Radio Bangla Rock
- Radio Bangladesh Co
- Radio Barakah
- Radio Gaan Baksho
- Radio Janata
- Radio Ritmo On Line
- Radio Sonali Dingulo
- Radio Vivid Voice | Mymensingh
- Radio Zenith FM
- Rick Astley
- Sagor FM
- Setanta Sport
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
- Uttorbango Betar
- Valobasar Rupali Sur
- Wc Music
- Whiples Cinema
- Wifm 100.9
- Wild Life
- Wow Kids
- Xrema Accion
- Xtrem Sports

## Scope and quality rules

- Only NVisionBD-Playlist.m3u is modified by the replacement workflow.
- A replacement must be a validated image, must not contain the CHANNEL MARK template, and must have a source recorded in the replacement-results report.
- If multiple channels share a name, or no trustworthy source is found, the placeholder is retained and listed for manual review.
- Old generic files are not deleted automatically, to avoid breaking any other reference.
