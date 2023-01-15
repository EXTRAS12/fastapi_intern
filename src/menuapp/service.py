from sqlalchemy.orm import Session

from menuapp.models import Menu, SubMenu, Dish
from .schemas import *


def get_menu_list(db: Session):
    return db.query(Menu).all()


def get_menu_by_id(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()


def create_menu(db: Session, item: BaseMenu):
    menu = Menu(**item.dict())
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu


def update_menu(db: Session, menu_id: int):
    db.commit()
    return get_menu_by_id(db=db, menu_id=menu_id)


def delete_menu(db: Session, menu_id: int):
    menu = db.query(Menu).filter(Menu.id == menu_id).first()
    if menu is None:
        return None
    else:
        db.delete(menu)
        db.commit()
        return True
