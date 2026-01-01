"""
Tests del Carrito de Compras usando Page Object Model
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def logged_in_inventory_page(driver):
    """Fixture para hacer login y retornar la página de inventario"""
    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')
    return InventoryPage(driver)


@pytest.mark.smoke
def test_agregar_producto_carrito(logged_in_inventory_page):
    """Test 1: Agregar producto al carrito y verificar"""
    inventory_page = logged_in_inventory_page

    # Obtener contador inicial del carrito
    initial_cart_count = inventory_page.get_cart_count()
    print(f"[OK] Contador inicial del carrito: {initial_cart_count}")

    # Agregar primer producto al carrito
    add_result = inventory_page.add_product_to_cart(0)
    assert add_result, "No se pudo agregar el producto al carrito"

    # Verificar que el contador del carrito se incrementó
    new_cart_count = inventory_page.get_cart_count()
    assert new_cart_count == initial_cart_count + 1, \
        f"El contador del carrito no se incrementó correctamente. Esperado: {initial_cart_count + 1}, Obtenido: {new_cart_count}"
    print(f"[OK] Contador después de agregar: {new_cart_count}")

    # Ir al carrito
    inventory_page.click_cart()
    cart_page = CartPage(inventory_page.driver)

    # Verificar que estamos en la página del carrito
    assert cart_page.verify_page_loaded(), "No se redirigió a la página del carrito"

    # Verificar que el producto está en el carrito
    cart_items_count = cart_page.get_cart_items_count()
    assert cart_items_count > 0, "No se encontraron productos en el carrito"
    print(f"[OK] Items en el carrito: {cart_items_count}")

    # Screenshot
    cart_page.take_screenshot("test_agregar_producto_carrito")
    print("[OK] Test 1 completado: Producto agregado al carrito")


@pytest.mark.smoke
def test_verificar_contenido_carrito(logged_in_inventory_page):
    """Test 2: Verificar contenido del carrito"""
    inventory_page = logged_in_inventory_page

    # Obtener nombre del primer producto antes de agregarlo
    product_name = inventory_page.get_first_product_name()
    print(f"[OK] Producto a agregar: {product_name}")

    # Agregar producto al carrito
    inventory_page.add_product_to_cart(0)

    # Ir al carrito
    inventory_page.click_cart()
    cart_page = CartPage(inventory_page.driver)

    # Verificar título de la página
    page_title = cart_page.get_page_title()
    assert page_title == "Your Cart", f"Título incorrecto: {page_title}"
    print(f"[OK] Título de la página del carrito: {page_title}")

    # Verificar que el producto agregado está en el carrito
    cart_item_name = cart_page.get_first_item_name()
    assert cart_item_name == product_name, \
        f"El producto en el carrito no coincide. Esperado: {product_name}, Obtenido: {cart_item_name}"
    print(f"[OK] Producto en el carrito: {cart_item_name}")

    # Screenshot
    cart_page.take_screenshot("test_verificar_contenido_carrito")
    print("[OK] Test 2 completado: Contenido del carrito verificado")


def test_agregar_multiples_productos(logged_in_inventory_page):
    """Test 3: Agregar múltiples productos al carrito"""
    inventory_page = logged_in_inventory_page

    # Agregar 3 productos al carrito
    num_products = 3
    for i in range(num_products):
        result = inventory_page.add_product_to_cart(i)
        assert result, f"No se pudo agregar el producto {i+1}"

    # Verificar contador del carrito
    cart_count = inventory_page.get_cart_count()
    assert cart_count == num_products, \
        f"El contador del carrito es incorrecto. Esperado: {num_products}, Obtenido: {cart_count}"
    print(f"[OK] {num_products} productos agregados al carrito")

    # Ir al carrito
    inventory_page.click_cart()
    cart_page = CartPage(inventory_page.driver)

    # Verificar cantidad de items en el carrito
    cart_items_count = cart_page.get_cart_items_count()
    assert cart_items_count == num_products, \
        f"La cantidad de items en el carrito es incorrecta. Esperado: {num_products}, Obtenido: {cart_items_count}"
    print(f"[OK] Items en el carrito: {cart_items_count}")

    # Screenshot
    cart_page.take_screenshot("test_agregar_multiples_productos")
    print("[OK] Test 3 completado: Múltiples productos agregados")


def test_remover_producto_carrito(logged_in_inventory_page):
    """Test 4: Remover producto del carrito"""
    inventory_page = logged_in_inventory_page

    # Agregar un producto
    inventory_page.add_product_to_cart(0)

    # Ir al carrito
    inventory_page.click_cart()
    cart_page = CartPage(inventory_page.driver)

    # Verificar que hay items en el carrito
    initial_count = cart_page.get_cart_items_count()
    assert initial_count > 0, "No hay items en el carrito"
    print(f"[OK] Items iniciales en el carrito: {initial_count}")

    # Remover el producto
    remove_result = cart_page.remove_item(0)
    assert remove_result, "No se pudo remover el producto"

    # Verificar que se removió
    final_count = cart_page.get_cart_items_count()
    assert final_count == initial_count - 1, "El producto no se removió correctamente"
    print(f"[OK] Items después de remover: {final_count}")

    # Screenshot
    cart_page.take_screenshot("test_remover_producto_carrito")
    print("[OK] Test 4 completado: Producto removido del carrito")
