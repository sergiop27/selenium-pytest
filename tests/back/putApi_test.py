import pytest
from api.api_client import ApiClient

@pytest.mark.back
def test_put_actualizar_usuario():
    client = ApiClient()

    payload = {
        "name": "SERGIO",
        "job": "QA Lead"
    }

    response = client.put("/users/2", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["job"] == "QA Lead"
    assert "updatedAt" in data
