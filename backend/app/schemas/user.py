from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    client = "client"
    admin = "admin"

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None
    role: UserRole = UserRole.client

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None
    role: UserRole

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None