package bdix.ftp.tester

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.viewmodel.compose.viewModel
import kotlinx.coroutines.*
import java.net.*

enum class ServerStatus { WORKING, NOT_WORKING, NO_RESPONSE, TESTING }
data class Server(val name:String,val endpoint:String,val category:String,val status:ServerStatus=ServerStatus.NO_RESPONSE,val latencyMs:Long?=null,val detail:String="")

private val seedServers=listOf(
 Server("FTPBD","ftp://ftpbd.net","Movies"), Server("FTPBD Server 1","ftp://server1.ftpbd.net","Movies"),
 Server("FTPBD Server 2","ftp://server2.ftpbd.net","Movies"), Server("Khulnaflix","ftp://khulnaflix.net","Movies"),
 Server("Khulnaflix File","ftp://file.khulnaflix.net","Movies"), Server("Showtime BD","ftp://showtimebd.com","Movies"),
 Server("EBOX Live","ftp://fs.ebox.live","Live TV"), Server("DhakaMovie","ftp://103.237.37.181","Movies"),
 Server("NaturalBD","ftp://103.43.148.68","Movies"), Server("TimepassBD","ftp://ftp.timepassbd.live","Movies"),
 Server("MovieDom","ftp://movie.moviedom.live","Movies"), Server("Rangdhanu Live","ftp://fs.rangdhanu.live","Live TV"),
 Server("DFLIX","ftp://fs1.dflix.live","Movies"), Server("MovieMaja","ftp://moviemaja.net","Movies"),
 Server("CloudOne Movies","ftp://cloudone.com.bd","Movies"), Server("Tajpata","ftp://file.tajpata.com","Movies")
)

class MainViewModel:ViewModel(){
 var servers by mutableStateOf(seedServers); private set
 var scanning by mutableStateOf(false); private set
 var category by mutableStateOf("All")
 var status by mutableStateOf("All")
 fun scanAll(){ if(scanning)return; scanning=true; servers=servers.map{it.copy(status=ServerStatus.TESTING,detail="")}; viewModelScope.launch{
  val results=coroutineScope{servers.map{async(Dispatchers.IO){probe(it)}}.awaitAll()}; servers=results; scanning=false }
 }
 private fun probe(s:Server):Server{
  val u=runCatching{URI(s.endpoint)}.getOrNull()?:return s.copy(status=ServerStatus.NOT_WORKING,detail="Invalid URL")
  val host=u.host?:return s.copy(status=ServerStatus.NOT_WORKING,detail="Missing host"); val port=if(u.port>0)u.port else 21; val start=System.currentTimeMillis()
  return try{ Socket().use{sock->sock.connect(InetSocketAddress(host,port),5000);sock.soTimeout=5000;val b=ByteArray(256);val n=runCatching{sock.getInputStream().read(b)}.getOrDefault(0);val banner=if(n>0)String(b,0,n).trim().replace("\n"," ") else "TCP port open";s.copy(status=ServerStatus.WORKING,latencyMs=System.currentTimeMillis()-start,detail=banner.take(120)) }}
  catch(_:SocketTimeoutException){s.copy(status=ServerStatus.NO_RESPONSE,detail="Timed out")}
  catch(e:Exception){s.copy(status=ServerStatus.NOT_WORKING,detail=e.javaClass.simpleName)}
 }
}

class MainActivity:ComponentActivity(){override fun onCreate(b:Bundle?){super.onCreate(b);setContent{App()}}}

@OptIn(ExperimentalMaterial3Api::class)
@Composable fun App(vm:MainViewModel=viewModel()){
 val visible=vm.servers.filter{(vm.category=="All"||it.category==vm.category)&&(vm.status=="All"||(vm.status=="Working"&&it.status==ServerStatus.WORKING)||(vm.status=="Not working"&&it.status==ServerStatus.NOT_WORKING)||(vm.status=="No response"&&it.status==ServerStatus.NO_RESPONSE)||(vm.status=="Testing"&&it.status==ServerStatus.TESTING))}
 Scaffold(topBar={TopAppBar(title={Text("BDIX FTP Server Tester")})},floatingActionButton={FloatingActionButton(onClick=vm::scanAll,enabled=!vm.scanning){Text(if(vm.scanning)"…" else "Scan")}}){pad->Column(Modifier.fillMaxSize().padding(pad).padding(12.dp)){
  Text("Status",style=MaterialTheme.typography.titleSmall);LazyRow(horizontalArrangement=Arrangement.spacedBy(8.dp)){items(listOf("All","Working","Not working","No response","Testing")){x->FilterChip(selected=vm.status==x,onClick={vm.status=x},label={Text(x)})}}
  Spacer(Modifier.height(10.dp));Text("Type",style=MaterialTheme.typography.titleSmall);LazyRow(horizontalArrangement=Arrangement.spacedBy(8.dp)){items(listOf("All","Live TV","Movies")){x->FilterChip(selected=vm.category==x,onClick={vm.category=x},label={Text(x)})}}
  Spacer(Modifier.height(10.dp));Text("${visible.size} servers",style=MaterialTheme.typography.labelLarge);Spacer(Modifier.height(8.dp));LazyColumn(verticalArrangement=Arrangement.spacedBy(8.dp)){items(visible,key={it.endpoint}){ServerCard(it)}}
 }} }

@Composable fun ServerCard(s:Server){val ctx=LocalContext.current;val open=s.status==ServerStatus.WORKING;val label=when(s.status){ServerStatus.WORKING->"Working";ServerStatus.NOT_WORKING->"Not working";ServerStatus.NO_RESPONSE->"No response";ServerStatus.TESTING->"Testing…"};Card(Modifier.fillMaxWidth().clickable(enabled=open){ctx.startActivity(Intent(Intent.ACTION_VIEW,Uri.parse(s.endpoint)))}){Column(Modifier.padding(14.dp)){Text(s.name,style=MaterialTheme.typography.titleMedium);Text(s.endpoint);Text(s.category,style=MaterialTheme.typography.labelMedium);Text(label+(s.latencyMs?.let{" • $it ms"}?:""));if(s.detail.isNotBlank())Text(s.detail,maxLines=2,style=MaterialTheme.typography.bodySmall);if(open)Text("Tap to open",style=MaterialTheme.typography.labelLarge)}}}
