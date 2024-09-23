from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from shop.schema import ShopPayload
from . import repository
from db.database import get_db
from uuid import UUID

router = APIRouter(prefix="/shops")

def getShopById(id: UUID, db: Session):
    shop = repository.get(db, id)

    if shop is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    else:
        return shop

@router.get("/")
def list(db: Session = Depends(get_db)):
    '''
    Returns a list of shops
    '''
    return repository.list(db)

@router.get("/{id}")
def get(id: UUID, db: Session = Depends(get_db)):
    '''
    Returns a specific shop based on the supplied `id`
    '''
    shop = getShopById(id, db)

    # Load owner
    shop.owner

    return shop

@router.post("/", status_code=201)
def create(payload: ShopPayload, db: Session = Depends(get_db)):
    '''
    Create a shop with the given `payload`
    '''
    shop = repository.create(db, payload)

    return {
        "message": "Shop has been created",
        "shop": shop
    }

@router.put("/{id}")
def update(id: UUID, payload: ShopPayload, db: Session = Depends(get_db)):
    '''
    Update a shop with the given `payload` based on the supplied `id`
    '''
    shop = repository.update(db, id, payload)

    return {
        "message": "Shop has been updated",
        "shop": shop
    }

@router.delete("/{id}")
def delete(id: UUID, db: Session = Depends(get_db)):
    '''
    Delete a shop based on the supplied `id`
    '''
    shop = repository.delete(db, id)

    return {
        "message": "Shop has been deleted",
        "shop": shop
    }






