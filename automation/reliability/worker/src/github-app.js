const encoder = new TextEncoder();

function base64Url(bytes) {
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replace(/=/g, "").replace(/\\+/g, "-").replace(/\\//g, "_");
}

function derLength(length) {
  if (length < 128) return Uint8Array.of(length);
  const bytes = [];
  let value = length;
  while (value > 0) {
    bytes.unshift(value & 0xff);
    value >>>= 8;
  }
  return Uint8Array.of(0x80 | bytes.length, ...bytes);
}

function der(tag, content) {
  const length = derLength(content.length);
  const output = new Uint8Array(1 + length.length + content.length);
  output[0] = tag;
  output.set(length, 1);
  output.set(content, 1 + length.length);
  return output;
}

function concatBytes(...parts) {
  const output = new Uint8Array(parts.reduce((sum, part) => sum + part.length, 0));
  let offset = 0;
  for (const part of parts) {
    output.set(part, offset);
    offset += part.length;
  }
  return output;
}

export function pkcs1ToPkcs8(pkcs1) {
  // PrivateKeyInfo(version=0, rsaEncryption OID + NULL, OCTET STRING PKCS#1 key).
  const algorithmIdentifier = Uint8Array.of(
    0x30, 0x0d, 0x06, 0x09, 0x2a, 0x86, 0x48, 0x86,
    0xf7, 0x0d, 0x01, 0x01, 0x01, 0x05, 0x00
  );
  const version = Uint8Array.of(0x02, 0x01, 0x00);
  return der(0x30, concatBytes(version, algorithmIdentifier, der(0x04, pkcs1)));
}

function pemBytes(pem) {
  if (typeof pem !== "string" || !pem.includes("BEGIN RSA PRIVATE KEY")) {
    throw new Error("GitHub App key must be a PEM RSA private key");
  }
  const body = pem.replace(/-----BEGIN RSA PRIVATE KEY-----|-----END RSA PRIVATE KEY-----|\\s/g, "");
  const binary = atob(body);
  return Uint8Array.from(binary, char => char.charCodeAt(0));
}

export async function createAppJwt({ appId, privateKeyPem, now = Date.now(), cryptoImpl = globalThis.crypto }) {
  if (!/^\\d+$/.test(String(appId || ""))) throw new Error("GITHUB_APP_ID must be numeric");
  if (!cryptoImpl?.subtle) throw new Error("Web Crypto is unavailable");
  const header = base64Url(encoder.encode(JSON.stringify({ alg: "RS256", typ: "JWT" })));
  const issuedAt = Math.floor(now / 1000) - 60;
  const payload = base64Url(encoder.encode(JSON.stringify({
    iat: issuedAt,
    exp: issuedAt + 540,
    iss: String(appId)
  })));
  const signingInput = `${header}.${payload}`;
  const key = await cryptoImpl.subtle.importKey(
    "pkcs8",
    pkcs1ToPkcs8(pemBytes(privateKeyPem)),
    { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const signature = await cryptoImpl.subtle.sign(
    "RSASSA-PKCS1-v1_5", key, encoder.encode(signingInput)
  );
  return `${signingInput}.${base64Url(new Uint8Array(signature))}`;
}

async function githubRequest(url, options) {
  const response = await fetch(url, options);
  if (!response.ok) {
    throw new Error(`GitHub API request failed (HTTP ${response.status})`);
  }
  return response.json();
}

export async function verifyGitHubAppAccess(env, fetchImpl = fetch) {
  const appId = String(env.GITHUB_APP_ID || "");
  const installationId = String(env.GITHUB_INSTALLATION_ID || "");
  if (!/^\\d+$/.test(appId)) throw new Error("GITHUB_APP_ID is missing or invalid");
  if (!/^\\d+$/.test(installationId)) throw new Error("GITHUB_INSTALLATION_ID is missing or invalid");
  if (!env.GITHUB_APP_PRIVATE_KEY) throw new Error("GITHUB_APP_PRIVATE_KEY is missing");

  const jwt = await createAppJwt({
    appId,
    privateKeyPem: env.GITHUB_APP_PRIVATE_KEY
  });
  const headers = {
    Accept: "application/vnd.github+json",
    Authorization: `Bearer ${jwt}`,
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "BDIX-IPTV-Reliability-Worker"
  };
  const tokenData = await githubRequest(
    `https://api.github.com/app/installations/${installationId}/access_tokens`,
    { method: "POST", headers }
  );
  if (!tokenData.token) throw new Error("GitHub did not issue an installation token");

  const installationHeaders = {
    ...headers,
    Authorization: `Bearer ${tokenData.token}`
  };
  const repository = await githubRequest(
    "https://api.github.com/repos/saeidrahmanbd/BDIX-IPTV",
    { method: "GET", headers: installationHeaders }
  );
  if (repository.full_name?.toLowerCase() !== "saeidrahmanbd/bdix-iptv") {
    throw new Error("GitHub App installation resolved to an unexpected repository");
  }
  if (tokenData.permissions?.actions !== "write") {
    throw new Error("GitHub installation token does not have Actions write permission");
  }
  return {
    ok: true,
    app_id: appId,
    installation_id: installationId,
    repository: repository.full_name,
    actions_permission: tokenData.permissions.actions
  };
}
