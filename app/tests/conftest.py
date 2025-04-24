from app.main import app
from fastapi.testclient import TestClient
from database import get_db
from unittest.mock import MagicMock

mock_db = MagicMock()

app.dependency_overrides[get_db] = lambda: mock_db

client = TestClient(app)


