from flask import Flask
from config.config import Config

# Importa rotas
from routes.web import web_bp
from routes.api import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registra blueprints
    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)

    return app