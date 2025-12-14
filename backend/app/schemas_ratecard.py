from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class RateCardCreate(BaseModel):
    vendor_id: UUID
    origin: str
    destination: str
    rate: float
    currency: str = "INR"

class RateCardRead(RateCardCreate):
    id: UUID
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
