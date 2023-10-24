# Auth Service
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.10-green)](https://www.python.org/downloads/)

This is a Flask-based RESTful application designed to streamline user authentication for web applications. It offers comprehensive features for user management, including user registration, login, and password reset, ensuring a secure and hassle-free user account management experience. Through a RESTful architecture, this service allows you to easily register new users, verify their identity, and facilitate password recovery, all while adhering to RESTful principles for efficient and structured communication between clients and the server.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Badges](#badges)
- [Documentation](#documentation)
- [Demo](#demo)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Introduction

Auth Service is designed to streamline user authentication. Whether you're building a small web app or a large-scale system, it helps you manage user accounts, store passwords securely, and handle password recovery.

## Installation

To set up and run Auth Service, follow these steps:

1. **Clone the repository:**
   ```shell
   git clone  https://github.com/munuhee/auth-service.git
   cd auth-service
   ```

2. **Create a virtual environment (optional but recommended):**
   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. **Install the required packages:**
   ```shell
   pip install -r requirements.txt
   ```

4. **Create a `.env` file and set the necessary environment variables.** You can use `variables.env` as a template and update it with your values.

5. **Initialize the database and apply migrations:**
   ```shell
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Start the application:**
   ```shell
   python run.py
   ```

The application will be accessible at `http://localhost:5000`. Customize the configuration in `config.py` to fit your needs.

## Configuration

The `config.py` file contains configuration settings for Auth Service. Set environment variables for secret keys, database URIs, email server settings, and more.

```plaintext
# .env

# Secret keys
SECRET_KEY=your_secret_key
REFRESH_SECRET_KEY=your_refresh_secret_key

# Database URI (SQLite example for development)
SQLALCHEMY_DATABASE_URI=sqlite:///dev.db

# Flask Environment (use 'testing' for testing, 'development' for development, 'production' for production)
FLASK_ENV=development

# Flask-Mail configuration for sending email (update with your email server details)
MAIL_USERNAME=your_email_username
MAIL_PASSWORD=your_email_password
MAIL_DEFAULT_SENDER=your_email_sender
```

Replace placeholder values with your actual configuration details.


## Usage

Auth Service provides the following endpoints:

- **`GET /api/status`**: Check the health status of the application.
- **`POST /api/register`**: Register a new user.
- **`POST /api/login`**: Log in a user.
- **`POST /api/reset-password`**: Initiate a password reset request, verify reset tokens, and reset passwords.

You can interact with these endpoints using a RESTful API client or within your application.

## Features

- **User Registration**: Register new users with unique usernames and email addresses.
- **Password Management**: Store and validate user passwords securely.
- **Password Reset**: Initiate password reset requests with email notifications.
- **Health Status**: Monitor the system's health with a dedicated endpoint.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix.
3. **Implement your changes**.
4. **Write tests** to ensure your code functions correctly.
5. **Create a pull request**, describing the changes you made.

You can also **report issues** and **suggest improvements** by opening a GitHub issue.

## License

This project is licensed under the [MIT License](LICENSE).

## Demo

Try out Auth Service by visiting our [live demo](link-to-demo).

## Contact

For questions or suggestions, please visit my [GitHub profile](https://github.com/munuhee).

## Acknowledgments

I'd like to acknowledge the following libraries, tools, and individuals who contributed to this project:

- [Flask](https://flask.palletsprojects.com/): A lightweight and flexible micro web framework for Python.
- [SQLAlchemy](https://www.sqlalchemy.org/): An SQL toolkit and Object-Relational Mapping (ORM) library.
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/): An extension for sending email from your Flask application.
- [Werkzeug](https://werkzeug.palletsprojects.com/): A WSGI utility library for Python.
- [Python Community](https://www.python.org/community/): For creating an amazing language and community.

## Authors

- [Stephen Murichu](https://github.com/munuhee)

Happy coding! 🚀