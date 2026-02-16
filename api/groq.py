from http.server import BaseHTTPRequestHandler
import os
import json
import urllib.request
import urllib.error
import traceback

GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_POST(self):
        api_key = os.getenv("GROQ_API_KEY")
        
        # Log for debugging (first 10 chars only)
        print(f"API Key present: {bool(api_key)}, starts with: {api_key[:10] if api_key else 'N/A'}")
        
        if not api_key:
            self.send_response(500)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "error": "GROQ_API_KEY not configured in Vercel environment variables. Please add it in Vercel Dashboard → Settings → Environment Variables."
            }).encode())
            return

        try:
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            
            # Parse and validate request
            try:
                request_data = json.loads(body)
                print(f"Request model: {request_data.get('model', 'unknown')}")
            except:
                pass

            # Forward request to Groq API
            req = urllib.request.Request(
                GROQ_ENDPOINT,
                data=body,
                method="POST"
            )
            req.add_header("Content-Type", "application/json")
            req.add_header("Authorization", f"Bearer {api_key}")
            req.add_header("User-Agent", "SolarVision/1.0")

            print(f"Sending request to Groq API...")
            
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = resp.read()
                status = resp.getcode()
                print(f"Groq API response: {status}")

            # Send success response
            self.send_response(status)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(result)

        except urllib.error.HTTPError as e:
            # Handle HTTP errors from Groq API
            try:
                error_body = e.read().decode('utf-8')
            except Exception:
                error_body = str(e)
            print(f"Groq API HTTPError {e.code}: {error_body[:200]}")
            
            # Provide helpful error messages
            if e.code == 403:
                error_response = {
                    "error": "API key forbidden. Please verify your Groq API key is valid and has not expired. Get a new key at https://console.groq.com/keys",
                    "status": 403,
                    "details": error_body
                }
                error_body = json.dumps(error_response)
            elif e.code == 401:
                error_response = {
                    "error": "Invalid API key. Please check your GROQ_API_KEY in Vercel environment variables.",
                    "status": 401
                }
                error_body = json.dumps(error_response)
            
            self.send_response(e.code)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            # Ensure the client receives valid JSON
            try:
                # If error_body is already JSON text, pass it through
                json.loads(error_body)
                payload = error_body
            except Exception:
                payload = json.dumps({
                    "error": "Upstream API error",
                    "status": e.code,
                    "details": error_body
                })
            self.wfile.write(payload.encode())

        except urllib.error.URLError as e:
            # Network-level errors (DNS, connection refused, timeouts)
            print(f"URLError when contacting Groq: {e}")
            self.send_response(502)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "error": "Network error when contacting Groq API",
                "details": str(e)
            }).encode())

        except Exception as e:
            # Handle other unexpected errors and print traceback
            tb = traceback.format_exc()
            print(f"Internal error: {str(e)}\n{tb}")
            self.send_response(500)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "error": "Internal server error",
                "details": str(e),
                "traceback": tb[:2000]
            }).encode())
