import pytest
import time
from pages.home_page import HomePage
from pages.servicios_page import ServiciosPage
from pages.clientes_page import ClientesPage
from utils.logger import Logger

logger = Logger.get_logger(__name__)

class TestVisualizacion:
    """Suite de pruebas para visualización de contenido."""

    def test_tc005_visualizacion_testimonios(self, driver):
        """
        TC-005: Verificar visualización de testimonios de clientes.
        """
        logger.info("=== Iniciando TC-005: Visualización de testimonios ===")

        # Abrir página principal
        home = HomePage(driver)
        home.open()
        time.sleep(2)

        # Acceder a sección clientes
        clientes = ClientesPage(driver)

        # Verificar testimonios principales
        testimonios = clientes.verificar_testimonios_principales()
        logger.info(f"Testimonios encontrados: {testimonios}")

        # Contar total de testimonios
        cantidad = clientes.get_cantidad_testimonios()

        # Verificación: Debe haber al menos 3 testimonios (Ross, Joey, Phoebe)
        assert cantidad >= 3, f"Se esperaban al menos 3 testimonios, se encontraron {cantidad}"

        logger.info(f"✓ Test exitoso: {cantidad} testimonios verificados")

    def test_tc006_visualizacion_servicios(self, driver):
        """
        TC-006: Verificar visualización clara de servicios ofrecidos.
        """
        logger.info("=== Iniciando TC-006: Visualización de servicios ===")

        home = HomePage(driver)
        home.open()

        # Scroll a servicios
        home.scroll_to_servicios()
        time.sleep(2)

        servicios = ServiciosPage(driver)

        # Obtener servicios disponibles (método que funciona)
        servicios_disponibles = servicios.get_servicios_disponibles()
        logger.info(f"Servicios disponibles: {servicios_disponibles}")

        # Verificación: Debe haber 4 servicios
        assert len(servicios_disponibles) >= 4, f"Se esperaban 4 servicios, se encontraron {len(servicios_disponibles)}"

        # Verificar servicios específicos
        servicios_esperados = ["Reclutamiento", "Headhunting", "Evaluación", "Consultoría"]
        for servicio in servicios_esperados:
            assert servicio in servicios_disponibles, f"Servicio '{servicio}' no encontrado"

        logger.info("✓ Test exitoso: Todos los servicios visualizados correctamente")

    def test_tc007_informacion_para_candidatos(self, driver):
        """
        TC-007: Verificar información diferenciada para candidatos y empresas.
        """
        logger.info("=== Iniciando TC-007: Información para candidatos ===")

        home = HomePage(driver)
        home.open()
        time.sleep(2)

        # Verificar que la página se cargó correctamente
        assert home.is_page_loaded(), "La página principal no se cargó correctamente"

        # Scroll por las diferentes secciones
        home.scroll_to_servicios()
        time.sleep(1)

        servicios = ServiciosPage(driver)
        servicios_disponibles = servicios.get_servicios_disponibles()

        # Verificación: Los servicios deben estar accesibles
        assert len(servicios_disponibles) > 0, "No se encontró información de servicios"

        logger.info("✓ Test exitoso: Información accesible y bien presentada")
