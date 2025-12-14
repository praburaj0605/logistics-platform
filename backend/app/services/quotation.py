from sqlalchemy.orm import Session
from app.models_ratecard import RateCard
from app.models_quote import Quote

def generate_quote(
    db: Session,
    client_id,
    origin: str,
    destination: str,
    service_type: str,
):
    rate = (
        db.query(RateCard)
        .join(RateCard.__table__.foreign_keys)
        .filter(
            RateCard.origin == origin,
            RateCard.destination == destination,
        )
        .first()
    )

    if not rate:
        return None

    final_rate = rate.rate  # future: add fuel surcharge, taxes

    quote = Quote(
        client_id=client_id,
        vendor_id=rate.vendor_id,
        service_type=service_type,
        origin=origin,
        destination=destination,
        base_rate=rate.rate,
        final_rate=final_rate,
        currency=rate.currency,
    )

    db.add(quote)
    db.commit()
    db.refresh(quote)
    return quote
