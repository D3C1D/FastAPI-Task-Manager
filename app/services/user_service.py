from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def create_user(
    db: Session,
    user: UserCreate
):
    db_user = User(
        username=user.username,
        email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(
    db: Session,
    user_id: int
):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

def get_users(
    db: Session
):
    return db.query(User).all()

def delete_user(
    db: Session,
    user_id: int
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )
    if user:
        db.delete(user)

        db.commit()
        return user
    return None

def update_user(
    db: Session,
    user_id: int,
    user_data: UserCreate
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )
    if not user:
        return None
    user.username = user_data.username
    user.email = user_data.email
    db.commit()
    db.refresh(user)
    return user