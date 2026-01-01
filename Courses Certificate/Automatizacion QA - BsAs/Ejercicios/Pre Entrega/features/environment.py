"""
Environment Configuration para Behave
Autor: Luciano Moliterno
Hooks globales para WebDriver, screenshots y logging
"""
import logging
import os
from pathlib import Path
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)


def before_all(context):
    """
    Hook ejecutado antes de todos los tests
    Configura el WebDriver y crea directorios necesarios
    """
    logger.info("="*80)
    logger.info("INICIANDO SUITE BDD CON BEHAVE")
    logger.info("Autor: Luciano Moliterno")
    logger.info("="*80)

    # Crear directorio para screenshots si no existe
    screenshots_dir = Path("reports/screens")
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Directorio de screenshots: {screenshots_dir}")

    # Configurar opciones de Chrome
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

    try:
        logger.info("Inicializando WebDriver...")
        if is_ci:
            # En CI, usar el driver del sistema
            context.driver = webdriver.Chrome(options=chrome_options)
        else:
            # En local, usar la ruta específica
            logger.info("Ejecutando en entorno local")
            CHROME_DRIVER_PATH = r"C:\chromedriver\chromedriver.exe"
            context.driver = webdriver.Chrome(
                service=Service(CHROME_DRIVER_PATH),
                options=chrome_options
            )

        context.driver.implicitly_wait(10)
        logger.info("WebDriver iniciado exitosamente")
    except Exception as e:
        logger.error(f"Error al inicializar WebDriver: {e}")
        raise


def before_feature(context, feature):
    """Hook ejecutado antes de cada feature"""
    logger.info("-"*80)
    logger.info(f"Iniciando Feature: {feature.name}")
    logger.info(f"Tags: {feature.tags}")
    logger.info("-"*80)


def before_scenario(context, scenario):
    """Hook ejecutado antes de cada escenario"""
    logger.info(f"\n>>> Iniciando Escenario: {scenario.name}")
    logger.info(f"    Tags: {scenario.tags}")


def after_step(context, step):
    """
    Hook ejecutado después de cada step
    Captura screenshot automáticamente si el step falla
    """
    if step.status == "failed":
        logger.error(f"✗ STEP FALLIDO: {step.name}")

        # Capturar screenshot
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # Sanitizar nombre del step para usarlo en el archivo
            step_name = step.name.replace(" ", "_").replace('"', '').replace("'", "")
            step_name = step_name[:50]  # Limitar longitud

            screenshot_name = f"FAILED_{step_name}_{timestamp}.png"
            screenshot_path = Path("reports/screens") / screenshot_name

            context.driver.save_screenshot(str(screenshot_path))
            logger.info(f"Screenshot capturado: {screenshot_path}")

            # Guardar referencia del screenshot en el contexto para el reporte
            if not hasattr(context, 'screenshots'):
                context.screenshots = []
            context.screenshots.append(str(screenshot_path))

        except Exception as e:
            logger.error(f"Error al capturar screenshot: {e}")

    elif step.status == "passed":
        logger.info(f"✓ STEP EXITOSO: {step.name}")
    else:
        logger.warning(f"⊘ STEP OMITIDO: {step.name}")


def after_scenario(context, scenario):
    """Hook ejecutado después de cada escenario"""
    if scenario.status == "failed":
        logger.error(f"<<< Escenario FALLIDO: {scenario.name}")
    elif scenario.status == "passed":
        logger.info(f"<<< Escenario EXITOSO: {scenario.name}")
    else:
        logger.warning(f"<<< Escenario OMITIDO: {scenario.name}")


def after_feature(context, feature):
    """Hook ejecutado después de cada feature"""
    logger.info("-"*80)
    logger.info(f"Feature completado: {feature.name}")

    # Estadísticas del feature
    passed = len([s for s in feature.scenarios if s.status == "passed"])
    failed = len([s for s in feature.scenarios if s.status == "failed"])
    skipped = len([s for s in feature.scenarios if s.status == "skipped"])
    total = len(feature.scenarios)

    logger.info(f"Resultados: {passed} exitosos, {failed} fallidos, {skipped} omitidos de {total} total")
    logger.info("-"*80)


def after_all(context):
    """
    Hook ejecutado después de todos los tests
    Cierra el WebDriver y limpia recursos
    """
    logger.info("="*80)
    logger.info("FINALIZANDO SUITE BDD")

    # Cerrar WebDriver
    if hasattr(context, 'driver'):
        try:
            logger.info("Cerrando WebDriver...")
            context.driver.quit()
            logger.info("WebDriver cerrado exitosamente")
        except Exception as e:
            logger.error(f"Error al cerrar WebDriver: {e}")

    # Resumen de screenshots capturados
    if hasattr(context, 'screenshots') and context.screenshots:
        logger.info(f"\nTotal de screenshots capturados: {len(context.screenshots)}")
        for screenshot in context.screenshots:
            logger.info(f"  - {screenshot}")

    logger.info("="*80)
    logger.info("SUITE BDD COMPLETADA")
    logger.info("="*80)
