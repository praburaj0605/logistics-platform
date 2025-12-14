from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas_quote import QuoteRequest, QuoteRead
from app.services.quotation import generate_quote
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/quotes", tags=["quotes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=QuoteRead)
def create_quote(
    quote_in: QuoteRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    quote = generate_quote(
        db=db,
        client_id=quote_in.client_id,
        origin=quote_in.origin,
        destination=quote_in.destination,
        service_type=quote_in.service_type,
    )
    if not quote:
        raise HTTPException(status_code=404, detail="No rate found for route")
    return quote
