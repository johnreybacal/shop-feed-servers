from sqlalchemy.orm import Session
from db.database import engine
from user.schema import UserMutation
from user import repository

def handle(event: UserMutation):
    user = event.user

    with Session(engine) as db:
        match event.event_type:
            case "CREATED":
                repository.create(db, user)
            case "UPDATED":
                repository.update(db, user)
            case "DELETED":
                repository.delete(db, user)