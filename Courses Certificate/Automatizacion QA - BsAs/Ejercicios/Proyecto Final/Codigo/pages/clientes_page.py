from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import Logger

class ClientesPage(BasePage):
    """Page Object para la sección Nuestros Clientes / Testimonios."""

    # Locators - ACTUALIZADOS
    SECCION_CLIENTES = (By.ID, "clientes")
    TESTIMONIOS = (By.CSS_SELECTOR, ".testimonials, #clientes .card, #clientes .testimonial")
    TESTIMONIO_ROSS = (By.XPATH, "//*[contains(text(), 'Ross')]")
    TESTIMONIO_JOEY = (By.XPATH, "//*[contains(text(), 'Joey')]")
    TESTIMONIO_PHOEBE = (By.XPATH, "//*[contains(text(), 'Phoebe')]")
    CARRUSEL_NAVEGACION = (By.CSS_SELECTOR, ".carousel-control-next, .slick-next")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger(__name__)

    def get_cantidad_testimonios(self):
        """Cuenta la cantidad de testimonios visibles."""
        try:
            testimonios = self.driver.find_elements(*self.TESTIMONIOS)
            cantidad = len(testimonios)
            self.logger.info(f"Se encontraron {cantidad} testimonios")
            return cantidad
        except Exception as e:
            self.logger.error(f"Error al contar testimonios: {str(e)}")
            return 0

    def verificar_testimonio_existe(self, nombre):
        """Verifica si un testimonio específico existe."""
        try:
            locator = (By.XPATH, f"//*[contains(text(), '{nombre}')]")
            element = self.find(locator)
            self.logger.info(f"Testimonio de {nombre} encontrado")
            return True
        except:
            self.logger.warning(f"Testimonio de {nombre} no encontrado")
            return False

    def verificar_testimonios_principales(self):
        """Verifica que los 3 testimonios principales existan."""
        nombres = ["Ross", "Joey", "Phoebe"]
        resultados = {}

        for nombre in nombres:
            resultados[nombre] = self.verificar_testimonio_existe(nombre)

        self.logger.info(f"Verificación de testimonios: {resultados}")
        return resultados

    def carrusel_funciona(self):
        """Verifica si el carrusel de navegación es funcional."""
        try:
            boton_next = self.driver.find_element(*self.CARRUSEL_NAVEGACION)
            self.logger.info("Carrusel de navegación encontrado")
            return True
        except:
            self.logger.warning("Carrusel de navegación no encontrado")
            return False
