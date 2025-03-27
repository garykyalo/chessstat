from fastapi import FastAPI
from .routes import router as app_router
from fastapi.staticfiles import StaticFiles

def create_app() -> FastAPI:
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(app_router)
    return app
