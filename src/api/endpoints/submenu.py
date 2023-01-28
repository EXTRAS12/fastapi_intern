from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core.utils import get_db
from src.menuapp import service
from src.menuapp.schemas import PatchSubMenu, SubMenu, SubMenuCreate

router = APIRouter()


@router.get("/api/v1/menus/{menu_id}/submenus", response_model=list[SubMenu], summary="Список подменю")
def submenu_list(menu_id: int, db: Session = Depends(get_db)):
    submenus = service.get_submenu_list(db=db, menu_id=menu_id)
    return submenus


@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=SubMenu, summary="Конкретное подменю")
def detail_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    db_submenu = service.get_submenu_by_id(db=db, submenu_id=submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu


@router.post("/api/v1/menus/{menu_id}/submenus", response_model=SubMenu, status_code=201, summary="Создать подменю")
def create_submenu(menu_id: int, submenu: SubMenuCreate, db: Session = Depends(get_db)):
    db_submenu = service.get_submenu_by_title(
        db=db,
        submenu_title=submenu.title,
    )
    if db_submenu:
        raise HTTPException(status_code=400, detail="submenu already exists")
    else:
        return service.create_submenu(db=db, submenu=submenu, menu_id=menu_id)


@router.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}", response_model=SubMenu, summary="Обновить подменю")
def update_submenu(
    menu_id: int,
    submenu_id: int,
    submenu: PatchSubMenu,
    db: Session = Depends(get_db),
):
    db_submenu = service.get_submenu_by_id(db=db, submenu_id=submenu_id)
    if db_submenu:
        db_submenu.title = submenu.title
        db_submenu.description = submenu.description
        return service.update_submenu(db=db, submenu_id=submenu_id)
    else:
        raise HTTPException(status_code=404, detail="submenu not found")


@router.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}", summary="Удалить подменю")
def delete_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    db_submenu = service.delete_submenu(
        db=db,
        menu_id=menu_id,
        submenu_id=submenu_id,
    )
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return {"status": True, "message": "The submenu has been deleted"}
