from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="E-Commerce Backend API",
    version="1.0.0"
)

app.include_router(health_router)
