from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core.utils import get_db
from menuapp import service
from menuapp.schemas import BaseMenu, PatchMenu, BaseSubMenu, PatchSubMenu

router = APIRouter()


@router.get("/api/v1/menus", response_model=List[BaseMenu])
def menu_list(db: Session = Depends(get_db)):
    return service.get_menu_list(db)


@router.get("/api/v1/menus/{menu_id}", response_model=BaseMenu)
def detail_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = service.get_menu_by_id(db=db, menu_id=menu_id)
    if menu is None:
        raise HTTPException(status_code=404, detail="menu not found")
    return menu


@router.post("/api/v1/menus", response_model=BaseMenu, status_code=status.HTTP_201_CREATED)
def menu_create(item: BaseMenu, db: Session = Depends(get_db)):
    return service.create_menu(db, item)


@router.patch("/api/v1/menus/{menu_id}", response_model=PatchMenu)
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


@router.get("/api/v1/menus/{menu_id}/submenus", response_model=List[BaseSubMenu])
def submenu_list(menu_id: int, db: Session = Depends(get_db)):
    submenus = service.get_submenu_list(db=db, menu_id=menu_id)
    return submenus


@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=BaseSubMenu)
def detail_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    db_submenu = service.get_submenu_by_id(db=db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu


@router.post('/api/v1/menus/{menu_id}/submenus', response_model=BaseSubMenu,
             status_code=status.HTTP_201_CREATED)
def create_submenu(menu_id: int, submenu: BaseSubMenu, db: Session = Depends(get_db)):
    db_submenu = service.get_submenu_by_title(db=db, submenu_title=submenu.title)
    if db_submenu:
        raise HTTPException(status_code=400, detail="submenu already exists")
    else:
        return service.create_submenu(db=db, submenu=submenu, menu_id=menu_id)


@router.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=BaseSubMenu)
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

