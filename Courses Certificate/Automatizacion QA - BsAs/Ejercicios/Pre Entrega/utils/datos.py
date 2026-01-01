"""
Utilidades para cargar y manejar datos de prueba desde archivos externos
"""
import csv
import json
import os


class DataLoader:
    """Clase para cargar datos desde archivos CSV y JSON"""

    @staticmethod
    def get_data_path(filename):
        """Obtiene la ruta absoluta del archivo de datos"""
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(current_dir, 'datos', filename)

    @staticmethod
    def load_csv(filename):
        """
        Carga datos desde un archivo CSV

        Args:
            filename (str): Nombre del archivo CSV

        Returns:
            list: Lista de diccionarios con los datos del CSV
        """
        data = []
        file_path = DataLoader.get_data_path(filename)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    data.append(row)
            print(f"[OK] Datos cargados desde {filename}: {len(data)} registros")
            return data
        except FileNotFoundError:
            print(f"[ERROR] Archivo no encontrado: {file_path}")
            return []
        except Exception as e:
            print(f"[ERROR] Error al leer CSV: {e}")
            return []

    @staticmethod
    def load_json(filename):
        """
        Carga datos desde un archivo JSON

        Args:
            filename (str): Nombre del archivo JSON

        Returns:
            dict: Diccionario con los datos del JSON
        """
        file_path = DataLoader.get_data_path(filename)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            print(f"[OK] Datos cargados desde {filename}")
            return data
        except FileNotFoundError:
            print(f"[ERROR] Archivo no encontrado: {file_path}")
            return {}
        except json.JSONDecodeError as e:
            print(f"[ERROR] Error al decodificar JSON: {e}")
            return {}
        except Exception as e:
            print(f"[ERROR] Error al leer JSON: {e}")
            return {}

    @staticmethod
    def get_login_data():
        """Obtiene los datos de login desde el CSV"""
        return DataLoader.load_csv('login.csv')

    @staticmethod
    def get_productos_data():
        """Obtiene los datos de productos desde el JSON"""
        return DataLoader.load_json('productos.json')


class TestDataHelper:
    """Clase auxiliar para preparar datos de test"""

    @staticmethod
    def filter_by_result(login_data, expected_result):
        """
        Filtra datos de login por resultado esperado

        Args:
            login_data (list): Lista de datos de login
            expected_result (str): Resultado esperado (success, error, locked)

        Returns:
            list: Lista filtrada
        """
        return [data for data in login_data if data['expected_result'] == expected_result]

    @staticmethod
    def prepare_test_ids(data_list, id_field='test_case'):
        """
        Prepara IDs descriptivos para parametrización de tests

        Args:
            data_list (list): Lista de datos
            id_field (str): Campo a usar como ID

        Returns:
            list: Lista de IDs
        """
        return [data.get(id_field, f"test_{i}") for i, data in enumerate(data_list)]
