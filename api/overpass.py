import urllib.request
import urllib.parse
import json

def handler(request):
    if request['method'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                'Access-Control-Allow-Headers': '*'
            }
        }
    
    if request['method'] != 'GET':
        return {
            'statusCode': 405,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    try:
        query = request.get('query', {})
        bbox = query.get('bbox', [''])[0] if 'bbox' in query else ''
        
        if not bbox:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Missing bbox parameter'})
            }
        
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
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': result.decode('utf-8')
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
