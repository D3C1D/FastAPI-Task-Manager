from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.task import TaskCreate
from app.schemas.task import TaskUpdate
from app.schemas.task import TaskResponse
from app.services.task_service import (
    create_task,
    get_task,
    get_tasks,
    update_task,
    delete_task
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post(
    "/",
    summary="Create task",
    description="Create a new task",
    response_model=TaskResponse,
    status_code=201
)

def create_new_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return create_task(
        db,
        task
    )

@router.get(
    "/",
    summary="Get all tasks",
    response_model=list[TaskResponse]
)

def read_tasks(
    db: Session = Depends(get_db)
):
    return get_tasks(db)

@router.get(
    "/{task_id}",
    summary="Get task by ID",
    response_model=TaskResponse
)

def read_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = get_task(
        db,
        task_id
    )
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return task

@router.put(
    "/{task_id}",
    summary="Update task",
    response_model=TaskResponse
)

def update_existing_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db)
):
    updated_task = update_task(
        db,
        task_id,
        task
    )
    if not updated_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return updated_task

@router.delete(
    "/{task_id}",
    summary="Delete task",
    response_model=TaskResponse
)

def delete_existing_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    deleted_task = delete_task(
        db,
        task_id
    )
    if not deleted_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return deleted_task