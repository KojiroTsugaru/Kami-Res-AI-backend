from flask import jsonify, request
from app.api import api_bp
from app.utils.prompt_utils import process_parameters

@api_bp.route('/prompt', methods=['POST'])
def handle_request():
    try:
        if request.method == 'POST':
            parameters = request.get_json()
            if not parameters:
                return jsonify({
                    "status": "error",
                    "message": "No JSON data provided",
                    "code": 400,
                    "example": {
                        "mood": "casual/humorous/cool/romantic/formal/empathetic",
                        "length": 1.0,
                        "description": "length: 1.0 (15文字以内), 2.0 (20-50文字), 3.0 (50文字以上)"
                    }
                }), 400
            
            response = process_parameters(parameters)
            return jsonify({
                "status": "success",
                "data": response,
                "code": 200
            }), 200
        
    except ValueError as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "code": 400,
            "example": {
                "mood": "casual/humorous/cool/romantic/formal/empathetic",
                "length": 1.0,
                "description": "length: 1.0 (15文字以内), 2.0 (20-50文字), 3.0 (50文字以上)"
            }
        }), 400
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "code": 500,
            "example": {
                "mood": "casual/humorous/cool/romantic/formal/empathetic",
                "length": 1.0,
                "description": "length: 1.0 (15文字以内), 2.0 (20-50文字), 3.0 (50文字以上)"
            }
        }), 500

# エラーハンドリングの追加
@api_bp.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        "status": "error",
        "message": "Method Not Allowed",
        "code": 405,
        "example": {
            "mood": "casual/humorous/cool/romantic/formal/empathetic",
            "length": 1.0,
            "description": "length: 1.0 (15文字以内), 2.0 (20-50文字), 3.0 (50文字以上)"
        }
    }), 405