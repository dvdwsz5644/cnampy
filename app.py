from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# Telebroad API credentials
TELEBROAD_API_URL = "https://webserv.telebroad.com/api/teleconsole/rest/cnam?number="

import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


@app.route('/lookup', methods=['GET'])
def lookup_number():
    phone_number = request.args.get('number')
    if not phone_number:
        return jsonify({"error": "Phone number is required"}), 400
    
    try:
        response = requests.get(TELEBROAD_API_URL + phone_number, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        response_data = response.json()
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": "Failed to fetch data", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
