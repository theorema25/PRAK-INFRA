from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LogCreate(BaseModel):
    account_id: int
    action: str
    ip_address: str
    user_agent: str
    entity: str
    entity_id: int
