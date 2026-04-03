#!/bin/bash
# H33 API Examples — cURL
# Get your API key at https://h33.ai/pricing/

API_KEY="${H33_API_KEY:-your_key_here}"
BASE="https://api.h33.ai"

echo "=== Health Check ==="
curl -s "$BASE/health" | python3 -m json.tool

echo -e "\n=== Create DID ==="
curl -s -X POST "$BASE/api/v1/did/create" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $API_KEY" \
  -d '{"label": "primary"}'

echo -e "\n\n=== Enroll Biometric ==="
curl -s -X POST "$BASE/api/v2/biometric/enroll" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $API_KEY" \
  -d "{\"user_id\": \"demo\", \"embedding\": $(python3 -c 'print([0.1]*512)'), \"product\": \"h33\"}"

echo -e "\n\nDone."
