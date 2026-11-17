import test from "node:test";
import assert from "node:assert/strict";
import {generateKeyPairSync,webcrypto} from "node:crypto";
import {createAppJwt,pkcs1ToPkcs8} from "./github-app.js";
function body(pem){return pem.split("\n").filter(x=>!x.startsWith("-----")).join("");}
function decode(s){return JSON.parse(atob(s.replaceAll("-","+").replaceAll("_","/")));}
test("wraps PKCS#1 RSA key as PKCS#8",()=>{
 const {privateKey}=generateKeyPairSync("rsa",{modulusLength:2048,privateKeyEncoding:{type:"pkcs1",format:"pem"},publicKeyEncoding:{type:"pkcs1",format:"pem"}});
 const raw=Uint8Array.from(atob(body(privateKey)),c=>c.charCodeAt(0));
 const wrapped=pkcs1ToPkcs8(raw); assert.equal(wrapped[0],48); assert.ok(wrapped.length>raw.length);
});
test("creates a verifiable short-lived RS256 App JWT",async()=>{
 const {privateKey,publicKey}=generateKeyPairSync("rsa",{modulusLength:2048,privateKeyEncoding:{type:"pkcs1",format:"pem"},publicKeyEncoding:{type:"spki",format:"pem"}});
 const now=1800000000000;
 const jwt=await createAppJwt({appId:"5794332",privateKeyPem:privateKey,now,cryptoImpl:webcrypto});
 const [h,p,s]=jwt.split(".");
 assert.deepEqual(decode(h),{alg:"RS256",typ:"JWT"});
 assert.equal(decode(p).iss,"5794332"); assert.equal(decode(p).iat,Math.floor(now/1000)-60);
 assert.equal(decode(p).exp-decode(p).iat,540);
 const pub=Buffer.from(body(publicKey),"base64");
 const key=await webcrypto.subtle.importKey("spki",pub,{name:"RSASSA-PKCS1-v1_5",hash:"SHA-256"},false,["verify"]);
 const sig=Uint8Array.from(atob(s.replaceAll("-","+").replaceAll("_","/")),c=>c.charCodeAt(0));
 assert.equal(await webcrypto.subtle.verify("RSASSA-PKCS1-v1_5",key,sig,new TextEncoder().encode(h+"."+p)),true);
});
test("rejects non-numeric App ID",async()=>{
 await assert.rejects(createAppJwt({appId:"bad",privateKeyPem:"bad"}),/GITHUB_APP_ID/);
});

import { verifyGitHubAppAccess } from "./github-app.js";

test("checks only the installed repository and never exposes its token", async () => {
  const { privateKey } = generateKeyPairSync("rsa", {
    modulusLength: 2048,
    privateKeyEncoding: { type: "pkcs1", format: "pem" },
    publicKeyEncoding: { type: "spki", format: "pem" }
  });
  const calls = [];
  const fakeFetch = async (url, options) => {
    calls.push({ url, options });
    if (calls.length === 1) {
      return Response.json({ token: "temporary-installation-token", permissions: { actions: "write" } });
    }
    return Response.json({ full_name: "saeidrahmanbd/BDIX-IPTV" });
  };
  const result = await verifyGitHubAppAccess({
    GITHUB_APP_ID: "5794332",
    GITHUB_INSTALLATION_ID: "182792735",
    GITHUB_APP_PRIVATE_KEY: privateKey
  }, fakeFetch);
  assert.equal(calls.length, 2);
  assert.equal(calls[0].options.method, "POST");
  assert.match(calls[0].url, /app\/installations\/182792735\/access_tokens$/);
  assert.equal(calls[1].url, "https://api.github.com/repos/saeidrahmanbd/BDIX-IPTV");
  assert.equal(calls[1].options.headers.Authorization, "Bearer temporary-installation-token");
  assert.deepEqual(result, {
    ok: true, app_id: "5794332", installation_id: "182792735",
    repository: "saeidrahmanbd/BDIX-IPTV", actions_permission: "write"
  });
  assert.equal(JSON.stringify(result).includes("temporary-installation-token"), false);
});

test("rejects an installation token without Actions write permission", async () => {
  const { privateKey } = generateKeyPairSync("rsa", {
    modulusLength: 2048,
    privateKeyEncoding: { type: "pkcs1", format: "pem" },
    publicKeyEncoding: { type: "spki", format: "pem" }
  });
  let calls = 0;
  const fakeFetch = async () => {
    calls += 1;
    if (calls === 1) return Response.json({ token: "temporary-token", permissions: { actions: "read" } });
    return Response.json({ full_name: "saeidrahmanbd/BDIX-IPTV" });
  };
  await assert.rejects(verifyGitHubAppAccess({
    GITHUB_APP_ID: "5794332",
    GITHUB_INSTALLATION_ID: "182792735",
    GITHUB_APP_PRIVATE_KEY: privateKey
  }, fakeFetch), /Actions write permission/);
});
