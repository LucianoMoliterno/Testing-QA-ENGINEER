# Proyecto Final - Automatización de Pruebas E2E (Remeras Shop)

Este repositorio contiene el código fuente del Trabajo Práctico Final para el curso de Testing Automatizado. El objetivo del proyecto es la automatización de pruebas End-to-End (E2E) para el sitio de comercio electrónico "Remeras Shop", simulando el flujo completo de compra de un usuario.

El proyecto ha sido desarrollado utilizando **Java**, **Selenium WebDriver** para la interacción con el navegador, y **Cucumber** para la definición de escenarios en lenguaje natural (BDD).

## Requisitos Previos

Para ejecutar este proyecto correctamente, asegúrese de tener instalado el siguiente software en su entorno local:

1.  **Java JDK 17** (o superior): Necesario para compilar y ejecutar el código.
2.  **Apache Maven**: Herramienta para la gestión de dependencias y ciclo de vida del proyecto.
3.  **Google Chrome**: El navegador web donde se ejecutarán las pruebas automatizadas.
4.  **IDE**: Se recomienda utilizar **IntelliJ IDEA** o Eclipse para facilitar la visualización y edición del código.

## Configuración del Proyecto

Si es la primera vez que trabaja con un proyecto de automatización Java/Maven, siga estos pasos para configurar el entorno:

1.  **Obtener el código**: Descargue el archivo comprimido o clone el repositorio utilizando Git.
2.  **Importar en el IDE**:
    *   Abra IntelliJ IDEA.
    *   Seleccione `File > Open` y navegue hasta la carpeta `TpFinalSelenium` (donde se encuentra el archivo `pom.xml`).
    *   Confirme la apertura del proyecto.
3.  **Resolución de Dependencias**: Al abrir el proyecto, Maven comenzará automáticamente a descargar las librerías necesarias (Selenium, Cucumber, JUnit, etc.). Espere a que este proceso finalice (indicado por la barra de progreso en la parte inferior del IDE).

## Estructura del Proyecto

El proyecto sigue la estructura estándar de Maven y el patrón de diseño para pruebas automatizadas. A continuación se detalla la organización de los archivos:

```
TpFinalSelenium/
├── pom.xml                 <-- Archivo de configuración de Maven (dependencias)
├── README.md               <-- Documentación del proyecto
└── src/
    └── test/               <-- Directorio principal de pruebas
        ├── java/           <-- Código fuente Java
        │   ├── runners/
        │   │   └── TestRunner.java  <-- Clase ejecutora de las pruebas (JUnit)
        │   └── steps/
        │       └── CompraSteps.java <-- Definición de pasos (Step Definitions) y lógica de Selenium
        └── resources/      <-- Recursos de prueba
            └── features/
                └── compra.feature   <-- Escenarios de prueba en lenguaje Gherkin
```

*   **`pom.xml`**: Gestiona las dependencias del proyecto. Aquí se definen las versiones de Selenium, Cucumber y JUnit.
*   **`features/compra.feature`**: Contiene la descripción funcional de la prueba en formato Gherkin (Given/When/Then).
*   **`steps/CompraSteps.java`**: Contiene la implementación técnica de cada paso definido en el archivo feature.
*   **`runners/TestRunner.java`**: Clase encargada de vincular Cucumber con JUnit para la ejecución de los tests.

## Ejecución de las Pruebas

Existen dos métodos para ejecutar las pruebas automatizadas:

### Opción A: Desde la Terminal (Recomendado)
Abra una terminal o línea de comandos en la raíz del proyecto y ejecute el siguiente comando:

```bash
mvn test
```

Este comando compilará el código y ejecutará todos los escenarios de prueba. Al finalizar, se mostrará un resumen con el resultado (`BUILD SUCCESS` o `BUILD FAILURE`).

### Opción B: Desde el IDE (IntelliJ IDEA)
1.  Navegue hasta el archivo `src/test/java/runners/TestRunner.java`.
2.  Haga clic derecho sobre el archivo.
3.  Seleccione la opción `Run 'TestRunner'`.

## Descripción del Escenario de Prueba

El escenario principal automatizado es **"Compra exitosa con cupón y tarjeta de crédito"**, el cual valida el siguiente flujo crítico de negocio:

1.  **Navegación**: Acceso a la página de inicio de la tienda.
2.  **Selección de Productos**:
    *   Búsqueda y selección de "Remera Negra Básica" (Talle M, Cantidad 2).
    *   Búsqueda y selección de "Remera Blanca Premium" (Talle L, Cantidad 1).
3.  **Carrito de Compras**: Ingreso al carrito y aplicación del cupón de descuento `CUPON10`.
4.  **Checkout**:
    *   Completado de formulario de contacto y envío.
    *   Selección de método de envío "Normal".
    *   Selección de método de pago "Tarjeta de Crédito" e ingreso de datos ficticios.
5.  **Confirmación y Validación**:
    *   Confirmación de la compra.
    *   Verificación del mensaje de éxito ("Pago confirmado").
    *   Validación de la generación del número de orden.
    *   Verificación de redirección a la URL de confirmación.

## Solución de Problemas Frecuentes

*   **Versión de ChromeDriver**: Si recibe un error relacionado con la versión del driver, asegúrese de que su navegador Google Chrome esté actualizado. Maven y Selenium Manager suelen gestionar esto automáticamente, pero en ocasiones puede requerir ejecutar `mvn clean test` para forzar una actualización.
*   **Timeouts / Elemento no encontrado**: Si la conexión a internet es inestable, es posible que algún elemento tarde en cargar más de lo esperado. El framework incluye esperas explícitas, pero si el problema persiste, intente ejecutar la prueba nuevamente.

---
Desarrollado para el Curso de Testing Automatizado.
