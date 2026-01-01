"""
Page Object para la página del Carrito de Compras
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object para la página del carrito de compras"""

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_QUANTITY = (By.CLASS_NAME, "cart_quantity")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        """Obtiene el título de la página del carrito"""
        return self.get_text(self.PAGE_TITLE)

    def get_cart_items_count(self):
        """Obtiene la cantidad de items en el carrito"""
        items = self.find_elements(self.CART_ITEMS)
        return len(items)

    def get_cart_item_names(self):
        """Obtiene los nombres de todos los productos en el carrito"""
        items = self.find_elements(self.CART_ITEM_NAMES)
        return [item.text for item in items]

    def get_first_item_name(self):
        """Obtiene el nombre del primer item en el carrito"""
        items = self.find_elements(self.CART_ITEM_NAMES)
        if items:
            return items[0].text
        return None

    def remove_item(self, item_index=0):
        """Remueve un item del carrito por índice"""
        try:
            buttons = self.find_elements(self.REMOVE_BUTTONS)
            if buttons and item_index < len(buttons):
                print(f"[OK] Removiendo item {item_index + 1} del carrito")
                buttons[item_index].click()
                return True
            return False
        except Exception as e:
            print(f"[ERROR] Error al remover item: {e}")
            return False

    def click_continue_shopping(self):
        """Hace clic en el botón 'Continue Shopping'"""
        print("[OK] Continuando con las compras")
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def click_checkout(self):
        """Hace clic en el botón 'Checkout'"""
        print("[OK] Procediendo al checkout")
        self.click(self.CHECKOUT_BUTTON)

    def verify_page_loaded(self):
        """Verifica que la página del carrito se haya cargado correctamente"""
        return "cart.html" in self.get_current_url()

    def is_cart_empty(self):
        """Verifica si el carrito está vacío"""
        return self.get_cart_items_count() == 0
"""
Paquete de Page Objects para el patrón POM
"""
