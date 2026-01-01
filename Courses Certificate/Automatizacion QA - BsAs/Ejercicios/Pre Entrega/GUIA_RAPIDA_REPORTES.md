# 🚀 Guía Rápida - Sistema de Reportes

## Autor: Luciano Moliterno

---

## 📋 Ejecución Rápida

### 1. Generar Reporte Completo (UI + API)
```bash
pytest -v
```
**Genera**: `reports/reporte_completo.html`

### 2. Solo Tests API con Reporte
```bash
pytest test_api/ -v --html=reports/reporte_api.html --self-contained-html
```

### 3. Solo Tests UI con Reporte
```bash
pytest tests/test_login.py -v --html=reports/reporte_ui.html --self-contained-html
```

### 4. Test E2E Específico
```bash
pytest test_api/test_post_lifecycle.py::test_post_lifecycle -v -s
```

---

## 📊 Qué Incluye el Reporte

✅ **Metadata del Autor**: Luciano Moliterno - QA Automation Engineer  
✅ **Timestamp**: Fecha y hora de ejecución  
✅ **Clasificación**: Tests UI/API/E2E automáticamente  
✅ **Screenshots**: Capturados automáticamente en fallos UI  
✅ **Logs Detallados**: En carpeta `logs/`  
✅ **Reintentos**: Hasta 2 reintentos automáticos  
✅ **Estadísticas**: Resumen completo de ejecución  

---

## 📂 Archivos Generados

Después de ejecutar las pruebas, encontrarás:

```
reports/
├── reporte_completo.html          # Reporte principal
├── reporte_api.html                # Solo tests API
└── reporte_ui.html                 # Solo tests UI

logs/
├── pytest_execution.log            # Log principal
└── test_execution_20251016_HHMMSS.log  # Log timestamped

screenshots/
└── test_name_20251016_HHMMSS.png   # Screenshots de fallos
```

---

## 🔍 Verificar Configuración

### 1. Verificar dependencias instaladas
```bash
pip list | findstr pytest
```

Debe mostrar:
- pytest (7.4.0)
- pytest-html (3.2.0)
- pytest-rerunfailures (12.0)

### 2. Verificar estructura de carpetas
```bash
dir logs
dir reports
dir screenshots
```

### 3. Ver configuración de pytest
```bash
pytest --version
pytest --markers
```

---

## 🎯 Ejemplo de Ejecución Completa

```bash
# 1. Limpiar reportes anteriores (opcional)
del reports\*.html
del logs\*.log

# 2. Ejecutar suite completa
pytest -v

# 3. Abrir el reporte generado
start reports\reporte_completo.html
```

---

## 📝 Logs en Tiempo Real

Durante la ejecución verás logs como:

```
2025-10-16 14:30:15 [INFO] INICIANDO EJECUCIÓN DE PRUEBAS
2025-10-16 14:30:15 [INFO] Autor: Luciano Moliterno
2025-10-16 14:30:20 [INFO] Iniciando WebDriver para test UI
2025-10-16 14:30:25 [INFO] ✓ PASSED: test_login_exitoso
2025-10-16 14:30:30 [INFO] ✓ PASSED: test_post_lifecycle
```

---

## ✅ Checklist Rápido

Antes de entregar, verifica:

- [ ] `requirements.txt` tiene pytest-html y pytest-rerunfailures
- [ ] Carpetas `logs/` y `reports/` tienen `.gitkeep`
- [ ] `conftest.py` tiene hooks de captura implementados
- [ ] `pytest.ini` tiene metadata del autor
- [ ] Tests ejecutan correctamente y generan reporte
- [ ] Screenshots se capturan en fallos
- [ ] Logs se generan correctamente

---

## 🆘 Troubleshooting Rápido

**Problema**: No se genera el reporte  
**Solución**: `pip install pytest-html==3.2.0`

**Problema**: Error de importación en conftest.py  
**Solución**: Comentar línea `extra.append(pytest_html.extras.image(...))` temporalmente

**Problema**: No se ven logs  
**Solución**: Verificar `pytest.ini` tiene `log_cli = true`

---

## 📞 Soporte

Para más información, consultar: `REPORTES_Y_LOGGING.md`

---

**Sistema de Reportes listo para Entrega Final** ✅

