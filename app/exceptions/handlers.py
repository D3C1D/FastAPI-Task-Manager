from fastapi.responses import JSONResponse
from fastapi import Request
from app.exceptions.custom_exceptions import (
    UserNotFoundException,
    TaskNotFoundException
)

async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": exc.message
        }
    )

async def task_not_found_handler(
    request: Request,
    exc: TaskNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": exc.message
        }
    )