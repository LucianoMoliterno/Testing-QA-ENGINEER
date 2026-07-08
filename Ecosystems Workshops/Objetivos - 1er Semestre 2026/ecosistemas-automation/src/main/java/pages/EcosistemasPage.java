package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

/**
 * Clase que representa la página principal de Ecosistemas Global.
 * Utiliza el patrón de diseño Page Object Model (POM) para separar
 * los selectores web (localizadores) y las acciones, de la lógica de las pruebas.
 */
public class EcosistemasPage {

    // El WebDriver es el controlador que envía las instrucciones al navegador
    private WebDriver driver;
    // WebDriverWait permite hacer "esperas explícitas" (esperar a que algo pase antes de actuar)
    private WebDriverWait wait;

    /* --- LOCALIZADORES (Mapeo de elementos de la interfaz) --- */

    // Uso XPath para encontrar el botón de aceptar cookies por su texto
    private By btnAceptarCookies = By.xpath("//button[contains(text(), 'Aceptar')]");

    // Uso linkText porque es la forma más rápida y estable de encontrar etiquetas <a> (enlaces)
    private By menuContacto = By.linkText("Contacto");
    private By menuTrabajaEnEco = By.linkText("Trabaja en ECO");

    /**
     * Constructor de la clase. Se ejecuta al instanciar (crear) la página en el test.
     * @param driver El controlador del navegador que le paso desde el test.
     */
    public EcosistemasPage(WebDriver driver) {
        this.driver = driver;
        // Configuro una espera máxima de 15 segundos para elementos lentos
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(15));
    }

    /* --- MÉTODOS DE ACCIÓN (Lo que un usuario haría en la web) --- */

    /**
     * Espera a que el botón de cookies sea clickeable, lo presiona y
     * maneja el tiempo de la animación de desaparición.
     */
    public void aceptarCookies() {
        // 1. Espera hasta que el botón esté listo y haz clic
        wait.until(ExpectedConditions.elementToBeClickable(btnAceptarCookies)).click();

        // 2. Pausa estática breve para permitir que la animación CSS del banner
        // termine de ocultarse y no bloquee los clics posteriores en el menú.
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    /**
     * Navega a la sección de Contacto.
     */
    public void irAContacto() {
        // Espero a que el enlace sea clickeable (visible y no bloqueado)
        wait.until(ExpectedConditions.elementToBeClickable(menuContacto)).click();
    }

    /**
     * Navega a la sección de reclutamiento / RRHH.
     */
    public void irATrabajaEnEco() {
        wait.until(ExpectedConditions.elementToBeClickable(menuTrabajaEnEco)).click();
    }
}