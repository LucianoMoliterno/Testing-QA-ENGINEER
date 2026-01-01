import pytest
import requests
from utils.logger import Logger

logger = Logger.get_logger(__name__)

class TestAPIJSONPlaceholder:
    """
    Suite de pruebas para API REST usando JSONPlaceholder (https://jsonplaceholder.typicode.com).
    Cubre diferentes métodos HTTP: GET, POST, DELETE, PUT.
    """

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def test_api_get_usuarios_lista(self):
        """
        API Test 1: GET - Obtener lista de usuarios.
        Valida código de estado y estructura de respuesta.
        """
        logger.info("=== Iniciando API Test 1: GET Lista de Usuarios ===")

        # Realizar petición GET
        endpoint = f"{self.BASE_URL}/users"
        response = requests.get(endpoint)

        logger.info(f"Endpoint: {endpoint}")
        logger.info(f"Status Code: {response.status_code}")

        # Validar código de estado
        assert response.status_code == 200, f"Se esperaba 200, se obtuvo {response.status_code}"

        # Validar estructura JSON
        data = response.json()
        assert isinstance(data, list), "La respuesta debe ser una lista"

        # Validar que hay usuarios
        assert len(data) > 0, "La lista de usuarios está vacía"

        # Validar estructura de un usuario
        primer_usuario = data[0]
        assert "id" in primer_usuario, "Usuario no tiene 'id'"
        assert "email" in primer_usuario, "Usuario no tiene 'email'"
        assert "name" in primer_usuario, "Usuario no tiene 'name'"

        logger.info(f"✓ Test exitoso: {len(data)} usuarios obtenidos")
        logger.info(f"Primer usuario: {primer_usuario['name']} ({primer_usuario['email']})")

    def test_api_get_usuario_individual(self):
        """
        API Test 2: GET - Obtener usuario específico por ID.
        """
        logger.info("=== Iniciando API Test 2: GET Usuario Individual ===")

        user_id = 1
        endpoint = f"{self.BASE_URL}/users/{user_id}"
        response = requests.get(endpoint)

        logger.info(f"Endpoint: {endpoint}")
        logger.info(f"Status Code: {response.status_code}")

        # Validaciones
        assert response.status_code == 200, f"Error: código {response.status_code}"

        usuario = response.json()
        assert usuario["id"] == user_id, f"ID incorrecto: esperado {user_id}, obtenido {usuario['id']}"
        assert "name" in usuario, "Usuario no tiene 'name'"
        assert "email" in usuario, "Usuario no tiene 'email'"

        logger.info(f"✓ Usuario obtenido: {usuario['name']}")
        logger.info(f"Email: {usuario['email']}")

    def test_api_get_usuario_no_encontrado(self):
        """
        API Test 3: GET - Caso negativo, usuario que no existe.
        Debe retornar 404.
        """
        logger.info("=== Iniciando API Test 3: GET Usuario No Encontrado (NEGATIVO) ===")

        user_id = 9999
        endpoint = f"{self.BASE_URL}/users/{user_id}"
        response = requests.get(endpoint)

        logger.info(f"Endpoint: {endpoint}")
        logger.info(f"Status Code: {response.status_code}")

        # Validar que retorna 404
        assert response.status_code == 404, f"Se esperaba 404, se obtuvo {response.status_code}"

        logger.info("✓ Test exitoso: Usuario inexistente retorna 404 correctamente")

    def test_api_post_crear_post(self):
        """
        API Test 4: POST - Crear nuevo post.
        Valida código 201 y que el post creado tenga ID.
        """
        logger.info("=== Iniciando API Test 4: POST Crear Post ===")

        endpoint = f"{self.BASE_URL}/posts"

        # Datos del nuevo post
        nuevo_post = {
            "title": "Test Automation - Talento Lab",
            "body": "Este es un test de automatización para el proyecto final",
            "userId": 1
        }

        # Realizar petición POST
        response = requests.post(endpoint, json=nuevo_post)

        logger.info(f"Endpoint: {endpoint}")
        logger.info(f"Datos enviados: {nuevo_post}")
        logger.info(f"Status Code: {response.status_code}")

        # Validaciones
        assert response.status_code == 201, f"Se esperaba 201, se obtuvo {response.status_code}"

        data = response.json()
        assert "id" in data, "Post creado no tiene 'id'"
        assert data["title"] == nuevo_post["title"], "Título no coincide"
        assert data["userId"] == nuevo_post["userId"], "UserId no coincide"

        logger.info(f"✓ Post creado exitosamente con ID: {data['id']}")

    def test_api_delete_post(self):
        """
        API Test 5: DELETE - Eliminar post.
        Debe retornar código 200.
        """
        logger.info("=== Iniciando API Test 5: DELETE Post ===")

        post_id = 1
        endpoint = f"{self.BASE_URL}/posts/{post_id}"

        # Realizar petición DELETE
        response = requests.delete(endpoint)

        logger.info(f"Endpoint: {endpoint}")
        logger.info(f"Status Code: {response.status_code}")

        # Validar código 200
        assert response.status_code == 200, f"Se esperaba 200, se obtuvo {response.status_code}"

        logger.info("✓ Post eliminado exitosamente")

    def test_api_encadenamiento_crear_y_obtener(self):
        """
        API Test 6: ENCADENAMIENTO - Crear post y luego obtener lista.
        Demuestra flujo donde una petición depende de otra.
        """
        logger.info("=== Iniciando API Test 6: Encadenamiento POST + GET ===")

        # Paso 1: Crear post
        endpoint_post = f"{self.BASE_URL}/posts"
        nuevo_post = {
            "title": "QA Automation Framework",
            "body": "Testing con Pytest y Requests",
            "userId": 1
        }

        logger.info("Paso 1: Creando post...")
        response_post = requests.post(endpoint_post, json=nuevo_post)

        assert response_post.status_code == 201, "Error al crear post"
        post_creado = response_post.json()
        post_id = post_creado["id"]

        logger.info(f"✓ Post creado con ID: {post_id}")

        # Paso 2: Obtener lista de posts para verificar
        endpoint_get = f"{self.BASE_URL}/posts"

        logger.info(f"Paso 2: Obteniendo lista de posts...")
        response_get = requests.get(endpoint_get)

        assert response_get.status_code == 200, "Error al obtener lista"
        posts = response_get.json()

        logger.info(f"✓ Lista obtenida: {len(posts)} posts encontrados")
        logger.info("✓ Encadenamiento de peticiones exitoso")
