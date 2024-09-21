from uuid import uuid4
from sqlalchemy import Column, text, types
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base

class Shop(Base):
    __tablename__ = "shops"

    id = Column(types.Uuid, primary_key=True, default=uuid4)

    name = Column(types.String)