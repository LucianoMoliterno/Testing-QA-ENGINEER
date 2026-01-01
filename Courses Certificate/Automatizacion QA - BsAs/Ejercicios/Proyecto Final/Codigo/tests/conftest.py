import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# 1. Configuración del Driver (Navegador) - Desktop
@pytest.fixture(scope="function")
def driver():
    """Fixture para navegador en modo Desktop."""
    # Descarga e instala automáticamente el driver de Chrome
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") # Abrir pantalla completa
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10) # Espera implícita básica
    yield driver
    driver.quit() # Cierra el navegador al terminar

# 2. Configuración del Driver para Mobile (2400x1080 según tu documentación)
@pytest.fixture(scope="function")
def driver_mobile():
    """Fixture para navegador en modo Mobile (2400x1080)."""
    service = ChromeService(ChromeDriverManager().install())

    # Configuración móvil
    mobile_emulation = {
        "deviceMetrics": {"width": 412, "height": 915, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36"
    }

    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# 3. Configuración para Capturas de Pantalla (Screenshots) en caso de fallo
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar screenshots cuando un test falla."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            # Obtener el driver del test (puede ser desktop o mobile)
            if 'driver' in item.funcargs:
                driver = item.funcargs['driver']
            elif 'driver_mobile' in item.funcargs:
                driver = item.funcargs['driver_mobile']
            else:
                return

            # Crear nombre del archivo con fecha y hora
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name.replace(" ", "_").replace("[", "_").replace("]", "_")
            file_name = f"reports/screenshots/screenshot_{test_name}_{now}.png"

            # Asegurar que la carpeta reports/screenshots existe
            os.makedirs("reports/screenshots", exist_ok=True)

            driver.save_screenshot(file_name)
            print(f"\n📸 Screenshot guardado en: {file_name}")

            # Adjuntar al reporte HTML (pytest-html)
            if hasattr(rep, "extra"):
                extra = getattr(rep, "extra", [])
            else:
                extra = []

            # Agregar screenshot al reporte HTML si pytest-html está disponible
            if hasattr(rep, "extra"):
                try:
                    from pytest_html import extras
                    extra.append(extras.image(file_name))
                    rep.extra = extra
                except ImportError:
                    pass

        except Exception as e:
            print(f"❌ Error al tomar screenshot: {e}")

# 4. Configuración de pytest-html
def pytest_configure(config):
    """Configuración adicional de pytest."""
    # Crear directorio de reportes si no existe
    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("reports/logs", exist_ok=True)

# 5. Configuración del reporte HTML
@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    """Personalizar título del reporte HTML."""
    report.title = "Talento Lab - Reporte de Automatización"

# 6. Agregar información adicional al reporte
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    """Agregar resumen personalizado al reporte HTML."""
    prefix.extend([
        "<h2>Proyecto Final - Automation Testing</h2>",
        "<p><strong>Alumno:</strong> Luciano Moliterno</p>",
        "<p><strong>Plataforma:</strong> Talento Lab</p>",
        "<p><strong>URL:</strong> <a href='https://talentolab-test.netlify.app'>https://talentolab-test.netlify.app</a></p>",
        f"<p><strong>Fecha de Ejecución:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"
    ])
