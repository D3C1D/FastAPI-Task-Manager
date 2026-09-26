from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post(
        "/tasks/",
        json={
            "title": "Pytest Task",
            "description": "Testing",
            "user_id": 1
        }
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Pytest Task"

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(
        response.json(),
        list
    )

def test_get_task():
    response = client.get("/tasks/1")
    assert response.status_code in [200, 404]

def test_update_task():
    response = client.put(
        "/tasks/1",
        json={
            "completed": True
        }
    )
    assert response.status_code in [200, 404]

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code in [200, 404]