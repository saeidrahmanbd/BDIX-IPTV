# Generic Channel Logo Audit — Three Playlists

Audit date: 2026-10-11  
Repository: https://github.com/saeidrahmanbd/BDIX-IPTV  
Method: parsed each playlist's `tvg-logo` values and cross-checked the logo assets whose SVG artwork contains the generic `CHANNEL MARK` placeholder design.

## Summary

| Playlist | Entries | Matches to identified generic placeholder assets |
|---|---:|---:|
| `IPTV-Playlist.m3u` | 1,186 | 0 |
| `BDIX-Playlist.m3u` | 217 | 0 |
| `NVisionBD-Playlist.m3u` | 561 | 99 |

The 99 affected NVisionBD entries use 97 distinct generic SVG files. This is a targeted placeholder audit, not proof that all other artwork is authentic. Other logos still need source/identity verification.

## Findings

The identified placeholders use the same templated design: dark gradient card, initials badge, channel name, and the text `CHANNEL MARK`. They must not be treated as official channel logos.

Affected channel labels (alphabetical):

- &tv HD
- &xplorer HD
- 10 TV
- Action 24
- Adt FM
- Adventure 4k
- Aflam
- Afra Film
- Afro Music Channel
- Afrobeats
- Alistiqamah
- Amar Ujala
- Anger Management Channel
- Ary News
- BTV Sangsad
- Balapan
- Bangla Hits
- Baraza TV
- Bd Radio FM
- Be.joy Kids
- Biz Cinema
- Blockbaster HD
- Boomerang
- Bt Sports 2
- Cafe Film
- Cartoon Channel
- Cooking TV
- Cowboy Movie Channel
- Cricbuzz
- Disney Channel Big City Greens
- Doyel Radio
- Ducktv
- ETV
- Epic
- Espn5 HD
- FX TV
- Fail Army
- Fashion 1
- Fashion TV HD
- Fifa+
- Fight 24/7
- Flo Racing
- Fubo Sports
- Golf Channel
- Hit
- Htv Sport
- India Today
- Kiev Sport HD
- Kronehit
- Lacrosse TV
- Laff TV
- Laliga Live 1
- Laliga Live 2
- Laligatv
- M4 Sport
- Madina Live
- Magic TV
- Max Sport 1
- Max Sport 2
- Max Sport 3
- Max Sport 4
- Moner Radio
- Nbc Sports
- Oman Sports
- Palki FM
- Power Turk
- Rick Astley
- Rtsh Sport
- Sagor FM
- Screamin
- Sine Plus
- Sony Cine
- Sport 1 HD
- Sport 2 HD
- Sports Grid
- Sportv
- Star Cinema
- TNT Sport 1
- Talk Sport
- Tapmad
- Tennis Channel
- The Q
- The Q India
- Tsn Aq1
- Utbd FM
- Wc Music
- Wifm 100.9
- Wild Earth
- Wild Life
- Willow TV
- Wow Kids
- Zee Cafe HD
- Zee Cinema HD
- Zee TV HD
- Ziggo Sport Live
- Zing
- Zoom Music

## Remediation status

- [x] Parsed all three playlist files.
- [x] Identified 97 unique SVG files matching the generic design.
- [x] Listed affected channel labels.
- [ ] Find and verify original broadcaster/provider logo sources.
- [ ] Download the original artwork into `/logos`.
- [ ] Update playlist `tvg-logo` references and validate that all local paths exist.
- [ ] Keep unresolved channels explicitly listed for manual review rather than inventing artwork.

## Source and quality rules

1. Prefer official broadcaster websites, official CDN assets, or a well-maintained logo repository with identifiable source files.
2. Validate that the downloaded artwork matches the channel—not merely a similar channel name.
3. Store the downloaded image in this repository's `logos/` directory and use its raw GitHub URL in playlists.
4. Preserve stream URLs and channel metadata during logo-only changes.
5. If no trustworthy original is found, do not fabricate an “official” logo; retain the current file temporarily and mark it unresolved.
