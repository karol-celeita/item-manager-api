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

# Test para el endpoint de listado de items
def test_list_items():
    # Crear algunos items de prueba usando Faker
    for _ in range(5):
        client.post("/api/v1/create/", json={"name": faker.name(), "price": faker.random_number(digits=2)})

    response = client.get("/api/v1/list/")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) >= 5  # Comprueba que al menos hay 5 items
    for item in data["items"]:
        assert "id" in item
        assert "name" in item
        assert "price" in item
        assert "created_at" in item
        assert "updated_at" in item