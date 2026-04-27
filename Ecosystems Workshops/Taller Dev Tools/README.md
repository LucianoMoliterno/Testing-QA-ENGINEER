# Auditoría QA y Debugging: Taller de Herramientas de Desarrollo

Este repositorio contiene el material práctico, el código fuente y la documentación técnica resultante de un taller intensivo sobre el uso de **Chrome DevTools** aplicado al aseguramiento de calidad (QA). 
El objetivo principal fue realizar pruebas de **Caja Negra**, **Caja Gris** y análisis de causa raíz (**Debugging**) sobre aplicaciones web reales y entornos de prueba.

## Estructura del Proyecto

* **`/src`**: Código fuente de la aplicación "Calculadora JS" utilizada para las pruebas de debugging.
* **`/auditorias-qa`**: Reportes detallados de ejecución de pruebas y hallazgos técnicos.
* **`/material-teorico`**: Documentación de apoyo sobre el ecosistema de herramientas de desarrollo.

## Herramientas Utilizadas
Durante el proyecto se explotaron las siguientes funcionalidades de las DevTools:
* **Elements Panel**: Inspección del DOM y validación de reglas CSS.
* **Console**: Monitoreo de logs y ejecución de scripts para interactuar con la página.
* **Sources**: Análisis de archivos fuente y uso de *breakpoints* para depuración paso a paso.
* **Network**: Análisis de tráfico, códigos de estado HTTP y simulación de condiciones de red (Throttling).
* **Lighthouse**: Auditorías de performance y cumplimiento de estándares de accesibilidad (A11y).
* **Recorder**: Grabación y reproducción de flujos de usuario para captura de bugs intermitentes.

## Resumen de Auditorías

### 1. Aplicación Calculadora (Caja Negra y Blanca)
Se realizaron pruebas sobre `calculadora.html` identificando defectos críticos en la lógica de negocio mediante el panel de **Sources**:
* **Bug de Suma (QA-CALC-01)**: El visor restaba 1 al primer operando antes de sumar debido a una instrucción errónea (`--operandoa;`).
* **Bug de Multiplicación (QA-CALC-02)**: Se detectó una alteración intencional en el cálculo final (`+1;`) dentro de la función `resolver()`.

### 2. Auditoría en Steam (Análisis de Rendimiento y Accesibilidad)
Se utilizó la web de Steam como entorno de prueba para condiciones reales:
* **Rendimiento**: Bajo simulación de red **Slow 3G**, se detectó un cuello de botella en recursos multimedia, con banners que demoran hasta 23.38 segundos en cargar.
* **Accesibilidad (Lighthouse)**: La puntuación obtenida fue de 72/100, identificando 11 imágenes sin atributo `alt` y fallos en el ratio de contraste de texto.

## Conclusiones
El uso de estas herramientas permitió transformar reportes genéricos en evidencias técnicas precisas. La identificación exacta de las líneas de código defectuosas facilita la labor de desarrollo y acelera el ciclo de vida del software.

---
**Revisión técnica a cargo de:** Fernando Mamani
**Fecha de ejecución:** 26 de Abril de 2026
