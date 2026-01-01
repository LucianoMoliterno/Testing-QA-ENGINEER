package runners;

import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
        // Acá le decimos dónde están los archivos .feature (los guiones de prueba)
        features = "src/test/resources/features",
        // Acá le indicamos en qué paquete están las clases Java con los pasos (CompraSteps)
        glue = "steps",
        // Esto genera un reporte HTML lindo en la carpeta target para ver qué pasó
        plugin = { "pretty", "html:target/cucumber-report.html" }
)
public class TestRunner {
    // Esta clase queda vacía, solo sirve para configurar y arrancar todo
}