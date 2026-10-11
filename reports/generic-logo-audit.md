# Generic Channel Logo Audit — Three Playlists

Audit date: 2026-10-11 11:35 UTC  
Repository: https://github.com/saeidrahmanbd/BDIX-IPTV  
Method: scans current playlist metadata and checks referenced local SVG files for the generic CHANNEL MARK template.

## Summary

| Playlist | Entries | Unique generic placeholder assets |
|---|---:|---:|
| IPTV-Playlist.m3u | 1145 | 0 |
| BDIX-Playlist.m3u | 217 | 0 |
| NVisionBD-Playlist.m3u | 561 | 139 |

Current NVisionBD placeholder assets: **139 unique files**.

## Remaining affected NVisionBD channel labels

- &xplorer HD
- 10 TV
- 24/7 Batul The Great
- 51 Radio TV [geo-blocked]
- 88 Stereo [not 24/7]
- 92.8 FM Radio Bhumi
- Abc Music Radio
- Adt FM
- Adventure 4k
- Afra Film
- Afrobeats
- Alistiqamah
- Amar Ujala
- Asean Cup 2026
- Asia Flix TV
- Aurora Media Flims
- BTV Sangsad
- Bangla Big Boss 24x7
- Bangla Hits
- Bangla Radio
- Banijoy Mr Been
- Bd Radio FM
- Be.joy Kids
- Blockbaster HD
- Boomerang
- Boomerang UK
- Bt Sports 2
- Cafe Film
- Cartoon Channel
- Comedy Central
- Cooking TV
- Cosmote Sports 1
- Cosmote Sports 4
- Cowboy Movie Channel
- Cricbuzz
- Dhaka FM 90.4
- Digi Sport 1
- Digi Sport 2
- Disney Channel Big City Greens
- Doyel Radio
- Dream Music Prime
- ETV
- English Premier League 2
- Epic
- Espn5 HD
- FX TV
- Fail Army
- Fashion 1
- Fashion TV HD
- Fight 24/7
- Filmua Drama
- Flo Racing
- Fuel TV Apac
- Fuel TV Europe
- Global Panjab
- Golf Channel
- Hindi Big Boss 24x7 2026
- Htv Sport
- Ind Unite8 Sports 1 HD
- Kiev Sport HD
- Ktv Sports Plus
- Laff TV
- Laliga Live 1
- Laliga Live 2
- Laligatv
- Love Gold Bangla
- Madani TV Bangla
- Madina Live
- Magenta Sports 2
- Magical Blade FM
- Moner Radio
- Movie Sphere
- Movie Sphere Au
- My 90s Bengali Online
- My Time Movie
- Nat Geo Bangla
- News 18 Assam
- Nexus Television
- Niki Jr Kids
- Oman Sports
- Palki FM
- Peoples Radio
- Persiana Travel
- Pk Geo Super
- Pk Ten Cricket
- Power Turk
- Premier Sports 1
- Radio Adamya
- Radio Bangla Rock
- Radio Bangladesh Co
- Radio Barakah
- Radio Bhumi 92.80 FM
- Radio Bushra
- Radio Capital FM 94.8
- Radio Din Raat 93.6 FM
- Radio Gaan Baksho
- Radio Janata
- Radio Mahananda - 98.8
- Radio Padma – 99.2 FM
- Radio Ritmo On Line
- Radio Shadhin - 92.4 FM
- Radio Shadin
- Radio Sonali Dingulo
- Radio Tangail
- Radio Vivid Voice | Mymensingh
- Radio Zenith FM
- Rick Astley
- Sagor FM
- Setanta Sport
- Sine Plus
- Sky Sports Laliga
- Sony Cine
- Spondon Radio
- Sport 1 HD
- Sports Digital Fsbl
- Sports Fishing TV
- Sports Grid
- Star Cinema
- TNT Sport 1
- Tapmad
- Tsn Aq1
- UK TNT Sports 1 HD
- UK TNT Sports 2 HD
- UK TNT Sports 3 HD
- UK TNT Sports 4 HD
- US Sky Sports Main Event
- US Sky Sports Premier League
- US Willow By Cricbuzz
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
- Ziggo Sport Live

## Scope and quality rules

- Only NVisionBD-Playlist.m3u is modified by the replacement workflow.
- A replacement must be a validated image, must not contain the CHANNEL MARK template, and must have a source recorded in the replacement-results report.
- If multiple channels share a name, or no trustworthy source is found, the placeholder is retained and listed for manual review.
- Old generic files are not deleted automatically, to avoid breaking any other reference.
