from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class EnquiryCreate(BaseModel):
    client_id: UUID
    origin: str
    destination: str
    service_type: str
    expected_ship_date: Optional[datetime] = None
    notes: Optional[str] = None

class EnquiryRead(BaseModel):
    id: UUID
    client_id: UUID
    origin: str
    destination: str
    service_type: str
    expected_ship_date: Optional[datetime]
    notes: Optional[str]
    status: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
