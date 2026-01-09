# User Management System

## Features
- JWT Authentication
- Profile Management
- Secure CRUD for Tasks
- Vanilla JS Frontend

## Setup
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  

## Test command
python manage.py test

## Swagger url
https://user-management-6o4y.onrender.com/swagger/

## Documentation url
https://user-management-6o4y.onrender.com/redoc/

## API
POST /api/auth/register  
POST /api/auth/login  
GET  /api/auth/profile  
PATCH /api/auth/profile  
POST /api/tasks  
GET /api/tasks  
PATCH /api/tasks/{id}  
DELETE /api/tasks/{id}
