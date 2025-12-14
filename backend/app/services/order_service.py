import uuid
from sqlalchemy.orm import Session
from app.models_order import Order
from app.models_shipment import Shipment

def create_order_from_quote(db: Session, quote_id):
    order = Order(quote_id=quote_id)
    db.add(order)
    db.commit()
    db.refresh(order)

    shipment = Shipment(
        order_id=order.id,
        tracking_number=f"TRK-{uuid.uuid4().hex[:12].upper()}",
        status="created",
    )
    db.add(shipment)
    db.commit()
    db.refresh(shipment)

    return order, shipment
