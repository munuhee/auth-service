
<div align="center">
  <img src="https://res.cloudinary.com/murste/image/upload/v1698907632/stevolve_x8ioeu.png" alt="Stephen Murichu's Logo" width="100" />
</div>

# Auth Service

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.10-green)

Auth Service is a Flask-based RESTful application designed to streamline user authentication for web applications. It offers comprehensive features for user management, including user registration, login, and password reset, ensuring a secure and hassle-free user account management experience. Auth Service is containerized using Docker for easy deployment.

## Table of Contents

- [Introduction](#introduction)
- [Docker Process](#docker-process)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)
- [Authors](#authors)

## Introduction

Auth Service is designed to streamline user authentication. Whether you're building a small web app or a large-scale system, it helps you manage user accounts, store passwords securely, and handle password recovery.
## Installation
### Installation (with Docker)

This service is containerized using Docker for easy deployment and management. The Docker Compose configuration includes three services:

- `auth-service`: This is the main application service.
- `auth-db`: A PostgreSQL database service for storing user data.
- `pgadmin`: A PgAdmin service for database management.

The Docker Compose file (`docker-compose.yml`) specifies the build process for the `auth-service` container, the usage of pre-built images for the `auth-db` and `pgadmin` services, and the necessary environment variables for each service. To run Auth Service using Docker, follow these steps:

   1. Clone the repository:
      ```shell
      git clone  https://github.com/munuhee/auth-service.git
      cd auth-service
      ```

   2. Create a `.env` file on the root directory and set the necessary environment variables for the `auth-service`. You can use the provided template and update it with your values.
      ```plaintext
         # Application Configuration
         FLASK_ENV=development  # Set this to 'testing' or 'production' as needed

         # Authentication
         SECRET_KEY=your_secret_key_value
         REFRESH_SECRET_KEY=your_refresh_secret_key_value

         # Database
         SQLALCHEMY_DATABASE_URI=postgresql://<username>:<password>@<host>:<port>/<database>

         # Email Configuration
         MAIL_USERNAME=your_mail_username
         MAIL_PASSWORD=your_mail_password
         MAIL_DEFAULT_SENDER=your_mail_default_sender

         # PostgreSQL Configuration (auth-db service)
         POSTGRES_USER=your_postgres_user
         POSTGRES_PASSWORD=your_postgres_password
         POSTGRES_DB=your_database_name

         # PgAdmin Configuration (pgadmin service)
         PGADMIN_DEFAULT_EMAIL=your_pgadmin_email
         PGADMIN_DEFAULT_PASSWORD=your_pgadmin_password
      ```
      Make sure to replace the variables with your actual configuration values.

   3. Run the application using Docker Compose:
      ```shell
      docker-compose up
      ```

The application will be accessible at `http://localhost:5000`. Customize the configuration in `config.py` to fit your needs.

### Installation (without Docker)

To set up and run Auth Service locally (without Docker), follow the installation steps below
   1. Clone the repository:
      ```shell
      git clone  https://github.com/munuhee/auth-service.git
      cd auth-service
      ```

   2. Create a virtual environment (optional but recommended):
      ```shell
      python -m venv venv
      source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
      ```

   3. Install the required packages:
      ```shell
      pip install -r requirements.txt
      ```

   4. Create a `.env` file on the root directory and set the necessary environment variables.
      ```plaintext
      # Application Configuration
      FLASK_ENV=development  # Set this to 'testing' or 'production' as needed

      # Authentication
      SECRET_KEY=your_secret_key_value
      REFRESH_SECRET_KEY=your_refresh_secret_key_value

      # Email Configuration
      MAIL_USERNAME=your_mail_username
      MAIL_PASSWORD=your_mail_password
      MAIL_DEFAULT_SENDER=your_mail_default_sender
      ```
      Make sure to replace the variables with your actual configuration values.

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

## Usage

Auth Service provides the following endpoints for user registration, login, and password reset:

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


## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or suggestions, please visit my [GitHub profile](https://github.com/munuhee).

## Acknowledgments

I'd like to acknowledge the following libraries, tools, and individuals who contributed to this project, including Docker for containerization:

- [Flask](https://flask.palletsprojects.com/): A lightweight and flexible micro web framework for Python.
- [SQLAlchemy](https://www.sqlalchemy.org/): An SQL toolkit and Object-Relational Mapping (ORM) library.
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/): An extension for sending email from your Flask application.
- [Werkzeug](https://werkzeug.palletsprojects.com/): A WSGI utility library for Python.
- [Python Community](https://www.python.org/community/): For creating an amazing language and community.

## Authors

- [Stephen Murichu](https://github.com/munuhee)

                                            Happy coding! 🚀
