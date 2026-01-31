#!/usr/bin/env python3
"""
Enhanced Local HTTP Server for SolarVision
Includes proxies for Overpass API and Groq AI
"""

import http.server
import socketserver
import urllib.request
import urllib.parse
import json
import os
from pathlib import Path

PORT = 8000

# Load .env file if it exists
env_path = Path(__file__).parent / '.env'
if env_path.exists():
    print("📄 Loading environment variables from .env file...")
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()
    print("✅ Environment variables loaded successfully")
else:
    print("⚠️  No .env file found - using environment variables")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY or GROQ_API_KEY == "YOUR_GROQ_API_KEY_HERE":
    print("❌ ERROR: GROQ_API_KEY not found!")
    print("📝 Please create a .env file with: GROQ_API_KEY=your_key_here")
    exit(1)
else:
    print(f"✅ Groq API Key loaded: {GROQ_API_KEY[:20]}...")

GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

class ProxyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def do_GET(self):
        # Proxy endpoint for Overpass API
        if self.path.startswith('/api/overpass'):
            try:
                query = urllib.parse.urlparse(self.path).query
                params = urllib.parse.parse_qs(query)
                
                bbox = params.get('bbox', [''])[0]
                
                if not bbox:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    error_data = json.dumps({'error': 'Missing bbox parameter'})
                    self.wfile.write(error_data.encode())
                    return
                
                overpass_query = f"""
                [out:json][timeout:25];
                (
                    way["building"]({bbox});
                    relation["building"]({bbox});
                );
                out geom;
                """
                
                print(f"📡 Proxying Overpass request for bbox: {bbox}")
                
                overpass_url = "https://overpass-api.de/api/interpreter"
                data = overpass_query.encode()
                
                req = urllib.request.Request(overpass_url, data=data, method='POST')
                req.add_header('User-Agent', 'Mozilla/5.0')
                req.add_header('Content-Type', 'application/x-www-form-urlencoded')
                
                with urllib.request.urlopen(req, timeout=30) as response:
                    result = response.read()
                
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(result)
                
            except Exception as e:
                print(f"❌ Overpass Proxy Error: {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                error_data = json.dumps({'error': str(e)})
                self.wfile.write(error_data.encode())
        
        else:
            # Serve static files normally
            super().do_GET()
    
    def do_POST(self):
        # Proxy endpoint for Groq AI API
        if self.path.startswith('/api/groq'):
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length)
                
                print(f"🤖 Proxying Groq AI request...")
                print(f"📦 Request size: {content_length} bytes")
                
                # Parse the request to validate
                try:
                    request_data = json.loads(body.decode('utf-8'))
                    print(f"📝 Model: {request_data.get('model', 'N/A')}")
                except Exception as parse_err:
                    print(f"⚠️  Could not parse request: {parse_err}")
                    request_data = {}
                
                # Create request with proper headers to avoid Cloudflare blocking
                req = urllib.request.Request(GROQ_ENDPOINT, data=body, method='POST')
                req.add_header('Content-Type', 'application/json')
                req.add_header('Authorization', f'Bearer {GROQ_API_KEY}')
                req.add_header('User-Agent', 'curl/8.4.0')  # Cloudflare-friendly User-Agent
                req.add_header('Accept', '*/*')
                req.add_header('Connection', 'keep-alive')
                
                try:
                    with urllib.request.urlopen(req, timeout=30) as response:
                        result = response.read()
                        status = response.getcode()
                    
                    print(f"✅ Groq API success! Status: {status}")
                    self.send_response(status)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(result)
                    
                except urllib.error.HTTPError as http_err:
                    # Log the detailed error
                    error_body = http_err.read().decode('utf-8') if http_err.fp else str(http_err)
                    print(f"❌ Groq API HTTP Error {http_err.code}: {error_body}")
                    
                    if http_err.code == 403:
                        print("💡 Cloudflare blocking detected - trying alternative approach...")
                    
                    # Return error to frontend
                    self.send_response(http_err.code)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    
                    error_response = {
                        "error": {
                            "message": f"Groq API Error: {error_body}",
                            "type": "api_error",
                            "code": http_err.code
                        }
                    }
                    self.wfile.write(json.dumps(error_response).encode())
                
            except Exception as e:
                print(f"❌ Groq Proxy Error: {type(e).__name__}: {e}")
                
                # Return error response
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                
                error_response = {
                    "error": {
                        "message": str(e),
                        "type": "server_error"
                    }
                }
                self.wfile.write(json.dumps(error_response).encode())
        else:
            self.send_response(405)
            self.end_headers()

if __name__ == '__main__':
    Handler = ProxyRequestHandler
    
    # Change to the project directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("=" * 60)
        print("🚀 SolarVision Local Server Running!")
        print("=" * 60)
        print(f"📍 Main App: http://localhost:{PORT}/solar_advanced.html")
        print(f"📍 Landing Page: http://localhost:{PORT}/index.html")
        print(f"🔧 Overpass API Proxy: http://localhost:{PORT}/api/overpass")
        print(f"🤖 Groq AI Proxy: http://localhost:{PORT}/api/groq")
        print("=" * 60)
        print(f"✅ All features enabled with NASA POWER data + AI")
        print(f"Press Ctrl+C to stop the server")
        print("=" * 60)
        httpd.serve_forever()
