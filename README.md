# H33 Integration Examples

Sample code for integrating H33's post-quantum authentication API.

## Quick Start

```bash
# Get a free API key at https://h33.ai/pricing/
export H33_API_KEY="your_key_here"

# Run any example
cd python && python enroll_and_verify.py
```

## Examples

| Language | File | Description |
|----------|------|-------------|
| Python | `python/enroll_and_verify.py` | Full enrollment + FHE verification flow |
| Python | `python/encrypted_search.py` | Search encrypted data without decrypting |
| JavaScript | `javascript/biometric_auth.mjs` | Browser biometric enrollment with FHE |
| JavaScript | `javascript/verify_hics_score.mjs` | Verify a HICS attestation by Proof ID |
| Rust | `rust/src/main.rs` | Native Rust client with Dilithium verification |
| Go | `go/main.go` | Go client for batch authentication |
| cURL | `curl/examples.sh` | Raw HTTP examples for any language |

## What the API Does

One API call runs the full post-quantum pipeline:

1. Your biometric → FHE encrypted (never plaintext on server)
2. Matching happens on encrypted data (homomorphic computation)
3. STARK proof attests the result is correct
4. Dilithium ML-DSA-65 signs the attestation (quantum-resistant)
5. 3-of-5 threshold decryption (no single server holds the key)

**Result:** You know if the biometric matched. The server never saw the biometric.

## Links

- [API Docs](https://h33.ai/docs/api/)
- [Live Demo](https://h33.ai/demo/live-fhe/)
- [Pricing](https://h33.ai/pricing/)
- [HICS Specification](https://github.com/H33ai-postquantum/h33-hics-specification)

---

**H33 Products:** [H33-74](https://h33.ai) · [Auth1](https://auth1.ai) · [Chat101](https://chat101.ai) · [Cachee](https://cachee.ai) · [Z101](https://z101.ai) · [RevMine](https://revmine.ai) · [BotShield](https://h33.ai/botshield)

*Introducing H33-74. 74 bytes. Any computation. Post-quantum attested. Forever.*


---

## H33 Product Suite

| Product | Description |
|---------|-------------|
| [H33.ai](https://h33.ai) | Post-quantum security infrastructure |
| [V100.ai](https://v100.ai) | AI Video API — 20 Rust microservices, post-quantum encrypted |
| [Auth1.ai](https://auth1.ai) | Multi-tenant auth without Auth0 |
| [Chat101.ai](https://chat101.ai) | AI chat widget with Rust gateway sidecar |
| [Cachee.ai](https://cachee.ai) | Sub-microsecond PQ-attested cache |
| [Z101.ai](https://z101.ai) | 20+ SaaS products on one backend |
| [RevMine.ai](https://revmine.ai) | Revenue intelligence platform |
| [BotShield](https://h33.ai/botshield) | Free CAPTCHA replacement |

*Introducing H33-74. 74 bytes. Any computation. Post-quantum attested. Forever.*
