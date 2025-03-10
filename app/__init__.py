import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Blueprintの登録
    from app.api import api_bp
    app.register_blueprint(api_bp)
    
    return app

app = create_app() 