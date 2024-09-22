from pydantic import BaseModel
from uuid import UUID

class User(BaseModel):
    id: UUID
    name: str
    email: str

class UserMutation(BaseModel):
    event_type: str
    user: User

    def __init__(self, dictionary: dict):
        dictionary["event_type"] = dictionary.pop("eventType")
        self.__dict__.update(dictionary)