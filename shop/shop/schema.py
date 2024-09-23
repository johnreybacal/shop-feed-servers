from pydantic import BaseModel
from uuid import UUID
from user.schema import User

class ShopPayload(BaseModel):
    name: str
    owner_id: UUID

class Shop(ShopPayload):
    id: UUID
    owner: User

    class Config:
        orm_mode = True