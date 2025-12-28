from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Propiedad de Javier Gutierrez Adan © 2025
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        email = query_params.get('email', ['test@test.com'])[0]
        
        # Lista de correos falsos para detectar fraude
        basura = ["tempmail.com", "yopmail.com", "10minutemail.com"]
        dominio = email.split('@')[-1].lower() if '@' in email else ""
        
        es_fraude = dominio in basura
        
        response = {
            "autor": "Javier Gutierrez Adan",
            "copyright": "2025",
            "resultado": "RECHAZAR" if es_fraude else "ACEPTAR",
            "mensaje": "Protegido por FraudShield Pro"
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
        return
