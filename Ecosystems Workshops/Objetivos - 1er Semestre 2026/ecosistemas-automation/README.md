# Automatización de Pruebas - Ecosistemas Global

Este proyecto contiene scripts de automatización para cubrir pruebas funcionales críticas de la regresión manual en la web de Ecosistemas Global. Se armó como parte del objetivo de desarrollo técnico de Automation QA.

## Tecnologías y Herramientas
* Java (JDK 17)
* Selenium WebDriver 4.18.1
* TestNG 7.9.0 (para la ejecución y aserciones)
* Maven (gestión de dependencias)

## Estructura del Código
Se aplicó el patrón Page Object Model (POM) para separar los elementos de la interfaz de la lógica de los tests:
* `src/main/java/pages/EcosistemasPage.java`: Mapeo de selectores (XPath, linkText) y métodos de acción (clics y manejo de esperas).
* `src/test/java/tests/EcosistemasTest.java`: Casos de prueba ejecutables con validaciones (`Assert`).

## Generación de Evidencias
El código está configurado para tomar capturas de pantalla automáticamente (`TakesScreenshot`) durante los pasos clave de cada prueba. Las imágenes se guardan en la carpeta `/capturas` en la raíz del proyecto en formato `.png`. Cada archivo incluye un timestamp dinámico en su nombre para mantener un historial de las ejecuciones sin sobreescribirse.

## Casos de Prueba Incluidos
1. **testAceptarCookies**: Verifica el comportamiento del banner de cookies y que no bloquee la interacción posterior.
2. **testNavegarAContacto**: Valida el redireccionamiento correcto a la sección de Contacto desde el menú principal.
3. **testNavegarATrabajaEnEco**: Valida el acceso a la sección de reclutamiento "Trabaja en ECO".

## Cómo ejecutar las pruebas localmente

1. Abrir el proyecto en IntelliJ IDEA.
2. Dejar que Maven recargue el proyecto y descargue las dependencias del `pom.xml`.
3. Ir a `src/test/java/tests/EcosistemasTest.java`.
4. Hacer clic derecho sobre la clase y seleccionar **Run 'EcosistemasTest'** (o usar el botón verde de Play).

*Nota: Selenium Manager (incluido en la versión 4) se encarga de gestionar el ChromeDriver de forma automática, por lo que no es necesario descargar binarios externos.*