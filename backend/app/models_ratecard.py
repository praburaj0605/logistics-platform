import uuid
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base

class RateCard(Base):
    __tablename__ = "rate_cards"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vendor_id = Column(UUID(as_uuid=True), ForeignKey("vendors.id"), nullable=False)
    origin = Column(String(50), nullable=False)
    destination = Column(String(50), nullable=False)
    rate = Column(Float, nullable=False)
    currency = Column(String(10), default="INR")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
