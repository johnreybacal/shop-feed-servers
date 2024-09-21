from fastapi import FastAPI
from shop.controller import router as shop_router
app = FastAPI()

app.include_router(shop_router)
