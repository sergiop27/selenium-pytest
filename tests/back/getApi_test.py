import requests
import pytest

BASE_URL = "https://reqres.in/api"
API_KEY = "reqres-free-v1"

@pytest.mark.back
def test_get_user_exitoso():
    """
    Consulta un usuario existente y valida que responda 200 y datos correctos.
    """
    headers = {
        "x-api-key": API_KEY
    }
    response = requests.get(f"{BASE_URL}/users/2", headers=headers)

    assert response.status_code == 200

    data = response.json()
    assert data["data"]["id"] == 2
    assert data["data"]["first_name"] == "Janet"
    assert data["data"]["email"].endswith("@reqres.in")


@pytest.mark.back
def test_get_user_inexistente_devuelve_404():
    """
    Consulta un usuario que no existe y valida que responda 404.
    """
    headers = {
        "x-api-key": API_KEY
    }
    response = requests.get(f"{BASE_URL}/users/99999", headers=headers)

    assert response.status_code == 404