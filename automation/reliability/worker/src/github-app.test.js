import test from "node:test";
import assert from "node:assert/strict";
import { generateKeyPairSync, webcrypto } from "node:crypto";
import { createAppJwt, pkcs1ToPkcs8 } from "./github-app.js";

test("wraps a PKCS#1 RSA key as valid PKCS#8", () => {
  const { privateKey } = generateKeyPairSync("rsa", {
    modulusLength: 2048,
    privateKeyEncoding: { type: "pkcs1", format: "pem" },
    publicKeyEncoding: { type: "pkcs1", format: "pem" }
  });
  const body = privateKey.replace(/-----[^-]+-----|\\s/g, "");
  const der = Uint8Array.from(atob(body), c => c.charCodeAt(0));
  const wrapped = pkcs1ToPkcs8(der);
  assert.equal(wrapped[0], 0x30);
  assert.ok(wrapped.length > der.length);
});

test("creates a verifiable short-lived RS256 GitHub App JWT", async () => {
  const { privateKey, publicKey } = generateKeyPairSync("rsa", {
    modulusLength: 2048,
    privateKeyEncoding: { type: "pkcs1", format: "pem" },
    publicKeyEncoding: { type: "spki", format: "pem" }
  });
  const now = 1_800_000_000_000;
  const jwt = await createAppJwt({
    appId: "5794332",
    privateKeyPem: privateKey,
    now,
    cryptoImpl: webcrypto
  });
  const [headerPart, payloadPart, signaturePart] = jwt.split(".");
  const decode = part => JSON.parse(atob(part.replace(/-/g, "+").replace(/_/g, "/")));
  assert.deepEqual(decode(headerPart), { alg: "RS256", typ: "JWT" });
  assert.equal(decode(payloadPart).iss, "5794332");
  assert.equal(decode(payloadPart).iat, Math.floor(now / 1000) - 60);
  assert.equal(decode(payloadPart).exp - decode(payloadPart).iat, 540);
  const publicDer = Buffer.from(publicKey.replace(/-----[^-]+-----|\\s/g, ""), "base64");
  const verifyKey = await webcrypto.subtle.importKey(
    "spki", publicDer, { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["verify"]
  );
  const signature = Uint8Array.from(atob(signaturePart.replace(/-/g, "+").replace(/_/g, "/")), c => c.charCodeAt(0));
  assert.equal(await webcrypto.subtle.verify(
    "RSASSA-PKCS1-v1_5", verifyKey, signature,
    new TextEncoder().encode(`${headerPart}.${payloadPart}`)
  ), true);
});

test("rejects non-numeric App IDs", async () => {
  await assert.rejects(
    createAppJwt({ appId: "not-an-id", privateKeyPem: "not-a-key" }),
    /GITHUB_APP_ID/
  );
});
