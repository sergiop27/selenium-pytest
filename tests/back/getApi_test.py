import pytest
from api.api_client import ApiClient

@pytest.mark.back
def test_get_usuario_exitoso():
    client = ApiClient()
    response = client.get("/users/2")

    assert response.status_code == 200

    data = response.json()
    assert data["data"]["id"] == 2
    assert data["data"]["first_name"] == "Janet"
    assert data["data"]["email"].endswith("@reqres.in")

@pytest.mark.back
def test_get_usuario_inexistente():
    client = ApiClient()
    response = client.get("/users/999")

    assert response.status_code == 404