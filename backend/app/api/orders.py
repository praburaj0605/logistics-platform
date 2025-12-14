from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas_order import OrderCreate, OrderRead
from app.services.order_service import create_order_from_quote
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderRead)
def create_order(
    order_in: OrderCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    order, _ = create_order_from_quote(db, order_in.quote_id)
    return order
