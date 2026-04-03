/**
 * H33 Biometric Authentication — JavaScript Example
 * Works in Node.js 18+ or browser with fetch API
 */
const API_URL = 'https://api.h33.ai';
const API_KEY = process.env.H33_API_KEY || 'your_key_here';

const headers = {
  'Content-Type': 'application/json',
  'X-API-Key': API_KEY,
};

// Create DID
const did = await fetch(`${API_URL}/api/v1/did/create`, {
  method: 'POST', headers,
  body: JSON.stringify({ label: 'primary' }),
}).then(r => r.json());
console.log('DID:', did.did);

// Enroll biometric (512-D embedding — replace with real data)
const embedding = Array(512).fill(0.1);
const enroll = await fetch(`${API_URL}/api/v2/biometric/enroll`, {
  method: 'POST', headers,
  body: JSON.stringify({ user_id: 'demo', embedding, product: 'h33' }),
}).then(r => r.json());
console.log('Enrolled:', enroll.fhe_encrypted, '| Commitment:', enroll.commitment_hash?.slice(0, 16));

// Verify
const verify = await fetch(`${API_URL}/api/v2/biometric/verify`, {
  method: 'POST', headers,
  body: JSON.stringify({ user_id: 'demo', embedding, product: 'h33' }),
}).then(r => r.json());
console.log('Verified:', verify.verified, '| Similarity:', verify.similarity);
