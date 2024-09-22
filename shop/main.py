from fastapi import FastAPI
from shop.controller import router as shop_router
from db.database import engine
import shop.model
import asyncio
from user.consumer import consume
from config import loop

shop.model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(shop_router)


loop.create_task(consume())