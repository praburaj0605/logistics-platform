from sqlalchemy.orm import Session
from app.models_enquiry import Enquiry

def create_enquiry(db: Session, enquiry_in):
    enquiry = Enquiry(**enquiry_in.dict())
    db.add(enquiry)
    db.commit()
    db.refresh(enquiry)
    return enquiry

def mark_enquiry_quoted(db: Session, enquiry_id):
    enquiry = db.query(Enquiry).filter(Enquiry.id == enquiry_id).first()
    if enquiry:
        enquiry.status = "quoted"
        db.commit()
    return enquiry
