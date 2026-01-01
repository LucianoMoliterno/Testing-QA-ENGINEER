"""
Pruebas de API para usuarios
"""
import pytest
from utils.api_utils import APIClient


BASE_URL = "https://reqres.in"


@pytest.fixture
def api_client():
    """Fixture para crear una instancia del cliente API"""
    return APIClient(BASE_URL)


def _retry_or_skip_reqres_page1(api_client: APIClient, endpoint: str, params: dict):
    """Helper para reintentar llamadas a ReqRes page=1 y skip si persiste 401/403/429."""
    response = api_client.get(endpoint, params=params)
    if response.status_code in (401, 403, 429):
        retry_headers = {
            "Referer": "https://reqres.in/",
            "User-Agent": "pre-entrega-automation-tests/1.0 (+https://example.com)",
            "Accept": "application/json",
        }
        response = api_client.get(endpoint, params=params, headers=retry_headers)
        if response.status_code in (401, 403, 429):
            pytest.skip(f"ReqRes devolvió {response.status_code} para page=1. Skip por bloqueo temporal del servicio externo.")
    return response


def test_get_users_page_1(api_client):
    """
    Obtiene la lista de usuarios de la página 1
    Valida que cada usuario tenga las claves: id, email, first_name, last_name
    Extra: valida que el avatar termina en .jpg
    """
    # Realizar petición GET a /api/users?page=1 (con manejo de bloqueos temporales)
    response = _retry_or_skip_reqres_page1(api_client, "/api/users", {"page": 1})

    # Validar código de estado
    api_client.validate_status_code(response, 200)

    # Obtener respuesta JSON
    response_json = response.json()

    # Validar que exista la clave 'data'
    assert "data" in response_json, "Clave 'data' no encontrada en respuesta"

    users = response_json["data"]
    assert len(users) > 0, "No se encontraron usuarios en la respuesta"

    # Validar cada usuario
    required_keys = ["id", "email", "first_name", "last_name"]

    for user in users:
        # Validar claves requeridas
        for key in required_keys:
            assert key in user, f"Clave '{key}' no encontrada en usuario {user.get('id', 'unknown')}"

        # Validar que los valores no estén vacíos
        assert user["id"], "ID del usuario esta vacio"
        assert user["email"], "Email del usuario esta vacio"
        assert user["first_name"], "First name del usuario esta vacio"
        assert user["last_name"], "Last name del usuario esta vacio"

        # Extra: Validar que el avatar termina en .jpg
        if "avatar" in user:
            assert user["avatar"].endswith(".jpg"), \
                f"Avatar del usuario {user['id']} no termina en .jpg: {user['avatar']}"

        print(f"\n[OK] Usuario validado: {user['first_name']} {user['last_name']} - {user['email']}")

    print(f"\n[OK] Total de usuarios validados: {len(users)}")


def test_get_users_structure(api_client):
    """Valida la estructura completa de la respuesta de usuarios"""
    # GET a page=1 con manejo de bloqueos
    response = _retry_or_skip_reqres_page1(api_client, "/api/users", {"page": 1})

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()

    # Validar estructura principal
    expected_main_keys = ["page", "per_page", "total", "total_pages", "data"]
    api_client.validate_json_keys(response_json, expected_main_keys)

    # Validar que page sea 1
    assert response_json["page"] == 1, "Page debe ser 1"

    # Validar que hay datos
    assert len(response_json["data"]) > 0, "La lista de usuarios esta vacia"

    print(f"\n[OK] Estructura validada correctamente")
    print(f"  - Pagina: {response_json['page']}")
    print(f"  - Por pagina: {response_json['per_page']}")
    print(f"  - Total: {response_json['total']}")
    print(f"  - Total paginas: {response_json['total_pages']}")


@pytest.mark.parametrize("page", [1, 2])
def test_get_users_multiple_pages(api_client, page):
    """Prueba parametrizada para obtener usuarios de diferentes páginas"""
    if page == 1:
        response = _retry_or_skip_reqres_page1(api_client, "/api/users", {"page": page})
    else:
        response = api_client.get("/api/users", params={"page": page})

    api_client.validate_status_code(response, 200)

    response_json = response.json()
    users = response_json["data"]

    # Validar que todos los usuarios tengan avatar con .jpg
    for user in users:
        assert "avatar" in user, f"Usuario {user['id']} no tiene avatar"
        assert user["avatar"].endswith(".jpg"), \
            f"Avatar no termina en .jpg: {user['avatar']}"

    print(f"\n[OK] Pagina {page} validada con {len(users)} usuarios")


def test_get_single_user(api_client):
    """Obtiene y valida un usuario individual"""
    user_id = 2
    response = api_client.get(f"/api/users/{user_id}")

    api_client.validate_status_code(response, 200)

    response_json = response.json()
    assert "data" in response_json, "Clave 'data' no encontrada"

    user = response_json["data"]
    required_keys = ["id", "email", "first_name", "last_name", "avatar"]

    for key in required_keys:
        assert key in user, f"Clave '{key}' no encontrada en usuario"

    # Validar avatar termina en .jpg
    assert user["avatar"].endswith(".jpg"), "Avatar no termina en .jpg"

    print(f"\n[OK] Usuario individual validado: {user['first_name']} {user['last_name']}")
