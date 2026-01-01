# 🚀 Guía de Comandos BDD - Ejecución Rápida

## Autor: Luciano Moliterno

---

## ✅ Verificación Rápida

### 1. Verificar que Behave está instalado
```bash
behave --version
```

### 2. Verificar que reconoce los features (dry-run)
```bash
behave --dry-run
```
**Resultado esperado**: Lista todos los escenarios sin ejecutarlos

---

## 🎯 Comandos Behave

### Ejecutar SOLO tests @smoke (críticos)
```bash
behave -t @smoke
```

### Ejecutar SOLO tests @regression
```bash
behave -t @regression
```

### Ejecutar TODOS los tests @ui
```bash
behave -t @ui
```

### Generar reporte JSON + Pretty
```bash
behave -f json -o reports/behave.json -f pretty
```

### Ejecutar sin captura (ver prints en tiempo real)
```bash
behave --no-capture
```

### Ejecutar con tags combinados
```bash
behave -t @ui -t @smoke     # AND: ui Y smoke
behave -t @ui,@regression   # OR: ui O regression
```

---

## 🧪 Comandos Pytest (Wrapper)

### Ejecutar suite BDD completa
```bash
pytest tests_behave/ -v
```

### Solo tests @smoke desde Pytest
```bash
pytest tests_behave/ -v -k "smoke"
```

### Solo tests @regression desde Pytest
```bash
pytest tests_behave/ -v -k "regression"
```

### Dry-run desde Pytest
```bash
pytest tests_behave/ -v -k "dry_run"
```

### Ejecutar con marcador BDD
```bash
pytest -m bdd -v
```

---

## 📊 Reportes

### Ubicación de reportes generados

**JSON**:
- `reports/behave_smoke.json`
- `reports/behave_regression.json`
- `reports/behave_all.json`

**Screenshots** (solo en fallos):
- `reports/screens/FAILED_*.png`

**Logs**:
- Consola en tiempo real
- `logs/pytest_execution.log`

---

## 🔍 Casos de Uso Específicos

### 1. Verificar que todos los steps están implementados
```bash
behave --dry-run
```

### 2. Ejecutar solo el feature de Login
```bash
behave features/login.feature
```

### 3. Ejecutar solo el feature de Cart
```bash
behave features/cart.feature
```

### 4. Ejecutar un escenario específico por nombre
```bash
behave -n "Login exitoso con credenciales válidas"
```

### 5. Ver salida detallada con timings
```bash
behave --format pretty --no-capture --show-timings
```

---

## 🐛 Troubleshooting

### Problema: "behave: command not found"
**Solución**:
```bash
pip install behave==1.2.6
```

### Problema: "No steps found"
**Solución**: Verificar que existe `features/steps/*.py`

### Problema: Screenshots no se capturan
**Solución**: Verificar que existe `reports/screens/` y que `environment.py` tiene el hook `after_step()`

### Problema: WebDriver no se cierra
**Solución**: Verificar que `environment.py` tiene el hook `after_all()`

---

## 📝 Ejemplo de Salida Esperada

```
Feature: Login en SauceDemo
  Como usuario del sistema
  Quiero poder autenticarme con mis credenciales
  Para acceder a la tienda online

  Scenario: Login exitoso con credenciales válidas
    Given que el usuario está en la página de login de SauceDemo  ✓
    When el usuario ingresa el nombre de usuario "standard_user"  ✓
    And el usuario ingresa la contraseña "secret_sauce"           ✓
    And el usuario hace clic en el botón de login                 ✓
    Then el usuario debe ser redirigido a la página de inventario ✓
    And el usuario debe ver el título "Products" en la página    ✓

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped, 0 undefined
```

---

## ✅ Checklist Pre-Ejecución

Antes de ejecutar, verificar:

- [ ] `behave --version` muestra versión 1.2.6
- [ ] Existe `features/login.feature`
- [ ] Existe `features/cart.feature`
- [ ] Existe `features/steps/login_steps.py`
- [ ] Existe `features/steps/cart_steps.py`
- [ ] Existe `features/environment.py`
- [ ] Existe `behave.ini`
- [ ] ChromeDriver está en `C:\chromedriver\chromedriver.exe`
- [ ] Carpeta `reports/screens/` existe

---

## 🎉 Ejecución Completa Sugerida

```bash
# 1. Verificar sintaxis
behave --dry-run

# 2. Ejecutar smoke tests
behave -t @smoke --no-capture

# 3. Ejecutar regression tests
behave -t @regression

# 4. Generar reportes completos
behave -f json -o reports/behave_complete.json -f pretty

# 5. Desde Pytest
pytest tests_behave/ -v
```

---

**¡Suite BDD lista para ejecutar!** 🚀

