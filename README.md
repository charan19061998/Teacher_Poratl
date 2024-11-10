# Teacher Portal

The Teacher Portal is a web-based application built using Django, HTML, CSS and JavaScript. It provides a platform for teachers to log in, view, manage student records, and add new students to the system. This project offers secure login functionality and an intuitive interface for handling student details efficiently.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)


## Project Overview

The Teacher Portal is designed to simplify student management for educators. It offers functionalities for securely logging in, viewing a comprehensive list of students, managing student data, and performing CRUD (Create, Read, Update, Delete) operations. It also provides a robust admin dashboard for overseeing both content and user management.

## Features
- **User Authentication**: Teachers can register, log in securely, and log out. Error handling is implemented for failed authentication attempts.
- **Student Listing**: Displays a list of students with details such as name, subject, and marks.
- **Add New Student**: Allows teachers to add a new student record through a form with validation checks to prevent duplicate entries.
- **Edit Student Records**: Teachers can edit student information directly from the list.
- **Delete Student**: Enables the deletion of student records from the system.
- **Admin Dashboard**: Admin-level capabilities for content and user management, available through the Django admin panel.
- **Validation and Security**: Custom validation rules and secure endpoints to prevent unauthorized access.

## Installation

### Clone the Repository
```bash
git clone https://github.com/charan19061998/Teacher_Poratl.git

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

Usage
Admin Interface: Access the Django admin panel at http://127.0.0.1:8000/admin for managing users and content.
API Testing: Use tools like Postman or cURL to test various API endpoints.

API Endpoints
/signup/ - Registration page for new users.
/login/ - Login page for teachers.
/home/ - Displays the home page with the list of students.
/add_student/ - Endpoint to add a new student.
/<int:id>/ - Edit specific student details.
/delete_student/<int:id>/ - Delete specific student records.
/logout/ - Log out the user.
