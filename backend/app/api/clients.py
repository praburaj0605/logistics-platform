from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from app.db.session import SessionLocal
from app.models import Client
from app.schemas import ClientCreate, ClientRead
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/clients", tags=["clients"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ClientRead)
def create_client(
    client_in: ClientCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    client = Client(name=client_in.name)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

@router.get("/", response_model=List[ClientRead])
def list_clients(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    return db.query(Client).all()

@router.get("/{client_id}", response_model=ClientRead)
def get_client(
    client_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(
    client_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(client)
    db.commit()
    return None
