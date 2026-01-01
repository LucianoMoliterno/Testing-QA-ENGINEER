import logging
import os
from datetime import datetime

class Logger:
    """Sistema de logging para registrar pasos clave durante la ejecución."""

    @staticmethod
    def get_logger(name=__name__):
        """Crea y configura un logger."""
        # Crear directorio de logs si no existe
        os.makedirs("reports/logs", exist_ok=True)

        # Nombre del archivo con fecha
        log_file = f"reports/logs/test_execution_{datetime.now().strftime('%Y-%m-%d')}.log"

        # Configurar logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # Evitar duplicados
        if not logger.handlers:
            # Handler para archivo
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(logging.INFO)

            # Handler para consola
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # Formato
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger

