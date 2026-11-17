const encoder = new TextEncoder();
const API = "https://api.github.com";
const REPOSITORY = "saeidrahmanbd/BDIX-IPTV";

function b64url(bytes) {
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replaceAll("=", "").replaceAll("+", "-").replaceAll("/", "_");
}
function derLength(n) {
  if (n < 128) return Uint8Array.of(n);
  const bytes = [];
  while (n > 0) { bytes.unshift(n & 255); n >>>= 8; }
  return Uint8Array.of(128 | bytes.length, ...bytes);
}
function der(tag, content) {
  const len = derLength(content.length), out = new Uint8Array(1 + len.length + content.length);
  out[0] = tag; out.set(len,1); out.set(content,1+len.length); return out;
}
function join(...parts) {
  const out = new Uint8Array(parts.reduce((n,p)=>n+p.length,0)); let offset=0;
  for (const p of parts) { out.set(p,offset); offset+=p.length; }
  return out;
}
export function pkcs1ToPkcs8(pkcs1) {
  const alg=Uint8Array.of(48,13,6,9,42,134,72,134,247,13,1,1,1,5,0);
  return der(48,join(Uint8Array.of(2,1,0),alg,der(4,pkcs1)));
}
function pemBytes(pem) {
  if (typeof pem !== "string" || !pem.includes("BEGIN RSA PRIVATE KEY"))
    throw new Error("GitHub App key must be a PEM RSA private key");
  const body=pem.split("\n").filter(line=>!line.startsWith("-----")).join("").replaceAll(" ","").replaceAll("\r","");
  return Uint8Array.from(atob(body),c=>c.charCodeAt(0));
}
function numeric(value) {
  const s=String(value || "");
  return s.length>0 && [...s].every(c=>c>="0" && c<="9");
}
export async function createAppJwt({appId,privateKeyPem,now=Date.now(),cryptoImpl=globalThis.crypto}) {
  if (!numeric(appId)) throw new Error("GITHUB_APP_ID must be numeric");
  if (!cryptoImpl?.subtle) throw new Error("Web Crypto is unavailable");
  const h=b64url(encoder.encode(JSON.stringify({alg:"RS256",typ:"JWT"})));
  const iat=Math.floor(now/1000)-60;
  const p=b64url(encoder.encode(JSON.stringify({iat,exp:iat+540,iss:String(appId)})));
  const input=h+"."+p;
  const key=await cryptoImpl.subtle.importKey("pkcs8",pkcs1ToPkcs8(pemBytes(privateKeyPem)),
    {name:"RSASSA-PKCS1-v1_5",hash:"SHA-256"},false,["sign"]);
  const sig=await cryptoImpl.subtle.sign("RSASSA-PKCS1-v1_5",key,encoder.encode(input));
  return input+"."+b64url(new Uint8Array(sig));
}
function headers(token) {
  return {Accept:"application/vnd.github+json",Authorization:"Bearer "+token,
    "X-GitHub-Api-Version":"2022-11-28","User-Agent":"BDIX-IPTV-Reliability-Worker"};
}
async function getJson(fetchImpl,url,options) {
  const response=await fetchImpl(url,options);
  if (!response.ok) throw new Error("GitHub API request failed (HTTP "+response.status+")");
  return response.json();
}
async function postNoContent(fetchImpl,url,options) {
  const response=await fetchImpl(url,options);
  if (!response.ok) throw new Error("GitHub workflow dispatch failed (HTTP "+response.status+")");
}
export async function createInstallationToken(env,fetchImpl=fetch) {
  const appId=String(env.GITHUB_APP_ID || ""), installationId=String(env.GITHUB_INSTALLATION_ID || "");
  if (!numeric(appId)) throw new Error("GITHUB_APP_ID is missing or invalid");
  if (!numeric(installationId)) throw new Error("GITHUB_INSTALLATION_ID is missing or invalid");
  if (!env.GITHUB_APP_PRIVATE_KEY) throw new Error("GITHUB_APP_PRIVATE_KEY is missing");
  const jwt=await createAppJwt({appId,privateKeyPem:env.GITHUB_APP_PRIVATE_KEY});
  const result=await getJson(fetchImpl,API+"/app/installations/"+installationId+"/access_tokens",
    {method:"POST",headers:headers(jwt)});
  if (!result.token) throw new Error("GitHub did not issue an installation token");
  if (!result.permissions || result.permissions.actions!=="write")
    throw new Error("GitHub installation token does not have Actions write permission");
  return {token:result.token,appId,installationId,permissions:result.permissions};
}
export async function createGitHubClient(env,fetchImpl=fetch) {
  const access=await createInstallationToken(env,fetchImpl), auth=headers(access.token);
  const repo=await getJson(fetchImpl,API+"/repos/"+REPOSITORY,{method:"GET",headers:auth});
  if (String(repo.full_name || "").toLowerCase()!==REPOSITORY.toLowerCase())
    throw new Error("GitHub App installation resolved to an unexpected repository");
  return {
    identity:{app_id:access.appId,installation_id:access.installationId,repository:repo.full_name,
      actions_permission:access.permissions.actions},
    async listWorkflowRuns(file,from,to) {
      const collected=[];
      for (let page=1;page<=3;page++) {
        const q=new URLSearchParams({per_page:"100",page:String(page),created:from+".."+to});
        const data=await getJson(fetchImpl,API+"/repos/"+REPOSITORY+"/actions/workflows/"+
          encodeURIComponent(file)+"/runs?"+q,{method:"GET",headers:auth});
        const found=Array.isArray(data.workflow_runs)?data.workflow_runs:[];
        collected.push(...found);
        if (found.length<100) break;
      }
      return collected;
    },
    async listWorkflowJobs(runId) {
      const q=new URLSearchParams({per_page:"100"});
      const data=await getJson(fetchImpl,API+"/repos/"+REPOSITORY+"/actions/runs/"+
        encodeURIComponent(runId)+"/jobs?"+q,{method:"GET",headers:auth});
      return Array.isArray(data.jobs)?data.jobs:[];
    },
    async dispatchWorkflow(file,ref="main") {
      await postNoContent(fetchImpl,API+"/repos/"+REPOSITORY+"/actions/workflows/"+
        encodeURIComponent(file)+"/dispatches",{method:"POST",headers:{...auth,"Content-Type":"application/json"},
          body:JSON.stringify({ref})});
      return {accepted:true,workflow_file:file,ref};
    }
  };
}
export async function verifyGitHubAppAccess(env,fetchImpl=fetch) {
  const client=await createGitHubClient(env,fetchImpl);
  return {ok:true,...client.identity};
}
