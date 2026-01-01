# Pruebas de API - Estructura Creada

## Estructura de archivos

```
test_api/
├── __init__.py
├── test_login_api.py      # Pruebas parametrizadas de login
├── test_users_api.py       # Pruebas de listado de usuarios
└── test_create_user_api.py # Pruebas de creación de usuarios

utils/
└── api_utils.py            # Utilidades para pruebas de API

pytest.ini                  # Configuración de pytest
```

## Descripción de las pruebas

### test_login_api.py
- **test_login_parametrizado**: Prueba parametrizada con casos exitosos e inválidos
  - Caso exitoso: email `eve.holt@reqres.in`, password `cityslicka`, espera 200 y token
  - Caso inválido: email sin password, espera 400
- **test_login_exitoso**: Prueba específica de login exitoso
- **test_login_datos_invalidos**: Prueba de login con datos inválidos

### test_users_api.py
- **test_get_users_page_1**: GET a `/api/users?page=1`
  - Valida que cada usuario tenga: id, email, first_name, last_name
  - Extra: valida que el avatar termina en .jpg
- **test_get_users_structure**: Valida la estructura completa de la respuesta
- **test_get_users_multiple_pages**: Prueba parametrizada para páginas 1 y 2
- **test_get_single_user**: Obtiene y valida un usuario individual

### test_create_user_api.py
- **test_create_user_parametrizado**: Prueba parametrizada para crear usuarios
- **test_create_user_simple**: Prueba simple de creación
- **test_update_user**: Actualización con PUT
- **test_delete_user**: Eliminación parametrizada de usuarios

## Cómo ejecutar las pruebas

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar todas las pruebas de API
```bash
pytest test_api/ -v
```

### Ejecutar pruebas específicas
```bash
# Solo pruebas de login
pytest test_api/test_login_api.py -v

# Solo pruebas de usuarios
pytest test_api/test_users_api.py -v

# Solo pruebas de creación
pytest test_api/test_create_user_api.py -v
```

### Ejecutar con salida detallada
```bash
pytest test_api/ -v -s
```

### Generar reporte HTML
```bash
pytest test_api/ -v --html=reports/reporte_api.html --self-contained-html
```

## Notas importantes

- La API utilizada es: https://reqres.in
- Las pruebas usan @pytest.mark.parametrize para casos múltiples
- Se valida el código de estado HTTP y la estructura JSON de las respuestas
- Los avatares se validan que terminen en .jpg

