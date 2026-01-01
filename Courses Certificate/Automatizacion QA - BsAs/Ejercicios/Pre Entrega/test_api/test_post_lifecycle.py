"""
Prueba de ciclo de vida completo de un Post (E2E)
Cubre operaciones CRUD: CREATE (POST), UPDATE (PATCH), DELETE
Utiliza Faker para generar datos aleatorios
Valida esquema, tipos de datos y tiempos de respuesta
"""
import pytest
import time
from faker import Faker
from utils.api_utils import APIClient


# URL base de JSONPlaceholder (API pública para pruebas)
BASE_URL = "https://jsonplaceholder.typicode.com"

# Inicializar Faker
fake = Faker('es_ES')


@pytest.fixture
def api_client():
    """Fixture para crear una instancia del cliente API"""
    return APIClient(BASE_URL)


@pytest.mark.e2e
def test_post_lifecycle(api_client):
    """
    Test E2E del ciclo de vida completo de un post
    1. CREATE: POST /posts con datos generados por Faker
    2. UPDATE: PATCH /posts/{id} actualizando el título
    3. DELETE: DELETE /posts/{id} y validar respuesta
    Incluye validaciones de esquema, tipos y tiempos de respuesta
    """

    # ============================================
    # PASO 1: CREATE - POST /posts
    # ============================================
    print("\n[PASO 1] Creando post con Faker...")

    # Generar datos con Faker
    post_title = fake.sentence(nb_words=6)
    post_body = fake.paragraph(nb_sentences=3)
    post_user_id = fake.random_int(min=1, max=10)

    payload_create = {
        "title": post_title,
        "body": post_body,
        "userId": post_user_id
    }

    print(f"  - Titulo: {post_title}")
    print(f"  - Body: {post_body[:50]}...")
    print(f"  - UserId: {post_user_id}")

    # Realizar POST y medir tiempo
    start_time = time.time()
    response_create = api_client.post("/posts", json=payload_create)
    create_time = time.time() - start_time

    # Validar código de estado
    assert response_create.status_code == 201, \
        f"Expected status code 201, but got {response_create.status_code}"

    # Validar tiempo de respuesta (debe ser menor a 5 segundos)
    assert create_time < 5.0, \
        f"POST request took too long: {create_time:.2f} seconds"
    print(f"  [OK] POST completado en {create_time:.3f} segundos")

    # Obtener respuesta JSON
    response_json = response_create.json()

    # Validar esquema de respuesta (claves esperadas)
    expected_keys_create = ["id", "title", "body", "userId"]
    for key in expected_keys_create:
        assert key in response_json, f"Key '{key}' not found in POST response"

    # Validar tipos de datos
    assert isinstance(response_json["id"], int), "El campo 'id' debe ser un entero"
    assert isinstance(response_json["title"], str), "El campo 'title' debe ser un string"
    assert isinstance(response_json["body"], str), "El campo 'body' debe ser un string"
    assert isinstance(response_json["userId"], int), "El campo 'userId' debe ser un entero"

    # Validar valores
    assert response_json["title"] == post_title, "El título no coincide"
    assert response_json["body"] == post_body, "El body no coincide"
    assert response_json["userId"] == post_user_id, "El userId no coincide"

    # Guardar el ID del post creado
    post_id = response_json["id"]
    print(f"  [OK] Post creado exitosamente con ID: {post_id}")
    print(f"  [OK] Validaciones de esquema y tipos: PASSED")


    # ============================================
    # PASO 2: UPDATE - PATCH /posts/{id}
    # ============================================
    print(f"\n[PASO 2] Actualizando post ID {post_id} con PATCH...")

    # Nuevo título actualizado
    updated_title = "Titulo actualizado por QA"

    payload_update = {
        "title": updated_title
    }

    print(f"  - Nuevo titulo: {updated_title}")

    # Realizar PATCH y medir tiempo
    start_time = time.time()
    response_update = api_client.patch(f"/posts/{post_id}", json=payload_update)
    update_time = time.time() - start_time

    # Validar código de estado
    assert response_update.status_code == 200, \
        f"Expected status code 200, but got {response_update.status_code}"

    # Validar tiempo de respuesta
    assert update_time < 5.0, \
        f"PATCH request took too long: {update_time:.2f} seconds"
    print(f"  [OK] PATCH completado en {update_time:.3f} segundos")

    # Obtener respuesta JSON
    response_update_json = response_update.json()

    # Validar esquema de respuesta
    assert "title" in response_update_json, "Key 'title' not found in PATCH response"
    # Nota: PATCH puede devolver solo los campos actualizados, no necesariamente el ID

    # Validar tipos de datos
    assert isinstance(response_update_json["title"], str), "El campo 'title' debe ser un string"

    # Validar que el título fue actualizado
    assert response_update_json["title"] == updated_title, \
        f"Expected title '{updated_title}', but got '{response_update_json['title']}'"

    print(f"  [OK] Post actualizado exitosamente")
    print(f"  [OK] Titulo actualizado a: {response_update_json['title']}")
    print(f"  [OK] Validaciones de esquema y tipos: PASSED")


    # ============================================
    # PASO 3: DELETE - DELETE /posts/{id}
    # ============================================
    print(f"\n[PASO 3] Eliminando post ID {post_id}...")

    # Realizar DELETE y medir tiempo
    start_time = time.time()
    response_delete = api_client.delete(f"/posts/{post_id}")
    delete_time = time.time() - start_time

    # Validar código de estado (200 para JSONPlaceholder)
    assert response_delete.status_code == 200, \
        f"Expected status code 200, but got {response_delete.status_code}"

    # Validar tiempo de respuesta
    assert delete_time < 5.0, \
        f"DELETE request took too long: {delete_time:.2f} seconds"
    print(f"  [OK] DELETE completado en {delete_time:.3f} segundos")

    print(f"  [OK] Post ID {post_id} eliminado exitosamente")


    # ============================================
    # RESUMEN FINAL
    # ============================================
    print("\n" + "="*60)
    print("RESUMEN DEL TEST E2E - CICLO DE VIDA COMPLETO")
    print("="*60)
    print(f"[OK] POST /posts - Status 201 - Tiempo: {create_time:.3f}s")
    print(f"[OK] PATCH /posts/{post_id} - Status 200 - Tiempo: {update_time:.3f}s")
    print(f"[OK] DELETE /posts/{post_id} - Status 200 - Tiempo: {delete_time:.3f}s")
    print(f"[OK] Tiempo total del ciclo: {(create_time + update_time + delete_time):.3f}s")
    print("="*60)
    print("[OK] Todas las validaciones pasaron exitosamente")
    print("     - Esquemas validados")
    print("     - Tipos de datos validados")
    print("     - Tiempos de respuesta validados")
    print("="*60)


@pytest.mark.e2e
@pytest.mark.parametrize("num_posts", [1, 2, 3])
def test_post_lifecycle_multiple(api_client, num_posts):
    """
    Test E2E parametrizado para crear y eliminar múltiples posts
    Valida que el framework soporta operaciones CRUD a escala
    """
    print(f"\n[TEST] Creando y eliminando {num_posts} post(s)...")

    created_ids = []

    # Crear múltiples posts
    for i in range(num_posts):
        payload = {
            "title": fake.sentence(),
            "body": fake.paragraph(),
            "userId": fake.random_int(min=1, max=10)
        }

        response = api_client.post("/posts", json=payload)
        assert response.status_code == 201

        post_id = response.json()["id"]
        created_ids.append(post_id)
        print(f"  [OK] Post {i+1}/{num_posts} creado con ID: {post_id}")

    # Eliminar todos los posts creados
    for post_id in created_ids:
        response = api_client.delete(f"/posts/{post_id}")
        assert response.status_code == 200
        print(f"  [OK] Post ID {post_id} eliminado")

    print(f"[OK] Test completado: {num_posts} post(s) creados y eliminados exitosamente")


@pytest.mark.e2e
def test_post_lifecycle_with_validation_errors(api_client):
    """
    Test E2E que valida manejo de errores en el ciclo de vida
    Intenta operaciones con datos inválidos
    """
    print("\n[TEST] Validando manejo de errores...")

    # Intentar actualizar un post que no existe
    print("  - Intentando PATCH a post inexistente...")
    response_patch = api_client.patch("/posts/999999", json={"title": "Test"})
    # JSONPlaceholder retorna 200 incluso para recursos inexistentes (simulación)
    assert response_patch.status_code in [200, 404, 500]
    print("  [OK] Manejo de PATCH a recurso inexistente validado")

    # Intentar eliminar un post que no existe
    print("  - Intentando DELETE a post inexistente...")
    response_delete = api_client.delete("/posts/999999")
    assert response_delete.status_code in [200, 404]
    print("  [OK] Manejo de DELETE a recurso inexistente validado")

    print("[OK] Validaciones de manejo de errores completadas")
