# Framework de Automatización de Pruebas - Talento Lab

**Autor:** Luciano Moliterno  
**Plataforma bajo prueba:**  <a href="https://talentolab-test.netlify.app"><img src="https://github.com/user-attachments/assets/d8175aff-7e93-45ca-b4cf-44067c689ef4" alt="TalentoLab" style="height: 40px; width: auto; vertical-align: middle;"></a>
  
**Lenguaje:** Python 3.11+  
**Framework:** Pytest + Selenium WebDriver + Requests

**Documentacion:**  <a href="https://drive.google.com/file/d/1ltj5PCKCXc09iVe1jnfX22SGfaXTAXQ-/view?usp=sharing"><img src="https://github.com/user-attachments/assets/c1f740f0-b2b7-4694-8aab-fc6862573a62" alt="Drive" style="height: 35px; width: auto; vertical-align: middle;"></a>

---

## Propósito del Proyecto

Este proyecto implementa un framework de automatización de pruebas para validar la funcionalidad de la plataforma web Talento Lab. El framework cubre tanto pruebas de interfaz de usuario (UI) como pruebas de API REST, siguiendo el patrón Page Object Model para mantener el código organizado y reutilizable.

El framework está diseñado para:
- Ejecutar pruebas automatizadas de regresión
- Validar funcionalidades críticas del sistema
- Generar reportes HTML detallados
- Documentar bugs encontrados
- Facilitar la integración continua mediante CI/CD

---

## Tecnologías Utilizadas

### Core
- **Python 3.11** - Lenguaje de programación
- **Pytest 9.0.1** - Framework de testing
- **Selenium 4.38.0** - Automatización de navegadores web
- **Requests 2.32.5** - Cliente HTTP para pruebas de API

### Herramientas Adicionales
- **Webdriver Manager 4.0.2** - Gestión automática de drivers de navegador
- **Pytest-HTML 4.1.1** - Generación de reportes HTML
- **Git** - Control de versiones
- **GitHub Actions** - Integración continua (CI/CD)

---

## Estructura del Proyecto

```
proyecto-final-automation-testing-LucianoMoliterno/
│
├── pages/                      # Page Object Model
│   ├── base_page.py           # Clase base con métodos comunes
│   ├── home_page.py           # Página principal
│   ├── register_page.py       # Página de registro y carga de CV
│   ├── contacto_page.py       # Formulario de contacto
│   ├── servicios_page.py      # Sección de servicios
│   └── clientes_page.py       # Sección de testimonios
│
├── tests/                      # Tests automatizados
│   ├── conftest.py            # Configuración de fixtures
│   ├── test_api.py            # 6 tests de API REST
│   ├── test_visualizacion.py  # 3 tests de visualización
│   ├── test_carga_cv.py       # 5 tests de registro y CV
│   ├── test_contacto.py       # 7 tests de formulario
│   ├── test_responsive.py     # 3 tests de responsividad
│   └── test_registro.py       # 1 test adicional
│
├── utils/                      # Utilidades
│   ├── logger.py              # Sistema de logging
│   └── data_reader.py         # Lectura de datos externos
│
├── test_data/                  # Datos de prueba
│   ├── contacto.csv           # Datos parametrizados
│   └── usuarios.json          # Datos de usuarios
│
├── reports/                    # Reportes generados
│   ├── *.html                 # Reportes de ejecución
│   ├── logs/                  # Logs detallados
│   └── screenshots/           # Capturas de pantalla
│
├── .github/workflows/          # CI/CD
│   └── tests.yml              # GitHub Actions
│
├── requirements.txt            # Dependencias
├── pytest.ini                 # Configuración de pytest
└── README.md                  # Este archivo
```

---

## Instalación de Dependencias

### Prerequisitos
- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Google Chrome (para ejecución de tests de UI)
- Git

### Pasos de Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/usuario/proyecto-final-automation-testing-LucianoMoliterno.git
cd proyecto-final-automation-testing-LucianoMoliterno
```

2. Crear entorno virtual (recomendado):
```bash
python -m venv venv
```

3. Activar entorno virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

**Nota:** Webdriver Manager descargará automáticamente el driver de Chrome correspondiente a tu versión instalada.

---

## Ejecución de Pruebas

### Ejecutar todos los tests
```bash
pytest tests/ -v
```

### Ejecutar tests específicos

**Tests de API:**
```bash
pytest tests/test_api.py -v
```

**Tests de UI:**
```bash
pytest tests/test_visualizacion.py tests/test_contacto.py tests/test_carga_cv.py -v
```

**Tests de responsividad móvil:**
```bash
pytest tests/test_responsive.py -v
```

### Generar reporte HTML
```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### Ejecutar con marcadores (markers)
```bash
pytest -m api       # Solo tests de API
pytest -m mobile    # Solo tests móviles
pytest -m negative  # Solo casos negativos
```

### Opciones útiles
```bash
pytest -v           # Modo verbose (detallado)
pytest -s           # Mostrar prints en consola
pytest -x           # Detener en el primer fallo
pytest -k "nombre"  # Ejecutar tests que contengan "nombre"
```

---

## Interpretación de Reportes

### Reporte HTML (reports/report.html)

El reporte HTML generado contiene:

1. **Resumen Ejecutivo**
   - Cantidad total de tests ejecutados
   - Tests pasados / fallados / omitidos
   - Duración total de la ejecución
   - Información del ambiente (Python, pytest, plugins)

2. **Detalle por Test**
   - Nombre del test y su ubicación
   - Estado (PASSED / FAILED / SKIPPED)
   - Duración de ejecución
   - Output capturado (logs)
   - Screenshot automático (si falló)

3. **Interpretación de Estados**
   - `PASSED` (verde): Test ejecutado exitosamente
   - `FAILED` (rojo): Test falló - revisar mensaje de error y screenshot
   - `SKIPPED` (amarillo): Test omitido intencionalmente

### Logs (reports/logs/test_execution_YYYY-MM-DD.log)

Archivo de texto plano con registro detallado de cada ejecución:

- `INFO`: Acciones normales del test (navegación, clicks, validaciones)
- `ERROR`: Errores encontrados durante la ejecución
- `WARNING`: Advertencias (bugs conocidos, comportamientos inesperados)

**Ejemplo de entrada en log:**
```
2025-11-22 22:21:53 - tests.test_api - INFO - === Iniciando API Test 1: GET Lista de Usuarios ===
2025-11-22 22:21:54 - tests.test_api - INFO - Endpoint: https://jsonplaceholder.typicode.com/users
2025-11-22 22:21:54 - tests.test_api - INFO - Status Code: 200
```

### Screenshots (reports/screenshots/)

- Se generan automáticamente cuando un test falla
- Nombre del archivo: `screenshot_{nombre_del_test}_{fecha_hora}.png`
- Útil para debugging visual de fallos en UI

### Reporte de Bugs (reports/reporte_bugs.html)

Documento HTML que detalla los bugs encontrados:
- ID del bug
- Severidad (Alta/Media/Baja)
- Descripción del problema
- Pasos para reproducir
- Resultado esperado vs obtenido
- Test automatizado vinculado

---

## Tests Implementados

### API Tests (6 tests)
- GET /users - Obtener lista de usuarios
- GET /users/{id} - Obtener usuario específico
- GET /users/999 - Usuario no encontrado (caso negativo)
- POST /posts - Crear nuevo post
- DELETE /posts/{id} - Eliminar post
- Encadenamiento POST + GET

**API utilizada:** JSONPlaceholder (https://jsonplaceholder.typicode.com)

### UI Tests (19 tests)
- **Visualización:** Servicios, testimonios, información
- **Registro y CV:** Registro válido, carga de archivos, validaciones
- **Contacto:** Formulario estándar + 5 casos parametrizados + validaciones
- **Responsividad:** Navegación móvil, formularios, servicios

**Total:** 25 tests automatizados

---

## Casos de Uso

### Ejecución Local Completa
```bash
# 1. Activar entorno
venv\Scripts\activate

# 2. Ejecutar todos los tests con reporte
pytest tests/ -v --html=reports/report_$(date +%Y%m%d).html --self-contained-html

# 3. Ver reporte
start reports/report_*.html
```

### Debug de Test Específico
```bash
# Ejecutar un solo test con logs visibles
pytest tests/test_contacto.py::TestContacto::test_tc003_envio_formulario_exitoso -v -s

# Ver el log generado
type reports\logs\test_execution_2025-11-22.log
```

### Integración Continua (CI/CD)

El proyecto incluye configuración de GitHub Actions en `.github/workflows/tests.yml` que:
- Se ejecuta automáticamente en cada push
- Ejecuta todos los tests
- Genera y guarda reportes como artefactos
- Notifica si algún test falla

---

## Bugs Documentados

El framework documenta 5 bugs reales encontrados en la plataforma Talento Lab:

| ID | Descripción | Severidad | Test Vinculado |
|----|-------------|-----------|----------------|
| BUG-001 | Archivo > 5MB aceptado sin validación | Alta | TC-009 |
| BUG-002 | Menú hamburguesa no responde en móvil | Media | TC-010 |
| BUG-003 | Formulario sin validación de campos vacíos | Alta | TC-004 |
| BUG-004 | Link "Carga tu CV" devuelve 404 | Alta | TC-002 |
| BUG-005 | Archivo corrupto no validado | Media | TC-008 |

Más detalles en `reports/reporte_bugs.html`

---

## Mantenimiento del Framework

### Agregar Nuevos Tests

1. Crear Page Object (si es necesario) en `pages/`
2. Crear archivo de test en `tests/`
3. Seguir convención de nombres: `test_*.py`
4. Usar fixtures definidos en `conftest.py`

**Ejemplo:**
```python
# tests/test_nuevo.py
from pages.home_page import HomePage

def test_nueva_funcionalidad(driver):
    home = HomePage(driver)
    home.open()
    # ... tu código de prueba
    assert condicion_esperada
```

### Actualizar Dependencias
```bash
pip list --outdated          # Ver paquetes desactualizados
pip install --upgrade paquete  # Actualizar paquete específico
pip freeze > requirements.txt  # Guardar nuevas versiones
```

---

## Solución de Problemas

### Error: "ModuleNotFoundError"
**Solución:** Verificar que el entorno virtual esté activado y las dependencias instaladas:
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Error: "WebDriver not found"
**Solución:** Webdriver Manager debería manejarlo automáticamente. Si persiste:
```bash
pip install --upgrade webdriver-manager
```

### Tests fallan con "TimeoutException"
**Posibles causas:**
- Conexión a internet lenta
- Página web caída o inaccesible
- Locators desactualizados (si la web cambió su HTML)

**Solución:** Revisar logs en `reports/logs/` y screenshots en `reports/screenshots/`

---

## Notas Técnicas

- Los tests de UI requieren conexión a internet para acceder a Talento Lab
- Los tests de API usan JSONPlaceholder (API pública, no requiere autenticación)
- El framework usa implicit wait de 10 segundos por defecto
- Screenshots solo se generan para tests fallidos
- Los logs se rotan por día (un archivo por día de ejecución)

---

## Licencia

Este proyecto es de uso académico para el curso de Testing QA.

