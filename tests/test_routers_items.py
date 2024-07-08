# tests/test_routers_items.py
from fastapi.testclient import TestClient
from app.main import app
from faker import Faker

client = TestClient(app)
faker = Faker()

# Test para el endpoint de ping
def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong"}

# Test para el endpoint de creación de item
def test_create_item():
    item_data = {
        "name": faker.name(),
        "price": faker.random_number(digits=2)
    }
    response = client.post(
        "/api/v1/create/",
        json=item_data
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["price"] == item_data["price"]
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data

