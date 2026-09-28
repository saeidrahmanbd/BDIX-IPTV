# Sample Configuration

Safe, copyable templates for configuring an IPTV client.

## M3U / M3U Plus

Use the main playlist URL:

```
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u
```

For an IPTV application with a **Playlist URL** field, paste the URL above.

## Xtream Codes

For clients that support Xtream Codes / XCIPTV, use:

- **Server URL:** your deployed BDIX-IPTV Xtream Gateway Worker URL
- **Username:** your configured Xtream username
- **Password:** your configured Xtream password

Example format:

```
Server: https://YOUR-WORKER.example.workers.dev
Username: YOUR_USERNAME
Password: YOUR_PASSWORD
```

**Do not publish or commit your real Xtream username/password.**

See **[Xtream Gateway documentation](../xtream/README.md)** for the supported endpoints and deployment instructions.

## EPG

The repository currently provides an **EPG Coverage Report**, not a complete public programme-data feed:

**[EPG Coverage Report](../reports/epg-coverage.md)**

## Compatible use

The main M3U playlist can be used with compatible M3U/IPTV applications. Xtream-compatible applications can use the deployed gateway where available.
