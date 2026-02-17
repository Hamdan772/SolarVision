from http.server import BaseHTTPRequestHandler
import os
import json
import urllib.request
import urllib.error
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("solarvision.groq")

GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
REQUEST_TIMEOUT = 15  # seconds (safe margin for Vercel's 30s limit)
MAX_REQUEST_SIZE = 64 * 1024  # 64KB max request body


class handler(BaseHTTPRequestHandler):
    def _send_json_response(self, status_code, data):
        """Helper to send a JSON response with CORS headers."""
        self.send_response(status_code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_POST(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            logger.error("GROQ_API_KEY not configured")
            self._send_json_response(500, {
                "error": "GROQ_API_KEY not configured. Please add it in Vercel Dashboard > Settings > Environment Variables."
            })
            return

        try:
            # Read and validate request body
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > MAX_REQUEST_SIZE:
                self._send_json_response(413, {"error": "Request body too large"})
                return
            if content_length == 0:
                self._send_json_response(400, {"error": "Empty request body"})
                return

            body = self.rfile.read(content_length)

            # Validate JSON payload
            try:
                request_data = json.loads(body)
            except json.JSONDecodeError:
                self._send_json_response(400, {"error": "Invalid JSON in request body"})
                return

            logger.info("Groq request: model=%s", request_data.get('model', 'unknown'))

            # Forward request to Groq API
            req = urllib.request.Request(
                GROQ_ENDPOINT,
                data=body,
                method="POST"
            )
            req.add_header("Content-Type", "application/json")
            req.add_header("Authorization", f"Bearer {api_key}")
            req.add_header("User-Agent", "SolarVision/1.0")

            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                result = resp.read()
                status = resp.getcode()

            logger.info("Groq response: status=%d", status)

            self._send_json_response(status, json.loads(result))

        except urllib.error.HTTPError as e:
            error_body = ""
            try:
                error_body = e.read().decode('utf-8')
            except Exception:
                error_body = str(e)

            logger.error("Groq API HTTP %d: %s", e.code, error_body[:300])

            error_messages = {
                401: "Invalid API key. Please check your GROQ_API_KEY in Vercel environment variables.",
                403: "API key forbidden or expired. Get a new key at https://console.groq.com/keys",
                429: "Rate limit exceeded. Please wait a moment and try again.",
            }
            message = error_messages.get(e.code, "Upstream AI service error")

            self._send_json_response(e.code, {"error": message, "status": e.code})

        except urllib.error.URLError as e:
            logger.error("Network error contacting Groq: %s", e.reason)
            self._send_json_response(502, {
                "error": "Network error when contacting AI service. Please try again."
            })

        except Exception as e:
            logger.exception("Unexpected error in Groq handler")
            self._send_json_response(500, {
                "error": "Internal server error. Please try again later."
            })
