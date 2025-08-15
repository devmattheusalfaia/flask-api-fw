import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secret-key")
    
class DevelopmentConfig(Config):
    DEBUG = True