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

@app.route('/health', methods=['GET'])
def health():
    """Check the health status of the application."""
    return jsonify({"message": "application is healthy"}), 200

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data['username']
    password = data['password']
    response, status_code = register_user(username, password)
    return jsonify(response), status_code

@app.route('/login', methods=['POST'])
def login():
    """Log in a user."""
    data = request.get_json()
    username = data['username']
    password = data['password']
    response, status_code = login_user(username, password)
    return jsonify(response), status_code
