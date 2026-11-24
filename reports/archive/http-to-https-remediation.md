# HTTP-to-HTTPS Remediation Audit

Generated: 2026-11-09
Playlist: `IPTV-Playlist.m3u`

## Changes applied

Promoted previously recorded, same-identity HTTPS backup routes to primary for four channels. Each prior HTTP primary was retained in `Backup`; no stream URL was deleted.

| Channel | Primary transport now | Prior HTTP route |
|---|---|---|
| Bangla TV | HTTPS AynaOTT | Retained in Backup |
| SA TV | HTTPS GPCDN | Retained in Backup |
| Hindi Hits | HTTPS TangoTV | Retained in Backup |
| Zee TV | HTTPS Wurl | Retained in Backup |
| Rajdhani TV | HTTPS same-host/same-path mirror | HTTP retained in Backup |

The four newly promoted HTTPS routes had recent successful HTTP 206 responses, zero consecutive failures, and success rates of at least 98% in the repository's 2026-11-09 stream-health history. Rajdhani TV's HTTPS mirror is the same host and path with TLS.

## Remaining active bare-IP HTTP exceptions

There are 16 remaining active bare-IP HTTP routes:

- Amar Bangla Digital
- Probashi TV
- Mon Bangla
- News 21
- SNB Cinema
- Colors Cineplex Bollywood
- Colors Cineplex Superhits
- Sony Wah
- Star Utsav Movies
- Vision (India)
- Sony Entertainment Television HD
- Star Utsav
- aur LIFE
- Disney Jr
- ESPN
- Fox Sports 1

Fifteen have no same-ID HTTPS backup in the current playlist. Amar Bangla Digital has an HTTPS route, but its opaque encoded path has not been cleared as a non-credential route. These 16 were left unchanged rather than inventing an unverified replacement or disabling a reachable channel. They remain explicit exceptions to the HTTPS-hardening target and need a verified provider mirror or an owner decision to quarantine.

The probe confirms HTTP reachability only; it does not verify decoded playback or identity from video frames.
