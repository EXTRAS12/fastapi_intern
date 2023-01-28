from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.db.database import Base


class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    submenus_count = Column(Integer, default=0)
    dishes_count = Column(Integer, default=0)

    submenus = relationship(
        'SubMenu', back_populates='menu', cascade='all, delete-orphan'
    )


class SubMenu(Base):
    __tablename__ = 'submenus'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    menu_id = Column(Integer, ForeignKey('menus.id'))
    dishes_count = Column(Integer, default=0)

    menu = relationship('Menu', back_populates='submenus')
    dishes = relationship(
        'Dish', back_populates='submenu', cascade='all, delete-orphan'
    )


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float(round(2)))
    submenu_id = Column(Integer, ForeignKey('submenus.id'))

    submenu = relationship('SubMenu', back_populates='dishes')
