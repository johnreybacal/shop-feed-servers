from uuid import uuid4
from sqlalchemy import Column, types
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(types.Uuid, primary_key=True)

    name = Column(types.String)

    email = Column(types.String)