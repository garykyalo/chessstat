from fastapi import FastAPI
from .routes import router as app_router

def create_app() -> FastAPI:
    app = FastAPI()
 
    app.include_router(app_router)
    return app
