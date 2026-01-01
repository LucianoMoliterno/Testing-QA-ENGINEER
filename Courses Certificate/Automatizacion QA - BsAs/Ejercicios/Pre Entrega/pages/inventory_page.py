"""
Page Object para la página de Inventario/Catálogo
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage(BasePage):
    """Page Object para la página de inventario de productos"""

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    PRODUCT_SORT = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        """Obtiene el título de la página"""
        return self.get_text(self.PAGE_TITLE)

    def get_products_count(self):
        """Obtiene la cantidad de productos disponibles"""
        products = self.find_elements(self.INVENTORY_ITEMS)
        return len(products)

    def get_all_product_names(self):
        """Obtiene los nombres de todos los productos"""
        products = self.find_elements(self.PRODUCT_NAMES)
        return [product.text for product in products]

    def get_first_product_name(self):
        """Obtiene el nombre del primer producto"""
        try:
            products = self.find_elements(self.PRODUCT_NAMES)
            if products:
                return products[0].text
        except NoSuchElementException:
            return None

    def get_first_product_price(self):
        """Obtiene el precio del primer producto"""
        try:
            prices = self.find_elements(self.PRODUCT_PRICES)
            if prices:
                return prices[0].text
        except NoSuchElementException:
            return None

    def add_product_to_cart(self, product_index=0):
        """Añade un producto al carrito por índice (robusto para headless)"""
        try:
            # Contar cuántos "Remove" hay antes de agregar
            pre_remove_count = len(self.find_elements(self.REMOVE_BUTTONS))

            # Localizador indexado del botón "Add to cart"
            indexed_add_locator = (By.XPATH, f"(//button[contains(text(), 'Add to cart')])[{product_index + 1}]")

            # Esperar a que sea cliqueable, hacer scroll y click JS (más estable en headless)
            button = self.wait.until(EC.element_to_be_clickable(indexed_add_locator))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            self.driver.execute_script("arguments[0].click();", button)

            # Esperar a que aparezca un botón "Remove" adicional (confirmación de agregado)
            def remove_count_increased(driver):
                return len(self.find_elements(self.REMOVE_BUTTONS)) > pre_remove_count

            try:
                self.wait.until(lambda d: remove_count_increased(d))
                return True
            except TimeoutException:
                # Como fallback, verificar si el badge del carrito apareció
                try:
                    self.wait.until(EC.presence_of_element_located(self.CART_BADGE))
                    return True
                except TimeoutException:
                    return False
        except Exception as e:
            print(f"[ERROR] Error al agregar producto: {e}")
            return False

    def get_cart_count(self):
        """Obtiene el número de items en el carrito"""
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except NoSuchElementException:
            return 0

    def click_cart(self):
        """Hace clic en el ícono del carrito y espera navegación"""
        print("[OK] Navegando al carrito")
        self.click(self.CART_LINK)
        # Esperar a que cargue la URL del carrito
        try:
            self.wait.until(EC.url_contains("cart.html"))
        except TimeoutException:
            pass

    def is_menu_button_present(self):
        """Verifica si el botón del menú está presente"""
        return self.is_element_present(self.MENU_BUTTON)

    def is_cart_icon_present(self):
        """Verifica si el ícono del carrito está presente"""
        return self.is_element_present(self.CART_LINK)

    def verify_page_loaded(self):
        """Verifica que la página de inventario se haya cargado correctamente"""
        return "inventory.html" in self.get_current_url()
