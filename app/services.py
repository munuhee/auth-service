"""
User Authentication Module
This module handles user registration and login functionality, 
including password hashing and JWT token generation.
"""

import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.models import User

def register_user(username, password):
    """Register a new user and store their information in the database."""
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return {"message": "Username already exists"}, 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return {"message": "Registration successful"}, 201

def login_user(username, password):
    """Log in a user and return an access token upon successful login."""
    user = User.query.filter_by(username=username).first()

    if not user:
        return {"message": "User not found"}, 404

    if check_password_hash(user.password, password):
        # Create a JWT token for authentication
        token = jwt.encode({'username': user.username}, app.config['SECRET_KEY'], algorithm='HS256')
        return {"message": "Login successful", "access_token": token}, 200
    return {"message": "Invalid password"}, 401
