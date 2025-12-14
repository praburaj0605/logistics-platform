from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class ShipmentRead(BaseModel):
    id: UUID
    order_id: UUID
    tracking_number: str
    status: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
