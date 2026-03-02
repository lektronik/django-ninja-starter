import pytest
from django.test import Client
from features.models import Product

@pytest.mark.django_db
def test_health_check(client: Client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.django_db
def test_product_list(client: Client):
    # Setup
    Product.objects.create(name="Test Product", price=10.99)
    
    # Test
    response = client.get("/api/products/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Test Product"
    assert data[0]["price"] == "10.99"

@pytest.mark.django_db
def test_user_registration(client: Client):
    payload = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "securepassword123"
    }
    response = client.post("/api/auth/register", data=payload, content_type="application/json")
    
    # Assert successful creation
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "newuser"
    assert data["email"] == "newuser@example.com"
    assert "id" in data
    
    # Assert conflict on duplicate username
    response2 = client.post("/api/auth/register", data=payload, content_type="application/json")
    assert response2.status_code == 400
    assert "already exists" in response2.json()["detail"]
