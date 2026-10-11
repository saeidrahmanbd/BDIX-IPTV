# Generic Channel Logo Audit — Three Playlists

Audit date: 2026-10-11  
Repository: https://github.com/saeidrahmanbd/BDIX-IPTV

## Current playlist integrity

| Playlist | Entries | Entries with logo | Entries without logo | Known generic-looking logo refs remaining | External-hosted logo refs | Missing local asset paths |
|---|---:|---:|---:|---:|---:|---:|
| IPTV-Playlist.m3u | 1,145 | 1,130 | 15 | 0 | 0 | 0 |
| BDIX-Playlist.m3u | 190 | 186 | 4 | 0 | 5 | 0 |
| NVisionBD-Playlist.m3u | 561 | 330 | 231 | 0 | 0 | 0 |

"Known generic-looking" means the specific generic-looking filenames previously identified (`channel-1.png`, `channel-9.png`, `channel-16.png`, `channel-24.png`, `channel-52.png`, and `nvisionbd-*`) are no longer referenced by these three playlists. It does **not** mean every remaining image has been authenticated.

## Corrective actions applied

- Unlinked 15 logo references across the primary and backup entries in `IPTV-Playlist.m3u` that pointed to the five generic-looking `channel-N.png` assets. All **1,145 entries and stream lines were preserved**.
- Unlinked three generic-looking logo references from `BDIX-Playlist.m3u` for Channel 1, Channel 9 and Channel 24. The mismatched logo for `EPL channel 1` had already been removed. All **190 entries and stream lines were preserved**.
- In `NVisionBD-Playlist.m3u`, removed generic-looking references for Channel 1 HD, Channel 9 HD and Channel 24 HD, preserved all 561 entries, and restored 17 references to pre-existing repository assets based on channel-name/filename alignment.
- Missing logo references are intentionally left blank until an exact channel-specific image can be verified. No invented logos were created and no channel entries were deleted.

## Remaining issues

- `IPTV-Playlist.m3u`: 15 entries now have no logo reference pending authentication of the five channel-number assets.
- `BDIX-Playlist.m3u`: four entries have no logo reference (Channel 1, Channel 9, Channel 24 and EPL channel 1). Five other logo URLs are served from Toffee's CDN; they were not copied into the repository because source terms and reuse rights need review.
- `NVisionBD-Playlist.m3u`: 231 entries have no logo reference pending source-by-source verification.
- The repository's previous replacement workflow only detected SVGs containing the `CHANNEL MARK` template. That detection alone is not sufficient to catch suspicious PNG/JPEG filenames or mismatched channel identities.

## Integrity limits

All remaining local logo references checked in this pass point to existing files. This is a path-integrity check, **not** visual authentication. A logo is approved only after comparing the image itself with an official broadcaster/brand source or another attributable reliable source for that exact channel.

## Next actions

1. Authenticate the remaining logo-less entries against exact broadcaster/brand sources; restore only verified assets.
2. Inspect other referenced logos for visual identity mismatches, watermarks, and unrelated brands.
3. Expand automated checks to flag generic-looking raster filenames and suspicious channel-name/logo combinations without automatically replacing uncertain images.
