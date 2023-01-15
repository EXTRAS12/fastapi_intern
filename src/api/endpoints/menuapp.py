from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core.utils import get_db
from menuapp import service
from menuapp.schemas import BaseMenu, PatchMenu

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
