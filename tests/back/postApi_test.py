import pytest
from api.api_client import ApiClient

@pytest.mark.back
def test_post_crear_usuario():
    client = ApiClient()

    payload = {
        "name": "SERGIO",
        "job": "Instructor"
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "id" in data
    assert "createdAt" in data
