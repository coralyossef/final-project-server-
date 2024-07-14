# Customer Management System - Backend

This is the backend part of our Customer Management System, built using Flask. This application provides the API endpoints for managing customers and services.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Description

The Customer Management System backend is designed to handle the server-side operations for managing customers and services. It provides a comprehensive platform for user authentication, role-based access control, and CRUD operations for managing customer and service data.

### Key Objectives

- **Centralized Management**: Provide a single platform to manage all customer and service data.
- **Role-Based Access Control**: Ensure that different user roles have access to the specific functionalities they need.
- **Secure Backend**: Implement secure authentication and authorization mechanisms.
- **Automation**: Automate tasks such as sending email notifications to reduce manual effort.

### User Roles

The system supports three types of user roles:
- **Customer**: Can view and manage their profile and services.
- **Manager**: Can manage customers and view all service details.
- **Operator**: Can manage the services offered by the business.

## Features

- User authentication and authorization
- Role-based access control (Customer, Manager, Operator)
- CRUD operations for customers and services
- Email notifications upon user registration
- RESTful API

## API Endpoints

The following endpoints are available in the Flask backend:

### Authentication

- `POST /register` - Register a new user
- `POST /login` - Authenticate a user

### Customers

- `GET /customers` - Get a list of customers
- `POST /customers` - Add a new customer
- `PUT /customers/:id` - Update a customer
- `DELETE /customers/:id` - Delete a customer

### Services

- `GET /services` - Get a list of services
- `POST /services` - Add a new service
- `PUT /services/:id` - Update a service
- `DELETE /services/:id` - Delete a service

## Project Structure

The project structure is organized to maintain a clean and scalable codebase. Here is an overview of the main directories and files:

### Directories

- `models`: Contains the database models.
  - These models define the structure of the database tables and their relationships.
  - Example: `Customer`, `Service`, `User`, etc.

- `routes`: Contains the API routes.
  - These routes define the endpoints and the corresponding request handlers.
  - Example: `customer_routes.py`, `service_routes.py`, `auth_routes.py`, etc.

- `utils`: Contains utility functions.
  - These functions provide common functionalities that are used across the application.
  - Example: `email_utils.py`, `auth_utils.py`, etc.

### Files

- `app.py`: The main entry point for the Flask application.
  - Sets up the Flask app, database, and registers the routes.

- `config.py`: Contains the configuration settings for the application.
  - Example: database URI, secret keys, etc.

- `requirements.txt`: Contains the list of dependencies required for the project.
  - Used to install the necessary packages using pip.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please make sure your code follows the project's coding style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
