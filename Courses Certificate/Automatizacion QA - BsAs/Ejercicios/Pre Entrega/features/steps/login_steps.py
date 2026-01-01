"""
Step Definitions para Login Feature
Autor: Luciano Moliterno
Integración con Page Object Model
"""
import logging
from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Configurar logger
logger = logging.getLogger(__name__)


@given('que el usuario está en la página de login de SauceDemo')
def step_impl(context):
    """Navegar a la página de login"""
    logger.info("Step: Navegando a la página de login de SauceDemo")
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.driver)
    logger.info("Página de login cargada exitosamente")


@when('el usuario ingresa el nombre de usuario "{username}"')
def step_impl(context, username):
    """Ingresar nombre de usuario (incluyendo strings vacíos)"""
    logger.info(f"Step: Ingresando nombre de usuario: '{username}'")
    # Manejar caso de string vacío
    if username:
        context.login_page.set_username(username)
        logger.info(f"Nombre de usuario '{username}' ingresado correctamente")
    else:
        logger.info("Nombre de usuario vacío - no se ingresa nada")


@when('el usuario ingresa la contraseña "{password}"')
def step_impl(context, password):
    """Ingresar contraseña (incluyendo strings vacíos)"""
    logger.info(f"Step: Ingresando contraseña")
    # Manejar caso de string vacío
    if password:
        context.login_page.set_password(password)
        logger.info("Contraseña ingresada correctamente")
    else:
        logger.info("Contraseña vacía - no se ingresa nada")


@when('el usuario hace clic en el botón de login')
def step_impl(context):
    """Hacer clic en el botón de login"""
    logger.info("Step: Haciendo clic en el botón de login")
    context.login_page.click_login()
    context.inventory_page = InventoryPage(context.driver)
    logger.info("Clic en botón de login ejecutado")


@when('el usuario hace clic en el botón de login sin ingresar credenciales')
def step_impl(context):
    """Hacer clic en login sin credenciales"""
    logger.info("Step: Haciendo clic en login sin ingresar credenciales")
    context.login_page.click_login()
    logger.info("Intento de login sin credenciales")


@when('el usuario hace clic en el botón de login sin ingresar contraseña')
def step_impl(context):
    """Hacer clic en login sin contraseña"""
    logger.info("Step: Haciendo clic en login sin contraseña")
    context.login_page.click_login()
    logger.info("Intento de login sin contraseña")


@then('el usuario debe ser redirigido a la página de inventario')
def step_impl(context):
    """Verificar redirección al inventario"""
    logger.info("Step: Verificando redirección a página de inventario")
    current_url = context.driver.current_url
    assert "inventory.html" in current_url, f"No se redirigió al inventario. URL actual: {current_url}"
    logger.info(f"Redirección exitosa a: {current_url}")


@then('el usuario debe ver el título "{titulo}" en la página')
def step_impl(context, titulo):
    """Verificar título de la página"""
    logger.info(f"Step: Verificando que el título sea '{titulo}'")
    page_title = context.inventory_page.get_page_title()
    assert page_title == titulo, f"Título esperado: '{titulo}', pero se obtuvo: '{page_title}'"
    logger.info(f"Título '{titulo}' encontrado correctamente")


@then('el usuario debe ver el mensaje de error "{mensaje}"')
def step_impl(context, mensaje):
    """Verificar mensaje de error"""
    logger.info(f"Step: Verificando mensaje de error")
    error_message = context.login_page.get_error_message()
    assert mensaje in error_message, f"Mensaje esperado: '{mensaje}', pero se obtuvo: '{error_message}'"
    logger.info(f"Mensaje de error verificado: {error_message}")
