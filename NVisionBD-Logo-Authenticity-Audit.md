# NVisionBD Playlist Logo Authenticity Audit

Audit date: 2026-10-11  
Playlist: [NVisionBD-Playlist.m3u](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/NVisionBD-Playlist.m3u)

## Acceptance rule

A logo is approved only when the **image itself** is matched to an official broadcaster/brand asset or an attributable, reliable source identifying that exact logo. A channel name, filename, search result, or a page merely proving that a channel exists is not sufficient. All playlist logos must remain local in `/logos`. Unverified entries stay in the playlist with their stream URLs intact but without a logo.

## Current integrity snapshot

- Playlist entries: **561**
- Entries with a logo reference: **519**
- Entries with no logo pending verification: **42**
- Distinct local logo asset paths referenced: **397**
- Missing local logo references among entries that have a logo: **0** (last integrity check)
- External-hosted logo URLs: **0** (the playlist references GitHub-hosted local repository assets)

**Important:** the 519 existing logo references are not automatically authenticated by the integrity checks. Their asset provenance still needs to be verified one by one. This report does not certify the whole logo collection.

## Corrective action already applied

Removed 42 references to unverified bespoke/custom artwork and deleted the corresponding unverified artwork files. Preserved all 561 channel entries and their stream URLs. The 42 entries below remain without `tvg-logo` until an exact authentic image can be obtained and localized.

## Source-by-source results for the 42 unresolved entries

Status meanings:
- **Official source located; asset not yet installed** — a primary source identifies the exact channel/brand or provides a logo, but the exact image has not been added to `/logos` and checked against the intended playlist entry.
- **Existence only / third-party listing** — source helps identify the service but does not prove the image is an official broadcaster logo.
- **No adequate exact match verified** — no qualifying source was established in this pass. Keep the logo omitted.

| Playlist entry | Source checked / result | Decision |
|---|---|---|
| Cafe Film | No adequate exact broadcaster-logo match verified | Keep omitted |
| Sine Plus | No adequate exact broadcaster-logo match verified | Keep omitted |
| 10 TV | Ambiguous channel name; no exact broadcaster-logo match verified | Keep omitted |
| Global Panjab | No adequate exact broadcaster-logo match verified | Keep omitted |
| Asia Flix TV | No adequate exact broadcaster-logo match verified | Keep omitted |
| Aurora Media Flims | Name may be misspelled; no exact match verified | Keep omitted |
| Blockbaster HD | Name may be misspelled; no exact match verified | Keep omitted |
| Digital Fashion | No exact broadcaster-logo match verified | Keep omitted |
| Fashion 1 | Ambiguous name; no exact broadcaster-logo match verified | Keep omitted |
| Power Turk | Official brand asset not yet matched to a local image | Keep omitted |
| Star Cinema | Ambiguous name; no exact channel-logo match verified | Keep omitted |
| Whiples Cinema | No adequate exact broadcaster-logo match verified | Keep omitted |
| Xrema Accion | No adequate exact broadcaster-logo match verified | Keep omitted |
| Adventure 4k | Ambiguous name; no exact broadcaster-logo match verified | Keep omitted |
| Banijoy Mr Been | Likely intended to reference a Mr Bean-branded feed, but exact channel identity/logo is not established. Banijay's [official announcement](https://www.banijay.com/blog/2024/06/21/mr-bean-expands-into-fast/) confirms a Mr Bean FAST channel, not this playlist feed's exact logo. | Keep omitted |
| Cartoon Channel | Generic name; no exact broadcaster-logo match verified | Keep omitted |
| Disney Channel Big City Greens | Disney's [official press page](https://www.detpress.com/disneykidsandfamily/shows/big-city-greens/) provides show-brand material, not proof that this playlist entry is an official Disney Channel feed or that an existing local file matches it. | Keep omitted |
| Alistiqamah | No adequate exact broadcaster-logo match verified | Keep omitted |
| Espn5 HD | No exact ESPN5 broadcaster-provided image installed/verified. A search result alone is insufficient. | Keep omitted |
| Fight 24/7 | No adequate exact broadcaster-logo match verified | Keep omitted |
| Flo Racing | FloRacing's [official site](https://www.floracing.com/events/6741741-floracing-247/videos?playing=10734977) identifies FloRacing 24/7 and labels an image `floracing247logo.png`; local image bytes have not yet been matched against that official asset. | Keep omitted until exact asset match |
| Htv Sport | The official [HT Spor imprint](https://tv.htspor.com/kunye) confirms HT SPOR as a broadcaster; exact match to this playlist's “Htv Sport” feed and a local logo file remains unverified. | Keep omitted |
| Kiev Sport HD | No adequate exact broadcaster-logo match verified | Keep omitted |
| Sport 1 HD | The broadcaster's [Poverkhnost TV logo page](https://www.poverkhnost.tv/pages/index.php?c=5&s=85) publishes a “Sport 1” logo. Exact local image is not present/matched yet. | Keep omitted until localized official asset is verified |
| Sport 2 HD | The broadcaster's [Poverkhnost TV logo page](https://www.poverkhnost.tv/pages/index.php?c=5&s=85) publishes a “Sport 2” logo. Exact local image is not present/matched yet. | Keep omitted until localized official asset is verified |
| Tapmad (3 entries) | Tapmad's [official website](https://www.tapmad.com/) verifies the service/brand, but the playlist entries' feed identity and a local image match are not established. | Keep all three omitted |
| 88 Stereo [not 24/7] | No adequate exact broadcaster-logo match verified | Keep omitted |
| Bangla Hits | Third-party radio directory listings are not enough to prove an official station logo | Keep omitted |
| Doyel Radio | No adequate exact station-logo match verified | Keep omitted |
| Dream Music Prime | No adequate exact broadcaster-logo match verified | Keep omitted |
| Magical Blade FM | No adequate exact station-logo match verified | Keep omitted |
| Moner Radio | No adequate exact station-logo match verified | Keep omitted |
| Radio Bangla Rock | No adequate exact station-logo match verified | Keep omitted |
| Radio Barakah | No adequate exact station-logo match verified | Keep omitted |
| Radio Janata | [Zeno.FM listing](https://zeno.fm/radio/radio-janata/) confirms a station listing and displays an image, but does not establish that the image was supplied by the station itself. | Keep omitted |
| Radio Ritmo On Line | No adequate exact station-logo match verified | Keep omitted |
| Radio Zenith FM | No adequate exact station-logo match verified | Keep omitted |
| Sagor FM | [Zeno.FM listing](https://zeno.fm/radio/sagor-fm/) confirms a station listing, but does not establish broadcaster ownership of the displayed image. | Keep omitted |
| Wc Music | Ambiguous name; no exact broadcaster-logo match verified | Keep omitted |
| Wifm 100.9 | Ambiguous station identity; no exact official-logo match verified | Keep omitted |

## Remaining source-by-source work

The playlist currently references **397 distinct local logo files across 519 entries**. Each distinct file needs an evidence record containing: channel/brand, local path, exact official source URL, confirmation that the image matches the source asset, and disposition (approved/replaced/removed). Until that check is complete, these files must be treated as **not yet certified**, even if their filenames look correct.

No substitute artwork should be drawn or generated to fill gaps. When a primary-source image cannot be retrieved and verified, keep the entry logo-less rather than using a lookalike.
