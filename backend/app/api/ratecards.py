from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import SessionLocal
from app.models_ratecard import RateCard
from app.schemas_ratecard import RateCardCreate, RateCardRead
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/ratecards", tags=["ratecards"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RateCardRead)
def create_ratecard(
    rate_in: RateCardCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    rate = RateCard(**rate_in.dict())
    db.add(rate)
    db.commit()
    db.refresh(rate)
    return rate

@router.get("/", response_model=List[RateCardRead])
def list_ratecards(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return db.query(RateCard).all()
