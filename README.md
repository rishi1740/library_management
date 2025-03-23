# Library Management System

A Django-based Library Management System with Admin and Student views.

## Features

- Admin Authentication (Signup/Login)
- Book CRUD Operations
- Student View for listing all books
- RESTful API
- MySQL Database

## Tech Stack

- Django 4.2
- Django REST Framework
- MySQL
- HTML/CSS/JavaScript (Frontend)

## Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL Server

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/library-management.git
   cd library-management
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create MySQL database:
   ```sql
   CREATE DATABASE library_db;
   CREATE USER 'library_user'@'localhost' IDENTIFIED BY 'library_password';
   GRANT ALL PRIVILEGES ON library_db.* TO 'library_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

5. Configure database settings in `settings.py` (update credentials if needed)

6. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application:
   - Student View: http://localhost:8000/api/
   - Admin Login: http://localhost:8000/api/admin/login.html
   - API Endpoints: http://localhost:8000/api/books/ (for student view)

## API Endpoints

### Admin Authentication
- POST `/api/admin/register/` - Register a new admin
- POST `/api/admin/login/` - Login for admin

### Book Management (Admin)
- GET `/api/admin/books/` - List all books
- POST `/api/admin/books/` - Create a new book
- GET `/api/admin/books/<id>/` - Retrieve a book
- PUT `/api/admin/books/<id>/` - Update a book
- DELETE `/api/admin/books/<id>/` - Delete a book

### Student View
- GET `/api/books/` - List all books (public access)

## Project Structure

```
library_management/
├── book_api/
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   │   ├── admin/
│   │   │   ├── login.html
│   │   │   └── dashboard.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── library_management/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## Security Considerations

- Token-based authentication for admin operations
- Email uniqueness enforcement for admin accounts
- Password hashing for secure storage
