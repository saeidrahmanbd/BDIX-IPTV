# Placeholder Stream Quarantine Audit

Generated: 2026-11-09
Playlist: `IPTV-Playlist.m3u`

## Decision

The legacy Colors and Star Gold placeholder candidates remain in the protected `Review` queue. Their stream URLs are preserved; no queue entry is deleted or promoted automatically. Legitimate active Colors variants remain in their existing primary groups and are not affected by this quarantine review.

## Verified Review entries

| Channel | tvg-id | Last recorded health evidence |
|---|---|---|
| Colors | `Colors.in` | 23 consecutive failures |
| Colors Bangla | `Colors.Bangla.in` | 23 consecutive failures |
| Colors Bangla Cinema | `ColorsBanglaCinema.in@SD` | 23 consecutive failures |
| Colors Cineplex [UK] | `ColorsCineplex.uk` | 23 consecutive failures |
| Star Gold | `StarGold.in@HD` | Two retained routes; 23 and 16 consecutive failures |

## A–D completion checklist

1. **Identify:** checked the exact playlist IDs and current Review group for the candidate rows.
2. **Quarantine:** confirmed they remain in `Review`; their stream URLs are retained without modification.
3. **Annotate:** this report records the identity, location and last recorded health evidence; raw URLs and possible access tokens are deliberately omitted.
4. **Xtream isolation:** the main Xtream worker excludes `Review`, `New Channels`, and `New Backups`; regression tests enforce hidden-group rules and verify the placeholder rows remain quarantined.

## Protected-stream policy

Do not delete or promote these Review rows only because an external health probe failed. The probe runs outside the Bangladesh network and may encounter provider-side restrictions. Promote a row only after a fresh Bangladesh-local playback test and a verified channel identity.
