"""
Utilidades para pruebas de API
"""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


class APIClient:
    """Cliente base para interactuar con APIs"""

    def __init__(self, base_url, timeout: float = 10.0):
        """
        Inicializa el cliente de API
        :param base_url: URL base de la API
        :param timeout: Timeout por defecto para las requests
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = timeout

        # Cabeceras por defecto (algunas APIs públicas fallan sin un User-Agent)
        self.session.headers.update({
            "User-Agent": "pre-entrega-automation-tests/1.0 (+https://example.com)",
            "Accept": "application/json",
        })

        # Configurar reintentos con backoff para errores transitorios
        retries = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[401, 403, 408, 425, 429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"],
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def _full_url(self, endpoint: str) -> str:
        # Asegura que no se dupliquen las barras
        if endpoint.startswith("http://") or endpoint.startswith("https://"):
            return endpoint
        return f"{self.base_url}{endpoint}"

    def get(self, endpoint, params=None, headers=None):
        """
        Realiza una petición GET
        :param endpoint: Endpoint de la API
        :param params: Parámetros de consulta
        :param headers: Headers adicionales
        :return: Response object
        """
        url = self._full_url(endpoint)
        # Limpiar cookies entre llamadas para evitar estados inesperados
        self.session.cookies.clear()
        response = self.session.get(url, params=params, headers=headers, timeout=self.timeout)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        """
        Realiza una petición POST
        :param endpoint: Endpoint de la API
        :param data: Datos del formulario
        :param json: Datos en formato JSON
        :param headers: Headers adicionales
        :return: Response object
        """
        url = self._full_url(endpoint)
        response = self.session.post(url, data=data, json=json, headers=headers, timeout=self.timeout)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        """
        Realiza una petición PUT
        :param endpoint: Endpoint de la API
        :param data: Datos del formulario
        :param json: Datos en formato JSON
        :param headers: Headers adicionales
        :return: Response object
        """
        url = self._full_url(endpoint)
        response = self.session.put(url, data=data, json=json, headers=headers, timeout=self.timeout)
        return response

    def patch(self, endpoint, data=None, json=None, headers=None):
        """
        Realiza una petición PATCH
        :param endpoint: Endpoint de la API
        :param data: Datos del formulario
        :param json: Datos en formato JSON
        :param headers: Headers adicionales
        :return: Response object
        """
        url = self._full_url(endpoint)
        response = self.session.patch(url, data=data, json=json, headers=headers, timeout=self.timeout)
        return response

    def delete(self, endpoint, headers=None):
        """
        Realiza una petición DELETE
        :param endpoint: Endpoint de la API
        :param headers: Headers adicionales
        :return: Response object
        """
        url = self._full_url(endpoint)
        response = self.session.delete(url, headers=headers, timeout=self.timeout)
        return response

    def validate_status_code(self, response, expected_status):
        """
        Valida el código de estado de la respuesta
        :param response: Objeto response
        :param expected_status: Código de estado esperado
        """
        assert response.status_code == expected_status, \
            f"Expected status code {expected_status}, but got {response.status_code}"

    def validate_json_keys(self, json_data, expected_keys):
        """
        Valida que el JSON tenga las claves esperadas
        :param json_data: Datos JSON
        :param expected_keys: Lista de claves esperadas
        """
        for key in expected_keys:
            assert key in json_data, f"Key '{key}' not found in response"
