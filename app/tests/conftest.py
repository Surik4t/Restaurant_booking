import pytest
from unittest.mock import MagicMock
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.main import app
from database import Base, get_db

# Реальная БД для тестов бронирования
@pytest.fixture
def test_db_client():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={
           "check_same_thread": False,
       },
        poolclass=StaticPool
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    Base.metadata.drop_all(engine)


# Моки для остальных тестов
@pytest.fixture
def mock_db_client():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    yield TestClient(app)
    app.dependency_overrides.clear()
