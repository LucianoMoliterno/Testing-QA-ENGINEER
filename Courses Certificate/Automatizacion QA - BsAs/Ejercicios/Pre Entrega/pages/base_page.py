"""
Clase base para todos los Page Objects
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


class BasePage:
    """Clase base con métodos comunes para todos los Page Objects"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, locator):
        """Encuentra un elemento en la página"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Encuentra múltiples elementos en la página"""
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """Hace clic en un elemento"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        time.sleep(1)

    def send_keys(self, locator, text):
        """Envía texto a un campo de entrada"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        time.sleep(0.5)

    def get_text(self, locator):
        """Obtiene el texto de un elemento"""
        element = self.find_element(locator)
        return element.text

    def get_current_url(self):
        """Obtiene la URL actual"""
        return self.driver.current_url

    def wait_for_url_contains(self, url_substring):
        """Espera hasta que la URL contenga un substring"""
        return self.wait.until(EC.url_contains(url_substring))

    def take_screenshot(self, test_name):
        """Toma una captura de pantalla"""
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            screenshot_dir = "screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            screenshot_path = f"{screenshot_dir}/{test_name}_{timestamp}.png"
            self.driver.save_screenshot(screenshot_path)
            print(f"[OK] Captura guardada: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            print(f"[ERROR] Error al guardar captura: {e}")
            return None

    def is_element_present(self, locator):
        """Verifica si un elemento está presente"""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False
