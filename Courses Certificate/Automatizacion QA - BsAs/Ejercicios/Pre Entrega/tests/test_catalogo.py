"""
Tests de Catálogo/Inventario usando Page Object Model
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def logged_in_inventory_page(driver):
    """Fixture para hacer login y retornar la página de inventario"""
    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')
    return InventoryPage(driver)


@pytest.mark.smoke
def test_navegacion_catalogo(logged_in_inventory_page):
    """Test 1: Navegación y verificación del catálogo"""
    inventory_page = logged_in_inventory_page

    # Verificar que estamos en la página correcta
    assert inventory_page.verify_page_loaded(), "No se cargó la página de inventario"

    # Verificar título de la página
    page_title = inventory_page.get_page_title()
    assert page_title == "Products", f"Título incorrecto: {page_title}"
    print(f"[OK] Título de página correcto: {page_title}")

    # Verificar presencia de productos
    products_count = inventory_page.get_products_count()
    assert products_count > 0, "No se encontraron productos en la página"
    print(f"[OK] Productos encontrados: {products_count}")

    # Verificar elementos de la interfaz
    assert inventory_page.is_menu_button_present(), "Botón de menú no encontrado"
    assert inventory_page.is_cart_icon_present(), "Ícono del carrito no encontrado"

    # Screenshot
    inventory_page.take_screenshot("test_navegacion_catalogo")
    print("[OK] Test 1 completado: Navegación del catálogo")


@pytest.mark.smoke
def test_verificar_informacion_productos(logged_in_inventory_page):
    """Test 2: Verificar información de productos"""
    inventory_page = logged_in_inventory_page

    # Obtener información del primer producto
    product_name = inventory_page.get_first_product_name()
    product_price = inventory_page.get_first_product_price()

    # Assert
    assert product_name is not None, "No se encontró el nombre del primer producto"
    assert product_price is not None, "No se encontró el precio del primer producto"
    assert "$" in product_price, "El precio no tiene formato correcto"

    print(f"[OK] Primer producto: {product_name} - Precio: {product_price}")

    # Verificar que hay múltiples productos
    all_products = inventory_page.get_all_product_names()
    assert len(all_products) >= 6, "No se encontraron suficientes productos"
    print(f"[OK] Total de productos: {len(all_products)}")

    # Screenshot
    inventory_page.take_screenshot("test_verificar_informacion_productos")
    print("[OK] Test 2 completado: Información de productos verificada")


def test_validar_elementos_interfaz(logged_in_inventory_page):
    """Test 3: Validar elementos de la interfaz"""
    inventory_page = logged_in_inventory_page

    # Verificar elementos clave de la interfaz
    assert inventory_page.is_menu_button_present(), "Botón de menú no está presente"
    assert inventory_page.is_cart_icon_present(), "Ícono del carrito no está presente"

    print("[OK] Botón de menú presente")
    print("[OK] Ícono del carrito presente")

    # Screenshot
    inventory_page.take_screenshot("test_validar_elementos_interfaz")
    print("[OK] Test 3 completado: Elementos de interfaz validados")
