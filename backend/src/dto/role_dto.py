from pydantic import BaseModel, field_validator
from typing import Optional

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    @field_validator("name")
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError("Nama Role tidak boleh kosong")
        if len(v) > 20:
            raise ValueError("Nama Role maksimal 20 karakter")
        return v

class RoleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    @field_validator("name")
    def validate_name(cls, v):
        if v is not None:
            if not v.strip():
                raise ValueError("Nama Role tidak boleh kosong")
            if len(v) > 20:
                raise ValueError("Nama Role maksimal 20 karakter")
        return v

class RoleResponse(RoleBase):
    id: int

    class Config:
        from_attributes = True