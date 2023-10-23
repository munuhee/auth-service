"""
This module defines the User model for storing user information.
It uses the SQLAlchemy database connection provided by the 'db' instance from the 'app' package.
"""
from datetime import datetime
from app import db

class User(db.Model):
    """User model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    refresh_token = db.Column(db.String(200), nullable=True)
    def __str__(self):
        return f"User(id={self.id}, username='{self.username}')"

class PasswordResetToken(db.Model):
    """Password reset model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(100), unique=True, nullable=False)
    expiration = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

    def is_expired(self):
        """Check if the expiration timestamp has passed."""
        return datetime.utcnow() > self.expiration
