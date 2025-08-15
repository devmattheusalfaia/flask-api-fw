from flask import Blueprint
from app.controllers.hello_controller import hello

web_bp = Blueprint('web', __name__)

web_bp.add_url_rule('/', 'hello', hello)