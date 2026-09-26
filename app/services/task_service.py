from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate
from app.schemas.task import TaskUpdate

def create_task(
    db: Session,
    task: TaskCreate
):
    db_task = Task(
        title=task.title,
        description=task.description,
        user_id=task.user_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(
    db: Session,
    task_id: int
):
    return (
        db.query(Task)
        .filter(Task.id == task_id)
        .first()
    )

def get_tasks(
    db: Session
):
    return db.query(Task).all()

def delete_task(
    db: Session,
    task_id: int
):
    task = (
        db.query(Task)
        .filter(Task.id == task_id)
        .first()
    )
    if task:
        db.delete(task)
        db.commit()
        return task
    return None

def update_task(
    db: Session,
    task_id: int,
    task_data: TaskUpdate
):
    task = (
        db.query(Task)
        .filter(Task.id == task_id)
        .first()
    )
    if not task:
        return None
    if task_data.title is not None:
        task.title = task_data.title
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.completed is not None:
        task.completed = task_data.completed
    db.commit()
    db.refresh(task)
    return task