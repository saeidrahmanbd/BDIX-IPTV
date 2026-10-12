# NVisionBD Playlist Logo Authenticity Audit

Audit date: 2026-10-11  
Playlist: [NVisionBD-Playlist.m3u](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/NVisionBD-Playlist.m3u)

## Acceptance rule

A logo is approved only when the **image itself** is matched to an official broadcaster/brand asset or an attributable, reliable source identifying that exact logo. A channel name, filename, search result, or page merely proving that a channel exists is not sufficient. All playlist logos should remain local in `/logos`. Unverified entries stay in the playlist with their stream URLs intact but without a logo.

## Current integrity snapshot

- Playlist entries: **561**
- Entries with a logo reference: **326**
- Entries with no logo pending verification: **235**
- Distinct local logo asset paths referenced: **227**
- Missing local logo asset paths: **0**
- External-hosted logo URLs: **0**

## Image-level findings in this pass

- `logos/bangla-tv.png` visibly contains a “BONGO FLIX” watermark over the Bangla TV branding. Removed its logo reference from both Bangla TV entries; entries and stream URLs remain intact.
- `logos/tom-and-jerry.png` depicts *Tom & Jerry Tales* show artwork, not a channel-specific broadcaster logo. Removed the reference from both Tom & Jerry channel entries; entries and stream URLs remain intact.
- Both image files were retained for traceability. No substitute logo was guessed.

## Previous changes retained

- Removed generic-looking references for Channel 1 HD, Channel 9 HD, and Channel 24 HD.
- Preserved all 561 playlist entries and their stream URLs.
- Kept entries without a verified exact image logo-less rather than using invented or similarly named artwork.

## Source leads for future verification

- [Bangladesh Television official website](https://btv.gov.bd/)
- [Wikimedia Commons category for Bangladeshi TV-channel logos](https://commons.wikimedia.org/wiki/Category:Logos_of_television_channels_in_Bangladesh)
- [JioStar official media toolkit](https://www.jiostar.com/mediatoolkit/all-logos/)

These are research leads only. Do not treat a remaining repository asset as authenticated until the image itself is compared with the source and that exact source is recorded.

## Remaining work

The other 326 referenced entries have not all been authenticated image-by-image. Continue checking actual image contents, comparing against exact official/attributable source assets, and removing references to contaminated or mismatched images without deleting playlist entries or stream URLs.


## Follow-up visual spot-check (2026-10-12)

A visual spot-check of repository assets found these additional issues:

- `logos/atn-news.png` included a third-party “BONGO FLIX” overlay in the ATN News mark. Its playlist logo reference was removed; the channel/stream entry was preserved.
- The file named `logos/arirang-tv.png` visually displays the KBS WORLD wordmark, not Arirang TV. This is a filename/content mismatch. The active Arirang playlist entry currently points to `logos/unused/arirang-cd34632359.png`, so that alternate file must be separately verified before restoring any logo.
- `logos/a-sports-5485adff.png` contains a phone number embedded in the artwork. This is not a clean broadcaster logo; no official replacement was installed because the exact official image bytes could not be retrieved and committed through this text-only GitHub file interface.

### Live playlist snapshot after this pass

- Entries: **561**
- Entries carrying a logo: **325**
- Entries without a logo: **236**
- Distinct local logo assets referenced: **227**
- All entries and stream URLs were preserved during logo-reference cleanup.

**Completion status:** this is not a completed image-by-image authentication of every referenced file. The 227 remaining distinct assets have not each been compared against a broadcaster-owned original. The available GitHub file-writing action accepts UTF-8 text, not binary image uploads, so I cannot honestly claim to have replaced raster mismatches with exact official image bytes in this pass. Continue by authenticating each asset and only installing a replacement when the actual official image file can be transferred intact; otherwise remove that logo reference pending verification.


## Expanded visual inspection and corrective pass (2026-10-12)

I visually inspected additional referenced local image files in batches and found further assets contaminated with a prominent **BONGO FLIX** watermark/overlay. Their `tvg-logo` attributes were removed from the playlist; channel entries and stream URLs were retained. This is a conservative quarantine, not a claim that the files themselves were deleted.

Confirmed contaminated/wrong-content references removed during the expanded pass:

- `logos/atn-news.png`
- `logos/a-sports-5485adff.png`
- `logos/bein-sports-3.png`
- `logos/colors.png`
- `logos/duronto-tv.png`
- `logos/ekushey-tv.png`
- `logos/global-tv.png`
- `logos/green-tv.png`
- `logos/mohona-tv.png`
- `logos/nagorik-tv.png`
- `logos/nick-bangla.png`
- `logos/sananda-tv.png`
- `logos/star-gold-select.png`
- `logos/star-gold.png`
- `logos/star-plus.png`
- `logos/zee-tv.png`

The active Arirang TV entry points to `logos/unused/arirang-cd34632359.png`, which visually contains the Arirang wordmark; the separate `logos/arirang-tv.png` file was a KBS WORLD logo and is not referenced by the active playlist. The unused A-Sports candidate still contains the BONGO FLIX overlay, so it was not substituted.

### Authoritative reference sources identified

- Sony Pictures Networks India channel portfolio and official logo library: https://www.sonypicturesnetworks.com/logos and https://www.sonypicturesnetworks.com/channels/12/entertainment
- ZEE Entertainment's official channel logo pages: https://www.zee.com/business_channels/regional-entertainment-channels/zee-bangla-hd/133x73-px_hd_logos/ and https://www.zee.com/business_channels/hindi-general-entertainment-channels/and-tv/tv-logo/
- Arirang's official site and media proposal: https://www.arirang.com/ and https://company.arirang.com/download/%EC%95%84%EB%A6%AC%EB%9E%91TV%EB%B8%8C%EB%A1%9C%EC%85%94_%EB%A7%A4%EC%B2%B4%EC%9E%90%EB%A3%8C_2019.pdf
- A Sports official site: https://a-sports.tv/
- ATN News official site: https://www.atnnewstv.com/ and its About page: https://www.atnnewstv.com/aboutus

These pages establish broadcaster identities and provide useful primary references, but I did not have the exact original image bytes for every remaining raster file available to compare and replace one by one. Do not treat the list of sources as proof that every matching filename is authentic.

### Integrity snapshot after expanded pass

- Playlist entries: **561**
- Entries carrying a logo: **311**
- Entries without a logo pending verification: **250**
- Distinct local assets referenced: **213**
- Missing local logo paths: **0**
- External logo URLs: **0**

### Completion status

**Still incomplete.** The current referenced assets have not all been authenticated individually against exact broadcaster-owned image originals. The work completed here is an expanded visual contamination screen and quarantine of the mismatches listed above, not a complete 227-image source authentication. Keep unverified channels logo-free until exact original artwork is sourced and its bytes can be committed to `/logos`.
