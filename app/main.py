from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Marketplace Processor",
    version="1.0.0",
)

app.include_router(router)
