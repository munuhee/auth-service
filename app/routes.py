"""
Routes for User Registration, Login, and Password Reset

This module defines the routes for user registration, login, and password reset
functionality, providing RESTful endpoints for managing user accounts and
password recovery.

Endpoints:
- /api/register: Register a new user.
- /api/login: Log in a user.
- /api/reset-password: Initiate a password reset, verify reset tokens, and reset passwords.

Returns: JSON responses with appropriate status codes.
"""

from flask import request, jsonify
from werkzeug.security import generate_password_hash
from app import app, db
from app.services import register_user, login_user, generate_reset_token, send_reset_email
from app.models import PasswordResetToken, User

@app.route('/api/status', methods=['GET'])
def health():
    """Check the health status of the application."""
    return jsonify({"message": "application is healthy"}), 200

@app.route('/api/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    response, status_code = register_user(username, email, password)
    return jsonify(response), status_code

@app.route('/api/login', methods=['POST'])
def login():
    """Log in a user."""
    data = request.get_json()
    identifier = data.get('username')
    password = data.get('password')
    response, status_code = login_user(identifier, password)
    return jsonify(response), status_code

@app.route('/api/reset-password', methods=['POST'])
def request_password_reset():
    """Initiate a password reset request."""
    data = request.get_json()
    email = data.get('email')

    user = User.query.filter_by(email=email).first()

    if not user:
        return {"message": "User not found"}, 404

    token = generate_reset_token(user)
    send_reset_email(user, token)

    return {"message": "Password reset email sent. Check your inbox."}, 200

@app.route('/api/reset-password/<token>', methods=['POST'])
def reset_password(token):
    """Reset a user's password using a valid reset token."""
    data = request.get_json()
    new_password = data.get('password')

    reset_token = PasswordResetToken.query.filter_by(token=token).first()

    if not reset_token:
        return {"message": "Invalid reset token"}, 400

    if reset_token.is_expired():
        return {"message": "Reset token has expired"}, 400

    user = User.query.get(reset_token.user_id)
    user.password = generate_password_hash(new_password, method='pbkdf2:sha256')
    db.session.delete(reset_token)
    db.session.commit()

    return {"message": "Password reset successful"}, 200
