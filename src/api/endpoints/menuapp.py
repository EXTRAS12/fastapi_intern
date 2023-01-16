from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.utils import get_db
from menuapp import service
from menuapp.schemas import (
    BaseMenu,
    BaseSubMenu,
    CreateMenu,
    Dish,
    DishCreate,
    DishUpdate,
    Menu,
    PatchMenu,
    PatchSubMenu,
    SubMenu,
    SubMenuCreate,
)

router = APIRouter()


@router.get("/api/v1/menus", response_model=List[Menu])
def menu_list(db: Session = Depends(get_db)):
    return service.get_menu_list(db)


@router.get("/api/v1/menus/{menu_id}", response_model=Menu)
def detail_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = service.get_menu_by_id(db=db, menu_id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return menu


@router.post("/api/v1/menus", response_model=Menu, status_code=status.HTTP_201_CREATED)
def menu_create(item: CreateMenu, db: Session = Depends(get_db)):
    return service.create_menu(db, item)


@router.patch("/api/v1/menus/{menu_id}", response_model=Menu)
def update_menu(menu_id: int, item: PatchMenu, db: Session = Depends(get_db)):
    menu = service.get_menu_by_id(db=db, menu_id=menu_id)
    if menu:
        menu.title = item.title
        menu.description = item.description
        return service.update_menu(db=db, menu_id=menu_id)
    else:
        raise HTTPException(status_code=404, detail="menu not found")


@router.delete("/api/v1/menus/{menu_id}", response_model=BaseMenu, status_code=status.HTTP_200_OK)
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = service.delete_menu(db=db, menu_id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return {"status": True, "message": "The menu has been deleted"}


@router.get("/api/v1/menus/{menu_id}/submenus", response_model=List[SubMenu])
def submenu_list(menu_id: int, db: Session = Depends(get_db)):
    submenus = service.get_submenu_list(db=db, menu_id=menu_id)
    return submenus


@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=SubMenu)
def detail_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    db_submenu = service.get_submenu_by_id(db=db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu


@router.post("/api/v1/menus/{menu_id}/submenus", response_model=SubMenu, status_code=201)
def create_submenu(menu_id: int, submenu: SubMenuCreate, db: Session = Depends(get_db)):
    db_submenu = service.get_submenu_by_title(db=db, submenu_title=submenu.title)
    if db_submenu:
        raise HTTPException(status_code=400, detail="submenu already exists")
    else:
        return service.create_submenu(db=db, submenu=submenu, menu_id=menu_id)


@router.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=SubMenu)
def update_submenu(menu_id: int, submenu_id: int, submenu: PatchSubMenu, db: Session = Depends(get_db)):
    db_submenu = service.get_submenu_by_id(db=db, submenu_id=submenu_id)
    if db_submenu:
        db_submenu.title = submenu.title
        db_submenu.description = submenu.description
        return service.update_submenu(db=db, submenu_id=submenu_id)
    else:
        raise HTTPException(status_code=404, detail="submenu not found")


@router.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}")
def delete_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    db_submenu = service.delete_submenu(db=db, menu_id=menu_id, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return {"status": True, "message": "The submenu has been deleted"}


@router.post("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes", response_model=Dish, status_code=201)
def create_dish(menu_id: int, submenu_id: int, dish: DishCreate, db: Session = Depends(get_db)):
    db_dish = service.get_dish_by_title(db=db, dish_title=dish.title)
    if db_dish:
        raise HTTPException(status_code=400, detail="dish already exists")
    else:
        return service.create_dish(db=db, dish=dish, menu_id=menu_id, submenu_id=submenu_id)


@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes", response_model=List[Dish])
def dishes_list(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    dishes = service.dishes_list(db=db, submenu_id=submenu_id)
    return dishes


@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", response_model=Dish)
def detail_dish(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
    db_dish = service.get_dish_by_id(db=db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return db_dish


@router.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", response_model=Dish)
def update_dish(menu_id: int, submenu_id: int, dish_id: int, dish: DishUpdate, db: Session = Depends(get_db)):
    db_dish = service.get_dish_by_id(db=db, dish_id=dish_id)
    if db_dish:
        db_dish.title = dish.title
        db_dish.description = dish.description
        db_dish.price = dish.price
        return service.update_dish(db=db, dish_id=dish_id)
    else:
        raise HTTPException(status_code=404, detail="dish not found")


@router.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
def delete_dish(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
    db_dish = service.delete_dish(db=db, dish_id=dish_id, menu_id=menu_id, submenu_id=submenu_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="dish not found")
    return {"status": True, "message": "The dish has been deleted"}
