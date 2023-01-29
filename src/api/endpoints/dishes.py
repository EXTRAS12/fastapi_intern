from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core.utils import get_db
from src.menuapp import service
from src.menuapp.schemas import Dish, DishCreate, DishUpdate

router = APIRouter()


@router.post(
    '/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes',
    response_model=Dish,
    status_code=201,
    summary='Создать блюдо',
)
def create_dish(
    menu_id: int,
    submenu_id: int,
    dish: DishCreate,
    db: Session = Depends(get_db),
):
    db_dish = service.get_dish_by_title(db=db, dish_title=dish.title)
    if db_dish:
        raise HTTPException(status_code=400, detail='dish already exists')
    else:
        return service.create_dish(
            db=db,
            dish=dish,
            menu_id=menu_id,
            submenu_id=submenu_id,
        )


@router.get('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes', response_model=list[Dish], summary='Список блюд')
def dishes_list(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    dishes = service.dishes_list(db=db, submenu_id=submenu_id)
    return dishes


@router.get(
    '/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', response_model=Dish, summary='Конкретное блюдо',
)
def detail_dish(
    menu_id: int,
    submenu_id: int,
    dish_id: int,
    db: Session = Depends(get_db),
):
    db_dish = service.get_dish_by_id(db=db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail='dish not found')
    return db_dish


@router.patch(
    '/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', response_model=Dish, summary='Обновить блюдо',
)
def update_dish(
    menu_id: int,
    submenu_id: int,
    dish_id: int,
    dish: DishUpdate,
    db: Session = Depends(get_db),
):
    db_dish = service.get_dish_by_id(db=db, dish_id=dish_id)
    if db_dish:
        db_dish.title = dish.title
        db_dish.description = dish.description
        db_dish.price = dish.price
        return service.update_dish(db=db, dish_id=dish_id)
    else:
        raise HTTPException(status_code=404, detail='dish not found')


@router.delete('/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', summary='Удалить блюдо')
def delete_dish(
    menu_id: int,
    submenu_id: int,
    dish_id: int,
    db: Session = Depends(get_db),
):
    db_dish = service.delete_dish(
        db=db,
        dish_id=dish_id,
        menu_id=menu_id,
        submenu_id=submenu_id,
    )
    if db_dish is None:
        raise HTTPException(status_code=404, detail='dish not found')
    return {'status': True, 'message': 'The dish has been deleted'}
