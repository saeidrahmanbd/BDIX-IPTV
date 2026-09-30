# ⚙️ Sample Configuration

This page provides a safe reference configuration for using the BDIX-IPTV playlist with common IPTV players and the optional Xtream Gateway.

> **Security:** Do not publish real Xtream usernames, passwords, private stream URLs, or other credentials in this repository.

## 📺 M3U Playlist

Use the maintained playlist URL:

```text
https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u
```

### XCIPTV / M3U-compatible players

Choose **M3U Playlist / URL** and paste the URL above.

The playlist includes channel groups, channel IDs and repository-hosted PNG logos.

## 🛜 Xtream Codes

If you have deployed the optional Xtream Gateway, use your Worker URL as the **Server URL**.

Example:

```text
Server URL: https://YOUR-WORKER.example.workers.dev
Username: YOUR_XTREAM_USERNAME
Password: YOUR_XTREAM_PASSWORD
```

Do not replace the placeholders with real credentials in this repository.

Supported Xtream-style endpoints are documented in [Xtream Gateway](../xtream/README.md).

## 📡 EPG

The repository maintains an EPG coverage report and source configuration.

See:

- [EPG Coverage Report](../reports/epg-coverage.md)
- [EPG directory](../epg/README.md)

## 🖥️ Playlist Studio

For playlist editing and management, download the latest Windows portable release from the [Playlist Studio releases](https://github.com/saeidrahmanbd/BDIX-IPTV/releases/latest).

## 🔐 Recommended practice

- Keep credentials outside the repository.
- Use environment variables or platform secrets for Xtream credentials.
- Treat public M3U URLs as public resources.
- Do not commit private IPTV provider URLs or passwords.
