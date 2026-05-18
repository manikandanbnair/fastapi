from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    age: Optional[int] = None
    is_active: bool = True

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    age: Optional[int] = None

class UserResponseList(BaseModel):
    success: bool
    users: list[UserResponse]
