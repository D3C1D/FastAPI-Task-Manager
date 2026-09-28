from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from app.database.database import engine
from app.database.database import Base
from app.models.user import User
from app.models.task import Task
from app.routers.user_router import router as user_router
from app.routers.task_router import router as task_router
from app.exceptions.custom_exceptions import (
    UserNotFoundException,
    TaskNotFoundException
)
from app.exceptions.handlers import (
    user_not_found_handler,
    task_not_found_handler
)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
    <head>
        <title>FastAPI Task Manager</title>

        <style>

            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                color: #333333;
                text-align: center;
                padding: 60px;
            }

            .card {
                background-color: white;
                max-width: 900px;
                margin: 0 auto;
                padding: 150px;
                border-radius: 10px;
                box-shadow: 0px 2px 8px rgba(0,0,0,0.15);
            }

            h1 {
                color: #0d47a1;
                margin-bottom: 25px;
            }

            p {
                line-height: 1.8;
                margin-bottom: 30px;
            }

            .button {
                display: inline-block;
                background-color: #1976d2;
                color: white;
                text-decoration: none;
                padding: 12px 18px;
                border-radius: 8px;
                margin: 10px;
            }

            .button:hover {
                text-decoration: underline;
                background-color: #0d47a1;
            }

        </style>
    </head>

    <body>

        <div class="card">

            <h1>FastAPI Task Manager</h1>

            <p>
                RESTful Task Management API built with FastAPI, SQLAlchemy, SQLite, Pydantic 
                validation, automated testing, and Swagger/OpenAPI documentation.
            </p>

            

            <a class="button"
                href="https://fastapi-task-manager-srm5.onrender.com/docs"
                target="_blank">
                 Swagger Documentation
            </a>

            <a class="button"
                href="https://github.com/D3C1D/FastAPI-Task-Manager"
                target="_blank">
                 GitHub Repository
            </a>

        </div>

    </body>
    </html>
    """

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(task_router)

app.add_exception_handler(
    UserNotFoundException,
    user_not_found_handler
)

app.add_exception_handler(
    TaskNotFoundException,
    task_not_found_handler
)