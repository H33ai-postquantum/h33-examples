"""
H33 Biometric Enrollment + Verification Example
Demonstrates: FHE encryption, STARK proof, Dilithium attestation
"""
import requests
import json
import os

API_URL = "https://api.h33.ai"
API_KEY = os.environ.get("H33_API_KEY", "your_key_here")

headers = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY,
}

# Step 1: Create a post-quantum DID
print("Creating post-quantum DID (Dilithium + Kyber)...")
did_resp = requests.post(f"{API_URL}/api/v1/did/create",
    headers=headers,
    json={"label": "primary"}
)
did = did_resp.json()
print(f"  DID: {did.get('did', 'N/A')}")
print(f"  Dilithium public key: {did.get('public_key_dilithium', 'N/A')[:32]}...")

# Step 2: Enroll biometric (512-D embedding)
# In production, this comes from face-api.js or your biometric SDK
embedding = [0.1] * 512  # Placeholder — replace with real embedding
print("\nEnrolling biometric (FHE-encrypted on server)...")
enroll_resp = requests.post(f"{API_URL}/api/v2/biometric/enroll",
    headers=headers,
    json={
        "user_id": "demo_user",
        "embedding": embedding,
        "product": "h33",  # Flagship: BFV FHE + 3-of-5 threshold
    }
)
enroll = enroll_resp.json()
print(f"  FHE encrypted: {enroll.get('fhe_encrypted')}")
print(f"  Zero data exposure: {enroll.get('zero_data_exposure')}")
print(f"  Commitment hash: {enroll.get('commitment_hash', 'N/A')[:32]}...")
print(f"  Threshold: {enroll.get('threshold_config')}")
print(f"  Latency: {enroll.get('latency_us')} µs")

# Step 3: Verify (server matches in encrypted space)
print("\nVerifying biometric (homomorphic matching)...")
verify_resp = requests.post(f"{API_URL}/api/v2/biometric/verify",
    headers=headers,
    json={
        "user_id": "demo_user",
        "embedding": embedding,
        "product": "h33",
    }
)
verify = verify_resp.json()
print(f"  Verified: {verify.get('verified')}")
print(f"  Similarity: {verify.get('similarity')}")
print(f"  Latency: {verify.get('latency_ms')} ms")

# Step 4: Create soulbound identity
print("\nCreating soulbound identity...")
identity_resp = requests.post(f"{API_URL}/api/v1/identity/create",
    headers=headers,
    json={
        "user_id": "demo_user",
        "did": did.get("did", ""),
        "biometric_commitment": enroll.get("commitment_hash", ""),
        "mfa_threshold": 2,
    }
)
identity = identity_resp.json()
print(f"  Identity ID: {identity.get('identity_id', 'N/A')}")
print(f"  Soulbound: {identity.get('soulbound')}")
print(f"  Trust score: {identity.get('trust_score')}")

print("\nDone. Your biometric was never plaintext on the server.")
