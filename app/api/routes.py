from flask import Flask, request, jsonify
from app.utils.prompt_utils import process_parameters

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def handle_request():
    parameters = request.get_json()
    response = process_parameters(parameters)
    return jsonify(response)