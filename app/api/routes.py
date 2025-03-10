from flask import jsonify, request
from app.api import api_bp
from app.utils.prompt_utils import process_parameters

@api_bp.route('/prompt', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        parameters = request.get_json()
        response = process_parameters(parameters)
        return jsonify(response)
    
    # GETリクエストの場合
    return jsonify({
        "message": "Please use POST method with JSON parameters",
        "example": {
            "mood": "casual/humorous/cool",
            "length": 1.0
        }
    })

# エラーハンドリングの追加
@api_bp.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        "error": "Method Not Allowed",
        "message": "This endpoint only accepts POST requests"
    }), 405