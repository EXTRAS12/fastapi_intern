from sqlalchemy.orm import Session

from menuapp.models import Menu, SubMenu, Dish
from .schemas import *


"""MENU SECTION"""


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


def get_menu_by_title(db: Session, menu_title: str):
    return db.query(Menu).filter(Menu.title == menu_title).first()


"""SUBMENU SECTION"""


def get_submenu_list(menu_id: int, db: Session):
    return db.query(SubMenu).filter(SubMenu.menu_id == menu_id).all()


def get_submenu_by_id(db: Session, submenu_id: int):
    return db.query(SubMenu).filter(SubMenu.id == submenu_id).first()


def create_submenu(db: Session, submenu: BaseSubMenu, menu_id: int):
    db_submenu = SubMenu(**submenu.dict())
    db_submenu.menu_id = menu_id
    get_menu_by_id(db=db, menu_id=menu_id).submenus_count += 1
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return db_submenu


def delete_submenu(db: Session, menu_id: int, submenu_id: int):
    submenu = get_submenu_by_id(db, submenu_id)
    if submenu is None:
        return None
    else:
        menu = get_menu_by_id(db=db, menu_id=menu_id)
        menu.submenus_count -= 1
        menu.dishes_count -= submenu.dishes_count
        db.delete(submenu)
        db.commit()
        return True


def update_submenu(db: Session, submenu_id: int):
    db.commit()
    return get_submenu_by_id(db=db, submenu_id=submenu_id)


def get_submenu_by_title(db: Session, submenu_title: str):
    return db.query(SubMenu).filter(SubMenu.title == submenu_title).first()


def get_submenus_count(db: Session, menu_id):
    return db.query(SubMenu).filter(SubMenu.menu_id == menu_id).count()


"""DISH SECTION"""


def get_dish_by_id(db: Session, dish_id: int):
    return db.query(Dish).filter(Dish.id == dish_id).first()


def get_dish_by_title(db: Session, dish_title: str):
    return db.query(Dish).filter(Dish.title == dish_title).first()


def get_dishes_count(db: Session, submenu_id):
    return db.query(Dish).filter(Dish.submenu_id == submenu_id).count()
