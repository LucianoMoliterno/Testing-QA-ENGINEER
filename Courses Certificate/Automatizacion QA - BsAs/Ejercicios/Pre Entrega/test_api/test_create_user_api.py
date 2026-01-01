"""
Pruebas de API para creación de usuarios
"""
import pytest
from utils.api_utils import APIClient


BASE_URL = "https://reqres.in"


@pytest.fixture
def api_client():
    """Fixture para crear una instancia del cliente API"""
    return APIClient(BASE_URL)


@pytest.mark.parametrize("name,job,expected_status", [
    ("John Doe", "Developer", 201),
    ("Jane Smith", "QA Engineer", 201),
    ("Bob Johnson", "Product Manager", 201),
])
def test_create_user_parametrizado(api_client, name, job, expected_status):
    """
    Prueba parametrizada para crear usuarios
    Valida que el usuario se crea correctamente y retorna id y createdAt
    """
    payload = {
        "name": name,
        "job": job
    }

    # Realizar petición POST para crear usuario
    response = api_client.post("/api/users", json=payload)

    # Validar código de estado
    api_client.validate_status_code(response, expected_status)

    # Obtener respuesta JSON
    response_json = response.json()

    # Validar que la respuesta contenga las claves esperadas
    required_keys = ["name", "job", "id", "createdAt"]
    api_client.validate_json_keys(response_json, required_keys)

    # Validar que los valores coinciden con los enviados
    assert response_json["name"] == name, f"Expected name '{name}', got '{response_json['name']}'"
    assert response_json["job"] == job, f"Expected job '{job}', got '{response_json['job']}'"

    # Validar que se generó un ID
    assert "id" in response_json, "ID no generado"
    assert response_json["id"] is not None, "ID es None"

    # Validar que se generó createdAt
    assert "createdAt" in response_json, "createdAt no generado"
    assert response_json["createdAt"] is not None, "createdAt es None"

    print(f"\n[OK] Usuario creado exitosamente:")
    print(f"  - ID: {response_json['id']}")
    print(f"  - Nombre: {response_json['name']}")
    print(f"  - Trabajo: {response_json['job']}")
    print(f"  - Creado: {response_json['createdAt']}")


def test_create_user_simple(api_client):
    """Prueba simple de creación de usuario"""
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = api_client.post("/api/users", json=payload)

    # Validaciones
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    response_json = response.json()
    assert response_json["name"] == "morpheus"
    assert response_json["job"] == "leader"
    assert "id" in response_json
    assert "createdAt" in response_json

    print(f"\n[OK] Usuario 'morpheus' creado con ID: {response_json['id']}")


def test_update_user(api_client):
    """Prueba de actualización de usuario con PUT"""
    user_id = 2
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = api_client.put(f"/api/users/{user_id}", json=payload)

    # Validar código de estado
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()

    # Validar que la respuesta contiene los datos actualizados
    assert response_json["name"] == "morpheus"
    assert response_json["job"] == "zion resident"
    assert "updatedAt" in response_json

    print(f"\n[OK] Usuario {user_id} actualizado exitosamente")
    print(f"  - Actualizado: {response_json['updatedAt']}")


@pytest.mark.parametrize("user_id,expected_status", [
    (2, 204),
    (5, 204),
])
def test_delete_user(api_client, user_id, expected_status):
    """Prueba parametrizada para eliminar usuarios"""
    response = api_client.delete(f"/api/users/{user_id}")

    # Validar código de estado (204 No Content)
    api_client.validate_status_code(response, expected_status)

    print(f"\n[OK] Usuario {user_id} eliminado exitosamente (Status: {response.status_code})")


def test_create_user_without_job(api_client):
    """Prueba de creación de usuario sin campo job"""
    payload = {
        "name": "Test User"
    }

    response = api_client.post("/api/users", json=payload)

    # La API igualmente permite crear el usuario
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    response_json = response.json()
    assert "id" in response_json
    assert "createdAt" in response_json

    print(f"\n[OK] Usuario creado sin job - ID: {response_json['id']}")
