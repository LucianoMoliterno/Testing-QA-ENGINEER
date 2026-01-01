from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import Logger

class RegisterPage(BasePage):
    """Page Object para la página de registro."""

    # Locators - ACTUALIZADOS según HTML real
    URL = "https://talentolab-test.netlify.app/register"
    INPUT_NOMBRE = (By.NAME, "nombre")
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "contrasena")
    INPUT_CV = (By.NAME, "cv")
    BTN_SUBMIT = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".alert-success, .success-message, h2")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger(__name__)

    def open(self):
        """Abre la página de registro."""
        self.logger.info(f"Navegando a: {self.URL}")
        self.driver.get(self.URL)

    def complete_form(self, nombre, email, password):
        """Llena el formulario de registro."""
        self.logger.info(f"Completando formulario: nombre={nombre}, email={email}")
        self.type(self.INPUT_NOMBRE, nombre)
        self.type(self.INPUT_EMAIL, email)
        self.type(self.INPUT_PASSWORD, password)

    def upload_cv(self, file_path):
        """Sube un archivo CV."""
        self.logger.info(f"Subiendo CV: {file_path}")
        try:
            cv_input = self.driver.find_element(*self.INPUT_CV)
            cv_input.send_keys(file_path)
            self.logger.info("CV cargado exitosamente")
        except Exception as e:
            self.logger.error(f"Error al cargar CV: {str(e)}")
            raise

    def submit_form(self):
        """Envía el formulario."""
        self.logger.info("Enviando formulario de registro")
        self.click(self.BTN_SUBMIT)

    def is_registration_successful(self):
        """Verifica si el registro fue exitoso."""
        try:
            msg = self.get_text(self.SUCCESS_MSG)
            self.logger.info(f"Mensaje encontrado: {msg}")
            return msg
        except:
            self.logger.warning("No se encontró mensaje de éxito")
            return None