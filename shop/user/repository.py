from sqlalchemy.orm import Session
from uuid import UUID
from . import model, schema


def get(db: Session, id: UUID):
    return db.query(model.User).filter(model.User.id == id).first()

def create(db: Session, data: schema.User):
    user = model.User(id=data.id,
                      name=data.name,
                      email=data.email
                      )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def update(db: Session, data: schema.User):
    user = get(db, data.id)

    user.name = data.name
    user.email = data.email
    db.commit()
    db.refresh(user)

    return user

def delete(db: Session, data: schema.User):
    user = get(db, data.id)

    db.delete(user)
    db.commit()

    return user