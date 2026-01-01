from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger import Logger

class BasePage:
    """Clase base que contiene métodos genéricos para interactuar con la página."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) # Espera explícita de 10 segundos
        self.logger = Logger.get_logger(__name__)

    def find(self, locator):
        """Espera a que un elemento sea visible y lo devuelve."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Elemento encontrado: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Timeout al buscar elemento: {locator}")
            raise

    def click(self, locator):
        """Hace clic en un elemento."""
        element = self.find(locator)
        element.click()
        self.logger.info(f"Click realizado en: {locator}")

    def type(self, locator, text):
        """Escribe texto en un campo (limpiándolo primero)."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        self.logger.info(f"Texto '{text}' ingresado en: {locator}")

    def get_text(self, locator):
        """Obtiene el texto de un elemento."""
        text = self.find(locator).text
        self.logger.info(f"Texto obtenido de {locator}: {text}")
        return text

    def is_element_visible(self, locator, timeout=10):
        """Verifica si un elemento es visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator):
        """Verifica si un elemento está presente en el DOM."""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def get_current_url(self):
        """Obtiene la URL actual."""
        url = self.driver.current_url
        self.logger.info(f"URL actual: {url}")
        return url

    def scroll_to_element(self, locator):
        """Hace scroll hasta un elemento específico."""
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.logger.info(f"Scroll realizado hacia: {locator}")

    def wait_for_url_contains(self, text, timeout=10):
        """Espera a que la URL contenga un texto específico."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            return True
        except TimeoutException:
            return False
