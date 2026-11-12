# Cryptographic implementation and TLS

Cryptographic security depends on the intended property, threat model, algorithm/mode, protocol and library versions, key/nonce lifecycle, message encoding, validation order and observable error channel. Nonce reuse under the same key, an observable verification oracle, a reachable weak key source and a missing identity check have different preconditions. Ciphertext appearance, a small RSA exponent or an error difference alone does not establish any of them.

Randomness, nonce uniqueness, authenticated-encryption use, signature/MAC verification, canonicalization, padding/error behavior, certificate/hostname validation, trust-store scope, downgrade handling and key separation protect different properties. Weak configuration, a reachable cryptographic primitive and demonstrated impact are distinct claims.

## Primitive assumptions and false positives

The following constructions have distinct preconditions and failure modes.

| Construction or signal | Preconditions and limits |
| --- | --- |
| CBC padding oracle | Requires reachable chosen-ciphertext decryption and a distinguishable padding-valid outcome. Padding, length, parse, MAC and rate-limit errors can have different meanings. Correct integrity verification before decryption can remove this oracle; ciphertext plus IV alone cannot demonstrate it. |
| ECB block patterns | Repeated aligned blocks suggest deterministic block encryption, not plaintext recovery. Cut-and-paste needs predictable field alignment and acceptance without independent integrity. Byte-at-a-time recovery additionally needs a stable same-key oracle and controllable placement relative to the secret. |
| Secret-prefix hash MAC | For `H(secret || message)`, length extension concerns state-exposing Merkle–Damgård hashes such as MD5/SHA-1/SHA-256, exposed digest state and accepted glue padding. It is not an attack on HMAC or SHA-3. Byte lengths, encoding and the content actually authenticated determine whether the construction has that property. |
| RSA | A small public exponent alone is insufficient. Unpadded short-message roots require the relevant bound, such as `m^e < n`; broadcast recovery needs compatible encoded messages and suitable moduli/bounds. Shared factors require a nontrivial gcd. Padding-oracle claims need observable validity under the actual padding scheme. |
| GCM/stream nonce reuse | Relevant reuse involves the same key and actual nonce. Reused keystream reveals XOR relations over overlapping plaintext bytes, not automatically both plaintexts or the encryption key. GCM tag/forgery claims also depend on AAD, lengths, tag truncation and independent validation. |
| Randomness and passwords | Prediction needs the actual generator, seed/state exposure, output layout and intervening draws; statistical patterns do not establish CSPRNG state recovery. Distinct per-record salts prevent amortizing precomputation across records; reused salts do not. Password-KDF cost raises per-guess work. Neither replaces secret entropy. Appropriate costs depend on current requirements and resource constraints; a historical iteration count is not universal. |
| Signatures and MACs | Validity depends on the exact encoded message, key purpose and algorithm parameters. Verifier/consumer disagreement can preserve a valid signature over a different interpreted meaning. A MAC-comparison timing signal can expose information about tags; it does not directly reveal the HMAC secret character by character. |

Partially known variables and root-based recovery depend on the original integer or modular equation and the positions of known bits. Substitution or scaling changes the reduced variable's domain; a bound on the original variable does not automatically hold for the transformed one. A reconstructed candidate remains subject to the original relation, even when its output has a readable prefix.

Authenticated-encryption integrity depends on rejecting unverified plaintext; nonce allocation must account for restart, concurrency, cloning and key rotation. Random nonce collision risk depends on the nonce space and total same-key use; a short sample without duplicates does not prove lifetime uniqueness. Key separation must distinguish purposes and protocols, not merely source labels. Constant-time verification APIs address comparison leakage, while application timing differences may instead originate in parsing, cache state or error handling.

## TLS identity, termination and replay

TLS behavior depends on endpoint, SNI/ALPN, client/server role and termination leg. Chain trust, validity period, key usage/EKU, reference-identity/hostname matching and application identity mapping are distinct. A trusted chain does not establish the intended peer; suppressing a warning does not establish that verification was disabled. A root store, hostname override or hook changes the tested environment. For mTLS, certificate validation and proof of private-key possession precede application authorization; copying a public certificate is not authentication. Forwarded certificate metadata is authoritative only through an authenticated proxy path that removes untrusted caller copies.

Protocol support, actual negotiation and downgrade resistance are different observations. Deprecated-version support or a scanner label does not establish a named exploit; applicability depends on implementation/build, role and relevant record/handshake preconditions. For 0-RTT, early-data acceptance and replayable application impact are distinct; duplicate effects depend on the deployed anti-replay/idempotency policy. Compression side channels require a secret and chosen input in a relevant shared compression context, observable lengths and sufficient noise control; gzip or reflection alone is not a working oracle. HSTS depends on browser state, preload/scope and the initial request path, not only a response header. Version-dependent defaults and feature availability require actual configuration or current primary documentation.

A timing or other side channel requires an observable signal whose distribution can be distinguished under the relevant control variables and noise conditions. One latency difference does not establish exploitable leakage.

Maintained cryptographic libraries and protocol specifications define supported interfaces, current defaults, deprecations and interoperability requirements. A new primitive does not repair incorrect protocol use.
