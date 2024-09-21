from fastapi import APIRouter, HTTPException
from shop.schema import Shop

router = APIRouter(prefix="/shops")

shops = []

for i in range(1, 10):
    shops.append(Shop(id=i, name="Shop " + str(i)))

def getShopById(id: int):
    shop = [shop for shop in shops if shop.id == id]

    if len(shop) == 0:
        raise HTTPException(status_code=404, detail="Shop not found")
    else:
        return shop[0]

@router.get("/")
def list(name: str = None):
    # TODO: filter by name if present
    return shops

@router.get("/{id}")
def get(id: int):
    return getShopById(id)

@router.post("/", status_code=201)
def create(shop: Shop):
    shop.id = len(shops) + 1
    shops.append(shop)

    return {
        "message": "Shop has been created",
        "shop": shop
    }

@router.put("/{id}")
def update(id: int, shop: Shop):
    shopToUpdate: Shop = getShopById(id)
    shopToUpdate.name = shop.name

    return {
        "message": "Shop has been updated",
        "shop": shopToUpdate
    }

@router.delete("/{id}")
def delete(id: int):
    shopToDelete = getShopById(id)
    shops.remove(shopToDelete)

    return {
        "message": "Shop has been deleted",
        "shop": shopToDelete
    }






