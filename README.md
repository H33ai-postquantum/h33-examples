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
