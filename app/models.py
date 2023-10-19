"""
This module defines the User model for storing user information.
It uses the SQLAlchemy database connection provided by the 'db' instance from the 'app' package.
"""

from app import db

class User(db.Model):
    """User model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    refresh_token = db.Column(db.String(200), nullable=True)
    def __str__(self):
        return f"User(id={self.id}, username='{self.username}')"
