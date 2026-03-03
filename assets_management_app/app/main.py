from fastapi import FastAPI

from app.routers import assets

app = FastAPI(title="Asset Management API")

app.include_router(assets.router)
