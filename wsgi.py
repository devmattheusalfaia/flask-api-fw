# wsgi.py — ponto de entrada WSGI para o Gunicorn
from bootstrap.app import create_app

app = create_app()