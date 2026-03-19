import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.database import Base, get_db
from app.db import models

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_create_item():
    response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "Test Description"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "Test Description"
    assert "id" in data


def test_get_items():
    # Create some items first
    client.post("/api/v1/items", json={"name": "Item 1", "description": "Description 1"})
    client.post("/api/v1/items", json={"name": "Item 2", "description": "Description 2"})
    
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_get_item():
    # Create an item
    create_response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "Test Description"},
    )
    item_id = create_response.json()["id"]
    
    # Get the item
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"


def test_update_item():
    # Create an item
    create_response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "Test Description"},
    )
    item_id = create_response.json()["id"]
    
    # Update the item
    response = client.put(
        f"/api/v1/items/{item_id}",
        json={"name": "Updated Item"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Item"


def test_delete_item():
    # Create an item
    create_response = client.post(
        "/api/v1/items",
        json={"name": "Test Item", "description": "Test Description"},
    )
    item_id = create_response.json()["id"]
    
    # Delete the item
    response = client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 204
    
    # Verify it's deleted
    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 404
