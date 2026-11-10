from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_api_root_endpoint() -> None:
    response = client.get("/api/v1")
    assert response.status_code == 200
    assert response.json()["name"] == "ISMS Review Center API"
