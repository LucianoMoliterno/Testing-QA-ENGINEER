# 🚀 Framework de Automatización Completo

## Autor: Luciano Moliterno
## QA Automation Engineer

![CI Status](https://github.com/LucianoMoliterno/pre-entrega-automation-testing-Luciano-Moliterno/actions/workflows/ci.yml/badge.svg)

> ✅ **CI/CD Pipeline Activo** - Tests automatizados ejecutándose en cada push

---

## 📋 Descripción

Framework profesional de automatización de pruebas que integra **UI Testing**, **API Testing**, **BDD** y **CI/CD** para demostrar un sistema completo de QA Automation.

---

## ✨ Características Principales

### 🎯 Cobertura Completa
- ✅ **Tests UI** con Selenium WebDriver (SauceDemo)
- ✅ **Tests API** con Requests (JSONPlaceholder)
- ✅ **Tests BDD** con Behave (Gherkin en español)
- ✅ **Pipeline CI/CD** con GitHub Actions

### 📊 Reportes Profesionales
- ✅ Reportes HTML interactivos con pytest-html
- ✅ Reportes BDD en JSON y Pretty format
- ✅ Logs detallados de ejecución
- ✅ Screenshots automáticos en fallos

### 🏗️ Arquitectura
- ✅ Page Object Model (POM) para UI
- ✅ Separación de responsabilidades
- ✅ Reutilización de código
- ✅ Configuración centralizada

---

## 📂 Estructura del Proyecto

```
pre-entrega-automation-testing-Luciano-Moliterno/
│
├── .github/workflows/
│   └── ci.yml                      # Pipeline CI/CD con GitHub Actions
│
├── features/                       # Features BDD con Behave
│   ├── login.feature               # Escenarios de autenticación
│   ├── cart.feature                # Escenarios del carrito
│   ├── environment.py              # Hooks globales (screenshots, WebDriver)
│   └── steps/
│       ├── login_steps.py          # Step definitions de login
│       └── cart_steps.py           # Step definitions de cart
│
├── pages/                          # Page Object Model
│   ├── base_page.py                # Clase base con métodos comunes
│   ├── login_page.py               # Page Object del login
│   ├── inventory_page.py           # Page Object del inventario
│   └── cart_page.py                # Page Object del carrito
│
├── test_api/                       # Suite de Tests API
│   ├── test_login_api.py           # Tests de login API (parametrizados)
│   ├── test_users_api.py           # Tests de usuarios API
│   ├── test_create_user_api.py     # Tests CRUD de usuarios
│   └── test_post_lifecycle.py      # Test E2E del ciclo de vida (POST/PATCH/DELETE)
│
├── tests/                          # Suite de Tests UI
│   ├── test_login.py               # Tests de login UI
│   ├── test_login_csv.py           # Login con datos CSV
│   ├── test_carrito.py             # Tests del carrito
│   ├── test_carrito_json.py        # Carrito con datos JSON
│   └── test_catalogo.py            # Tests del catálogo
│
├── tests_behave/                   # Wrapper Pytest para Behave
│   └── test_behave_suite.py        # Integración Behave + Pytest
│
├── utils/                          # Utilidades
│   ├── api_utils.py                # Cliente API reutilizable
│   ├── datos.py                    # Manejo de datos de prueba
│   └── helpers.py                  # Funciones auxiliares
│
├── datos/                          # Datos de prueba
│   ├── login.csv                   # Credenciales de prueba
│   └── productos.json              # Datos de productos
│
├── reports/                        # Reportes generados
│   ├── *.html                      # Reportes HTML
│   ├── *.json                      # Reportes BDD JSON
│   └── screens/                    # Screenshots de fallos
│
├── logs/                           # Logs de ejecución
│   └── *.log                       # Logs detallados
│
├── conftest.py                     # Configuración de pytest (fixtures, hooks)
├── pytest.ini                      # Configuración de pytest
├── behave.ini                      # Configuración de Behave
├── requirements.txt                # Dependencias del proyecto
└── verificar_ci.sh                 # Script de verificación local
```

---

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/USUARIO/pre-entrega-automation-testing-Luciano-Moliterno.git
cd pre-entrega-automation-testing-Luciano-Moliterno
```

### 2. Crear entorno virtual (recomendado)
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar ChromeDriver (local)
- Descargar ChromeDriver compatible con tu versión de Chrome
- Colocar en `C:\chromedriver\chromedriver.exe` (Windows)
- En CI, se instala automáticamente

---

## 🧪 Ejecución de Tests

### Tests Locales

#### **Ejecutar TODOS los tests**
```bash
pytest -v
```

#### **Tests Smoke (críticos)**
```bash
pytest -m smoke -v
```

#### **Tests UI (SauceDemo)**
```bash
pytest tests/ -v
```

#### **Tests API (JSONPlaceholder)**
```bash
pytest test_api/ -v
```

#### **Test E2E Específico**
```bash
pytest test_api/test_post_lifecycle.py::test_post_lifecycle -v -s
```

#### **Tests BDD con Behave**
```bash
# Verificar sintaxis
behave --dry-run

# Ejecutar smoke tests
behave -t @smoke

# Ejecutar todos los tests
behave -t @ui

# Con reportes
behave -f json -o reports/behave.json -f pretty
```

#### **Tests BDD desde Pytest**
```bash
pytest tests_behave/ -v
```

---

## 🔄 Pipeline CI/CD

### Ejecución Automática

El pipeline se ejecuta automáticamente en:
- ✅ Push a `main` o `develop`
- ✅ Pull Requests a estas ramas
- ✅ Ejecución manual desde GitHub Actions

### ¿Qué Hace el Pipeline?

1. **Instala Python 3.11 y dependencias**
2. **Instala Chrome y ChromeDriver**
3. **Ejecuta Tests @smoke** (falla si estos fallan)
4. **Ejecuta Tests API** (JSONPlaceholder)
5. **Ejecuta Tests UI** (SauceDemo)
6. **Ejecuta Tests BDD** (Behave)
7. **Genera reportes** en múltiples formatos
8. **Sube artefactos** (disponibles 90 días)

### Ver Resultados del Pipeline

1. Ve a **GitHub** → Tu repositorio
2. Pestaña **"Actions"**
3. Click en el workflow ejecutado
4. Descarga artefactos desde la sección "Artifacts"

---

## 📊 Reportes Generados

### Reportes HTML
- `smoke_report.html` - Tests críticos
- `api_report.html` - Tests de API
- `ui_report.html` - Tests de UI
- Incluyen metadata del autor y timestamps

### Reportes BDD
- `behave_smoke.json` - Resultados smoke
- `behave_all.json` - Resultados completos
- `junit/*.xml` - Formato JUnit

### Logs
- `test_execution_*.log` - Logs timestamped
- `pytest_execution.log` - Log principal
- Nivel INFO con formato detallado

### Screenshots
- Capturados automáticamente en fallos
- Ubicación: `screenshots/` y `reports/screens/`
- Nomenclatura: `{test_name}_{timestamp}.png`

---

## 🎯 Tests Implementados

### 📱 Tests UI (SauceDemo)

#### Login
- ✅ Login exitoso con credenciales válidas (@smoke)
- ✅ Login con usuario bloqueado
- ✅ Login con credenciales inválidas
- ✅ Login parametrizado con CSV

#### Carrito
- ✅ Agregar producto al carrito (@smoke)
- ✅ Agregar múltiples productos
- ✅ Eliminar producto del carrito
- ✅ Verificar contenido del carrito
- ✅ Tests parametrizados con JSON

#### Catálogo
- ✅ Navegación del catálogo
- ✅ Verificar información de productos
- ✅ Ordenamiento de productos

### 🔌 Tests API (JSONPlaceholder)

#### Login API
- ✅ Login exitoso (validar token)
- ✅ Login sin password (error 400)
- ✅ Tests parametrizados con múltiples casos

#### Usuarios
- ✅ GET usuarios con paginación
- ✅ Validar esquema (id, email, first_name, last_name)
- ✅ Validar que avatares terminan en .jpg

#### CRUD Usuarios
- ✅ POST crear usuario
- ✅ PUT actualizar usuario
- ✅ DELETE eliminar usuario

#### E2E Post Lifecycle (@e2e)
- ✅ POST /posts con Faker (guarda ID)
- ✅ PATCH /posts/{id} (actualiza título a "Título actualizado por QA")
- ✅ DELETE /posts/{id} (valida 200)
- ✅ Validaciones de esquema, tipo y tiempo

### 🎭 Tests BDD (Behave)

#### Login Feature
- ✅ Login exitoso (@ui @smoke)
- ✅ Scenario Outline con 3 casos de error
- ✅ Usuario bloqueado
- ✅ Campos vacíos

#### Cart Feature
- ✅ Agregar "Sauce Labs Backpack" (@ui @regression @smoke)
- ✅ Agregar múltiples productos
- ✅ Eliminar producto
- ✅ Scenario Outline con 4 productos

---

## 🏆 Tecnologías Utilizadas

### Testing
- **Selenium WebDriver** 4.15.1 - Automatización UI
- **Pytest** 7.4.0 - Framework de testing
- **Behave** 1.2.6 - BDD con Gherkin
- **Requests** 2.31.0 - Cliente HTTP para API

### Reportes y Logging
- **pytest-html** 3.2.0 - Reportes HTML
- **pytest-rerunfailures** 12.0 - Reintentos automáticos
- **logging** - Sistema de logging de Python

### Generación de Datos
- **Faker** 20.0.0 - Datos de prueba aleatorios

### CI/CD
- **GitHub Actions** - Pipeline de integración continua
- **Ubuntu** latest - Runner de CI

---

## 📚 Documentación

- 📄 **CI_CD_DOCUMENTACION.md** - Guía completa del pipeline CI/CD
- 📄 **REPORTES_Y_LOGGING.md** - Sistema de reportes y logs
- 📄 **BDD_DOCUMENTACION.md** - Suite BDD con Behave
- 📄 **BDD_COMANDOS.md** - Comandos rápidos de Behave
- 📄 **GUIA_RAPIDA_REPORTES.md** - Guía rápida de reportes
- 📄 **README_BDD.md** - Resumen ejecutivo BDD
- 📄 **README_REPORTES.md** - Resumen ejecutivo de reportes

---

## ✅ Verificación Pre-Push

Antes de hacer push a GitHub, ejecuta:

```bash
# Linux/Mac
bash verificar_ci.sh

# Windows (Git Bash)
bash verificar_ci.sh
```

Este script:
- ✅ Verifica dependencias instaladas
- ✅ Valida estructura de archivos
- ✅ Ejecuta tests @smoke (CRÍTICOS)
- ✅ Verifica sintaxis BDD
- ✅ Genera reporte de estado

---

## 🔒 Branch Protection (Recomendado)

Para equipos, configurar reglas en `main`:

1. **Settings** → **Branches** → **Add rule**
2. Branch name pattern: `main`
3. ☑️ Require status checks to pass
4. Seleccionar: **"CI TalentoLab"**
5. ☑️ Require branches to be up to date

**Resultado**: No se puede mergear si CI falla

---

## 🎓 Patrones y Mejores Prácticas

### Page Object Model (POM)
- ✅ Separación de lógica de prueba y UI
- ✅ Reutilización de código
- ✅ Mantenibilidad mejorada

### Data-Driven Testing
- ✅ Tests parametrizados con `@pytest.mark.parametrize`
- ✅ Datos externos (CSV, JSON)
- ✅ Generación de datos con Faker

### Behavior-Driven Development (BDD)
- ✅ Especificaciones en lenguaje natural
- ✅ Colaboración con stakeholders
- ✅ Documentación viva

### Continuous Integration (CI/CD)
- ✅ Tests automáticos en cada cambio
- ✅ Detección temprana de bugs
- ✅ Artefactos profesionales

---

## 📈 Métricas del Framework

| Métrica | Cantidad |
|---------|----------|
| **Tests UI** | 15+ |
| **Tests API** | 20+ |
| **Tests BDD** | 15+ escenarios |
| **Page Objects** | 4 |
| **Features BDD** | 2 |
| **Líneas de código** | 3000+ |
| **Cobertura** | UI + API + E2E |
| **Tiempo de ejecución** | ~5-8 min en CI |

---

## 🐛 Troubleshooting

### ChromeDriver no funciona
**Solución**: Verifica que la versión coincide con tu Chrome instalado

### Tests fallan en CI pero pasan localmente
**Solución**: 
- Revisa modo headless
- Verifica rutas absolutas vs relativas
- Revisa logs en Artifacts

### Behave no encuentra steps
**Solución**: Verifica que existe `features/steps/*.py`

### Pipeline tarda mucho
**Solución**: 
- Optimiza waits implícitos
- Considera ejecución paralela con pytest-xdist

---

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-feature`)
3. Commit cambios (`git commit -m 'Add: nueva feature'`)
4. Push a la rama (`git push origin feature/nueva-feature`)
5. Abre un Pull Request

---

## 📞 Contacto

**Luciano Moliterno**  
QA Automation Engineer  
[GitHub](https://github.com/USUARIO) | [LinkedIn](https://linkedin.com/in/USUARIO)

---

## 📄 Licencia

Este proyecto es parte de un trabajo académico de QA Automation.

---

## 🎉 Características del Proyecto Final

✅ **Framework completo** con UI, API y BDD  
✅ **Pipeline CI/CD** funcional en GitHub Actions  
✅ **Reportes profesionales** en múltiples formatos  
✅ **Documentación completa** y detallada  
✅ **Código mantenible** con patrones reconocidos  
✅ **Evidencia legible** para stakeholders  

**Framework listo para demostrar al cliente** 🚀

---

_Última actualización: Octubre 2025_
