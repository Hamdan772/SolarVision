import os
import json
import urllib.request

GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

def handler(request):
    if request['method'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        }

    if request['method'] != 'POST':
        return {
            'statusCode': 405,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Method not allowed'})
        }

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({"error": "GROQ_API_KEY not configured"})
        }

    try:
        body = request.get('body', '{}')
        if isinstance(body, str):
            body = body.encode('utf-8')

        req = urllib.request.Request(GROQ_ENDPOINT, data=body, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Authorization", f"Bearer {api_key}")

        with urllib.request.urlopen(req, timeout=30) as resp:
            result = resp.read()
            status = resp.getcode()
            resp_headers = dict(resp.headers)

        headers = {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': resp_headers.get('Content-Type', 'application/json')
        }

        return {
            'statusCode': status,
            'headers': headers,
            'body': result.decode('utf-8')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': str(e)})
        }
