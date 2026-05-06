from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class UserCreate(SQLModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    whatsapp: str = Field(..., min_length=10, max_length=15)


class UserUpdate(SQLModel):
    first_name: Optional[str] = Field(default=None, min_length=1)
    last_name: Optional[str] = Field(default=None, min_length=1)
    whatsapp: Optional[str] = Field(default=None, min_length=10, max_length=15)


class UserResponse(SQLModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    whatsapp: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]