package tests;

import java.util.logging.Level;
import java.util.logging.Logger;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import pages.EcosistemasPage;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Clase principal de pruebas (Suite de Regresión) para Ecosistemas Global.
 * Utiliza TestNG para gestionar el ciclo de vida de los tests y las aserciones.
 */
public class EcosistemasTest {

    private WebDriver driver;
    private EcosistemasPage ecosistemasPage;

    @BeforeMethod
    public void setUp() {
        // Silencia los warnings rojos internos de Selenium en la consola
        Logger.getLogger("org.openqa.selenium").setLevel(Level.SEVERE);

        driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("https://ecosistemasglobal.com");
        ecosistemasPage = new EcosistemasPage(driver);
    }

    @Test(description = "Validar el cierre exitoso del banner de cookies")
    public void testAceptarCookies() {
        ecosistemasPage.aceptarCookies();

        // Tomo captura justo después de la acción y antes de validar
        tomarCaptura("AceptarCookies_Exito");

        String tituloPestana = driver.getTitle().toLowerCase();
        Assert.assertTrue(tituloPestana.contains("ecosistemas"), "Error: La página principal no cargó correctamente tras aceptar cookies.");
    }

    @Test(description = "Navegar exitosamente a la sección de Contacto")
    public void testNavegarAContacto() {
        ecosistemasPage.aceptarCookies();
        ecosistemasPage.irAContacto();

        // Tomo captura de la página de Contacto
        tomarCaptura("Navegacion_Contacto");

        String urlActual = driver.getCurrentUrl().toLowerCase();
        Assert.assertTrue(urlActual.contains("contacto"), "Error: No se redirigió a la vista de Contacto.");
    }

    @Test(description = "Navegar exitosamente a la sección Trabaja en ECO")
    public void testNavegarATrabajaEnEco() {
        ecosistemasPage.aceptarCookies();
        ecosistemasPage.irATrabajaEnEco();

        // Tomo captura de la página de RRHH
        tomarCaptura("Navegacion_TrabajaEnEco");

        String urlActual = driver.getCurrentUrl().toLowerCase();
        Assert.assertTrue(urlActual.contains("trabaja-en-eco") || urlActual.contains("trabaja"),
                "Error: No se redirigió a la vista de RRHH/Trabajo.");
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    /**
     * Método auxiliar para tomar capturas de pantalla y guardarlas en el proyecto.
     * @param nombreTest Nombre del archivo de salida (se le añadirá la fecha y hora).
     */
    private void tomarCaptura(String nombreTest) {
        try {
            // 1. Convierto el driver a la interfaz que permite sacar fotos
            TakesScreenshot screenshot = (TakesScreenshot) driver;

            // 2. Tomo la captura temporal en memoria
            File archivoOrigen = screenshot.getScreenshotAs(OutputType.FILE);

            // 3. Creo la carpeta "capturas" en la raíz del proyecto si no existe
            File directorio = new File("capturas");
            if (!directorio.exists()) {
                directorio.mkdirs();
            }

            // 4. Genero un nombre único usando la fecha y hora actual para no sobreescribir fotos viejas
            String timestamp = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
            String rutaDestino = "capturas/" + nombreTest + "_" + timestamp + ".png";

            // 5. Copio el archivo temporal a la carpeta destino
            Files.copy(archivoOrigen.toPath(), Paths.get(rutaDestino), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("📸 Evidencia guardada: " + rutaDestino);

        } catch (Exception e) {
            System.out.println("⚠️ Error al tomar la captura de pantalla: " + e.getMessage());
        }
    }
}