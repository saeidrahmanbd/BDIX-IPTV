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

The four promoted HTTPS URLs had recent successful HTTP 206 responses, zero consecutive failures, and success rates of at least 98% in the repository's 2026-11-09 stream-health history. Rajdhani TV's HTTPS mirror is the same host and path with TLS.

## Remaining exceptions

The current playlist still has bare-IP HTTP primary routes where the retained inventory contains no same-ID HTTPS backup. Those routes were left in place rather than inventing an unverified replacement or disabling a reachable channel. They require a verified secure source from the provider or an owner decision to quarantine them.

The probe confirms HTTP reachability only; it does not verify decoded playback or identity from video frames.
