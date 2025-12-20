import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base

class Enquiry(Base):
    __tablename__ = "enquiries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_id = Column(UUID(as_uuid=True), ForeignKey("clients.id"), nullable=False)

    origin = Column(String(50), nullable=False)
    destination = Column(String(50), nullable=False)
    service_type = Column(String(100), nullable=False)

    expected_ship_date = Column(DateTime(timezone=True), nullable=True)
    notes = Column(Text, nullable=True)

    status = Column(String(30), default="open")  # open, quoted, closed
    created_at = Column(DateTime(timezone=True), server_default=func.now())
