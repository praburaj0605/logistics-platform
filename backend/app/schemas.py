from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class ClientCreate(BaseModel):
    name: str

class ClientRead(ClientCreate):
    id: UUID4
    status: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
