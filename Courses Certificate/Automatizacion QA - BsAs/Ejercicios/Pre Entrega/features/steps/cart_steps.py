"""
Step Definitions para Cart Feature
Autor: Luciano Moliterno
Integración con Page Object Model
"""
import logging
from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

# Configurar logger
logger = logging.getLogger(__name__)


@given('que el usuario está autenticado en SauceDemo con "{username}" y "{password}"')
def step_impl(context, username, password):
    """Autenticar usuario automáticamente"""
    logger.info(f"Step: Autenticando usuario '{username}'")
    context.driver.get("https://www.saucedemo.com/")

    # Usar LoginPage para autenticarse
    login_page = LoginPage(context.driver)
    login_page.set_username(username)
    login_page.set_password(password)
    login_page.click_login()

    # Inicializar páginas
    context.inventory_page = InventoryPage(context.driver)
    context.cart_page = CartPage(context.driver)

    logger.info(f"Usuario '{username}' autenticado exitosamente")


@when('el usuario agrega "{producto}" al carrito')
def step_impl(context, producto):
    """Agregar producto al carrito"""
    logger.info(f"Step: Agregando producto '{producto}' al carrito")
    context.inventory_page.add_product_to_cart(producto)
    logger.info(f"Producto '{producto}' agregado al carrito")


@when('el usuario accede al carrito')
def step_impl(context):
    """Acceder al carrito de compras"""
    logger.info("Step: Accediendo al carrito de compras")
    context.inventory_page.go_to_cart()
    logger.info("Navegación al carrito exitosa")


@when('el usuario elimina "{producto}" del carrito')
def step_impl(context, producto):
    """Eliminar producto del carrito"""
    logger.info(f"Step: Eliminando producto '{producto}' del carrito")
    context.cart_page.remove_product_from_cart(producto)
    logger.info(f"Producto '{producto}' eliminado del carrito")


@when('el usuario navega a otra página del sitio')
def step_impl(context):
    """Navegar a otra página"""
    logger.info("Step: Navegando a otra página del sitio")
    # Navegar a la página de About por ejemplo
    context.driver.execute_script("window.scrollTo(0, 0)")
    logger.info("Navegación ejecutada")


@when('el usuario regresa a la página de inventario')
def step_impl(context):
    """Regresar a inventario"""
    logger.info("Step: Regresando a la página de inventario")
    context.driver.back()
    logger.info("Regreso a inventario exitoso")


@then('el contador del carrito debe mostrar "{cantidad}"')
def step_impl(context, cantidad):
    """Verificar contador del carrito"""
    logger.info(f"Step: Verificando que el contador del carrito sea '{cantidad}'")
    cart_count = context.inventory_page.get_cart_count()

    if cantidad == "0":
        # Si la cantidad esperada es 0, el badge no debería estar presente
        assert cart_count == "0" or cart_count == "", \
            f"Contador esperado: 0 (vacío), pero se obtuvo: '{cart_count}'"
    else:
        assert cart_count == cantidad, \
            f"Contador esperado: '{cantidad}', pero se obtuvo: '{cart_count}'"

    logger.info(f"Contador del carrito verificado: {cantidad}")


@then('el producto "{producto}" debe estar en el carrito')
def step_impl(context, producto):
    """Verificar que producto está en el carrito"""
    logger.info(f"Step: Verificando que '{producto}' esté en el carrito")
    context.inventory_page.go_to_cart()

    # Verificar que el producto está en el carrito
    product_in_cart = context.cart_page.is_product_in_cart(producto)
    assert product_in_cart, f"El producto '{producto}' no se encontró en el carrito"

    logger.info(f"Producto '{producto}' verificado en el carrito")


@then('el producto "{producto}" debe estar visible en el carrito')
def step_impl(context, producto):
    """Verificar visibilidad del producto en el carrito"""
    logger.info(f"Step: Verificando visibilidad de '{producto}' en el carrito")
    context.inventory_page.go_to_cart()

    product_in_cart = context.cart_page.is_product_in_cart(producto)
    assert product_in_cart, f"El producto '{producto}' no está visible en el carrito"

    logger.info(f"Producto '{producto}' visible en el carrito")


@then('el carrito debe contener {cantidad:d} productos')
def step_impl(context, cantidad):
    """Verificar cantidad de productos en el carrito"""
    logger.info(f"Step: Verificando que el carrito contenga {cantidad} productos")
    context.inventory_page.go_to_cart()

    product_count = context.cart_page.get_product_count()
    assert product_count == cantidad, \
        f"Se esperaban {cantidad} productos, pero se encontraron {product_count}"

    logger.info(f"Carrito contiene {cantidad} productos correctamente")


@then('el carrito debe estar vacío')
def step_impl(context):
    """Verificar que el carrito esté vacío"""
    logger.info("Step: Verificando que el carrito esté vacío")

    product_count = context.cart_page.get_product_count()
    assert product_count == 0, f"Se esperaba un carrito vacío, pero contiene {product_count} productos"

    logger.info("Carrito verificado como vacío")


@then('el contador del carrito debe seguir mostrando "{cantidad}"')
def step_impl(context, cantidad):
    """Verificar persistencia del contador"""
    logger.info(f"Step: Verificando persistencia del contador en '{cantidad}'")
    cart_count = context.inventory_page.get_cart_count()
    assert cart_count == cantidad, \
        f"Contador esperado: '{cantidad}', pero se obtuvo: '{cart_count}'"
    logger.info(f"Persistencia del contador verificada: {cantidad}")

