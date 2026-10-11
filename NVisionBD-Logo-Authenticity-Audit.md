# NVisionBD Playlist Logo Authenticity Audit

Audit date: 2026-10-11  
Playlist: [NVisionBD-Playlist.m3u](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/NVisionBD-Playlist.m3u)

## Acceptance rule

A logo is approved only when the **image itself** is matched to an official broadcaster/brand asset or an attributable, reliable source identifying that exact logo. A channel name, filename, search result, or a page merely proving that a channel exists is not sufficient. All playlist logos must remain local in `/logos`. Unverified entries stay in the playlist with their stream URLs intact but without a logo.

## Current integrity snapshot

- Playlist entries: **561**
- Entries with a logo reference: **330**
- Entries with no logo pending verification: **231**
- Distinct local logo asset paths referenced: **230**
- Missing local logo references among entries that have a logo: **0** (verified against the complete recursive Git tree)
- External-hosted logo URLs: **0** (the playlist references GitHub-hosted local repository assets)

**Important:** the logo references currently remaining are not automatically authenticated by the integrity checks. Their asset provenance still needs to be verified one by one. This report does not certify the whole logo collection.

## Corrective action already applied

Removed 42 references to unverified bespoke/custom artwork in an earlier pass, and removed three additional generic-looking PNG references in this pass. Seventeen references to existing repository assets were restored in this pass based on filename/channel-name alignment; these still require source-by-source image authentication. Preserved all 561 channel entries and their stream URLs. Unverified entries remain without `tvg-logo` until an exact authentic image can be obtained and localized.

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

The playlist currently references **230 distinct local logo files across 330 entries with a logo**. Each distinct file needs an evidence record containing: channel/brand, local path, exact official source URL, confirmation that the image matches the source asset, and disposition (approved/replaced/removed). Until that check is complete, these files must be treated as **not yet certified**, even if their filenames look correct.

No substitute artwork should be drawn or generated to fill gaps. When a primary-source image cannot be retrieved and verified, keep the entry logo-less rather than using a lookalike.

## Additional conservative cleanup — 2026-10-11

A visual spot-check showed that at least one asset named as an “official” logo (`nvisionbd-official-btv-sangsad.png`) was a recreated illustration rather than a verified broadcaster-supplied logo. A filename/prefix is not provenance. Therefore, **149 playlist logo references** pointing to `logos/nvisionbd-*` files were removed from playlist metadata until the actual images can be matched against primary sources. The channel entries and stream URLs were preserved; the asset files were not deleted. This is a precautionary quarantine, not a claim that all 149 images are fake.

### Channels quarantined from unverified `nvisionbd-*` logo references

- BTV Sangsad
- Bangla Big Boss 24x7
- CTVN AKD Plus
- Afra Film
- Anmol Cinema
- Anmol Cinema 2
- Biz Cinema
- The Q India
- Afro Music Channel
- Euro Indie Music Chart TV
- Amar Ujala
- &tv HD
- Epic
- Hindi Big Boss 24x7 2026
- Hindi Khabar
- India Today
- News 18 Assam
- The Q
- Ary News
- Action 24
- Aflam
- Anger Management Channel
- Baraza TV
- Comedy Central
- ETV
- Fail Army
- Filmua Drama
- FX TV
- Hard Knocks
- Hit
- Kronehit
- Laff TV
- Magic TV
- Movie Sphere
- Movie Sphere Au
- My Time Movie
- Nexus Television
- Screamin
- Silk Way Cinema
- Star Family
- Topestrada TV
- Viju Tv1000 Action
- &xplorer HD
- Cooking TV
- Fashion TV HD
- Nat Geo Bangla
- Persiana Travel
- Balapan
- Be.joy Kids
- Boomerang
- Boomerang UK
- Disney Junior
- Niki Jr Kids
- Madani TV Bangla
- Madina Live
- Arena Sport 1
- Asean Cup 2026
- Bt Sports 2
- Claro Sports
- Cosmote Sports 1
- Cosmote Sports 4
- Cricbuzz
- Digi Sport 1
- Digi Sport 2
- English Premier League 2
- Fifa+
- Fight Network
- Fubo Sports
- Fuel TV Apac
- Fuel TV Europe
- Golf Channel
- In Eurosport HD
- Ind Unite8 Sports 1 HD
- Jordan Sport
- Ktv Sport Plus
- Lacrosse TV
- Laliga Live 1
- Laliga Live 2
- Laligatv
- M4 Sport
- Magenta Sports 2
- Max Sport 1
- Max Sport 2
- Max Sport 3
- Max Sport 4
- Nbc Sports
- Nova Sport 1 HD
- Oman Sports
- Pk Geo Super
- Pk Ten Cricket
- Premier Sports 1
- Rtsh Sport
- Setanta Sport
- Sky Sports Laliga
- Sports Digital Fsbl
- Sports First TV
- Sports Fishing TV
- Sports Grid
- Sportv
- Supersport Cricket
- Tennis Channel
- TNT Sport 1
- Tsn Aq1
- Turkmenistan Sport
- UK TNT Sports 1 HD
- UK TNT Sports 2 HD
- UK TNT Sports 3 HD
- UK TNT Sports 4 HD
- Unite8 Sports 1
- Unite8 Sports 2
- US Sky Sports Main Event
- US Sky Sports Premier League
- US Willow By Cricbuzz
- Willow TV
- Xtrem Sports
- Ziggo Sport Live
- Ziggo Sport 2 HD
- Ziggo Sport 3 HD
- 51 Radio TV [geo-blocked]
- 92.8 FM Radio Bhumi
- 98.1 Pearl FM
- Abc Music Radio
- Adt FM
- Bangla Radio
- Bd Radio FM
- Dhaka FM 90.4
- Love Gold Bangla
- My 90s Bengali Online
- Palki FM
- Peoples Radio
- Radio Adamya
- Radio Bangladesh Co
- Radio Bhumi 92.80 FM
- Radio Bushra
- Radio Capital FM 94.8
- Radio Din Raat 93.6 FM
- Radio Gaan Baksho
- Radio Mahananda - 98.8
- Radio Padma – 99.2 FM
- Radio Shadhin - 92.4 FM
- Radio Shadin
- Radio Sonali Dingulo
- Radio Tangail
- Radio Vivid Voice | Mymensingh
- Rick Astley
- Saudia Radio
- Utbd FM
- Uttorbango Betar
- Valobasar Rupali Sur

### Integrity after cleanup

- Playlist entries: **561**
- Entries still carrying a logo: **330**
- Entries without a logo pending verification: **231**
- Distinct local logo files still referenced: **230**
- Remaining `nvisionbd-*` logo references: **0**
- All entries and stream lines retained; logo metadata only was changed in this cleanup.

The remaining 230 distinct logo assets still require source-by-source image authentication. They are not certified merely because they remain in the playlist. Only restore a quarantined reference after documenting the exact official asset URL and verifying the image itself against that source.
