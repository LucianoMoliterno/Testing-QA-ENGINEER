"""
Tests del Carrito usando Data-Driven Testing (DDT) con JSON
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.datos import DataLoader


# Cargar datos desde JSON
productos_data = DataLoader.get_productos_data()


@pytest.fixture
def logged_in_user(driver):
    """Fixture que hace login y retorna el driver"""
    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')
    return driver


@pytest.mark.parametrize("producto", productos_data.get('productos_a_comprar', []))
@pytest.mark.smoke
def test_agregar_productos_desde_json(logged_in_user, producto):
    """Test parametrizado: Agregar productos al carrito desde JSON"""
    driver = logged_in_user
    inventory_page = InventoryPage(driver)

    producto_id = producto['id']
    nombre_esperado = producto['nombre']
    descripcion = producto['descripcion']

    print(f"\n[TEST] {descripcion}")
    print(f"[DATA] Producto: {nombre_esperado} - ID: {producto_id}")

    # Obtener contador inicial
    initial_count = inventory_page.get_cart_count()

    # Agregar producto
    result = inventory_page.add_product_to_cart(producto_id)
    assert result, f"No se pudo agregar el producto {nombre_esperado}"

    # Verificar contador
    new_count = inventory_page.get_cart_count()
    assert new_count == initial_count + 1, "El contador no se incrementó correctamente"

    print(f"[OK] Producto agregado - Contador: {initial_count} -> {new_count}")

    # Screenshot
    inventory_page.take_screenshot(f"test_producto_json_{producto_id}")

    # Limpiar carrito para el siguiente test
    driver.get("https://www.saucedemo.com/inventory.html")


@pytest.mark.parametrize("compra", productos_data.get('compras_multiples', []))
@pytest.mark.smoke
def test_compras_multiples_desde_json(logged_in_user, compra):
    """Test parametrizado: Compras múltiples desde JSON"""
    driver = logged_in_user
    inventory_page = InventoryPage(driver)

    productos_indices = compra['productos_indices']
    cantidad_esperada = compra['cantidad_esperada']
    descripcion = compra['descripcion']

    print(f"\n[TEST] {descripcion}")
    print(f"[DATA] Productos a agregar: {productos_indices}")

    # Agregar múltiples productos
    for index in productos_indices:
        result = inventory_page.add_product_to_cart(index)
        assert result, f"Error al agregar producto en índice {index}"

    # Verificar contador del carrito
    cart_count = inventory_page.get_cart_count()
    assert cart_count == cantidad_esperada, \
        f"Cantidad incorrecta. Esperado: {cantidad_esperada}, Obtenido: {cart_count}"

    print(f"[OK] {cantidad_esperada} productos agregados correctamente")

    # Ir al carrito y verificar
    inventory_page.click_cart()
    cart_page = CartPage(driver)

    items_in_cart = cart_page.get_cart_items_count()
    assert items_in_cart == cantidad_esperada, \
        f"Items en carrito incorrectos. Esperado: {cantidad_esperada}, Obtenido: {items_in_cart}"

    print(f"[OK] Carrito verificado - {items_in_cart} items")

    # Screenshot
    cart_page.take_screenshot(f"test_compra_multiple_{cantidad_esperada}_productos")

    # Limpiar para el siguiente test
    driver.get("https://www.saucedemo.com/inventory.html")


@pytest.mark.parametrize("escenario", productos_data.get('escenarios_carrito', []))
@pytest.mark.smoke
def test_escenarios_carrito_desde_json(logged_in_user, escenario):
    """Test parametrizado: Diferentes escenarios de carrito desde JSON"""
    driver = logged_in_user
    inventory_page = InventoryPage(driver)

    accion = escenario['accion']
    producto_index = escenario['producto_index']
    descripcion = escenario['descripcion']

    print(f"\n[TEST] {descripcion}")
    print(f"[DATA] Acción: {accion}, Producto: {producto_index}")

    if accion == 'agregar_y_verificar':
        # Agregar y verificar contador
        initial_count = inventory_page.get_cart_count()
        inventory_page.add_product_to_cart(producto_index)
        new_count = inventory_page.get_cart_count()

        assert new_count == initial_count + 1, "Contador no se incrementó"
        print(f"[OK] Contador verificado: {initial_count} -> {new_count}")

    elif accion == 'agregar_y_remover':
        # Agregar producto y luego removerlo
        inventory_page.add_product_to_cart(producto_index)
        initial_count = inventory_page.get_cart_count()

        inventory_page.click_cart()
        cart_page = CartPage(driver)

        cart_page.remove_item(0)

        # Volver a inventory para verificar contador
        driver.get("https://www.saucedemo.com/inventory.html")
        inventory_page = InventoryPage(driver)
        final_count = inventory_page.get_cart_count()

        assert final_count < initial_count, "El producto no se removió"
        print(f"[OK] Producto removido - Contador: {initial_count} -> {final_count}")

    elif accion == 'verificar_contenido':
        # Agregar y verificar que el producto correcto está en el carrito
        product_name = inventory_page.get_all_product_names()[producto_index]
        inventory_page.add_product_to_cart(producto_index)

        inventory_page.click_cart()
        cart_page = CartPage(driver)

        cart_items = cart_page.get_cart_item_names()
        assert product_name in cart_items, f"Producto {product_name} no está en el carrito"
        print(f"[OK] Producto verificado en carrito: {product_name}")

    # Screenshot
    inventory_page.take_screenshot(f"test_escenario_{accion}")

    # Limpiar
    driver.get("https://www.saucedemo.com/inventory.html")


@pytest.mark.smoke
def test_flujo_completo_compra_desde_json(logged_in_user):
    """Test de flujo completo usando datos del JSON"""
    driver = logged_in_user
    inventory_page = InventoryPage(driver)

    # Obtener el primer escenario de compra múltiple
    compras = productos_data.get('compras_multiples', [])
    if not compras:
        pytest.skip("No hay datos de compras en el JSON")

    compra = compras[0]
    productos_indices = compra['productos_indices']

    print(f"\n[TEST] Flujo completo de compra")
    print(f"[DATA] Comprando {len(productos_indices)} productos")

    # 1. Agregar productos
    for index in productos_indices:
        inventory_page.add_product_to_cart(index)

    cart_count = inventory_page.get_cart_count()
    print(f"[OK] Paso 1: {cart_count} productos en el carrito")

    # 2. Ir al carrito
    inventory_page.click_cart()
    cart_page = CartPage(driver)

    items_count = cart_page.get_cart_items_count()
    assert items_count == len(productos_indices), "Cantidad de items incorrecta"
    print(f"[OK] Paso 2: Carrito verificado - {items_count} items")

    # 3. Verificar página del carrito
    assert cart_page.verify_page_loaded(), "No se cargó la página del carrito"
    page_title = cart_page.get_page_title()
    assert page_title == "Your Cart", f"Título incorrecto: {page_title}"
    print(f"[OK] Paso 3: Página del carrito correcta")

    # Screenshot final
    cart_page.take_screenshot("test_flujo_completo_json")
    print(f"[OK] Flujo completo ejecutado exitosamente")


def test_validar_estructura_json():
    """Test que valida la estructura del archivo JSON"""
    data = DataLoader.get_productos_data()

    assert data, "El JSON debe contener datos"

    # Verificar secciones principales
    assert 'productos_a_comprar' in data, "Falta sección 'productos_a_comprar'"
    assert 'compras_multiples' in data, "Falta sección 'compras_multiples'"
    assert 'escenarios_carrito' in data, "Falta sección 'escenarios_carrito'"

    # Verificar estructura de productos
    productos = data['productos_a_comprar']
    for producto in productos:
        assert 'id' in producto, "Producto sin campo 'id'"
        assert 'nombre' in producto, "Producto sin campo 'nombre'"
        assert 'precio' in producto, "Producto sin campo 'precio'"

    print(f"[OK] Estructura del JSON validada")
    print(f"     - {len(productos)} productos")
    print(f"     - {len(data['compras_multiples'])} escenarios de compra múltiple")
    print(f"     - {len(data['escenarios_carrito'])} escenarios de carrito")
"""
Tests de Login usando Data-Driven Testing (DDT) con CSV
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.datos import DataLoader, TestDataHelper


# Cargar datos desde CSV
login_data = DataLoader.get_login_data()


@pytest.mark.parametrize("test_data", login_data, ids=TestDataHelper.prepare_test_ids(login_data))
@pytest.mark.smoke
def test_login_desde_csv(driver, test_data):
    """Test parametrizado: Login con datos desde CSV"""
    # Arrange
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    username = test_data['username']
    password = test_data['password']
    expected_result = test_data['expected_result']
    test_case = test_data['test_case']

    print(f"\n[TEST] Ejecutando: {test_case}")
    print(f"[DATA] Usuario: '{username}', Password: '{'*' * len(password) if password else '(vacío)'}'")

    # Act
    login_page.login(username, password)

    # Assert según el resultado esperado
    if expected_result == 'success':
        assert inventory_page.verify_page_loaded(), f"Login debería ser exitoso para: {test_case}"
        assert "inventory.html" in driver.current_url, "No se redirigió a inventory"
        print(f"[OK] Login exitoso - {test_case}")

    elif expected_result == 'locked':
        assert login_page.is_error_message_displayed(), f"Debería mostrar error para: {test_case}"
        error_msg = login_page.get_error_message()
        assert "locked out" in error_msg.lower(), f"Mensaje de error incorrecto: {error_msg}"
        print(f"[OK] Usuario bloqueado detectado - {test_case}")

    elif expected_result == 'error':
        assert login_page.is_error_message_displayed(), f"Debería mostrar error para: {test_case}"
        error_msg = login_page.get_error_message()
        assert error_msg is not None, "No se mostró mensaje de error"
        print(f"[OK] Error detectado correctamente - {test_case}")

    # Screenshot
    login_page.take_screenshot(f"test_login_csv_{test_case.replace(' ', '_')}")


@pytest.mark.smoke
def test_login_exitosos_desde_csv(driver):
    """Test que valida solo los logins exitosos del CSV"""
    # Filtrar solo los casos exitosos
    successful_logins = TestDataHelper.filter_by_result(login_data, 'success')

    print(f"\n[INFO] Validando {len(successful_logins)} casos de login exitoso")

    for test_data in successful_logins:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        username = test_data['username']
        password = test_data['password']
        test_case = test_data['test_case']

        print(f"\n[TEST] {test_case}")

        # Navegar a la página de login si no estamos ahí
        if "inventory.html" in driver.current_url:
            driver.get("https://www.saucedemo.com/")

        login_page.login(username, password)

        # Verificar login exitoso
        assert inventory_page.verify_page_loaded(), f"Login falló para: {username}"
        print(f"[OK] {username} - Login verificado")

        # Volver a login para el siguiente test
        driver.get("https://www.saucedemo.com/")


@pytest.mark.smoke
def test_login_con_errores_desde_csv(driver):
    """Test que valida los casos de error del CSV"""
    # Filtrar solo los casos con error
    error_logins = TestDataHelper.filter_by_result(login_data, 'error')

    print(f"\n[INFO] Validando {len(error_logins)} casos de login con error")

    login_page = LoginPage(driver)

    for test_data in error_logins:
        username = test_data['username']
        password = test_data['password']
        test_case = test_data['test_case']

        print(f"\n[TEST] {test_case}")

        login_page.login(username, password)

        # Verificar que se muestra error
        assert login_page.is_error_message_displayed(), f"No se mostró error para: {test_case}"
        print(f"[OK] Error validado - {test_case}")

        # Refrescar para el siguiente test
        driver.refresh()


def test_validar_estructura_csv():
    """Test que valida la estructura del archivo CSV"""
    data = DataLoader.get_login_data()

    assert len(data) > 0, "El CSV debe contener datos"

    # Verificar que todos los registros tienen los campos requeridos
    required_fields = ['username', 'password', 'expected_result', 'test_case']

    for i, record in enumerate(data):
        for field in required_fields:
            assert field in record, f"Registro {i} no tiene el campo '{field}'"

    print(f"[OK] Estructura del CSV validada - {len(data)} registros correctos")

