import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "running" in r.get_json()["message"]


def test_health(client):
    r = client.get("/health")
    assert r.get_json() == {"status": "ok"}


def test_add_and_list_task(client):
    r = client.post("/tasks", json={"title": "Write report"})
    assert r.status_code == 201
    r = client.get("/tasks")
    assert any(t["title"] == "Write report" for t in r.get_json())


def test_add_task_without_title(client):
    r = client.post("/tasks", json={})
    assert r.status_code == 200


def test_delete_task(client):
    tid = client.post("/tasks", json={"title": "Temp"}).get_json()["id"]
    assert client.delete(f"/tasks/{tid}").status_code == 200
    assert client.delete(f"/tasks/{tid}").status_code == 404
