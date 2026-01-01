import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.base import BaseTest
from utils.helpers import Helpers


class TestSauceDemo(BaseTest):
    """Tests de automatización para saucedemo.com"""

    def test_login_exitoso(self):
        """Test 1: Login exitoso con credenciales válidas"""
        helpers = Helpers(self.driver, self.wait)

        # Realizar login
        login_result = helpers.login('standard_user', 'secret_sauce')

        # Verificar login exitoso
        assert login_result, "El login no fue exitoso"
        assert "inventory.html" in self.driver.current_url, "No se redirigió a la página de inventario"

        # Tomar captura de pantalla
        helpers.take_screenshot("test_login_exitoso")
        print(" Test 1 completado: Login exitoso")
        time.sleep(2)  # Pausa final

    def test_navegacion_catalogo(self):
        """Test 2: Navegación y verificación del catálogo"""
        helpers = Helpers(self.driver, self.wait)

        # Realizar login primero
        helpers.login('standard_user', 'secret_sauce')
        time.sleep(2)  # Pausa después del login

        # Validar título de la página
        page_title = helpers.get_page_title()
        assert page_title == "Swag Labs", f"Título incorrecto: {page_title}"
        print(f" Título de página correcto: {page_title}")

        # Validar presencia de productos
        products = helpers.get_products_list()
        assert len(products) > 0, "No se encontraron productos en la página"
        print(f" Productos encontrados: {len(products)}")

        # Obtener información del primer producto
        product_name, product_price = helpers.get_first_product_info()
        assert product_name is not None, "No se encontró el nombre del primer producto"
        assert product_price is not None, "No se encontró el precio del primer producto"

        print(f" Primer producto: {product_name} - Precio: {product_price}")

        # Validar elementos de la interfaz
        menu_button = self.driver.find_elements(By.ID, "react-burger-menu-btn")
        cart_icon = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_link")

        assert len(menu_button) > 0, "Botón de menú no encontrado"
        assert len(cart_icon) > 0, "Ícono del carrito no encontrado"

        helpers.take_screenshot("test_navegacion_catalogo")
        print(" Test 2 completado: Navegación del catálogo")
        time.sleep(2)  # Pausa final

    def test_agregar_producto_carrito(self):
        """Test 3: Agregar producto al carrito y verificar"""
        helpers = Helpers(self.driver, self.wait)

        # Realizar login primero
        helpers.login('standard_user', 'secret_sauce')
        time.sleep(2)  # Pausa después del login

        # Obtener contador inicial del carrito
        initial_cart_count = helpers.get_cart_count()
        print(f" Contador inicial del carrito: {initial_cart_count}")

        # Agregar primer producto al carrito
        add_result = helpers.add_product_to_cart(0)
        assert add_result, "No se pudo agregar el producto al carrito"

        # Verificar que el contador del carrito se incrementó
        time.sleep(2)  # Espera para la actualización
        new_cart_count = helpers.get_cart_count()
        assert new_cart_count == initial_cart_count + 1, \
            f"El contador del carrito no se incrementó correctamente. Esperado: {initial_cart_count + 1}, Obtenido: {new_cart_count}"

        print(f" Contador después de agregar: {new_cart_count}")

        # Ir al carrito de compras
        print(" Navegando al carrito...")
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        time.sleep(2)  # Pausa para la navegación

        # Verificar que estamos en la página del carrito
        self.wait.until(EC.url_contains("cart.html"))
        assert "cart.html" in self.driver.current_url, "No se redirigió a la página del carrito"

        # Verificar que el producto agregado está en el carrito
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) > 0, "No se encontraron productos en el carrito"

        print(f" Productos en carrito: {len(cart_items)}")

        helpers.take_screenshot("test_agregar_producto_carrito")
        print(" Test 3 completado: Producto agregado al carrito")
        time.sleep(2)  # Pausa final