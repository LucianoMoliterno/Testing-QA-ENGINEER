import json
import csv
import os

class DataReader:
    """Clase para leer datos de prueba desde archivos externos."""

    @staticmethod
    def read_json(file_path):
        """Lee datos desde un archivo JSON."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo {file_path} no existe")

        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def read_csv(file_path):
        """Lee datos desde un archivo CSV y retorna una lista de diccionarios."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo {file_path} no existe")

        data = []
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data
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

