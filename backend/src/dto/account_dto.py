from pydantic import BaseModel, field_validator
from typing import Optional


class AccountCreate(BaseModel):
    user_id: int
    role_id: int
    email: str
    username: str
    password: str

    @field_validator("username")
    def validate_username(cls, v):
        if len(v) > 16:
            raise ValueError("Username maksimal 16 karakter")
        if not v.strip():
            raise ValueError("Username tidak boleh kosong")
        return v

    @field_validator("email")
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Email tidak valid")
        return v


class AccountUpdate(BaseModel):
    user_id: Optional[int] = None
    role_id: Optional[int] = None
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

    @field_validator("username")
    def validate_username(cls, v):
        if v is not None:
            if len(v) > 16:
                raise ValueError("Username maksimal 16 karakter")
            if not v.strip():
                raise ValueError("Username tidak boleh kosong")
        return v


class AccountResponse(BaseModel):
    id: int
    user_id: int
    role_id: int
    email: str
    username: str

    class Config:
        from_attributes = True
