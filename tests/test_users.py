from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={
            "username": "pytest_user",
            "email": "pytest@example.com"
        }
    )
    assert response.status_code == 201
    assert response.json()["username"] == "pytest_user"
    assert response.json()["email"] == "pytest@example.com"

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(
        response.json(),
        list
    )

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code in [200, 404]

def test_invalid_email():
    response = client.post(
        "/users/",
        json={
            "username": "bad",
            "email": "banana"
        }
    )
    assert response.status_code == 422

def test_missing_fields():
    response = client.post(
        "/users/",
        json={}
    )
    assert response.status_code == 422