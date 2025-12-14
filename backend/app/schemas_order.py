from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class OrderCreate(BaseModel):
    quote_id: UUID

class OrderRead(BaseModel):
    id: UUID
    quote_id: UUID
    status: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
