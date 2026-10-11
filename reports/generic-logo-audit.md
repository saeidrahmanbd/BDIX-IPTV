# Channel Logo Audit — Three Playlists

Audit date: 2026-10-11  
Repository: https://github.com/saeidrahmanbd/BDIX-IPTV

## Current playlist integrity

| Playlist | Entries | Entries with logo | Entries without logo | Known generic filename refs | External logo refs | Missing local asset paths |
|---|---:|---:|---:|---:|---:|---:|
| IPTV-Playlist.m3u | 1,145 | 1,122 | 23 | 0 | 0 | 0 |
| BDIX-Playlist.m3u | 190 | 184 | 6 | 0 | 5 | 0 |
| NVisionBD-Playlist.m3u | 561 | 326 | 235 | 0 | 0 | 0 |
| **Total** | **1,896** | **1,632** | **264** | **0** | **5** | **0** |

“Known generic filename refs” only covers the specific previously identified `channel-1/9/16/24/52.png` and `nvisionbd-*` patterns. It does **not** mean every remaining image is authentic.

## Image-by-image findings in this pass

1. `logos/btv-news.png` visibly combines BTV News branding with an unrelated **“M3U World 4K”** overlay.
2. `logos/bangla-tv.png` visibly adds a **“BONGO FLIX”** watermark over the Bangla TV logo.
3. `logos/tom-and-jerry.png` is artwork for the *Tom & Jerry Tales* show, not a channel-specific broadcaster logo.

Removed references to these three suspect assets across the playlists (14 `tvg-logo` references total). The affected channel entries and stream URLs were preserved. The image files were retained for traceability, and no replacement was guessed. Those entries now remain without logos until exact, clean assets are verified.

## Earlier corrective actions retained

- Removed references to generic-looking `channel-N.png` assets from all three playlists without deleting channel entries.
- Kept missing logo references blank rather than substituting artwork from similarly named channels.
- All referenced local logo paths resolve to files in the repository. The five external logo references in BDIX are still present and need a separate source/rights review.

## Reliable source leads for continued verification

These are candidate source registries, not proof that a particular file in this repository matches the official image:

- [Bangladesh Television official website](https://btv.gov.bd/) — official source for BTV branding and channel identity.
- [Wikimedia Commons: logos of television channels in Bangladesh](https://commons.wikimedia.org/wiki/Category:Logos_of_television_channels_in_Bangladesh) — includes source pages for BTV News, Channel 9, Channel 16, Channel 24, Jamuna TV, ATN Bangla, and others.
- [JioStar media toolkit — official channel logos](https://www.jiostar.com/mediatoolkit/all-logos/) — includes downloadable brand assets such as Star Jalsha, Colors Bangla, and Jalsha Movies.

## Remaining work

The remaining 1,632 referenced logos have **not** all been authenticated image-by-image. Continue by visually checking each distinct file, comparing it with an official broadcaster asset or a reliable attributable source, quarantining watermarked/mismatched images, and only restoring a logo reference after an exact match. Never infer authenticity from a filename alone.

## Integrity safeguards

- No channel entries or stream URLs were deleted in this pass.
- No logo artwork was invented.
- Suspect image files were retained for traceability; only playlist references were removed.
- Counts reflect the latest playlist edits.
