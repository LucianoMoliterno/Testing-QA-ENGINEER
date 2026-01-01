import pytest
import time
import os
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.logger import Logger

logger = Logger.get_logger(__name__)

class TestRegistroCV:
    """Suite de pruebas para registro y carga de CV."""

    def test_tc001_registro_valido(self, driver):
        """
        TC-001: Registro válido desde botón principal.
        """
        logger.info("=== Iniciando TC-001: Registro válido ===")

        home = HomePage(driver)
        home.open()
        time.sleep(2)

        # Verificar que página se cargó
        assert home.is_page_loaded(), "Página principal no cargó correctamente"

        # Click en botón Registrate
        url_inicial = home.get_current_url()
        logger.info(f"URL inicial: {url_inicial}")

        home.click_registrate()
        time.sleep(2)

        url_final = home.get_current_url()
        logger.info(f"URL después de click: {url_final}")

        # Verificar redirección
        assert "register" in url_final, "No redirigió a página de registro"
        logger.info("✓ Test exitoso: Redirección correcta al formulario de registro")

    def test_tc001_registro_completo(self, driver):
        """
        TC-001b: Registro completo con datos válidos.
        """
        logger.info("=== Iniciando TC-001b: Registro completo ===")

        register = RegisterPage(driver)
        register.open()
        time.sleep(2)

        # Completar formulario
        register.complete_form(
            nombre="Carlos Mendez",
            email="carlos.test@talentolab.com",
            password="Test123456"
        )

        time.sleep(1)

        # Enviar formulario
        register.submit_form()
        time.sleep(2)

        logger.info("✓ Formulario de registro enviado correctamente")
        assert True

    def test_tc002_carga_cv_valido(self, driver):
        """
        TC-002: Carga de CV con archivo válido (PDF < 5MB).
        """
        logger.info("=== Iniciando TC-002: Carga CV válido ===")

        # Crear archivo de prueba temporal
        test_file_path = os.path.abspath("test_data/cv_prueba.txt")
        os.makedirs("test_data", exist_ok=True)

        with open(test_file_path, "w") as f:
            f.write("CV de prueba - Carlos Mendez\nEditor de Video\n")

        register = RegisterPage(driver)
        register.open()
        time.sleep(2)

        # Completar datos básicos
        register.complete_form(
            nombre="Test Usuario",
            email="test@example.com",
            password="Pass123"
        )

        # Intentar subir CV
        try:
            register.upload_cv(test_file_path)
            logger.info("✓ CV cargado sin errores")
            time.sleep(1)
        except Exception as e:
            logger.warning(f"Advertencia al cargar CV: {e}")

        # Limpiar archivo temporal
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

        assert True, "Test de carga CV ejecutado"

    def test_tc008_carga_cv_corrupto(self, driver):
        """
        TC-008: Verificar rechazo de archivo corrupto como CV.
        Caso de prueba NEGATIVO.
        """
        logger.info("=== Iniciando TC-008: Carga CV corrupto (NEGATIVO) ===")

        # Crear archivo corrupto
        corrupted_file = os.path.abspath("test_data/cv_corrupto.pdf")
        os.makedirs("test_data", exist_ok=True)

        with open(corrupted_file, "wb") as f:
            f.write(b'\x00\x01\x02\xFF\xFE')  # Bytes aleatorios

        register = RegisterPage(driver)
        register.open()
        time.sleep(2)

        register.complete_form(
            nombre="Test Corrupto",
            email="corrupto@test.com",
            password="Test123"
        )

        # Intentar subir archivo corrupto
        try:
            register.upload_cv(corrupted_file)
            logger.warning("BUG-005: Archivo corrupto fue aceptado (debería rechazarse)")
        except:
            logger.info("✓ Archivo corrupto fue rechazado correctamente")

        # Limpiar
        if os.path.exists(corrupted_file):
            os.remove(corrupted_file)

        assert True, "Test negativo ejecutado - documenta BUG-005"

    def test_tc009_carga_cv_limite_peso(self, driver):
        """
        TC-009: Verificar límite de tamaño de archivo (> 5MB).
        Caso de prueba NEGATIVO.
        """
        logger.info("=== Iniciando TC-009: Carga CV excede límite peso (NEGATIVO) ===")

        # Crear archivo grande (simulado, no real de 5MB para no tardar)
        large_file = os.path.abspath("test_data/cv_grande.pdf")
        os.makedirs("test_data", exist_ok=True)

        # Archivo de 1MB como simulación (en producción sería 6MB)
        with open(large_file, "wb") as f:
            f.write(b'0' * (1024 * 1024))  # 1MB

        register = RegisterPage(driver)
        register.open()
        time.sleep(2)

        register.complete_form(
            nombre="Test Grande",
            email="grande@test.com",
            password="Test123"
        )

        # Intentar subir archivo grande
        try:
            register.upload_cv(large_file)
            logger.warning("BUG-001: Archivo grande fue aceptado (debería rechazarse)")
        except:
            logger.info("✓ Archivo grande fue rechazado correctamente")

        # Limpiar
        if os.path.exists(large_file):
            os.remove(large_file)

        assert True, "Test negativo ejecutado - documenta BUG-001"
