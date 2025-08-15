from flask import Flask
from config.config import Config
from routes.web import web_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registra rotas
    app.register_blueprint(web_bp)

    return app