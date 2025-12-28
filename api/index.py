from http.server import BaseHTTPRequestHandler
import requests
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Headers CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        # Obtener el parámetro 'text' de la query string
        if '?text=' in self.path:
            text = self.path.split('?text=')[1]
        else:
            response = {'error': 'Falta el parámetro text'}
            self.wfile.write(json.dumps(response).encode())
            return

        # Configurar la API de RapidAPI
        url = "https://twinword-text-analysis-bundle.p.rapidapi.com/analyze/"
        headers = {
            "x-rapidapi-key": os.environ.get('RAPIDAPI_KEY'),
            "x-rapidapi-host": "twinword-text-analysis-bundle.p.rapidapi.com"
        }
        params = {"text": text}

        try:
            # Hacer la petición a RapidAPI
            api_response = requests.get(url, headers=headers, params=params)
            response_data = api_response.json()
            self.wfile.write(json.dumps(response_data).encode())
        except Exception as e:
            error_response = {'error': str(e)}
            self.wfile.write(json.dumps(error_response).encode())
