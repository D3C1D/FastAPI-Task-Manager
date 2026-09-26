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