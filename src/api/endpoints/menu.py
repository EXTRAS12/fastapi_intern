import time

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_cache.decorator import cache
from sqlalchemy.orm import Session

from src.core.utils import get_db
from src.menuapp import service
from src.menuapp.schemas import CreateMenu, Menu, PatchMenu

router = APIRouter()


@router.get('/long/', summary='Проверяем работу кэша')
@cache(expire=30)
def get_long():
    time.sleep(4)
    return 'Пробуем работу кэш'


@router.get('/api/v1/menus', response_model=list[Menu], summary='Список меню')
@cache(expire=30)
def menu_list(db: Session = Depends(get_db)):
    return service.get_menu_list(db)


@router.get('/api/v1/menus/{menu_id}', response_model=Menu, summary='Конкретное меню')
@cache(expire=30)
def detail_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = service.get_menu_by_id(db=db, menu_id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail='menu not found')
    return menu


@router.post('/api/v1/menus', response_model=Menu, status_code=status.HTTP_201_CREATED, summary='Создать меню')
def menu_create(item: CreateMenu, db: Session = Depends(get_db)):
    return service.create_menu(db, item)


@router.patch('/api/v1/menus/{menu_id}', response_model=Menu, summary='Обновить меню')
def update_menu(menu_id: int, item: PatchMenu, db: Session = Depends(get_db)):
    menu = service.get_menu_by_id(db=db, menu_id=menu_id)
    if menu:
        menu.title = item.title
        menu.description = item.description
        return service.update_menu(db=db, menu_id=menu_id)
    else:
        raise HTTPException(status_code=404, detail='menu not found')


@router.delete('/api/v1/menus/{menu_id}', status_code=status.HTTP_200_OK, summary='Удалить меню')
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = service.delete_menu(db=db, menu_id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail='menu not found')
    return {'status': True, 'message': 'The menu has been deleted'}
