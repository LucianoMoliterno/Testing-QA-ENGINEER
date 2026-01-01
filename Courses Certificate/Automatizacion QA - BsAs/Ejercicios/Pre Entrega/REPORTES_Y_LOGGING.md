# 📊 Generación de Reportes y Logging

## Documentación del Sistema de Reportes
**Autor**: Luciano Moliterno  
**Proyecto**: Automation Testing Framework - SauceDemo UI + JSONPlaceholder API

---

## 📋 Índice
1. [Descripción General](#descripción-general)
2. [Tecnologías Implementadas](#tecnologías-implementadas)
3. [Estructura de Carpetas](#estructura-de-carpetas)
4. [Configuración de Reportes](#configuración-de-reportes)
5. [Sistema de Logging](#sistema-de-logging)
6. [Captura de Screenshots](#captura-de-screenshots)
7. [Reintentos Automáticos](#reintentos-automáticos)
8. [Cómo Ejecutar y Generar Reportes](#cómo-ejecutar-y-generar-reportes)
9. [Interpretación de Reportes](#interpretación-de-reportes)

---

## 📖 Descripción General

Este framework de automatización incluye un **sistema completo de generación de reportes y logging** que proporciona evidencia legible y profesional para el cliente. El sistema está integrado tanto con las pruebas UI de **SauceDemo** como con las pruebas API de **JSONPlaceholder**.

### Características Principales:
✅ Reportes HTML interactivos con `pytest-html`  
✅ Logging detallado en archivos y consola  
✅ Captura automática de screenshots en fallos  
✅ Reintentos automáticos con `pytest-rerunfailures`  
✅ Metadata personalizada del autor y proyecto  
✅ Clasificación automática de tests (UI/API/E2E)  
✅ Timestamps y seguimiento temporal  

---

## 🛠️ Tecnologías Implementadas

### Dependencias Instaladas:
```
pytest==7.4.0
pytest-html==3.2.0
pytest-rerunfailures==12.0
selenium==4.15.1
requests==2.31.0
faker==20.0.0
```

### Librerías Utilizadas:
- **pytest-html**: Generación de reportes HTML profesionales
- **pytest-rerunfailures**: Reintentos automáticos para tests flaky
- **logging**: Sistema de logging nativo de Python
- **pathlib**: Gestión de rutas y archivos

---

## 📁 Estructura de Carpetas

```
pre-entrega-automation-testing-Luciano-Moliterno/
│
├── reports/                          # Reportes HTML generados
│   ├── .gitkeep                      # Asegura versionado en Git
│   └── reporte_completo.html         # Reporte principal (autogenerado)
│
├── logs/                             # Archivos de logging
│   ├── .gitkeep                      # Asegura versionado en Git
│   ├── pytest_execution.log          # Log principal (autogenerado)
│   └── test_execution_YYYYMMDD_HHMMSS.log  # Logs timestamped
│
├── screenshots/                      # Capturas de pantalla
│   └── test_name_YYYYMMDD_HHMMSS.png # Screenshots de fallos
│
├── conftest.py                       # Hooks y fixtures de pytest
├── pytest.ini                        # Configuración de pytest
└── requirements.txt                  # Dependencias del proyecto
```

### ⚠️ Nota sobre Versionado
Las carpetas `reports/` y `logs/` contienen archivos `.gitkeep` para asegurar que se versionan en Git aunque estén vacías. Los archivos generados (logs y reportes) se excluyen típicamente del control de versiones mediante `.gitignore`.

---

## ⚙️ Configuración de Reportes

### pytest.ini - Configuración Principal

```ini
[pytest]
# Autor: Luciano Moliterno
# Proyecto: SauceDemo UI + JSONPlaceholder API Testing

addopts = 
    -v                                    # Verbose
    --strict-markers                      # Validación estricta de marcadores
    --tb=short                            # Traceback corto
    --html=reports/reporte_completo.html  # Ubicación del reporte
    --self-contained-html                 # Reporte autocontenido
    --reruns 2                            # 2 reintentos en caso de fallo
    --reruns-delay 1                      # 1 segundo entre reintentos
```

### conftest.py - Hooks Implementados

#### 1. **pytest_configure()**
- Configura marcadores personalizados (smoke, api, ui, e2e)
- Agrega metadata del autor y proyecto al reporte
- Inicializa el sistema de logging

#### 2. **pytest_html_report_title()**
- Personaliza el título del reporte HTML
- Muestra: "Reporte de Pruebas Automatizadas - Luciano Moliterno"

#### 3. **pytest_html_results_summary()**
- Agrega información del proyecto y autor al resumen
- Visible en la parte superior del reporte

#### 4. **pytest_html_results_table_header()**
- Personaliza columnas de la tabla de resultados
- Columnas: Test, Time, Description, Test Type, Result

#### 5. **pytest_html_results_table_row()**
- Clasifica automáticamente tests como UI/API/E2E
- Agrega timestamps a cada test ejecutado

#### 6. **pytest_runtest_makereport()**
- Hook principal para captura de evidencia
- Registra logs detallados de cada test
- Captura screenshots automáticamente en fallos UI
- Agrega screenshots al reporte HTML

#### 7. **pytest_sessionstart() / pytest_sessionfinish()**
- Registra inicio y fin de la sesión de pruebas
- Genera resumen de ejecución

---

## 📝 Sistema de Logging

### Configuración Multi-Handler

El sistema de logging escribe simultáneamente en:
1. **Archivo timestamped**: `logs/test_execution_YYYYMMDD_HHMMSS.log`
2. **Archivo principal**: `logs/pytest_execution.log` (configurado en pytest.ini)
3. **Consola**: Salida en tiempo real durante ejecución

### Niveles de Logging

```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / f"test_execution_{timestamp}.log"),
        logging.StreamHandler()
    ]
)
```

### Tipos de Mensajes

- **INFO**: Ejecución normal, inicio/fin de tests
- **ERROR**: Fallos en tests, errores de ejecución
- **WARNING**: Tests skipped, advertencias

### Ejemplo de Log

```
2025-10-16 14:30:15 [INFO] __main__ - INICIANDO EJECUCIÓN DE PRUEBAS
2025-10-16 14:30:15 [INFO] __main__ - Autor: Luciano Moliterno
2025-10-16 14:30:20 [INFO] __main__ - Iniciando WebDriver para test UI
2025-10-16 14:30:25 [INFO] __main__ - ✓ PASSED: tests/test_login.py::test_login_exitoso
2025-10-16 14:30:30 [ERROR] __main__ - ✗ FAILED: tests/test_carrito.py::test_agregar_producto
2025-10-16 14:30:30 [INFO] __main__ - Screenshot capturado: screenshots/test_agregar_producto_20251016_143030.png
```

---

## 📸 Captura de Screenshots

### Captura Automática en Fallos

El sistema captura screenshots automáticamente cuando:
- Un test UI **falla** durante la fase de ejecución
- El test tiene acceso al fixture `driver`
- El WebDriver está activo

### Proceso de Captura

```python
if report.failed and report.when == "call":
    if "driver" in item.funcargs:
        screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        # Agregar al reporte HTML
        report.extra.append(pytest_html.extras.image(screenshot_path))
```

### Nomenclatura de Screenshots

```
test_login_exitoso_20251016_143025.png
test_agregar_producto_carrito_20251016_143045.png
test_verificar_contenido_carrito_20251016_143102.png
```

Formato: `{nombre_test}_{YYYYMMDD}_{HHMMSS}.png`

---

## 🔄 Reintentos Automáticos

### Configuración de pytest-rerunfailures

```ini
--reruns 2          # Máximo 2 reintentos por test
--reruns-delay 1    # 1 segundo de espera entre reintentos
```

### Funcionamiento

1. Test falla en el primer intento
2. Sistema espera 1 segundo
3. Reintenta el test (hasta 2 veces)
4. Si pasa en algún reintento → ✅ PASSED
5. Si falla todos los intentos → ❌ FAILED

### Casos de Uso

- Tests flaky por timing issues
- Problemas transitorios de red (API tests)
- Carga lenta de elementos UI

### Deshabilitar Reintentos en Test Específico

```python
@pytest.mark.no_rerun
def test_sin_reintentos():
    """Este test no se reintentará si falla"""
    pass
```

---

## 🚀 Cómo Ejecutar y Generar Reportes

### Ejecutar Todos los Tests

```bash
pytest
```
Genera: `reports/reporte_completo.html`

### Ejecutar Solo Tests UI

```bash
pytest tests/ -v
```

### Ejecutar Solo Tests API

```bash
pytest test_api/ -v
```

### Ejecutar Tests E2E

```bash
pytest -m e2e -v
```

### Ejecutar Tests Smoke

```bash
pytest -m smoke -v
```

### Ejecutar con Reporte Personalizado

```bash
pytest --html=reports/reporte_custom.html --self-contained-html
```

### Ejecutar sin Reintentos

```bash
pytest --reruns 0
```

### Ejecutar con Más Reintentos

```bash
pytest --reruns 5 --reruns-delay 2
```

---

## 📊 Interpretación de Reportes

### Estructura del Reporte HTML

El reporte generado incluye:

#### 1. **Encabezado**
- Título: "Reporte de Pruebas Automatizadas - Luciano Moliterno"
- Fecha y hora de ejecución
- Metadata del proyecto y autor

#### 2. **Resumen Ejecutivo**
```
Proyecto: Automation Testing Framework
Autor: Luciano Moliterno - QA Automation Engineer
Ambiente: Testing
Python: 3.11.2
Pytest: 7.4.0
```

#### 3. **Estadísticas Generales**
- Total de tests ejecutados
- Tests pasados ✅
- Tests fallidos ❌
- Tests omitidos ⊘
- Tiempo total de ejecución

#### 4. **Tabla de Resultados**

| Test | Time | Description | Test Type | Result |
|------|------|-------------|-----------|--------|
| test_login_exitoso | 14:30:25 | Prueba login exitoso | UI | ✅ PASSED |
| test_post_lifecycle | 14:31:10 | Test E2E ciclo completo | E2E | ✅ PASSED |
| test_get_users | 14:31:45 | Obtiene usuarios | API | ✅ PASSED |

#### 5. **Detalles de Fallos**
- Stack trace completo
- Mensaje de error
- Screenshot (si aplica)
- Logs relacionados

#### 6. **Screenshots Embebidos**
Los screenshots de fallos se incrustan directamente en el reporte HTML para fácil visualización.

---

## 🎯 Integración con el Proyecto Final

### Tests UI (SauceDemo)

✅ Login con diferentes usuarios  
✅ Navegación del catálogo  
✅ Gestión del carrito de compras  
✅ Validación de productos  
✅ Captura de screenshots en fallos  

### Tests API (JSONPlaceholder)

✅ Operaciones CRUD (POST, PATCH, DELETE)  
✅ Validación de esquemas JSON  
✅ Validación de tipos de datos  
✅ Medición de tiempos de respuesta  
✅ Tests parametrizados  

### Tests E2E

✅ Ciclo de vida completo de posts  
✅ Datos generados con Faker  
✅ Validaciones exhaustivas  
✅ Logging detallado de cada paso  

---

## 📈 Métricas y KPIs

El sistema de reportes proporciona:

### Métricas de Ejecución
- Tiempo promedio por test
- Tasa de éxito/fallo
- Tests más lentos
- Tests con reintentos

### Métricas de Calidad
- Cobertura de funcionalidades
- Estabilidad de tests (flakiness)
- Distribución UI vs API
- Tests críticos (smoke)

---

## 🔧 Troubleshooting

### Problema: No se genera el reporte HTML
**Solución**: Verificar que pytest-html esté instalado
```bash
pip install pytest-html==3.2.0
```

### Problema: No se capturan screenshots
**Solución**: Verificar permisos de escritura en carpeta `screenshots/`

### Problema: Logs vacíos
**Solución**: Verificar configuración de logging en pytest.ini

### Problema: Reintentos no funcionan
**Solución**: Verificar que pytest-rerunfailures esté instalado
```bash
pip install pytest-rerunfailures==12.0
```

---

## 📚 Recursos Adicionales

- [Documentación pytest-html](https://pytest-html.readthedocs.io/)
- [Documentación pytest-rerunfailures](https://github.com/pytest-dev/pytest-rerunfailures)
- [Pytest Logging](https://docs.pytest.org/en/stable/logging.html)
- [Selenium Screenshots](https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.save_screenshot)

---

## ✅ Checklist de Entrega Final

- [x] pytest-html instalado y configurado
- [x] pytest-rerunfailures instalado y configurado
- [x] requirements.txt actualizado
- [x] Carpetas reports/ y logs/ versionadas con .gitkeep
- [x] Hooks de captura implementados en conftest.py
- [x] pytest.ini con título y metadata de autor
- [x] Sistema de logging completo
- [x] Captura automática de screenshots
- [x] Integración con tests UI de SauceDemo
- [x] Integración con tests API de JSONPlaceholder
- [x] Documentación completa

---

## 👨‍💻 Autor

**Luciano Moliterno**  
QA Automation Engineer  
Proyecto: Automation Testing Framework  
Fecha: Octubre 2025

---

**Este sistema de reportes cumple con todos los requisitos de la entrega final y proporciona evidencia profesional y legible para el cliente.**

