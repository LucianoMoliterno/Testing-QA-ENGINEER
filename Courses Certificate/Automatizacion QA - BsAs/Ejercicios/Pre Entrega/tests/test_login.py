"""
Tests de Login usando Page Object Model
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_login_exitoso(driver):
    """Test 1: Login exitoso con credenciales válidas"""
    # Arrange
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Act
    login_page.login('standard_user', 'secret_sauce')

    # Assert
    assert inventory_page.verify_page_loaded(), "No se redirigió a la página de inventario"
    assert "inventory.html" in driver.current_url, "La URL no contiene 'inventory.html'"

    # Screenshot
    login_page.take_screenshot("test_login_exitoso")
    print("[OK] Test 1 completado: Login exitoso")


@pytest.mark.smoke
def test_login_usuario_bloqueado(driver):
    """Test 2: Login con usuario bloqueado"""
    # Arrange
    login_page = LoginPage(driver)

    # Act
    login_page.login('locked_out_user', 'secret_sauce')

    # Assert
    assert login_page.is_error_message_displayed(), "No se mostró mensaje de error"
    error_message = login_page.get_error_message()
    assert "locked out" in error_message.lower(), f"Mensaje de error incorrecto: {error_message}"

    # Screenshot
    login_page.take_screenshot("test_login_usuario_bloqueado")
    print("[OK] Test 2 completado: Usuario bloqueado detectado")


def test_login_credenciales_invalidas(driver):
    """Test 3: Login con credenciales inválidas"""
    # Arrange
    login_page = LoginPage(driver)

    # Act
    login_page.login('usuario_invalido', 'password_invalido')

    # Assert
    assert login_page.is_error_message_displayed(), "No se mostró mensaje de error"
    error_message = login_page.get_error_message()
    assert error_message is not None, "No se pudo obtener el mensaje de error"

    # Screenshot
    login_page.take_screenshot("test_login_credenciales_invalidas")
    print("[OK] Test 3 completado: Credenciales inválidas detectadas")

