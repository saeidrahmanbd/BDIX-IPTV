package bdix.ftp.tester

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.AssistChip
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Divider
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FilterChip
import androidx.compose.material3.FloatingActionButton
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.viewmodel.compose.viewModel
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.async
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.launch
import java.net.InetSocketAddress
import java.net.Socket
import java.net.SocketTimeoutException
import java.net.URI

enum class ServerStatus { WORKING, NOT_WORKING, NO_RESPONSE, TESTING }

data class Server(
    val name: String,
    val endpoint: String,
    val category: String,
    val status: ServerStatus = ServerStatus.NO_RESPONSE,
    val latencyMs: Long? = null,
    val detail: String = ""
)

private val seedServers = listOf(
    Server("FTPBD", "ftp://ftpbd.net", "Movies"),
    Server("FTPBD Server 1", "ftp://server1.ftpbd.net", "Movies"),
    Server("FTPBD Server 2", "ftp://server2.ftpbd.net", "Movies"),
    Server("Khulnaflix", "ftp://khulnaflix.net", "Movies"),
    Server("Khulnaflix File", "ftp://file.khulnaflix.net", "Movies"),
    Server("Showtime BD", "ftp://showtimebd.com", "Movies"),
    Server("EBOX Live", "ftp://fs.ebox.live", "Live TV"),
    Server("DhakaMovie", "ftp://103.237.37.181", "Movies"),
    Server("NaturalBD", "ftp://103.43.148.68", "Movies"),
    Server("TimepassBD", "ftp://ftp.timepassbd.live", "Movies"),
    Server("MovieDom", "ftp://movie.moviedom.live", "Movies"),
    Server("Rangdhanu Live", "ftp://fs.rangdhanu.live", "Live TV"),
    Server("DFLIX", "ftp://fs1.dflix.live", "Movies"),
    Server("MovieMaja", "ftp://moviemaja.net", "Movies"),
    Server("CloudOne Movies", "ftp://cloudone.com.bd", "Movies"),
    Server("Tajpata", "ftp://file.tajpata.com", "Movies")
)

class MainViewModel : ViewModel() {
    var servers by mutableStateOf(seedServers)
        private set
    var scanning by mutableStateOf(false)
        private set
    var category by mutableStateOf("All")
    var status by mutableStateOf("All")

    fun scanAll() {
        if (scanning) return
        scanning = true
        servers = servers.map { it.copy(status = ServerStatus.TESTING, detail = "") }
        viewModelScope.launch {
            val results = coroutineScope {
                servers.map { server -> async(Dispatchers.IO) { probe(server) } }.awaitAll()
            }
            servers = results
            scanning = false
        }
    }

    private fun probe(server: Server): Server {
        val uri = runCatching { URI(server.endpoint) }.getOrNull()
            ?: return server.copy(status = ServerStatus.NOT_WORKING, detail = "Invalid URL")
        val host = uri.host
            ?: return server.copy(status = ServerStatus.NOT_WORKING, detail = "Missing host")
        val port = if (uri.port > 0) uri.port else 21
        val start = System.currentTimeMillis()

        return try {
            Socket().use { socket ->
                socket.connect(InetSocketAddress(host, port), 5000)
                socket.soTimeout = 5000
                val buffer = ByteArray(256)
                val bytes = runCatching { socket.getInputStream().read(buffer) }.getOrDefault(0)
                val banner = if (bytes > 0) String(buffer, 0, bytes).trim().replace("\n", " ") else "TCP port open"
                server.copy(
                    status = ServerStatus.WORKING,
                    latencyMs = System.currentTimeMillis() - start,
                    detail = banner.take(120)
                )
            }
        } catch (_: SocketTimeoutException) {
            server.copy(status = ServerStatus.NO_RESPONSE, detail = "Timed out")
        } catch (e: Exception) {
            server.copy(status = ServerStatus.NOT_WORKING, detail = e.javaClass.simpleName)
        }
    }
}

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { App() }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun App(vm: MainViewModel = viewModel()) {
    var showInfo by remember { mutableStateOf(false) }
    val visible = vm.servers.filter {
        (vm.category == "All" || it.category == vm.category) &&
            (vm.status == "All" ||
                (vm.status == "Working" && it.status == ServerStatus.WORKING) ||
                (vm.status == "Not working" && it.status == ServerStatus.NOT_WORKING) ||
                (vm.status == "No response" && it.status == ServerStatus.NO_RESPONSE) ||
                (vm.status == "Testing" && it.status == ServerStatus.TESTING))
    }
    val working = vm.servers.count { it.status == ServerStatus.WORKING }
    val failed = vm.servers.count { it.status == ServerStatus.NOT_WORKING }
    val noResponse = vm.servers.count { it.status == ServerStatus.NO_RESPONSE }

    MaterialTheme {
        Scaffold(
            topBar = {
                TopAppBar(
                    title = {
                        Column {
                            Text("BDIX FTP Tester", fontWeight = FontWeight.Bold)
                            Text(
                                "BDIX server connectivity checker",
                                style = MaterialTheme.typography.labelSmall,
                                color = MaterialTheme.colorScheme.onSurfaceVariant
                            )
                        }
                    },
                    actions = {
                        IconButton(onClick = { showInfo = true }) {
                            Text("ⓘ", style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold)
                        }
                    },
                    colors = TopAppBarDefaults.topAppBarColors(
                        containerColor = MaterialTheme.colorScheme.surface
                    )
                )
            },
            floatingActionButton = {
                FloatingActionButton(onClick = vm::scanAll) {
                    Text(if (vm.scanning) "…" else "SCAN", fontWeight = FontWeight.Bold)
                }
            }
        ) { padding ->
            LazyColumn(
                modifier = Modifier.fillMaxSize().padding(padding),
                contentPadding = PaddingValues(start = 16.dp, top = 12.dp, end = 16.dp, bottom = 96.dp),
                verticalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                item {
                    HeroCard(
                        scanning = vm.scanning,
                        total = vm.servers.size,
                        onScan = vm::scanAll
                    )
                }
                item {
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        SummaryCard("Working", working, Modifier.weight(1f))
                        SummaryCard("Failed", failed, Modifier.weight(1f))
                        SummaryCard("No response", noResponse, Modifier.weight(1f))
                    }
                }
                item {
                    Text("Filter by status", style = MaterialTheme.typography.titleSmall, fontWeight = FontWeight.Bold)
                }
                item {
                    LazyRow(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                        items(listOf("All", "Working", "Not working", "No response", "Testing")) { value ->
                            FilterChip(
                                selected = vm.status == value,
                                onClick = { vm.status = value },
                                label = { Text(value) }
                            )
                        }
                    }
                }
                item {
                    Text("Server type", style = MaterialTheme.typography.titleSmall, fontWeight = FontWeight.Bold)
                }
                item {
                    LazyRow(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                        items(listOf("All", "Live TV", "Movies")) { value ->
                            FilterChip(
                                selected = vm.category == value,
                                onClick = { vm.category = value },
                                label = { Text(value) }
                            )
                        }
                    }
                }
                item {
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Text(
                            "${visible.size} servers",
                            style = MaterialTheme.typography.titleMedium,
                            fontWeight = FontWeight.Bold
                        )
                        Spacer(Modifier.weight(1f))
                        if (vm.scanning) {
                            AssistChip(onClick = {}, enabled = false, label = { Text("Scanning…") })
                        }
                    }
                }
                items(visible, key = { it.endpoint }) { server -> ServerCard(server) }
            }
        }
    }

    if (showInfo) InfoDialog(onDismiss = { showInfo = false })
}

@Composable
private fun HeroCard(scanning: Boolean, total: Int, onScan: () -> Unit) {
    Card(
        modifier = Modifier.fillMaxWidth(),
        shape = RoundedCornerShape(24.dp),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.primaryContainer)
    ) {
        Column(Modifier.padding(20.dp)) {
            Text("Check your BDIX servers", style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold)
            Spacer(Modifier.height(6.dp))
            Text(
                "Test FTP connectivity, response time and server availability in one scan.",
                style = MaterialTheme.typography.bodyMedium
            )
            Spacer(Modifier.height(16.dp))
            Row(verticalAlignment = Alignment.CenterVertically) {
                Surface(shape = CircleShape, color = MaterialTheme.colorScheme.primary) {
                    Text(
                        "BDIX",
                        modifier = Modifier.padding(horizontal = 12.dp, vertical = 8.dp),
                        color = MaterialTheme.colorScheme.onPrimary,
                        fontWeight = FontWeight.Bold
                    )
                }
                Spacer(Modifier.width(10.dp))
                Text("${total} servers configured", style = MaterialTheme.typography.labelLarge)
                Spacer(Modifier.weight(1f))
                TextButton(onClick = onScan, enabled = !scanning) {
                    Text(if (scanning) "SCANNING" else "START SCAN")
                }
            }
        }
    }
}

@Composable
private fun SummaryCard(label: String, value: Int, modifier: Modifier) {
    Card(modifier = modifier, shape = RoundedCornerShape(16.dp)) {
        Column(Modifier.padding(12.dp)) {
            Text(value.toString(), style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold)
            Text(label, style = MaterialTheme.typography.labelSmall, maxLines = 1, overflow = TextOverflow.Ellipsis)
        }
    }
}

@Composable
private fun ServerCard(server: Server) {
    val context = LocalContext.current
    val working = server.status == ServerStatus.WORKING
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .clickable(enabled = working) {
                context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(server.endpoint)))
            },
        shape = RoundedCornerShape(18.dp),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceContainer)
    ) {
        Column(Modifier.padding(16.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                StatusDot(server.status)
                Spacer(Modifier.width(10.dp))
                Column(Modifier.weight(1f)) {
                    Text(server.name, style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
                    Text(
                        server.endpoint,
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                }
                Text(
                    when (server.status) {
                        ServerStatus.WORKING -> "WORKING"
                        ServerStatus.NOT_WORKING -> "FAILED"
                        ServerStatus.NO_RESPONSE -> "TIMEOUT"
                        ServerStatus.TESTING -> "TESTING"
                    },
                    style = MaterialTheme.typography.labelSmall,
                    fontWeight = FontWeight.Bold
                )
            }
            Spacer(Modifier.height(10.dp))
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                AssistChip(onClick = {}, enabled = false, label = { Text(server.category) })
                server.latencyMs?.let {
                    AssistChip(onClick = {}, enabled = false, label = { Text("${it} ms") })
                }
            }
            if (server.detail.isNotBlank()) {
                Spacer(Modifier.height(6.dp))
                Text(
                    server.detail,
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
            }
            if (working) {
                Spacer(Modifier.height(6.dp))
                Text(
                    "Tap to open FTP",
                    style = MaterialTheme.typography.labelMedium,
                    color = MaterialTheme.colorScheme.primary,
                    fontWeight = FontWeight.Bold
                )
            }
        }
    }
}

@Composable
private fun StatusDot(status: ServerStatus) {
    val color = when (status) {
        ServerStatus.WORKING -> Color(0xFF2E7D32)
        ServerStatus.NOT_WORKING -> Color(0xFFC62828)
        ServerStatus.NO_RESPONSE -> Color(0xFFF57C00)
        ServerStatus.TESTING -> Color(0xFF1565C0)
    }
    Box(Modifier.size(12.dp).background(color, CircleShape))
}

@Composable
private fun InfoDialog(onDismiss: () -> Unit) {
    AlertDialog(
        onDismissRequest = onDismiss,
        title = { Text("About BDIX FTP Tester", fontWeight = FontWeight.Bold) },
        text = {
            Column(verticalArrangement = Arrangement.spacedBy(10.dp)) {
                Text("A lightweight Android utility for checking BDIX FTP server availability, response time and connectivity.")
                Divider()
                InfoLine("Developer", "SAEID RAHMAN")
                InfoLine("Role", "Marketing & Brand")
                InfoLine("Project", "BDIX-IPTV")
                InfoLine("App", "BDIX FTP Server Tester")
                InfoLine("Version", "1.0.0")
                Text(
                    "GitHub: saeidrahmanbd/BDIX-IPTV",
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.primary
                )
            }
        },
        confirmButton = { TextButton(onClick = onDismiss) { Text("CLOSE") } }
    )
}

@Composable
private fun InfoLine(label: String, value: String) {
    Row(modifier = Modifier.fillMaxWidth()) {
        Text("${label}: ", fontWeight = FontWeight.Bold, modifier = Modifier.width(82.dp))
        Text(value)
    }
}
