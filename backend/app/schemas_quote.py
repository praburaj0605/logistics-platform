from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class QuoteRequest(BaseModel):
    client_id: UUID
    origin: str
    destination: str
    service_type: str

class QuoteRead(BaseModel):
    id: UUID
    client_id: UUID
    vendor_id: UUID
    service_type: str
    origin: str
    destination: str
    base_rate: float
    final_rate: float
    currency: str
    status: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
