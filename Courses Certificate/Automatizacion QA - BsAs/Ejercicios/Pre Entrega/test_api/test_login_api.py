"""
Pruebas parametrizadas de Login API
"""
import pytest
from utils.api_utils import APIClient


BASE_URL = "https://reqres.in"


@pytest.fixture
def api_client():
    """Fixture para crear una instancia del cliente API"""
    return APIClient(BASE_URL)


@pytest.mark.parametrize("email,password,expected_status,validate_token", [
    # Caso exitoso: credenciales válidas
    ("eve.holt@reqres.in", "cityslicka", 200, True),
    # Caso fallido: email sin password
    ("eve.holt@reqres.in", None, 400, False),
])
def test_login_parametrizado(api_client, email, password, expected_status, validate_token):
    """
    Prueba parametrizada de login con diferentes casos
    Valida el código de estado y la presencia del token cuando es exitoso
    """
    # Preparar datos del request
    payload = {"email": email}
    if password is not None:
        payload["password"] = password
    
    # Realizar petición POST a /api/login
    response = api_client.post("/api/login", json=payload)
    
    # Validar código de estado
    api_client.validate_status_code(response, expected_status)
    
    # Obtener respuesta JSON
    response_json = response.json()
    
    # Si se espera validar token (caso exitoso)
    if validate_token:
        assert "token" in response_json, "Token no encontrado en la respuesta"
        assert response_json["token"] is not None, "Token es None"
        assert len(response_json["token"]) > 0, "Token esta vacio"
        print(f"\n[OK] Login exitoso. Token recibido: {response_json['token']}")
    else:
        # Caso fallido: validar que viene un mensaje de error
        assert "error" in response_json, "Se esperaba un mensaje de error"
        print(f"\n[OK] Error esperado: {response_json['error']}")


@pytest.mark.parametrize("email,password", [
    ("eve.holt@reqres.in", "cityslicka"),
])
def test_login_exitoso(api_client, email, password):
    """Prueba de login exitoso con credenciales válidas"""
    payload = {
        "email": email,
        "password": password
    }
    
    response = api_client.post("/api/login", json=payload)
    
    # Validaciones
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    response_json = response.json()
    assert "token" in response_json, "Token no encontrado en respuesta"
    assert response_json["token"], "Token esta vacio"
    
    print(f"\n[OK] Test exitoso - Token: {response_json['token']}")


@pytest.mark.parametrize("email,password,expected_status", [
    ("eve.holt@reqres.in", None, 400),
    ("", "", 400),
])
def test_login_datos_invalidos(api_client, email, password, expected_status):
    """Prueba de login con datos inválidos"""
    payload = {"email": email}
    if password is not None:
        payload["password"] = password
    
    response = api_client.post("/api/login", json=payload)
    
    # Validar código de estado
    assert response.status_code == expected_status, \
        f"Expected status {expected_status}, got {response.status_code}"
    
    response_json = response.json()
    assert "error" in response_json, "Se esperaba un mensaje de error en la respuesta"
    
    print(f"\n[OK] Error esperado capturado: {response_json['error']}")
