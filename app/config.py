"""
Module to store configuration settings for the auth-service.
"""
import os

SECRET_KEY = 'your-secret-key'
REFRESH_SECRET_KEY = 'your-refresh-secret-key'

if os.environ.get('FLASK_ENV') == 'testing':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
else:
    SQLALCHEMY_DATABASE_URI = 'postgresql://stephen:testing321@auth-db:5432/auth-service'
