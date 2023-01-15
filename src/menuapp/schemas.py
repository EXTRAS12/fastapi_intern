from typing import Optional

from pydantic import BaseModel


class BaseMenu(BaseModel):
    id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    dishes_count: Optional[int]
    submenus_count: Optional[int]

    class Config:
        orm_mode = True


class PatchMenu(BaseMenu):
    title: str
    description: str
    dishes_count: Optional[int]


class CreateMenu(BaseModel):
    title: Optional[str]
    description: Optional[str]


class BaseSubMenu(BaseModel):
    id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    dishes_count: Optional[int]

    class Config:
        orm_mode = True


class PatchSubMenu(BaseSubMenu):
    title: Optional[str]
    description: Optional[str]


class Dish(BaseModel):
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    price: Optional[str]

    class Config:
        orm_mode = True


class UpgradeDish(Dish):
    title: str
    description: str
    price: float
