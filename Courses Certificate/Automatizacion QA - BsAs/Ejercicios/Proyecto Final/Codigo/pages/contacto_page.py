from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import Logger

class ContactoPage(BasePage):
    """Page Object para la sección de Contacto."""

    # Locators - ACTUALIZADOS según HTML real
    SECCION_CONTACTO = (By.ID, "contacto")
    INPUT_NOMBRE = (By.CSS_SELECTOR, "input[placeholder='Nombre']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[placeholder='Email']")
    INPUT_MENSAJE = (By.CSS_SELECTOR, "textarea[placeholder='Mensaje'], textarea")
    BTN_ENVIAR = (By.XPATH, "//button[contains(text(), 'Enviar')]")
    MENSAJE_CONFIRMACION = (By.CSS_SELECTOR, ".alert-success, .success-message")
    MENSAJE_ERROR = (By.CSS_SELECTOR, ".alert-danger, .error-message")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger(__name__)

    def completar_formulario(self, nombre, email, mensaje):
        """Completa el formulario de contacto."""
        self.logger.info(f"Completando formulario con: nombre={nombre}, email={email}")

        try:
            self.type(self.INPUT_NOMBRE, nombre)
            self.type(self.INPUT_EMAIL, email)
            self.type(self.INPUT_MENSAJE, mensaje)
            self.logger.info("Formulario completado exitosamente")
        except Exception as e:
            self.logger.error(f"Error al completar formulario: {str(e)}")
            raise

    def enviar_formulario(self):
        """Hace clic en el botón Enviar."""
        self.logger.info("Enviando formulario de contacto")
        self.click(self.BTN_ENVIAR)

    def verificar_campos_vacios(self):
        """Verifica si los campos están vacíos antes de enviar."""
        try:
            nombre = self.driver.find_element(*self.INPUT_NOMBRE).get_attribute("value")
            email = self.driver.find_element(*self.INPUT_EMAIL).get_attribute("value")
            mensaje = self.driver.find_element(*self.INPUT_MENSAJE).get_attribute("value")

            campos_vacios = not nombre or not email or not mensaje
            self.logger.info(f"Campos vacíos: {campos_vacios}")
            return campos_vacios
        except Exception as e:
            self.logger.error(f"Error al verificar campos: {str(e)}")
            return False

    def obtener_mensaje_confirmacion(self):
        """Obtiene el mensaje de confirmación si existe."""
        try:
            mensaje = self.get_text(self.MENSAJE_CONFIRMACION)
            self.logger.info(f"Mensaje de confirmación: {mensaje}")
            return mensaje
        except:
            self.logger.warning("No se encontró mensaje de confirmación")
            return None

    def formulario_bloqueado(self):
        """Verifica si el formulario está bloqueado para envío."""
        try:
            boton = self.driver.find_element(*self.BTN_ENVIAR)
            esta_deshabilitado = not boton.is_enabled()
            self.logger.info(f"Botón enviar deshabilitado: {esta_deshabilitado}")
            return esta_deshabilitado
        except Exception as e:
            self.logger.error(f"Error al verificar estado del botón: {str(e)}")
            return False
