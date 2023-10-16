"""
This module initializes the Flask app and sets up the database.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes

# Create the database tables during app initialization
with app.app_context():
    db.create_all()
