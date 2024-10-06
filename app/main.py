# app/main.py

from fastapi import FastAPI
from app.routers import recommendations, users

app = FastAPI()

# Include routers
app.include_router(recommendations.router)
app.include_router(users.router)
