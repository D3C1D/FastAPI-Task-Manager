from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import UserCreate
from app.schemas.user import UserResponse
from app.services.user_service import (
    create_user,
    get_user,
    get_users,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "/",
    summary="Create user",
    description="Create a new user",
    response_model=UserResponse,
    status_code=201
)

def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(
        db,
        user
    )

@router.get(
    "/",
    summary="Get all users",
    response_model=list[UserResponse]
)

def read_users(
    db: Session = Depends(get_db)
):
    return get_users(db)

@router.get(
    "/{user_id}",
    summary="Get user by ID",
    response_model=UserResponse
)

def read_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = get_user(
        db,
        user_id
    )
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

@router.put(
    "/{user_id}",
    summary="Update user",
    response_model=UserResponse
)

def update_existing_user(
    user_id: int,
    user: UserCreate,
    db: Session = Depends(get_db)
):
    updated_user = update_user(
        db,
        user_id,
        user
    )
    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return updated_user

@router.delete(
    "/{user_id}",
    summary="Delete user",
    response_model=UserResponse
)

def delete_existing_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    deleted_user = delete_user(
        db,
        user_id
    )
    if not deleted_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return deleted_user