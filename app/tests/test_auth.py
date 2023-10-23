"""
Authentication Unit Testing Module
This module contains unit tests for the authentication functionality of the application.
"""
import os
import unittest
import json
from app import app, db
class TestAuth(unittest.TestCase):
    """Unit tests for the authentication functionality of the application."""
    def setUp(self):
        """Set up a test environment."""
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('FLASK_ENV')
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        """Clean up after tests."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_health(self):
        """Test the health endpoint."""
        response = self.app.get('/api/status')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'application is healthy')

    def test_register(self):
        """Test the register endpoint."""
        user_data = {
            'username': 'user1',
            'email': 'example@domain.com',
            'password': 'testing321'
        }
        response = self.app.post(
            '/api/register',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Registration successful')

    def test_login(self):
        """Test the login endpoint with a registered user."""
        user_data = {
            'username': 'user1',
            'email': 'example@domain.com',
            'password': 'testing321'
        }
        registration_response = self.app.post(
            '/api/register',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        self.assertEqual(registration_response.status_code, 201)
        response = self.app.post(
            '/api/login',
            data=json.dumps(user_data),
            content_type='application/json')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access_token' in data)
        self.assertEqual(data['message'], 'Login successful')

    def test_reset_request_password(self):
        """Test the password reset request functionality."""
        user_data = {
            'username': 'user1',
            'email': 'example@domain.com',
            'password': 'testing321'
        }

        # Register a user
        registration_response = self.app.post(
            '/api/register',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        self.assertEqual(registration_response.status_code, 201)

        # Simulate a password reset request
        reset_request = self.app.post(
            '/api/reset-password',
            data=json.dumps({'email': 'example@domain.com'}),
            content_type='application/json'
        )
        self.assertEqual(reset_request.status_code, 200)

    def test_reset_password(self):
        """Test the password reset functionality."""
        reset_link = ('http://localhost:5000/api/reset-password/'
            'ABCdEf_GH_IJkui-qpY-mnJCBSG32LOuntR1TH6-zGm55515AbeWBpegGDXZZVsFlRI')
        new_password = {'password':'testing654'}
        reset = self.app.post(
            reset_link,
            data=json.dumps(new_password),
            content_type='application/json'
        )
        self.assertEqual(reset.status_code, 400)

if __name__ == '__main__':
    unittest.main()
    