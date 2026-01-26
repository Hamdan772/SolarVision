#!/usr/bin/env python3
"""
Enhanced HTTP server with CORS proxy for Solar Calculator
Includes proxy endpoint for Overpass API (building detection)
"""

import http.server
import socketserver
import urllib.request
import urllib.parse
import json
from pathlib import Path

PORT = 8000

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
                
                # Validate bbox parameter
                if not bbox:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    error_data = json.dumps({'error': 'Missing bbox parameter. Use /api/overpass?bbox=<south>,<west>,<north>,<east>'})
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
                req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36')
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

if __name__ == '__main__':
    Handler = ProxyRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 Enhanced Solar Calculator Server Running!")
        print(f"📍 Open in browser: http://localhost:{PORT}/solar_advanced.html")
        print(f"🔧 PVGIS Proxy: http://localhost:{PORT}/api/pvgis")
        print(f"🔧 Overpass Proxy: http://localhost:{PORT}/api/overpass")
        print(f"Press Ctrl+C to stop the server")
        httpd.serve_forever()
