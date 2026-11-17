import test from "node:test";
import assert from "node:assert/strict";
import {generateKeyPairSync,webcrypto} from "node:crypto";
import {createAppJwt,pkcs1ToPkcs8,createGitHubClient,verifyGitHubAppAccess} from "./github-app.js";
function body(pem){return pem.split("\n").filter(x=>!x.startsWith("-----")).join("");}
function keyPair(){return generateKeyPairSync("rsa",{modulusLength:2048,
  privateKeyEncoding:{type:"pkcs1",format:"pem"},publicKeyEncoding:{type:"spki",format:"pem"}});}
function decode(s){return JSON.parse(atob(s.replaceAll("-","+").replaceAll("_","/")));}
test("PKCS#1 RSA key wraps into PKCS#8",()=>{
  const {privateKey}=keyPair(), raw=Uint8Array.from(atob(body(privateKey)),c=>c.charCodeAt(0));
  assert.equal(pkcs1ToPkcs8(raw)[0],48);
});
test("App JWT signs with RS256 and a short lifetime",async()=>{
  const {privateKey,publicKey}=keyPair(), now=1800000000000;
  const jwt=await createAppJwt({appId:"5794332",privateKeyPem:privateKey,now,cryptoImpl:webcrypto});
  const [h,p,s]=jwt.split(".");
  assert.deepEqual(decode(h),{alg:"RS256",typ:"JWT"});
  assert.equal(decode(p).iss,"5794332"); assert.equal(decode(p).exp-decode(p).iat,540);
  const pub=Buffer.from(body(publicKey),"base64");
  const key=await webcrypto.subtle.importKey("spki",pub,{name:"RSASSA-PKCS1-v1_5",hash:"SHA-256"},false,["verify"]);
  const sig=Uint8Array.from(atob(s.replaceAll("-","+").replaceAll("_","/")),c=>c.charCodeAt(0));
  assert.equal(await webcrypto.subtle.verify("RSASSA-PKCS1-v1_5",key,sig,new TextEncoder().encode(h+"."+p)),true);
});
test("invalid App ID is rejected",async()=>{
  await assert.rejects(createAppJwt({appId:"bad",privateKeyPem:"bad"}),/GITHUB_APP_ID/);
});
test("App access verifies only the installed repository and hides token",async()=>{
  const {privateKey}=keyPair(), calls=[];
  const fake=async(url,options)=>{calls.push({url,options});return calls.length===1
    ?Response.json({token:"secret-token",permissions:{actions:"write"}})
    :Response.json({full_name:"saeidrahmanbd/BDIX-IPTV"});};
  const result=await verifyGitHubAppAccess({GITHUB_APP_ID:"5794332",GITHUB_INSTALLATION_ID:"182792735",
    GITHUB_APP_PRIVATE_KEY:privateKey},fake);
  assert.equal(result.ok,true); assert.equal(result.repository,"saeidrahmanbd/BDIX-IPTV");
  assert.equal(JSON.stringify(result).includes("secret-token"),false);
  assert.equal(calls.length,2);
});
test("installation without Actions write permission is rejected",async()=>{
  const {privateKey}=keyPair(); let count=0;
  const fake=async()=>{count++;return Response.json(count===1
    ?{token:"x",permissions:{actions:"read"}}:{full_name:"saeidrahmanbd/BDIX-IPTV"});};
  await assert.rejects(verifyGitHubAppAccess({GITHUB_APP_ID:"5794332",GITHUB_INSTALLATION_ID:"182792735",
    GITHUB_APP_PRIVATE_KEY:privateKey},fake),/Actions write permission/);
});
test("GitHub client scopes run, job and dispatch calls to this repository",async()=>{
  const {privateKey}=keyPair(), calls=[];
  const fake=async(url,options)=>{
    calls.push({url,options});
    if(url.endsWith("/access_tokens"))return Response.json({token:"temporary",permissions:{actions:"write"}});
    if(url.endsWith("/repos/saeidrahmanbd/BDIX-IPTV"))return Response.json({full_name:"saeidrahmanbd/BDIX-IPTV"});
    if(url.includes("/runs?")&&url.includes("created=2026-11-13..2026-11-19"))return Response.json({workflow_runs:[{id:7}]});
    if(url.endsWith("/actions/runs/7/jobs?per_page=100"))return Response.json({jobs:[{name:"maintain",conclusion:"success"}]});
    if(url.endsWith("/actions/workflows/iptv-maintenance.yml/dispatches"))return new Response(null,{status:204});
    throw new Error("Unexpected URL "+url);
  };
  const client=await createGitHubClient({GITHUB_APP_ID:"5794332",GITHUB_INSTALLATION_ID:"182792735",
    GITHUB_APP_PRIVATE_KEY:privateKey},fake);
  assert.equal((await client.listWorkflowRuns("iptv-maintenance.yml","2026-11-13","2026-11-19"))[0].id,7);
  assert.equal((await client.listWorkflowJobs(7))[0].name,"maintain");
  assert.equal((await client.dispatchWorkflow("iptv-maintenance.yml","main")).accepted,true);
  assert.equal(calls.at(-1).options.method,"POST");
  assert.deepEqual(JSON.parse(calls.at(-1).options.body),{ref:"main"});
});
