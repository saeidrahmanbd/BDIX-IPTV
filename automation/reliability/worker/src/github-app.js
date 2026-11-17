const encoder = new TextEncoder();
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
  const len = derLength(content.length);
  const out = new Uint8Array(1 + len.length + content.length);
  out[0] = tag; out.set(len, 1); out.set(content, 1 + len.length); return out;
}
function join(...parts) {
  const out = new Uint8Array(parts.reduce((n, p) => n + p.length, 0));
  let offset = 0;
  for (const part of parts) { out.set(part, offset); offset += part.length; }
  return out;
}
export function pkcs1ToPkcs8(pkcs1) {
  const algorithm = Uint8Array.of(48,13,6,9,42,134,72,134,247,13,1,1,1,5,0);
  return der(48, join(Uint8Array.of(2,1,0), algorithm, der(4, pkcs1)));
}
function pemBytes(pem) {
  if (typeof pem !== "string" || !pem.includes("BEGIN RSA PRIVATE KEY")) throw new Error("GitHub App key must be a PEM RSA private key");
  const body = pem.split("\n").filter(line => !line.startsWith("-----")).join("").replaceAll(" ", "").replaceAll("\r", "");
  return Uint8Array.from(atob(body), c => c.charCodeAt(0));
}
function numeric(value) {
  const s = String(value || "");
  return s.length > 0 && [...s].every(c => c >= "0" && c <= "9");
}
export async function createAppJwt({appId, privateKeyPem, now = Date.now(), cryptoImpl = globalThis.crypto}) {
  if (!numeric(appId)) throw new Error("GITHUB_APP_ID must be numeric");
  if (!cryptoImpl?.subtle) throw new Error("Web Crypto is unavailable");
  const header = b64url(encoder.encode(JSON.stringify({alg:"RS256",typ:"JWT"})));
  const iat = Math.floor(now / 1000) - 60;
  const payload = b64url(encoder.encode(JSON.stringify({iat,exp:iat+540,iss:String(appId)})));
  const input = header + "." + payload;
  const key = await cryptoImpl.subtle.importKey("pkcs8", pkcs1ToPkcs8(pemBytes(privateKeyPem)),
    {name:"RSASSA-PKCS1-v1_5",hash:"SHA-256"}, false, ["sign"]);
  const signature = await cryptoImpl.subtle.sign("RSASSA-PKCS1-v1_5", key, encoder.encode(input));
  return input + "." + b64url(new Uint8Array(signature));
}
async function requestJson(fetchImpl, url, options) {
  const response = await fetchImpl(url, options);
  if (!response.ok) throw new Error("GitHub API request failed (HTTP " + response.status + ")");
  return response.json();
}
export async function verifyGitHubAppAccess(env, fetchImpl = fetch) {
  const appId = String(env.GITHUB_APP_ID || "");
  const installationId = String(env.GITHUB_INSTALLATION_ID || "");
  if (!numeric(appId)) throw new Error("GITHUB_APP_ID is missing or invalid");
  if (!numeric(installationId)) throw new Error("GITHUB_INSTALLATION_ID is missing or invalid");
  if (!env.GITHUB_APP_PRIVATE_KEY) throw new Error("GITHUB_APP_PRIVATE_KEY is missing");
  const jwt = await createAppJwt({appId,privateKeyPem:env.GITHUB_APP_PRIVATE_KEY});
  const headers = {Accept:"application/vnd.github+json",Authorization:"Bearer " + jwt,
    "X-GitHub-Api-Version":"2022-11-28","User-Agent":"BDIX-IPTV-Reliability-Worker"};
  const token = await requestJson(fetchImpl,
    "https://api.github.com/app/installations/" + installationId + "/access_tokens",
    {method:"POST",headers});
  if (!token.token) throw new Error("GitHub did not issue an installation token");
  const repo = await requestJson(fetchImpl,"https://api.github.com/repos/saeidrahmanbd/BDIX-IPTV",
    {method:"GET",headers:{...headers,Authorization:"Bearer " + token.token}});
  if (String(repo.full_name || "").toLowerCase() !== "saeidrahmanbd/bdix-iptv")
    throw new Error("GitHub App installation resolved to an unexpected repository");
  if (!token.permissions || token.permissions.actions !== "write")
    throw new Error("GitHub installation token does not have Actions write permission");
  return {ok:true,app_id:appId,installation_id:installationId,repository:repo.full_name,actions_permission:token.permissions.actions};
}
