from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/api/check', methods=['GET'])
def handler():
    # Propiedad de Javier Gutierrez Adan © 2025
    email = request.args.get('email', 'test@test.com')

    # Lista de correos falsos para detectar fraude
    basura = ["tempmail.com", "yopmail.com", "10minutemail.com"]
    dominio = email.split('@')[-1].lower() if '@' in email else ""

    es_fraude = dominio in basura

    return jsonify({
        "autor": "Javier Gutierrez Adan",
        "copyright": "2025",
        "resultado": "RECHAZAR" if es_fraude else "ACEPTAR",
        "mensaje": "Protegido por FraudShield Pro"
    })
