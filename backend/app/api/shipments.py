from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import SessionLocal
from app.models_shipment import Shipment
from app.schemas_shipment import ShipmentRead
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/shipments", tags=["shipments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ShipmentRead])
def list_shipments(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return db.query(Shipment).all()
