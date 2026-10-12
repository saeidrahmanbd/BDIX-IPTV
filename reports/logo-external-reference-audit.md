# Logo Authenticity Audit — 2026-10-12

## Scope and method

This review compares playlist identity (display name and `tvg-id`) with the referenced asset path and available broadcaster/source evidence. A local filename or successful HTTP response is not, by itself, proof that an image is the exact broadcaster logo. No channel streams or playlist entries were changed during this investigation.

## Five non-repository logo URLs in `BDIX-Playlist.m3u`

All five external references point to `assets-prod.services.toffeelive.com` and use a `/posters/` path. They appear to be Toffee CDN poster/artwork assets, not a broadcaster press/logo library. The CDN is a plausible source for the image, but the exact image content could not be inspected from the available fetch response, so authenticity and suitability as a channel logo remain unverified.

| Playlist channel | tvg-id | External asset | Finding | Action |
|---|---|---|---|---|
| Toffee Movies | `hmair.toffeemovies` | [Open asset](https://assets-prod.services.toffeelive.com/b60Ss5UBrjBfS2_RJPb8/posters/c68ede73-0be0-41b7-9130-9628a16f2feb.png) | Toffee CDN poster path; image content not verified | Keep pending visual/source verification |
| Toffee TV | `hmair.toffeetv` | [Open asset](https://assets-prod.services.toffeelive.com/DNMXs5UBm1RY_In7IJ72/posters/737b5c6e-8435-4cd8-81de-16a499fa6f4e.png) | Toffee CDN poster path; image content not verified | Keep pending visual/source verification |
| Channel News Asia | `hmair.channelnewsasia` | [Open asset](https://assets-prod.services.toffeelive.com/rYOv_p8BJIOHmUelrnXh/posters/d537453f-7e5b-45f3-9b52-42f6f65950c8.png) | Toffee CDN poster path; not yet matched to CNA's official wordmark | Find official CNA logo and compare before replacing |
| Russia Today | `hmair.russiatoday` | [Open asset](https://assets-prod.services.toffeelive.com/CNT2_p8BalKyvLQIBSUG/posters/1e937055-a014-4274-bb69-b1b56d18c434.png) | Toffee CDN poster path; current channel branding should be checked against RT's official identity | Find official RT logo and compare before replacing |
| BFL | Live 1 | `hmair.bfllive1` | [Open asset](https://assets-prod.services.toffeelive.com/HHnAgJkBcqxnFHJBabwO/posters/967dd1fe-c2af-442e-a0b1-22320ed82c88.png) | Toffee CDN poster path; channel/asset identity not independently verified | Keep pending visual/source verification |

## Findings from source lookup

- Sony Pictures Networks India publishes an official logos page that includes Sony Sports Ten 2 HD. This is a useful primary source for any Sony Sports logo in the repository: https://www.sonypicturesnetworks.com/logos
- NDTV announced a refreshed identity in August 2026, so older NDTV 24x7 artwork may now be outdated. Prefer the current logo from NDTV's own communications: https://www.ndtv.com/communication/ndtv-24x7-becomes-ndtv-unveils-new-identity-anchored-in-when-it-really-matters-11914675
- The current five external URLs are not direct links to those broadcasters' official logo libraries; they are Toffee-hosted poster assets. They should not be automatically classified as `official_verified`.

## Decision

No blind substitution was made. Keep the five references unchanged until the actual image pixels can be inspected and compared against official assets. After confirmation, download the exact matching logo to `logos/`, update only the affected `tvg-logo` value, and record the source URL and status in `reports/logo-source-registry.json`. If an image is artwork/poster rather than a logo, replace it with the official channel logo or a clearly labeled generated fallback.

## Broader logo-file audit status

The repository currently has a large retained `logos/unused/` archive. Files there are candidate source assets, not automatically verified logos. A reliable exact-match audit must compare each in-use image against the broadcaster's own logo or a trustworthy attributable source; filenames alone are insufficient. The provenance manifest and source registry are intended to keep verified assets distinct from generated fallback art and unreviewed files.
