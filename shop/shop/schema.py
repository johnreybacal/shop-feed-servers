from pydantic import BaseModel

class Shop(BaseModel):
    id: int | None
    name: str