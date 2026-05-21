from fastapi import FastAPI
from src.api.routers.markets import router

app = FastAPI()

app.include_router(router=router)
