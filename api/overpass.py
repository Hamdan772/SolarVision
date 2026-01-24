from http.server import BaseHTTPRequestHandler
import urllib.request
import urllib.parse
import json

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()
    
    def do_GET(self):
        try:
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            
            bbox = params.get('bbox', [''])[0]
            
            if not bbox:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
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
            
            overpass_url = "https://overpass-api.de/api/interpreter"
            data = overpass_query.encode()
            
            req = urllib.request.Request(overpass_url, data=data, method='POST')
            req.add_header('User-Agent', 'Mozilla/5.0 (compatible; SolarVision/1.0)')
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            
            with urllib.request.urlopen(req, timeout=30) as response:
                result = response.read()
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(result)
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error_data = json.dumps({'error': str(e)})
            self.wfile.write(error_data.encode())
