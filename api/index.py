from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def analyze_text():
    # Get 'text' parameter from query string
    text = request.args.get('text')
    
    if not text:
        return jsonify({'error': 'Falta el parámetro text'}), 400
    
    # Configure RapidAPI request
    url = "https://twinword-text-analysis-bundle.p.rapidapi.com/analyze/"
    headers = {
        "x-rapidapi-key": os.environ.get('RAPIDAPI_KEY', ''),
        "x-rapidapi-host": "twinword-text-analysis-bundle.p.rapidapi.com"
    }
    params = {"text": text}
    
    try:
        # Make request to RapidAPI
        api_response = requests.get(url, headers=headers, params=params, timeout=10)
        return jsonify(api_response.json()), api_response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
