from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Smart Code Reviewer")

app.include_router(router)
