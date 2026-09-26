from typing import Optional
from pydantic import BaseModel
from pydantic import Field

class TaskCreate(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=100
    )
    description: str = Field(
        min_length=5,
        max_length=500
    )
    user_id: int = Field(
        gt=0
    )

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    user_id: int
    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=100
    )
    description: Optional[str] = Field(
        default=None,
        min_length=5,
        max_length=500
    )
    completed: Optional[bool] = None