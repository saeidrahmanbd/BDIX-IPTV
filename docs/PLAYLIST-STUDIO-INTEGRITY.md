# Playlist Studio v5.1 Release Integrity

The SHA-256 digests below are taken from the published GitHub release asset metadata for [Playlist Studio v5.1](https://github.com/saeidrahmanbd/BDIX-IPTV/releases/tag/v5.1).

| Asset | Size | SHA-256 |
|---|---:|---|
| `Playlist-Studio-5.1.exe` | 102,526,298 bytes | `ef0b58e0108dc76d886b92a88170ff5fd231704604150d6283feb6f1b9f48412` |
| `Playlist-Studio-5_1-Windows-Build-Kit-r2.zip` | 688,328 bytes | `66d1de92f3d2285c38afae767697dae71e74a842266ce644700f8cd745453335` |

These values identify the exact assets published on the v5.1 release at the time this file was updated. Verify a downloaded file locally before running or extracting it.

## Verify on Windows

In PowerShell, run:

    Get-FileHash .\Playlist-Studio-5.1.exe -Algorithm SHA256
    Get-FileHash .\Playlist-Studio-5_1-Windows-Build-Kit-r2.zip -Algorithm SHA256

Compare the resulting `Hash` values with the corresponding values above. The release page remains the authoritative source if an asset is replaced.
