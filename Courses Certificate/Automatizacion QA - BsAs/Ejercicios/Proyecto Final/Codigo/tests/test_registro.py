import pytest
import time
from pages.register_page import RegisterPage

# El parámetro 'driver' viene mágicamente de tu archivo conftest.py
def test_registro_nuevo_usuario(driver):
    """
    TC-001: Validar registro de usuario con datos válidos.
    """
    # 1. Instanciar la página (Darle el control del navegador al Page Object)
    registro = RegisterPage(driver)

    # 2. Navegar a la URL
    registro.open()

    # 3. Datos de prueba
    nombre_usuario = "Luciano Automation"
    email_usuario = "test_luciano@example.com"
    pass_usuario = "123456"

    # 4. Acciones: Llenar el formulario
    # Usamos el método que creamos en la Parte 2
    registro.complete_form(nombre_usuario, email_usuario, pass_usuario)

    # (Opcional) Espera visual de 2 segundos para que veas lo que pasa
    time.sleep(2)

    # 5. Validación (Assert)
    # Verificamos si el registro fue exitoso buscando el mensaje de bienvenida
    resultado = registro.is_registration_successful()

    # Si 'resultado' es None (no encontró el mensaje), el test fallará y tomará foto
    assert resultado is not None, "Error: No se mostró el mensaje de bienvenida tras el registro."

    print(f"Test Finalizado. Texto encontrado: {resultado}")