import requests
from typing import Any, Dict, Optional

class ApiClient:
    """
    Cliente HTTP para interactuar con APIs REST.
    Contiene:
    - BASE_URL
    - API_KEY
    - Métodos GET, POST, PUT, DELETE
    """
    BASE_URL = "https://reqres.in/api"
    API_KEY = "reqres_8ed957a1d5874212a513c0c4bc25a5a8"

    def __init__(self):
        self.session = requests.Session()

    def _headers(self, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = {
            "x-api-key": self.API_KEY
        }
        
        if extra_headers:
            headers.update(extra_headers)
        return headers

    def get(self, path: str, params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None):

        url = f"{self.BASE_URL}{path}"
        return self.session.get(url, params=params, headers=self._headers(headers))

    def post(self, path: str, json: Optional[Any] = None,
             headers: Optional[Dict[str, str]] = None):

        url = f"{self.BASE_URL}{path}"
        return self.session.post(url, json=json, headers=self._headers(headers))

    def put(self, path: str, json: Optional[Any] = None,
            headers: Optional[Dict[str, str]] = None):

        url = f"{self.BASE_URL}{path}"
        return self.session.put(url, json=json, headers=self._headers(headers))

    def delete(self, path: str, headers: Optional[Dict[str, str]] = None):
        url = f"{self.BASE_URL}{path}"
        return self.session.delete(url, headers=self._headers(headers))