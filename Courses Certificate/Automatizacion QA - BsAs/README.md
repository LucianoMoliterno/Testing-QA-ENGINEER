# 🚀 Proyecto Final - Automation Testing

Este repositorio contiene el framework de automatización desarrollado como proyecto final para la carrera de **Automation Testing**. El proyecto integra pruebas End-to-End (Web UI) y pruebas de API, ejecutadas automáticamente mediante un pipeline de CI/CD.

## 📋 Contexto del Proyecto
El objetivo principal fue construir una solución robusta de aseguramiento de calidad para [Nombre de tu App/Sistema], cubriendo los flujos críticos de negocio y validando tanto la interfaz de usuario como los servicios de backend.

## 🛠 Tech Stack
El framework utiliza las herramientas y prácticas aprendidas durante el curso:

* **Lenguaje:** Python
* **Web UI:** Selenium WebDriver (Implementando Page Object Model)
* **API Testing:** Pytest + Requests
* **BDD (Opcional):** Behave
* **Reportes:** Allure Reports
* **CI/CD:** GitHub Actions
* **Calidad de Código:** Pylint / Flake8

## 📂 Estructura del Framework
* **Page Objects:** Abstracción de páginas para fácil mantenimiento.
* **Fixtures:** Gestión de setup/teardown y datos de prueba.
* **Data Driven:** Uso de archivos JSON/CSV para pruebas parametrizadas.
* **Logs & Screenshots:** Evidencia automática en caso de fallos.

## ⚙️ Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/usuario/proyecto-final.git](https://github.com/usuario/proyecto-final.git)
    cd proyecto-final
    ```

2.  **Crear entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Ejecución de Pruebas

Para correr la suite completa de pruebas:
```bash
pytest
