from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import requests
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query_start = self.path.find('?')
        if query_start != -1:
            query_string = self.path[query_start + 1:]
            params = parse_qs(query_string)
        else:
            params = {}
        
        # CORS headers
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        # Get 'text' parameter
        if 'text' not in params:
            response = {'error': 'Falta el parámetro text'}
            self.wfile.write(json.dumps(response).encode())
            return
        
        text = params['text'][0]
        
        # Configure RapidAPI request
        url = "https://twinword-text-analysis-bundle.p.rapidapi.com/analyze/"
        headers = {
            "x-rapidapi-key": os.environ.get('RAPIDAPI_KEY', ''),
            "x-rapidapi-host": "twinword-text-analysis-bundle.p.rapidapi.com"
        }
        api_params = {"text": text}
        
        try:
            # Make request to RapidAPI
            api_response = requests.get(url, headers=headers, params=api_params, timeout=10)
            response_data = api_response.json()
            self.wfile.write(json.dumps(response_data).encode())
        except Exception as e:
            error_response = {'error': str(e)}
            self.wfile.write(json.dumps(error_response).encode())
