from fastapi import APIRouter
from .endpoints import menuapp


routes = APIRouter()

routes.include_router(menuapp.router)
