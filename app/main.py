from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="Marketplace Processor")

app.include_router(router)
