import pytest
from py.xml import html
import datetime
import logging
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Configuración de logging
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Configurar logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / f"test_execution_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def pytest_configure(config):
    """Configuración de marcadores personalizados y metadata"""
    config.addinivalue_line(
        "markers", "smoke: Marca los tests críticos de tipo smoke"
    )
    config.addinivalue_line(
        "markers", "api: Pruebas de API"
    )
    config.addinivalue_line(
        "markers", "ui: Pruebas de interfaz de usuario"
    )
    config.addinivalue_line(
        "markers", "e2e: Pruebas end-to-end del ciclo completo"
    )

    # Agregar metadata al reporte HTML
    config._metadata = {
        'Proyecto': 'Automation Testing - SauceDemo & JSONPlaceholder',
        'Autor': 'Luciano Moliterno',
        'Tester': 'QA Automation Engineer',
        'Ambiente': 'Testing',
        'Python': '3.11.2',
        'Pytest': '7.4.0',
        'Frameworks': 'Selenium WebDriver + Requests',
        'Fecha de Ejecución': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    logger.info("="*80)
    logger.info("INICIANDO EJECUCIÓN DE PRUEBAS")
    logger.info(f"Autor: {config._metadata['Autor']}")
    logger.info(f"Fecha: {config._metadata['Fecha de Ejecución']}")
    logger.info("="*80)


def pytest_html_report_title(report):
    """Personalizar título del reporte HTML"""
    report.title = "Reporte de Pruebas Automatizadas - Luciano Moliterno"


def pytest_html_results_summary(prefix, summary, postfix):
    """Agregar información adicional al resumen del reporte"""
    prefix.extend([html.p("Proyecto: Automation Testing Framework")])
    prefix.extend([html.p("Autor: Luciano Moliterno - QA Automation Engineer")])


def pytest_html_results_table_header(cells):
    """Personalizar encabezados de la tabla de resultados"""
    cells.insert(2, html.th("Description"))
    cells.insert(1, html.th("Time", class_="sortable time", col="time"))
    cells.insert(3, html.th("Test Type"))


def pytest_html_results_table_row(report, cells):
    """Personalizar filas de la tabla de resultados (tolerante a CollectReport)"""
    # Fallbacks seguros si no hay description durante la colección
    description = getattr(report, 'description', None) or getattr(report, 'nodeid', '')
    cells.insert(2, html.td(description))
    cells.insert(1, html.td(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), class_="col-time"))

    # Determinar tipo de test basado en marcadores cuando aplique
    test_type = "General"
    if hasattr(report, 'keywords'):
        try:
            if 'api' in report.keywords or 'test_api' in getattr(report, 'nodeid', ''):
                test_type = "API"
            elif 'ui' in report.keywords or any(k in getattr(report, 'nodeid', '') for k in ['test_login', 'test_carrito']):
                test_type = "UI"
            elif 'e2e' in report.keywords:
                test_type = "E2E"
        except Exception:
            pass

    cells.insert(3, html.td(test_type))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook mejorado para captura de screenshots y logging
    Captura screenshots en tests UI cuando fallan
    Registra información detallada de todos los tests
    """
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__) if item.function.__doc__ else item.name

    # Logging de inicio/fin de tests
    if report.when == "call":
        test_name = item.nodeid

        if report.passed:
            logger.info(f"PASSED: {test_name}")
        elif report.failed:
            logger.error(f"FAILED: {test_name}")
            logger.error(f"  Error: {report.longreprtext}")
        elif report.skipped:
            logger.warning(f"SKIPPED: {test_name}")

    # Captura de screenshot para tests UI que fallan
    if report.failed and report.when == "call":
        driver = None

        # Intentar obtener el driver del test
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]

        if driver:
            try:
                # Crear directorio de screenshots si no existe
                screenshot_dir = Path("screenshots")
                screenshot_dir.mkdir(exist_ok=True)

                # Generar nombre del screenshot
                test_name = item.name
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = screenshot_dir / f"{test_name}_{timestamp}.png"

                # Capturar screenshot
                driver.save_screenshot(str(screenshot_path))
                logger.info(f"Screenshot capturado: {screenshot_path}")

                # Agregar screenshot al reporte HTML
                if hasattr(report, 'extra'):
                    extra = getattr(report, 'extra', [])
                    # Evita dependencia directa de pytest_html.extras si no está disponible
                    try:
                        import pytest_html  # type: ignore
                        extra.append(pytest_html.extras.image(str(screenshot_path)))
                        report.extra = extra
                    except Exception:
                        pass

            except Exception as e:
                logger.error(f"Error al capturar screenshot: {e}")


def pytest_sessionstart(session):
    """Hook ejecutado al inicio de la sesión de pruebas"""
    logger.info("Sesión de pruebas iniciada")
    logger.info(f"Directorio de trabajo: {os.getcwd()}")
    logger.info(f"Total de tests a ejecutar: {session.testscollected}")


def pytest_sessionfinish(session, exitstatus):
    """Hook ejecutado al final de la sesión de pruebas (tolerante a streams cerrados)"""
    try:
        logger.info("="*80)
        logger.info("FINALIZACIÓN DE EJECUCIÓN DE PRUEBAS")
        logger.info(f"Estado de salida: {exitstatus}")

        # Resumen de resultados
        if hasattr(session, 'testscollected'):
            logger.info(f"Total de tests ejecutados: {session.testscollected}")

        if exitstatus == 0:
            logger.info("Todos los tests pasaron exitosamente")
        else:
            logger.warning(f"Algunos tests fallaron (código: {exitstatus})")

        logger.info("="*80)
    except Exception:
        # Evitar que un stream cerrado provoque INTERNALERROR en CI
        pass


@pytest.fixture
def driver():
    """Fixture para configurar el WebDriver con logging mejorado"""
    logger.info("-" * 60)
    logger.info("Iniciando WebDriver para test UI")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")  # Para CI
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Detectar si estamos en CI (GitHub Actions)
    is_ci = os.environ.get('CI') == 'true' or os.environ.get('GITHUB_ACTIONS') == 'true' or os.environ.get('HEADLESS') == 'true'

    if is_ci:
        logger.info("Ejecutando en entorno CI - Configurando modo headless")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")

    logger.info("Configurando ChromeDriver...")

    driver = None
    try:
        # Inicializar el WebDriver
        if is_ci:
            # En CI, usar el driver del sistema
            driver = webdriver.Chrome(options=chrome_options)
        else:
            # En local, usar la ruta específica
            logger.info("Ejecutando en entorno local")
            CHROME_DRIVER_PATH = r"C:\chromedriver\chromedriver.exe"
            driver = webdriver.Chrome(
                service=Service(CHROME_DRIVER_PATH),
                options=chrome_options
            )

        driver.implicitly_wait(10)

        logger.info("ChromeDriver iniciado exitosamente")

        # Navegar a la página inicial
        logger.info("Navegando a saucedemo.com...")
        driver.get("https://www.saucedemo.com/")
        logger.info(f"Página cargada: {driver.current_url}")

        yield driver

    except Exception as e:
        logger.error(f"Error al inicializar WebDriver: {e}")
        raise

    finally:
        # Cleanup después de cada test
        if driver:
            logger.info("Cerrando navegador...")
            driver.quit()
            logger.info("WebDriver cerrado exitosamente")
            logger.info("-" * 60)


@pytest.fixture
def api_client():
    """Fixture para tests API con logging"""
    from utils.api_utils import APIClient

    logger.info("-" * 60)
    logger.info("Iniciando cliente API para test")

    # Este fixture puede ser usado por tests que necesiten un cliente API genérico
    # Los tests específicos pueden tener sus propios fixtures

    yield None

    logger.info("Finalizando test API")
    logger.info("-" * 60)
