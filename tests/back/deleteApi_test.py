import pytest
from api.api_client import ApiClient

@pytest.mark.back
def test_delete_usuario():
    client = ApiClient()

    response = client.delete("/users/2")

    assert response.status_code == 204
