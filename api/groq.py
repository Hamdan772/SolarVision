import os
import json
import urllib.request
from http.server import BaseHTTPRequestHandler

GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"


def send_cors_headers(handler):
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type")


class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        send_cors_headers(self)
        self.end_headers()

    def do_POST(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            self.send_response(500)
            send_cors_headers(self)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "GROQ_API_KEY not configured"}).encode())
            return

        try:
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length) if content_length > 0 else b"{}"

            req = urllib.request.Request(GROQ_ENDPOINT, data=body, method="POST")
            req.add_header("Content-Type", "application/json")
            req.add_header("Authorization", f"Bearer {api_key}")

            with urllib.request.urlopen(req, timeout=30) as resp:
                result = resp.read()
                status = resp.getcode()
                resp_headers = resp.headers

            self.send_response(status)
            send_cors_headers(self)
            # forward content-type if present
            self.send_header("Content-Type", resp_headers.get("Content-Type", "application/json"))
            self.end_headers()
            self.wfile.write(result)
        except Exception as e:
            self.send_response(500)
            send_cors_headers(self)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
