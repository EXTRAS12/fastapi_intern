import pytest
from fastapi.testclient import TestClient

from src.db.database import db_init
from src.main import app


@pytest.fixture(scope='module')
def client():
    db_init()
    client = TestClient(app=app)
    yield client
