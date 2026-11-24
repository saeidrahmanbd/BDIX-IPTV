# Local Logo URL Repair Report — 2026-11-24

## Scope
Audited the current `main` branch of `saeidrahmanbd/BDIX-IPTV` using the repository Git tree and the exact playlist blobs.

## Repairs staged
| Playlist | Relative logo paths converted to full repository raw URLs | Missing logo attributes filled from a unique exact tvg-id match |
|---|---:|---:|
| IPTV-Playlist.m3u | 411 | 0 |
| International-Playlist.m3u | 8 | 16 |

All converted references were checked against the repository tree; no referenced logo asset path was absent at audit time. Existing canonical full raw URLs were preserved.

## Remaining limitation
International-Playlist.m3u still has 407 entries without a `tvg-logo` attribute after safe repairs. These were not assigned arbitrary, visually similar, or generic logos. They require exact channel-logo identification and authentic local assets before they can be filled safely.

## Policy
- Use only `https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/...` URLs.
- Do not use external hosts, relative paths, generic placeholders, or guessed channel artwork.
- Preserve channel order, names, stream URLs, group assignments, numbering, and all unrelated metadata.
- Validate every referenced asset path against the repository tree.
