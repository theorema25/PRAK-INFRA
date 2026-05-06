from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventCreate(BaseModel):
    name: str
    description: Optional[str] = None
    quota: int
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None

class EventUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quota: Optional[int] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None