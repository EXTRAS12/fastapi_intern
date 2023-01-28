from fastapi import APIRouter

from .endpoints import dishes, menu, submenu

routes = APIRouter()

routes.include_router(menu.router, tags=['Меню'])
routes.include_router(submenu.router, tags=['Подменю'])
routes.include_router(dishes.router, tags=['Блюдо'])
