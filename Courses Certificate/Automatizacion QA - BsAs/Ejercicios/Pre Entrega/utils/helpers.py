from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os


class Helpers:
    """Clase con funciones auxiliares para los tests"""

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def login(self, username='standard_user', password='secret_sauce'):
        """Realiza el login en la aplicación"""
        try:
            print(f" Intentando login con usuario: {username}")
            # Localizar elementos del login
            username_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "login-button")

            # Ingresar credenciales y hacer login
            username_field.clear()
            username_field.send_keys(username)
            time.sleep(1)  # Pausa para ver la entrada

            password_field.clear()
            password_field.send_keys(password)
            time.sleep(1)  # Pausa para ver la entrada

            login_button.click()
            print(" Credenciales ingresadas, haciendo click en login...")

            # Verificar login exitoso
            self.wait.until(
                EC.url_contains("inventory.html")
            )
            time.sleep(2)  # Pausa para ver el resultado
            return True

        except Exception as e:
            print(f" Error durante login: {e}")
            return False

    def get_page_title(self):
        """Obtiene el título de la página actual"""
        return self.driver.title

    def get_products_list(self):
        """Obtiene la lista de productos disponibles"""
        try:
            products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            return products
        except NoSuchElementException:
            return []

    def get_first_product_info(self):
        """Obtiene nombre y precio del primer producto"""
        try:
            product_name = self.driver.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text
            product_price = self.driver.find_element(
                By.CLASS_NAME, "inventory_item_price"
            ).text
            return product_name, product_price
        except NoSuchElementException:
            return None, None

    def add_product_to_cart(self, product_index=0):
        """Añade un producto al carrito"""
        try:
            add_buttons = self.driver.find_elements(
                By.XPATH, "//button[contains(text(), 'Add to cart')]"
            )

            if add_buttons:
                print(f" Agregando producto {product_index + 1} al carrito...")
                add_buttons[product_index].click()
                time.sleep(2)  # Pausa para ver el botón clickeado
                return True
            return False

        except Exception as e:
            print(f" Error al añadir producto: {e}")
            return False

    def get_cart_count(self):
        """Obtiene el número de items en el carrito"""
        try:
            cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            return int(cart_badge.text)
        except NoSuchElementException:
            return 0

    def take_screenshot(self, test_name):
        """Toma una captura de pantalla y la guarda"""
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"{screenshot_dir}/{test_name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        print(f" Captura guardada: {filename}")
        return filename