from sqlalchemy import Table, Column, Integer, String, ForeignKey, TEXT, DECIMAL
from src.db.database import metadata

menu = Table(
    "menu",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("title", String, nullable=False, unique=True),
    Column("description", TEXT)
)

submenu = Table(
    "submenu",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("title", String, nullable=False, unique=True),
    Column("description", TEXT),
    Column("menu_id", Integer, ForeignKey("menu.id", ondelete="CASCADE"))
)

dish = Table(
    "dish",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("title", String, nullable=False, unique=True),
    Column("price", DECIMAL(scale=2)),
    Column("description", TEXT),
    Column("submenu_id", Integer, ForeignKey("submenu.id", ondelete="CASCADE"))
)
