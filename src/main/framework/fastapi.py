"""
This file contains FastAPI app.
Modify the routes as you wish.
"""

from fastapi import FastAPI

from src.main.routes import health_route


app = FastAPI(
    title=" 🍜 Boilerplate API",
)

app.include_router(health_route)
