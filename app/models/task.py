from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from app.database.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(
        Integer,
        primary_key=True
    )
    title = Column(
        String,
        nullable=False
    )
    description = Column(
        String
    )
    completed = Column(
        Boolean,
        default=False
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )