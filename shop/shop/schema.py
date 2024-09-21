from pydantic import BaseModel
from uuid import UUID

class ShopPayload(BaseModel):
    name: str

class Shop(ShopPayload):
    id: UUID

    class Config:
        orm_mode = True