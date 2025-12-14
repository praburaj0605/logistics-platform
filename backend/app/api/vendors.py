from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import SessionLocal
from app.models_vendor import Vendor
from app.schemas_vendor import VendorCreate, VendorRead
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/vendors", tags=["vendors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VendorRead)
def create_vendor(
    vendor_in: VendorCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    vendor = Vendor(**vendor_in.dict())
    db.add(vendor)
    db.commit()
    db.refresh(vendor)
    return vendor

@router.get("/", response_model=List[VendorRead])
def list_vendors(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return db.query(Vendor).all()
