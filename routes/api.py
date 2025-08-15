from flask import Blueprint
from app.controllers.api_controller import get_api_message

api_bp = Blueprint('api', __name__, url_prefix="/api")

api_bp.add_url_rule('/', 'api_home', get_api_message)