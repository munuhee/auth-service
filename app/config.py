"""
Module to store configuration settings for the auth-service.
"""
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = 'your-secret-key'
REFRESH_SECRET_KEY = 'your-refresh-secret-key'

if os.environ.get('FLASK_ENV') == 'testing':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
else:
    SQLALCHEMY_DATABASE_URI = 'postgresql://stephen:testing321@auth-db:5432/auth-service'

# Flask-Mail configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
