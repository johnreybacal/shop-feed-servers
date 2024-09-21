from fastapi import HTTPException
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

def update(db: Session, id: UUID, data: schema.ShopPayload):
    shop = get(db, id)

    if shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")

    shop.name = data.name
    db.commit()
    db.refresh(shop)

    return shop

def delete(db: Session, id: UUID):
    shop = get(db, id)

    if shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")

    db.delete(shop)
    db.commit()

    return shop