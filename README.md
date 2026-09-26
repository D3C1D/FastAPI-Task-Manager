# FastAPI Task Manager

## Overview

FastAPI Task Manager is a REST API built using FastAPI, SQLAlchemy, and SQLite.

The application allows users and tasks to be created, retrieved, updated, and deleted through a structured CRUD API.

The project follows a layered architecture using routers, services, schemas, models, validation, custom exceptions, and automated testing.

## Features

- User CRUD operations
- Task CRUD operations
- SQLite database integration
- SQLAlchemy ORM models
- Pydantic validation
- Custom exception handling
- Swagger/OpenAPI documentation
- Automated testing with pytest

## Technology Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest

## Project Structure

```text
app/
├── core/
├── database/
├── exceptions/
├── models/
├── routers/
├── schemas/
├── services/
└── main.py

tests/
├── test_users.py
└── test_tasks.py
```

## Installation

git clone <repository-url>

cd FastAPI-Task-Manager

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

## Running The Application

uvicorn app.main:app --reload

## API Documentation

Swagger UI is available at:

http://127.0.0.1:8000/docs

## Running Tests

pytest

## Current Test Coverage

Users

- Create User
- Get All Users
- Get User By ID
- Validation Testing
- Missing Field Testing

Tasks

- Create Task
- Get All Tasks
- Get Task By ID
- Update Task
- Delete Task

## Validation Rules

User Validation

- Username minimum length: 3
- Username maximum length: 50
- Valid email required

Task Validation

- Title minimum length: 3
- Title maximum length: 100
- Description minimum length: 5
- Description maximum length: 500
- User ID must be greater than 0

## Architecture

The application follows a layered architecture:

Router Layer
→ receives HTTP requests

Service Layer
→ contains business logic

Model Layer
→ defines database tables

Database Layer
→ handles persistence

Schema Layer
→ validates request and response data

Exception Layer
→ centralizes error handling