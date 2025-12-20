from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import SessionLocal
from app.schemas_enquiry import EnquiryCreate, EnquiryRead
from app.services.enquiry_service import create_enquiry
from app.models_enquiry import Enquiry
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/enquiries", tags=["enquiries"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EnquiryRead)
def create_enquiry_api(
    enquiry_in: EnquiryCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return create_enquiry(db, enquiry_in)

@router.get("/", response_model=List[EnquiryRead])
def list_enquiries(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return db.query(Enquiry).all()
