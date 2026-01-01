"""
Page Object para la página de Login
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    """Page Object para la página de login de Saucedemo"""

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        """Ingresa el nombre de usuario"""
        print(f"[OK] Ingresando usuario: {username}")
        self.send_keys(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Ingresa la contraseña"""
        print("[OK] Ingresando contraseña")
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Hace clic en el botón de login"""
        print("[OK] Haciendo clic en Login")
        self.click(self.LOGIN_BUTTON)
        time.sleep(2)

    def login(self, username, password):
        """Realiza el proceso completo de login"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_error_message_displayed(self):
        """Verifica si se muestra un mensaje de error"""
        return self.is_element_present(self.ERROR_MESSAGE)

    def get_error_message(self):
        """Obtiene el texto del mensaje de error"""
        if self.is_error_message_displayed():
            return self.get_text(self.ERROR_MESSAGE)
        return None
