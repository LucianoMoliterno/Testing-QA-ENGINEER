from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import Logger

class HomePage(BasePage):
    """Page Object para la página principal de Talento Lab."""

    # Locators - ACTUALIZADOS según estructura real
    BTN_REGISTRATE = (By.LINK_TEXT, "Registrate")
    BTN_CARGA_CV = (By.LINK_TEXT, "Carga tu CV")
    SECCION_SERVICIOS = (By.ID, "servicios")  # Cambiado a ID
    SECCION_CONTACTO = (By.ID, "contacto")    # Cambiado a ID
    SECCION_NOSOTROS = (By.ID, "nosotros")
    SECCION_CLIENTES = (By.ID, "clientes")
    MENU_HAMBURGUESA = (By.CSS_SELECTOR, ".navbar-toggler")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://talentolab-test.netlify.app"
        self.logger = Logger.get_logger(__name__)

    def open(self):
        """Abre la página principal."""
        self.logger.info(f"Navegando a: {self.url}")
        self.driver.get(self.url)
        self.logger.info("Página principal cargada exitosamente")

    def click_registrate(self):
        """Hace clic en el botón 'Registrate'."""
        self.logger.info("Haciendo clic en botón 'Registrate'")
        self.click(self.BTN_REGISTRATE)

    def click_carga_cv(self):
        """Hace clic en el botón 'Carga tu CV'."""
        self.logger.info("Haciendo clic en botón 'Carga tu CV'")
        self.click(self.BTN_CARGA_CV)

    def scroll_to_servicios(self):
        """Hace scroll a la sección de servicios."""
        self.logger.info("Scrolling a sección Servicios")
        element = self.find(self.SECCION_SERVICIOS)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_contacto(self):
        """Hace scroll a la sección de contacto."""
        self.logger.info("Scrolling a sección Contacto")
        element = self.find(self.SECCION_CONTACTO)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_page_loaded(self):
        """Verifica que la página principal esté cargada."""
        try:
            self.find(self.BTN_REGISTRATE)
            self.logger.info("Página principal verificada correctamente")
            return True
        except:
            self.logger.error("Error al verificar carga de página principal")
            return False
