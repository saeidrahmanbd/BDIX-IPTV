"""Single source of truth for owner-authorized permanent channel removals."""

PERMANENTLY_REMOVED_NAMES = (
    "Bollywood Masala",
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
