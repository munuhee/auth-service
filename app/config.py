"""
Module to store configuration settings for the auth-service.
"""
import os

SECRET_KEY = 'your-secret-key'

# Using an environment variable to determine which database URI to use
if os.environ.get('FLASK_ENV') == 'testing':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
else:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:testing321@localhost/auth-service'
