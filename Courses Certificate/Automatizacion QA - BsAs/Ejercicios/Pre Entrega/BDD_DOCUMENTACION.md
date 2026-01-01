# 🎭 Suite BDD con Behave - Documentación Completa

## Autor: Luciano Moliterno
## Framework: Behavior-Driven Development para SauceDemo

---

## 📋 Descripción General

Este módulo implementa una **suite BDD (Behavior-Driven Development)** completa usando **Behave**, permitiendo que stakeholders no técnicos comprendan qué está siendo probado mediante escenarios escritos en lenguaje natural (Gherkin).

---

## ✅ Componentes Implementados

### 1. Features (Especificaciones Ejecutables)

#### 📄 `features/login.feature`
Escenarios de autenticación con múltiples casos de prueba:

- **Tags**: `@ui`, `@smoke`
- **Background**: Navegación automática a la página de login
- **Escenarios**:
  - ✅ Login exitoso con credenciales válidas
  - ✅ Esquema de escenario con 3 casos de error
  - ✅ Login con usuario bloqueado
  - ✅ Login con campos vacíos
  - ✅ Login sin contraseña

**Total**: 6+ escenarios cubriendo casos positivos y negativos

#### 📄 `features/cart.feature`
Funcionalidad del carrito de compras:

- **Tags**: `@ui`, `@regression`, `@smoke`
- **Background**: Login automático con standard_user
- **Escenarios**:
  - ✅ Agregar "Sauce Labs Backpack" al carrito
  - ✅ Agregar múltiples productos (3 productos)
  - ✅ Eliminar producto del carrito
  - ✅ Esquema con diferentes productos
  - ✅ Verificar persistencia del carrito

**Total**: 7+ escenarios cubriendo funcionalidad completa del carrito

### 2. Step Definitions (Conectores Python)

#### 📄 `features/steps/login_steps.py`
Step definitions para login que **reutilizan** las clases del Page Object Model:

- Importa y usa `LoginPage` e `InventoryPage`
- Implementa todos los steps de login.feature
- Logging detallado con `logger.info()`
- Validaciones completas de redirección y mensajes de error

#### 📄 `features/steps/cart_steps.py`
Step definitions para carrito que **reutilizan** POM:

- Importa y usa `InventoryPage` y `CartPage`
- Implementa todos los steps de cart.feature
- Login automático en el Background
- Validaciones de contador y contenido del carrito

**Patrón**: Cada step importa y usa los métodos del Page Object Model existente

### 3. Environment Configuration

#### 📄 `features/environment.py`
Configuración global con hooks completos:

**Hooks Implementados**:
- `before_all()` - Configura WebDriver una sola vez
- `before_feature()` - Log al iniciar cada feature
- `before_scenario()` - Log al iniciar cada escenario
- `after_step()` - **Captura screenshot automático en fallos**
- `after_scenario()` - Resumen del escenario
- `after_feature()` - Estadísticas del feature
- `after_all()` - Cierra WebDriver y limpia recursos

**Screenshots**: Guardados en `reports/screens/` con nombres descriptivos:
```
FAILED_{nombre_step}_{YYYYMMDD_HHMMSS}.png
```

### 4. Integración con Pytest

#### 📄 `tests_behave/test_behave_suite.py`
Wrapper completo para ejecutar Behave desde Pytest:

**Métodos Implementados**:
- `test_behave_smoke_tests()` - Ejecuta tests @smoke
- `test_behave_regression_tests()` - Ejecuta tests @regression
- `test_behave_all_ui_tests()` - Ejecuta todos los tests @ui
- `test_behave_dry_run()` - Verifica sintaxis sin ejecutar

**Formatos de Reporte**:
- JSON: `reports/behave_smoke.json`
- Pretty: Salida en consola
- JUnit: `reports/junit/` (opcional)

### 5. Configuración

#### 📄 `behave.ini`
Configuración completa de Behave:
```ini
lang = es                    # Idioma español
format = pretty              # Formato de salida
color = true                 # Salida con colores
show_timings = true          # Mostrar tiempos
logging_level = INFO         # Nivel de logging
```

#### 📄 `pytest.ini` (actualizado)
Marcadores BDD añadidos:
```ini
markers =
    bdd: Pruebas BDD con Behave
    dry_run: Verificación de sintaxis sin ejecución
```

---

## 🚀 Cómo Ejecutar

### Comandos Behave Directos

#### Verificar que Behave reconoce los features
```bash
behave --dry-run
```

#### Ejecutar solo smoke tests
```bash
behave -t @smoke
```

#### Ejecutar solo regression tests
```bash
behave -t @regression
```

#### Ejecutar todos los tests UI
```bash
behave -t @ui
```

#### Generar reportes completos
```bash
behave -f json -o reports/behave.json -f pretty
```

### Comandos Pytest (Wrapper)

#### Ejecutar suite BDD completa desde Pytest
```bash
pytest tests_behave/ -v
```

#### Ejecutar solo smoke tests BDD
```bash
pytest tests_behave/ -v -k "smoke"
```

#### Ejecutar solo regression tests BDD
```bash
pytest tests_behave/ -v -k "regression"
```

#### Verificar sintaxis (dry-run)
```bash
pytest tests_behave/ -v -k "dry_run"
```

---

## 📊 Reportes Generados

### 1. Reportes JSON
Ubicación: `reports/`
- `behave_smoke.json` - Resultados de tests @smoke
- `behave_regression.json` - Resultados de tests @regression
- `behave_all.json` - Todos los tests @ui
- `behave.json` - Reporte general

### 2. Reportes Pretty (Consola)
Salida legible en consola con:
- Colores para pasar/fallar
- Tiempos de ejecución
- Resumen de estadísticas

### 3. Screenshots de Fallos
Ubicación: `reports/screens/`
- Capturados automáticamente en cada step que falla
- Nomenclatura: `FAILED_{step_name}_{timestamp}.png`

### 4. Logs Detallados
Ubicación: `logs/`
- Logging de cada step ejecutado
- Estados: ✓ EXITOSO, ✗ FALLIDO, ⊘ OMITIDO

---

## 🎯 Ventajas del Enfoque BDD

### Para Stakeholders No Técnicos
✅ **Especificaciones Legibles**: Escenarios en lenguaje natural  
✅ **Documentación Viva**: Los features se actualizan con el código  
✅ **Claridad**: Entienden exactamente qué se está probando  

### Para Desarrolladores
✅ **Integración con POM**: Reutiliza clases existentes  
✅ **Mantenibilidad**: Cambios en una sola ubicación  
✅ **Ejecución desde Pytest**: Integración perfecta con CI/CD  

### Para el Proyecto
✅ **Cobertura Completa**: UI + API + BDD  
✅ **Framework Robusto**: Múltiples enfoques de testing  
✅ **Preparado para CI/CD**: Reportes en múltiples formatos  

---

## 📝 Ejemplo de Feature

### Login.feature
```gherkin
@ui @smoke
Escenario: Login exitoso con credenciales válidas
  Cuando el usuario ingresa el nombre de usuario "standard_user"
  Y el usuario ingresa la contraseña "secret_sauce"
  Y el usuario hace clic en el botón de login
  Entonces el usuario debe ser redirigido a la página de inventario
  Y el usuario debe ver el título "Products" en la página
```

### Cart.feature
```gherkin
@ui @regression @smoke
Escenario: Agregar un producto al carrito
  Cuando el usuario agrega "Sauce Labs Backpack" al carrito
  Entonces el contador del carrito debe mostrar "1"
  Y el producto "Sauce Labs Backpack" debe estar en el carrito
```

---

## 🔧 Estructura del Proyecto BDD

```
features/
├── login.feature              # Escenarios de autenticación
├── cart.feature               # Escenarios del carrito
├── environment.py             # Hooks globales (screenshots, WebDriver)
└── steps/
    ├── login_steps.py         # Step definitions de login (usa LoginPage)
    └── cart_steps.py          # Step definitions de cart (usa CartPage)

tests_behave/
└── test_behave_suite.py       # Wrapper de Pytest para Behave

behave.ini                     # Configuración de Behave
pytest.ini                     # Configuración de Pytest (actualizado con BDD)

reports/
├── behave_*.json              # Reportes JSON
├── junit/                     # Reportes JUnit
└── screens/                   # Screenshots de fallos
```

---

## ✅ Checklist de Entrega

- [x] `features/login.feature` con 6+ escenarios (1 exitoso + 5 de error)
- [x] `features/cart.feature` con Background de login y escenario "Sauce Labs Backpack"
- [x] Steps que importan y usan `LoginPage`, `InventoryPage` y `CartPage`
- [x] Hook de screenshots funcionando en `environment.py`
- [x] Wrapper de Pytest en `tests_behave/test_behave_suite.py`
- [x] `behave.ini` configurado con idioma español y opciones
- [x] `pytest.ini` actualizado con marcadores BDD
- [x] Comando `behave --dry-run` funciona sin errores
- [x] Comando `behave -t @smoke` funciona sin errores
- [x] Comando `pytest tests_behave/ -v` ejecuta la suite BDD

---

## 📈 Estadísticas de Cobertura

### Features Implementados: 2
- Login (Autenticación)
- Cart (Carrito de Compras)

### Escenarios Totales: 13+
- Login: 6 escenarios
- Cart: 7 escenarios

### Steps Implementados: 25+
- Login steps: 12+
- Cart steps: 13+

### Tags Utilizados:
- `@ui` - Todos los tests de interfaz
- `@smoke` - Tests críticos (login exitoso, agregar producto)
- `@regression` - Tests de regresión completa

---

## 🎓 Glosario BDD

**Feature**: Funcionalidad de alto nivel (ej: Login, Carrito)  
**Scenario**: Caso de prueba específico  
**Background**: Pasos comunes ejecutados antes de cada escenario  
**Given**: Estado inicial  
**When**: Acción del usuario  
**Then**: Resultado esperado  
**Scenario Outline**: Escenario parametrizado con tabla de ejemplos  

---

## 🔗 Conexión con Proyecto Final

Este trabajo cumple directamente con la sección **BDD del Framework Final**:

✅ **Comunicación Clara**: Stakeholders leen y entienden las pruebas  
✅ **Documentación Viva**: Especificaciones ejecutables siempre actualizadas  
✅ **Cobertura Completa**: BDD + Pytest + API = Framework robusto  
✅ **CI/CD Ready**: Reportes en JSON, Pretty y JUnit para integración  

---

## 👨‍💻 Autor

**Luciano Moliterno**  
QA Automation Engineer  
Framework: Behavior-Driven Development con Behave  

---

**Suite BDD completa lista para Entrega Final** ✅

