"""
Wrapper de Pytest para ejecutar suite BDD de Behave
Autor: Luciano Moliterno
Permite integrar tests BDD con la suite de Pytest
"""
import subprocess
import pytest
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class TestBehaveSuite:
    """Clase que ejecuta la suite BDD usando Behave desde Pytest"""

    def setup_method(self):
        """Configuración antes de cada test"""
        logger.info("Preparando ejecución de suite BDD con Behave")

        # Crear directorios necesarios
        Path("reports").mkdir(exist_ok=True)
        Path("reports/screens").mkdir(parents=True, exist_ok=True)

    @pytest.mark.bdd
    @pytest.mark.smoke
    def test_behave_smoke_tests(self):
        """
        Ejecuta solo los tests marcados con @smoke usando Behave
        Genera reportes en formato JSON y pretty
        """
        logger.info("="*80)
        logger.info("Ejecutando tests BDD @smoke con Behave")
        logger.info("="*80)

        # Comando para ejecutar Behave con tag @smoke
        cmd = [
            "behave",
            "-t", "@smoke",
            "-f", "json",
            "-o", "reports/behave_smoke.json",
            "-f", "pretty",
            "--no-capture"
        ]

        logger.info(f"Comando: {' '.join(cmd)}")

        # Ejecutar Behave
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        # Imprimir salida
        if result.stdout:
            print("\n" + result.stdout)

        if result.stderr:
            print("\nErrores/Warnings:")
            print(result.stderr)

        # Verificar resultado
        logger.info(f"Código de salida: {result.returncode}")

        assert result.returncode == 0, \
            f"Los tests BDD @smoke fallaron con código {result.returncode}"

        logger.info("Tests BDD @smoke completados exitosamente")

    @pytest.mark.bdd
    @pytest.mark.regression
    def test_behave_regression_tests(self):
        """
        Ejecuta solo los tests marcados con @regression usando Behave
        Genera reportes en formato JSON y pretty
        """
        logger.info("="*80)
        logger.info("Ejecutando tests BDD @regression con Behave")
        logger.info("="*80)

        # Comando para ejecutar Behave con tag @regression
        cmd = [
            "behave",
            "-t", "@regression",
            "-f", "json",
            "-o", "reports/behave_regression.json",
            "-f", "pretty",
            "--no-capture"
        ]

        logger.info(f"Comando: {' '.join(cmd)}")

        # Ejecutar Behave
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        # Imprimir salida
        if result.stdout:
            print("\n" + result.stdout)

        if result.stderr:
            print("\nErrores/Warnings:")
            print(result.stderr)

        # Verificar resultado
        logger.info(f"Código de salida: {result.returncode}")

        assert result.returncode == 0, \
            f"Los tests BDD @regression fallaron con código {result.returncode}"

        logger.info("Tests BDD @regression completados exitosamente")

    @pytest.mark.bdd
    def test_behave_all_ui_tests(self):
        """
        Ejecuta todos los tests UI usando Behave
        Genera reportes completos en múltiples formatos
        """
        logger.info("="*80)
        logger.info("Ejecutando TODOS los tests BDD @ui con Behave")
        logger.info("="*80)

        # Comando para ejecutar todos los tests @ui
        cmd = [
            "behave",
            "-t", "@ui",
            "-f", "json",
            "-o", "reports/behave_all.json",
            "-f", "pretty",
            "--no-capture",
            "--no-skipped"
        ]

        logger.info(f"Comando: {' '.join(cmd)}")

        # Ejecutar Behave
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        # Imprimir salida
        if result.stdout:
            print("\n" + result.stdout)

        if result.stderr:
            print("\nErrores/Warnings:")
            print(result.stderr)

        # Verificar resultado
        logger.info(f"Código de salida: {result.returncode}")

        assert result.returncode == 0, \
            f"Los tests BDD @ui fallaron con código {result.returncode}"

        logger.info("Todos los tests BDD @ui completados exitosamente")

    @pytest.mark.bdd
    @pytest.mark.dry_run
    def test_behave_dry_run(self):
        """
        Ejecuta Behave en modo dry-run para verificar que todos los steps están implementados
        No ejecuta los tests realmente, solo verifica la sintaxis
        """
        logger.info("="*80)
        logger.info("Ejecutando Behave en modo DRY-RUN (verificación)")
        logger.info("="*80)

        # Comando dry-run
        cmd = [
            "behave",
            "--dry-run",
            "--no-capture"
        ]

        logger.info(f"Comando: {' '.join(cmd)}")

        # Ejecutar Behave
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        # Imprimir salida
        if result.stdout:
            print("\n" + result.stdout)

        if result.stderr:
            print("\nErrores/Warnings:")
            print(result.stderr)

        # Verificar resultado
        logger.info(f"Código de salida: {result.returncode}")

        assert result.returncode == 0, \
            f"Dry-run falló: hay steps sin implementar o errores de sintaxis"

        logger.info("Dry-run completado: Todos los steps están implementados correctamente")


# Funciones auxiliares para ejecutar Behave directamente
def run_behave_with_tags(tags, output_file="behave.json"):
    """
    Función auxiliar para ejecutar Behave con tags específicos

    Args:
        tags: String con los tags a filtrar (ej: "@smoke", "@regression")
        output_file: Nombre del archivo JSON de salida

    Returns:
        subprocess.CompletedProcess con el resultado
    """
    cmd = [
        "behave",
        "-t", tags,
        "-f", "json",
        "-o", f"reports/{output_file}",
        "-f", "pretty"
    ]

    return subprocess.run(cmd, capture_output=True, text=True)


def run_behave_all_formats():
    """
    Ejecuta Behave generando reportes en todos los formatos disponibles
    """
    logger.info("Generando reportes en múltiples formatos...")

    cmd = [
        "behave",
        "-f", "json",
        "-o", "reports/behave_complete.json",
        "-f", "pretty",
        "--junit",
        "--junit-directory", "reports/junit"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    logger.info(f"Reportes generados en reports/")
    return result


if __name__ == "__main__":
    """
    Permite ejecutar este archivo directamente para testing
    """
    print("="*80)
    print("Ejecutando suite BDD completa...")
    print("="*80)

    # Ejecutar tests smoke
    print("\n[1/3] Ejecutando tests @smoke...")
    result_smoke = run_behave_with_tags("@smoke", "smoke.json")
    print(result_smoke.stdout)

    # Ejecutar tests regression
    print("\n[2/3] Ejecutando tests @regression...")
    result_regression = run_behave_with_tags("@regression", "regression.json")
    print(result_regression.stdout)

    # Ejecutar todos los formatos
    print("\n[3/3] Generando reportes completos...")
    result_all = run_behave_all_formats()
    print(result_all.stdout)

    print("\n" + "="*80)
    print("Suite BDD completada")
    print("="*80)

