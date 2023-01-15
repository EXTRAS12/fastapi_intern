from sqlalchemy import Column, Integer, String, ForeignKey, Float
from db.database import Base
from sqlalchemy.orm import relationship


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer(), primary_key=True, index=True)
    title = Column(String(200), nullable=False, unique=True)
    description = Column(String())
    submenus = relationship("SubMenu", cascade="all, delete-orphan")
    submenus_count = Column(Integer, default=0)
    dishes_count = Column(Integer, default=0)


class SubMenu(Base):
    __tablename__ = 'submenu'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False, unique=True)
    description = Column(String)
    menu_id = Column(Integer, ForeignKey('menu.id'))
    menus = relationship("Menu")
    dishes_count = Column(Integer, default=0)
    dish = relationship("Dish", cascade="all, delete-orphan")


class Dish(Base):
    __tablename__ = 'dish'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), unique=True)
    description = Column(String)
    price = Column(Float(round(2)))
    submenu_id = Column(Integer, ForeignKey('submenu.id'))
    menu_id = Column(Integer, ForeignKey('menu.id'))
    submenu = relationship('SubMenu')

