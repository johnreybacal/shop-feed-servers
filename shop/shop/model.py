from uuid import uuid4
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.database import Base
from user.model import User

class Shop(Base):
    __tablename__ = "shops"

    id = Column(types.Uuid, primary_key=True, default=uuid4)

    name = Column(types.String)

    owner_id: Mapped[types.Uuid] = mapped_column(ForeignKey("users.id"))

    owner: Mapped[User] = relationship()