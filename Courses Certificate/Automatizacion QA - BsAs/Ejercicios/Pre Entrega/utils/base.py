from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


class BaseTest:
    """Clase base para configurar el WebDriver y funciones comunes"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Configuración inicial del WebDriver"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        # Ruta FIJA del ChromeDriver
        CHROME_DRIVER_PATH = r"C:\chromedriver\chromedriver.exe"

        try:
            print(" Iniciando ChromeDriver...")
            # Inicializar el WebDriver con la ruta FIJA
            self.driver = webdriver.Chrome(
                service=Service(CHROME_DRIVER_PATH),
                options=chrome_options
            )
            self.driver.implicitly_wait(10)
            self.wait = WebDriverWait(self.driver, 15)

            # Navegar a la página inicial
            print(" Navegando a saucedemo.com...")
            self.driver.get("https://www.saucedemo.com/")

            # PAUSA para ver la página de login
            time.sleep(2)

            yield

            # PAUSA antes de cerrar
            print(" Cerrando navegador...")
            time.sleep(1)

            # Cleanup después de cada test
            if self.driver:
                self.driver.quit()

        except Exception as e:
            print(f" Error al inicializar WebDriver: {e}")
            raise