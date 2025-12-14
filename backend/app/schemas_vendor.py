from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class VendorCreate(BaseModel):
    name: str
    service_type: str

class VendorRead(VendorCreate):
    id: UUID
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
