from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class UserCreate(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50
    )
    username: str
    email: EmailStr = Field(
       max_length=100
    )

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    class Config:
      from_attributes = True