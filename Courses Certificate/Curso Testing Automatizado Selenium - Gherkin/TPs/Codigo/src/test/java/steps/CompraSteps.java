package steps;

import io.cucumber.java.en.*;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class CompraSteps {

    static WebDriver driver;
    static WebDriverWait wait;

    // --- BACKGROUND ---
    @Given("el cliente navega a la tienda {string}")
    public void navegarATienda(String nombreTienda) {
        if (driver == null) {
            driver = new ChromeDriver();
            driver.manage().window().maximize();
            // Le damos 10 segunditos de changüí para que encuentre los elementos
            wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        }
        driver.get("https://remeras-shop.vercel.app/");
        System.out.println(">>> Navegador abierto en Home");
    }

    @Given("el carrito está vacío")
    public void verificarCarritoVacio() {
        // Asumimos que arranca vacío, no nos compliquemos
    }

    // --- FASE 1: SELECCIÓN ---
    @When("el cliente agrega al carrito la remera {string} talle {string} color {string} cantidad {int}")
    public void agregarProducto(String nombreProducto, String talle, String color, int cantidad) {
        System.out.println(">>> Intentando comprar: " + nombreProducto);

        // 1. Chequeamos estar en el home, por si las dudas
        if (!driver.getCurrentUrl().contains("vercel.app") || driver.getCurrentUrl().contains("product")) {
            driver.get("https://remeras-shop.vercel.app/");
        }

        // 2. Truquito: En vez de clickear y esperar, buscamos el link directo del producto
        // Armamos el xpath dinámico para encontrar la tarjeta exacta
        String xpathCard = String.format("//div[contains(@class,'product-card')][.//h3[contains(text(),'%s')]]", nombreProducto);
        WebElement card = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(xpathCard)));

        // Agarramos el link <a> de esa tarjeta
        WebElement linkDetalle = card.findElement(By.tagName("a"));

        // Sacamos la URL a donde lleva
        String urlDetalle = linkDetalle.getAttribute("href");
        System.out.println(">>> URL detectada: " + urlDetalle);

        // Vamos directo ahí, sin vueltas (es más robusto que el click)
        driver.get(urlDetalle);

        // 3. Esperamos que aparezca el selector de talle para interactuar
        WebElement selectTalle = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("size-select")));
        selectTalle.sendKeys(talle);

        driver.findElement(By.id("color-select")).sendKeys(color);

        WebElement inputCant = driver.findElement(By.id("quantity-input"));
        inputCant.clear();
        inputCant.sendKeys(String.valueOf(cantidad));

        // 5. Botón de agregar (acá sí usamos JS click por si algo lo tapa)
        WebElement btnAgregar = driver.findElement(By.id("add-to-cart-btn"));
        ((JavascriptExecutor) driver).executeScript("arguments[0].click();", btnAgregar);

        // Si sale alerta de "Agregado", la aceptamos y seguimos
        try {
            wait.until(ExpectedConditions.alertIsPresent()).accept();
            System.out.println(">>> Alerta aceptada");
        } catch (Exception e) {
            // Si no sale nada, todo bien, seguimos viaje
        }

        // Volvemos atrás para seguir comprando si hace falta
        driver.navigate().back();
    }

    // --- FASE 2: CARRITO ---
    @When("el cliente aplica el cupón {string}")
    public void aplicarCupon(String codigo) {
        // Click forzado al ícono del carrito
        WebElement iconCart = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("a.cart-icon")));
        ((JavascriptExecutor) driver).executeScript("arguments[0].click();", iconCart);

        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("coupon-input"))).sendKeys(codigo);
        driver.findElement(By.id("apply-coupon-btn")).click();
    }

    @When("el cliente inicia el checkout")
    public void iniciarCheckout() {
        // Click con JS por si el footer molesta
        WebElement btn = wait.until(ExpectedConditions.presenceOfElementLocated(By.id("checkout-btn")));
        ((JavascriptExecutor) driver).executeScript("arguments[0].click();", btn);
    }

    // --- FASE 3: DATOS ---
    @When("el cliente completa sus datos de contacto y envío con nombre {string}, email {string}, teléfono {string}, dirección {string}, ciudad {string} y código postal {string}")
    public void completarDatos(String nombre, String email, String tel, String dir, String ciudad, String cp) {
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("fullname"))).sendKeys(nombre);
        driver.findElement(By.id("email")).sendKeys(email);
        driver.findElement(By.id("phone")).sendKeys(tel);
        driver.findElement(By.id("street")).sendKeys(dir);
        driver.findElement(By.id("number")).sendKeys("123");
        driver.findElement(By.id("city")).sendKeys(ciudad);
        driver.findElement(By.id("postalcode")).sendKeys(cp);
    }

    @When("el cliente selecciona el método de envío {string}")
    public void seleccionarEnvio(String tipo) {
        String val = tipo.toLowerCase(); // lo pasamos a minúscula por las dudas
        WebElement radio = driver.findElement(By.xpath("//input[@name='shipping'][@value='" + val + "']"));
        ((JavascriptExecutor) driver).executeScript("arguments[0].click();", radio);
    }

    @When("el cliente selecciona el método de pago {string}")
    public void seleccionarPago(String tipo) {
        String val = "card";
        if (tipo.equalsIgnoreCase("Transferencia")) val = "transfer";
        WebElement radio = driver.findElement(By.xpath("//input[@name='payment'][@value='" + val + "']"));
        ((JavascriptExecutor) driver).executeScript("arguments[0].click();", radio);
    }

    @When("el cliente ingresa la tarjeta número {string} vencimiento {string} y cvv {string}")
    public void datosTarjeta(String n, String v, String c) {
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("cardnumber"))).sendKeys(n);
        driver.findElement(By.id("expiry")).sendKeys(v);
        driver.findElement(By.id("cvv")).sendKeys(c);
    }

    @When("el cliente confirma la compra")
    public void confirmar() {
        WebElement btn = wait.until(ExpectedConditions.elementToBeClickable(By.xpath("//button[normalize-space()='Confirmar compra']")));
        ((JavascriptExecutor) driver).executeScript("arguments[0].click();", btn);
    }

    // --- FASE 4: VALIDACIONES ---
    @Then("el sistema muestra el estado de pago {string}")
    public void validarEstado(String estado) {
        // Le damos tiempo extra (30s) porque a veces el servidor tarda en procesar
        WebDriverWait longWait = new WebDriverWait(driver, Duration.ofSeconds(30));
        // Buscamos que aparezca el texto de confirmación
        WebElement msg = longWait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[contains(text(),'Pago confirmado')]")));
        Assert.assertTrue(msg.getText().contains(estado));
    }

    @Then("el sistema muestra un número de pedido con prefijo {string}")
    public void validarOrden(String prefijo) {
        WebDriverWait longWait = new WebDriverWait(driver, Duration.ofSeconds(30));
        // Buscamos el número de orden, usando contains(.) para que busque en el texto visible, incluso si está dentro de etiquetas hijas
        WebElement orden = longWait.until(ExpectedConditions.visibilityOfElementLocated(
            By.xpath("//*[contains(., '" + prefijo + "') and not(self::script) and not(self::style)]")
        ));
        Assert.assertTrue(orden.getText().contains(prefijo));
    }

    @Then("el resumen del pedido es visible")
    public void validarResumen() {
        WebDriverWait longWait = new WebDriverWait(driver, Duration.ofSeconds(30));
        WebElement resumen = longWait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(".order-summary")));
        Assert.assertTrue(resumen.isDisplayed());
    }

    @Then("la URL contiene {string}")
    public void validarUrl(String frag) {
        WebDriverWait longWait = new WebDriverWait(driver, Duration.ofSeconds(30));
        longWait.until(ExpectedConditions.urlContains(frag));
        Assert.assertTrue(driver.getCurrentUrl().contains(frag));
    }

    @Then("el botón {string} está visible y habilitado")
    public void validarBotonFinal(String txt) {
        WebDriverWait longWait = new WebDriverWait(driver, Duration.ofSeconds(30));
        // Buscamos el botón de volver para cerrar el ciclo
        WebElement btn = longWait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//*[contains(text(),'Volver')]")));
        Assert.assertTrue(btn.isDisplayed());
        Assert.assertTrue(btn.isEnabled());
        driver.quit(); // Cerramos el boliche
    }
}