from pydantic import BaseModel


class BaseMenu(BaseModel):
    title: str | None
    description: str | None


class PatchMenu(BaseMenu):
    pass


class CreateMenu(BaseMenu):
    submenus_count: int = 0
    dishes_count: int = 0


class Menu(BaseMenu):
    id: str
    submenus_count: int
    dishes_count: int

    class Config:
        orm_mode = True


class BaseSubMenu(BaseModel):
    title: str
    description: str | None


class SubMenu(BaseSubMenu):
    id: str
    dishes_count: int

    class Config:
        orm_mode = True


class PatchSubMenu(BaseSubMenu):
    pass


class SubMenuCreate(BaseSubMenu):
    dishes_count: int = 0


class DishBase(BaseModel):
    title: str
    description: str | None
    price: str | None


class DishCreate(DishBase):
    pass


class DishUpdate(DishBase):
    pass


class Dish(DishBase):
    id: str

    class Config:
        orm_mode = True
