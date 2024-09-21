from sqlalchemy.orm import Session
from uuid import UUID

from . import model, schema

def list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model.Shop).offset(skip).limit(limit).all()

def get(db: Session, id: UUID):
    return db.query(model.Shop).filter(model.Shop.id == id).first()

def create(db: Session, data: schema.ShopPayload):
    shop = model.Shop(name=data.name)

    db.add(shop)
    db.commit()
    db.refresh(shop)

    return shop
