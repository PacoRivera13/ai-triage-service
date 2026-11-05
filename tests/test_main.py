from fastapi.testclient import TestClient

from app.main import app


def test_health_answers() -> None:
    # The "with" block also runs the app's startup and shutdown code.
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
