#!/usr/bin/env python3
"""
Test script to verify Groq API connection
"""

import os
import json
import urllib.request
from pathlib import Path

# Load .env file
env_path = Path(__file__).parent / '.env'
if env_path.exists():
    print("📄 Loading .env file...")
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("\n" + "="*60)
print("🧪 Testing Groq API Connection")
print("="*60)

if not GROQ_API_KEY:
    print("❌ ERROR: GROQ_API_KEY not found in environment!")
    print("📝 Create a .env file with: GROQ_API_KEY=your_key_here")
    exit(1)

print(f"✅ API Key found: {GROQ_API_KEY[:20]}...{GROQ_API_KEY[-10:]}")
print(f"📏 Key length: {len(GROQ_API_KEY)} characters")

# Test the API
print("\n🚀 Sending test request to Groq API...")

test_payload = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {
            "role": "user",
            "content": "Say 'Hello from SolarVision!' in exactly 5 words."
        }
    ],
    "temperature": 0.7,
    "max_tokens": 50
}

try:
    GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
    
    req = urllib.request.Request(
        GROQ_ENDPOINT,
        data=json.dumps(test_payload).encode('utf-8'),
        method='POST'
    )
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', f'Bearer {GROQ_API_KEY}')
    req.add_header('User-Agent', 'curl/8.4.0')  # Cloudflare-friendly User-Agent
    req.add_header('Accept', '*/*')
    
    with urllib.request.urlopen(req, timeout=10) as response:
        result = json.loads(response.read().decode('utf-8'))
        
        print("✅ API Connection Successful!")
        print("\n📨 Response:")
        print("-" * 60)
        print(result['choices'][0]['message']['content'])
        print("-" * 60)
        print(f"\n📊 Model: {result.get('model', 'N/A')}")
        print(f"⏱️  Response time: {result.get('usage', {}).get('total_tokens', 'N/A')} tokens")
        print("\n" + "="*60)
        print("✅ Groq API is working correctly!")
        print("="*60)
        
except urllib.error.HTTPError as e:
    error_body = e.read().decode('utf-8')
    print(f"\n❌ HTTP Error {e.code}: {e.reason}")
    print(f"📄 Response: {error_body}")
    
    if e.code == 401:
        print("\n💡 This is likely an authentication error.")
        print("   Please verify your API key at: https://console.groq.com/keys")
    elif e.code == 429:
        print("\n💡 Rate limit exceeded. Wait a moment and try again.")
    
except Exception as e:
    print(f"\n❌ Error: {type(e).__name__}: {e}")
    print("\n💡 Possible issues:")
    print("   - Check your internet connection")
    print("   - Verify the API key is correct")
    print("   - Ensure you have access to api.groq.com")
