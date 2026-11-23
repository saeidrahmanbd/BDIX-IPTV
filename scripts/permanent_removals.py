"""Single source of truth for owner-authorized permanent channel removals."""

PERMANENTLY_REMOVED_NAMES = (
    "Crime + Investigation",
    "History Hunters",
    "True History",
    "FX 2",
    "Al-Mahdi TV",
    "IBN TV",
    "IBN TV Africa",
    "Safeer TV",
    "AccuWeather",
    "America's Got Talent",
    "American Idol",
    "Baraza Music TV",
    "The Walking Dead Universe",
    "Popflix",
    "60 Days In",
    "Deadly Women",
    "Highway Thru Hell",
    "MINI",
    "Mundial",
    "TVC Arabic Kids",
    "Grace Network",
    "Joshua TV",
    "King TV",
    "Jeremiah TV",
    "CBN TV USA",
    "Dios Te Ve Kids",
    "ZB Bhakti",
    "Aaj Tak",
    "GNT",
    "Good News Today",
    "Network 10",
    "Angel TV",
    "Calvary TV",
    "Hosanna TV",
    "Hosanna TV Hindi",
    "Prarthana TV",
    "Santvani Channel",
    "Sharnam TV",
)

# Exact owner-authorized removal of orphan Backup rows. Both channel ID and URL
# must match; a different endpoint for the same identity is not covered.
AUTHORIZED_ORPHAN_BACKUP_REMOVALS = {
    "bhi.channel.in": "https://server.livelegitpro.in/bhichannel/bhichannel/tracks-v1a1/mono.m3u8",
    "rplus.in@sd": "https://vglivessai.akamaized.net/sg/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/e5dcc9dc-3a33-4b19-a361-5a5b3aa022f7/index.m3u8",
    # US kids feed is outside the IPTV-Playlist country/genre scope; retain its failed Review candidates.
    "cartoonnetwork.us": "https://vodzong.mjunoon.tv:8087/streamtest/cartoon-network-87/playlist.m3u8",
}

# Exact owner-authorized primary-channel removals. Each entry requires the
# channel ID, original group, and exact stream URL to match.
AUTHORIZED_PRIMARY_CHANNEL_REMOVALS = {
    "fight.tv.com": (
        "https://streams2.sofast.tv/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/70e45fc8-1f6c-4492-ac26-9868f70f4e02/manifest.m3u8",
        "Sports",
    ),
    "FutbolTV.uz@HD": (
        "http://stream3.cinerama.uz/1010/tracks-v1a1/mono.m3u8",
        "Sports",
    ),
    "MoviesNowPlus.in@HD": (
        "http://116.90.120.149:8000/play/a11k/index.m3u8",
        "International",
    ),
    "MyTimeMovieNetwork.us@SD": (
        "https://mytime-tcl.amagi.tv/1080p-en-cc/index.m3u8",
        "International",
    ),
    "TravelChannel.us@SD": (
        "https://tvsen3.aynaott.com/sFwCR6Fu/index.m3u8",
        "Documentary & Wildlife",
    ),
}
