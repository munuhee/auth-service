"""Routes for user registration and login.

Keyword arguments:
- health -- Check the health status of the application.
- register -- Register a new user.
- login -- Log in a user.
Return: JSON responses with appropriate status codes.
"""
from flask import request, jsonify
from app import app
from app.services import register_user, login_user

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
