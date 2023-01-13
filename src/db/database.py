from databases import Database
from sqlalchemy import create_engine, MetaData
from src.core.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

database = Database(DATABASE_URL)

metadata = MetaData()

engine = create_engine(
    DATABASE_URL,
)
