# 🚀 Pipeline CI/CD con GitHub Actions

## Autor: Luciano Moliterno
## Framework: Integración Continua Completa

---

## 📋 Descripción

Este pipeline de CI/CD ejecuta **automáticamente** toda la suite de pruebas (UI + API + BDD) en cada push o pull request a las ramas `main` o `develop`.

---

## ✅ ¿Qué Incluye el Pipeline?

### 1. **Tests Smoke (@smoke)** 🔥
- Ejecuta tests críticos marcados con `@smoke`
- **Falla el pipeline** si algún test smoke falla
- Incluye: Login exitoso, agregar producto al carrito

### 2. **Tests de API** 🔌
- Suite completa de tests API con JSONPlaceholder
- Valida operaciones CRUD (POST, PATCH, DELETE)
- Test E2E del ciclo de vida completo

### 3. **Tests UI** 🖥️
- Suite completa de tests UI con SauceDemo
- Login, carrito, catálogo
- Captura screenshots en fallos

### 4. **Tests BDD** 🎭
- Ejecución de features con Behave
- Login y Cart features
- Reportes en JSON y Pretty

---

## 📊 Artefactos Generados

El pipeline genera y almacena los siguientes artefactos por **90 días**:

### 1. **Reportes HTML**
- `smoke_report.html` - Reporte de tests smoke
- `api_report.html` - Reporte de tests API
- `ui_report.html` - Reporte de tests UI
- Accesibles desde la pestaña "Actions" → Run → "Artifacts"

### 2. **Reportes BDD JSON**
- `behave_smoke.json` - Resultados BDD smoke
- `behave_all.json` - Resultados BDD completos
- `junit/*.xml` - Reportes JUnit

### 3. **Logs de Ejecución**
- `*.log` - Logs detallados de cada ejecución
- `summary.txt` - Resumen consolidado

### 4. **Screenshots**
- Capturas automáticas de tests que fallan
- Ubicación: `screenshots/` y `reports/screens/`

---

## 🎯 Criterios de Aceptación

### ✅ El pipeline cumple con:

1. **Falla si tests @smoke fallan** 
   - `continue-on-error: false` en step de smoke tests
   
2. **Artefactos disponibles 90 días**
   - `retention-days: 90` en todos los uploads

3. **Badge cambia a rojo en caso de fallo**
   - GitHub Actions badge se actualiza automáticamente

4. **Incluye tests de SauceDemo (UI) y JSONPlaceholder (API)**
   - Steps separados para cada tipo de test

5. **Se ejecuta en < 8 minutos**
   - `timeout-minutes: 15` como máximo
   - Optimizado para ~5-8 minutos

---

## 🔧 Configuración del Pipeline

### Archivo: `.github/workflows/ci.yml`

```yaml
name: CI TalentoLab - Framework Testing Completo

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]
  workflow_dispatch:  # Ejecución manual
```

### Jobs Principales:

#### **1. test-framework**
- Instala Python 3.11
- Instala Chrome y ChromeDriver
- Ejecuta todas las suites de tests
- Genera y sube artefactos

#### **2. code-quality** (opcional)
- Análisis estático con flake8
- Validación de calidad de código

---

## 🚀 Cómo Usar

### Ejecución Automática

El pipeline se ejecuta automáticamente cuando:
- Haces `push` a `main` o `develop`
- Abres un Pull Request a estas ramas
- Sincronizas un PR existente

### Ejecución Manual

1. Ve a GitHub → Tu repositorio
2. Pestaña "Actions"
3. Selecciona "CI TalentoLab"
4. Click en "Run workflow"
5. Selecciona la rama
6. Click en "Run workflow" (botón verde)

---

## 📥 Ver Resultados

### En GitHub Actions

1. Ve a la pestaña **"Actions"**
2. Click en el workflow que quieres ver
3. Verás el estado: ✅ Success o ❌ Failure

### Ver Artefactos

1. Entra al workflow ejecutado
2. Scroll abajo hasta la sección **"Artifacts"**
3. Descarga los artefactos que necesites:
   - `html-reports` - Reportes HTML
   - `bdd-reports` - Reportes BDD JSON
   - `test-logs` - Logs de ejecución
   - `screenshots` - Capturas de pantalla

---

## 🔒 Branch Protection (Opcional)

### Configurar para que el CI deba pasar antes de mergear:

1. Ve a **Settings** → **Branches**
2. Click en **"Add rule"**
3. En "Branch name pattern" escribe: `main`
4. Marca: ☑️ **"Require status checks to pass before merging"**
5. Busca y selecciona: **"CI TalentoLab / test-framework"**
6. Marca: ☑️ **"Require branches to be up to date"**
7. Click en **"Create"** o **"Save changes"**

**Resultado**: No se podrá mergear a `main` si el CI falla.

---

## 🎨 Badge de Estado

### Agregar badge al README:

```markdown
![CI Status](https://github.com/USUARIO/REPO/actions/workflows/ci.yml/badge.svg)
```

Reemplaza `USUARIO` y `REPO` con tus datos.

El badge mostrará:
- 🟢 **passing** - Todos los tests pasaron
- 🔴 **failing** - Algún test falló
- 🟡 **running** - En ejecución

---

## 📊 Ejemplo de Ejecución

```
🔥 Ejecutando Tests @smoke
   ✅ test_login_exitoso PASSED
   ✅ test_agregar_producto_carrito PASSED
   
🔌 Ejecutando Tests de API
   ✅ test_post_lifecycle PASSED
   ✅ test_users_api PASSED
   
🖥️ Ejecutando Tests UI (SauceDemo)
   ✅ test_login_csv PASSED
   ✅ test_carrito_json PASSED
   
🎭 Ejecutando Tests BDD con Behave
   ✅ Login feature PASSED
   ✅ Cart feature PASSED

📊 Generando reportes...
📤 Subiendo artefactos...

✅ Pipeline completado exitosamente en 6m 23s
```

---

## 🐛 Troubleshooting

### Problema: ChromeDriver no funciona
**Solución**: El workflow instala automáticamente Chrome y ChromeDriver

### Problema: Tests fallan en CI pero pasan localmente
**Solución**: 
- Verifica que los tests no dependan de rutas absolutas
- Usa modo headless en CI (ya configurado)
- Revisa logs en Artifacts

### Problema: Pipeline tarda más de 8 minutos
**Solución**:
- Revisa tests lentos
- Considera ejecutar en paralelo (pytest-xdist)
- Ajusta `implicitly_wait`

---

## 📝 Notas Importantes

### Diferencias CI vs Local

**Local (Windows)**:
- ChromeDriver: `C:\chromedriver\chromedriver.exe`
- Navegador visible
- Archivos en carpetas locales

**CI (Linux - GitHub Actions)**:
- ChromeDriver: `/usr/local/bin/chromedriver`
- Modo headless (sin interfaz gráfica)
- Ambiente Ubuntu

El `conftest.py` y `environment.py` detectan automáticamente el entorno.

---

## ✅ Checklist de Configuración

Antes de hacer push, verifica:

- [ ] Archivo `.github/workflows/ci.yml` existe
- [ ] `conftest.py` detecta CI con `os.environ.get('CI')`
- [ ] `environment.py` de Behave también detecta CI
- [ ] `requirements.txt` está actualizado
- [ ] Tests @smoke están marcados correctamente
- [ ] `.gitignore` excluye `__pycache__`, `.pytest_cache`

---

## 🎉 Ventajas del CI/CD

✅ **Automatización**: Tests se ejecutan sin intervención  
✅ **Prevención**: Detecta bugs antes de producción  
✅ **Evidencia**: Reportes profesionales para stakeholders  
✅ **Consistencia**: Mismo ambiente en cada ejecución  
✅ **Integración**: Se integra con el flujo de desarrollo  

---

## 🔗 Conexión con Proyecto Final

Este pipeline integra **TODO** lo construido en el curso:

✅ **Tests UI** (Clases 7-10): Page Object Model  
✅ **Tests API** (Clases 11-12): Requests con validaciones  
✅ **Reportes** (Clase 13): HTML, logs, screenshots  
✅ **BDD** (Clase 14): Behave con features  
✅ **CI/CD** (Clase 15): GitHub Actions pipeline  

---

## 👨‍💻 Autor

**Luciano Moliterno**  
QA Automation Engineer  
Pipeline CI/CD: GitHub Actions + Pytest + Behave + Selenium  

---

**Pipeline listo para demostrar automatización profesional** 🚀

