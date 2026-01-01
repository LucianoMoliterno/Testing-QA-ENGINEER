# Test de Ciclo de Vida Completo (E2E) - Post Lifecycle

## Descripción

Este archivo contiene las pruebas End-to-End (E2E) del ciclo de vida completo de un Post, cubriendo las operaciones CRUD requeridas para la entrega final.

## 📋 Funcionalidades Implementadas

### ✅ Test Principal: `test_post_lifecycle()`

Cubre el ciclo de vida completo de un post con las siguientes operaciones:

#### 1. **CREATE - POST /posts**
- ✅ Genera datos aleatorios con **Faker** (title, body, userId)
- ✅ Realiza POST a `/posts`
- ✅ Guarda el **ID** del post creado
- ✅ Valida código de estado **201**
- ✅ Valida esquema JSON (claves: id, title, body, userId)
- ✅ Valida tipos de datos
- ✅ Mide y valida tiempo de respuesta (< 5 segundos)

#### 2. **UPDATE - PATCH /posts/{id}**
- ✅ Actualiza el título a **"Titulo actualizado por QA"**
- ✅ Realiza PATCH a `/posts/{id}`
- ✅ Valida código de estado **200**
- ✅ Valida esquema JSON
- ✅ Valida que el título fue actualizado correctamente
- ✅ Mide y valida tiempo de respuesta (< 5 segundos)

#### 3. **DELETE - DELETE /posts/{id}**
- ✅ Elimina el post creado
- ✅ Realiza DELETE a `/posts/{id}`
- ✅ Valida código de estado **200**
- ✅ Mide y valida tiempo de respuesta (< 5 segundos)

### ✅ Tests Adicionales

#### `test_post_lifecycle_multiple()` - Parametrizado
- Crea y elimina múltiples posts (1, 2, 3)
- Valida operaciones CRUD a escala
- Usa `@pytest.mark.parametrize`

#### `test_post_lifecycle_with_validation_errors()`
- Valida manejo de errores
- Intenta operaciones con recursos inexistentes
- Verifica respuestas de error apropiadas

## 🎯 Validaciones Implementadas

### ✅ Validaciones de Esquema
- Verifica que el JSON de respuesta contiene todas las claves esperadas
- Valida estructura de datos correcta

### ✅ Validaciones de Tipos
- Verifica que `id` sea `int`
- Verifica que `title` y `body` sean `str`
- Verifica que `userId` sea `int`

### ✅ Validaciones de Tiempo
- Todas las operaciones deben completarse en menos de 5 segundos
- Se mide y reporta el tiempo de cada operación
- Se calcula el tiempo total del ciclo completo

## 🏷️ Marcadores de Pytest

Todos los tests están marcados con `@pytest.mark.e2e` para identificarlos como pruebas End-to-End.

## 🚀 Cómo Ejecutar

### Ejecutar todos los tests E2E
```bash
pytest test_api/test_post_lifecycle.py -v
```

### Ejecutar solo el test principal del ciclo de vida
```bash
pytest test_api/test_post_lifecycle.py::test_post_lifecycle -v -s
```

### Ejecutar solo tests marcados con e2e
```bash
pytest test_api/test_post_lifecycle.py -m e2e -v
```

### Ejecutar con salida detallada
```bash
pytest test_api/test_post_lifecycle.py -v -s
```

## 📊 Ejemplo de Salida

```
[PASO 1] Creando post con Faker...
  - Titulo: Doloremque itaque excepturi corrupti.
  - Body: Excepturi voluptates architecto ex ipsa...
  - UserId: 1
  [OK] POST completado en 0.251 segundos
  [OK] Post creado exitosamente con ID: 101
  [OK] Validaciones de esquema y tipos: PASSED

[PASO 2] Actualizando post ID 101 con PATCH...
  - Nuevo titulo: Titulo actualizado por QA
  [OK] PATCH completado en 0.155 segundos
  [OK] Post actualizado exitosamente
  [OK] Titulo actualizado a: Titulo actualizado por QA
  [OK] Validaciones de esquema y tipos: PASSED

[PASO 3] Eliminando post ID 101...
  [OK] DELETE completado en 0.154 segundos
  [OK] Post ID 101 eliminado exitosamente

============================================================
RESUMEN DEL TEST E2E - CICLO DE VIDA COMPLETO
============================================================
[OK] POST /posts - Status 201 - Tiempo: 0.251s
[OK] PATCH /posts/101 - Status 200 - Tiempo: 0.155s
[OK] DELETE /posts/101 - Status 200 - Tiempo: 0.154s
[OK] Tiempo total del ciclo: 0.560s
============================================================
[OK] Todas las validaciones pasaron exitosamente
     - Esquemas validados
     - Tipos de datos validados
     - Tiempos de respuesta validados
============================================================
```

## 🔧 Tecnologías Utilizadas

- **pytest**: Framework de testing
- **Faker**: Generación de datos aleatorios
- **requests**: Cliente HTTP para APIs
- **JSONPlaceholder**: API pública para pruebas

## 📝 API Utilizada

- **Base URL**: `https://jsonplaceholder.typicode.com`
- **Endpoints**:
  - POST `/posts` - Crear post
  - PATCH `/posts/{id}` - Actualizar post
  - DELETE `/posts/{id}` - Eliminar post

## ✅ Cumplimiento de Requisitos

Este test cumple con todos los requisitos de la entrega final:

✅ POST con Faker (title, body) y guarda el ID  
✅ PATCH actualizando título a "Titulo actualizado por QA"  
✅ DELETE y valida código 200  
✅ Asserts de esquema (estructura JSON)  
✅ Asserts de tipo (validación de tipos de datos)  
✅ Asserts de tiempo (< 5 segundos por operación)  
✅ Marcado con @pytest.mark.e2e  
✅ Demuestra que el framework soporta operaciones CRUD completas

