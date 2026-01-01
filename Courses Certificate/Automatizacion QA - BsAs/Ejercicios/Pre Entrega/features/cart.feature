# language: es
# Autor: Luciano Moliterno
# Funcionalidad: Gestión del Carrito de Compras

@ui @regression
Característica: Carrito de Compras en SauceDemo
  Como usuario autenticado
  Quiero poder agregar productos al carrito
  Para posteriormente realizar una compra

  Antecedentes:
    Dado que el usuario está autenticado en SauceDemo con "standard_user" y "secret_sauce"

  @smoke
  Escenario: Agregar un producto al carrito
    Cuando el usuario agrega "Sauce Labs Backpack" al carrito
    Entonces el contador del carrito debe mostrar "1"
    Y el producto "Sauce Labs Backpack" debe estar en el carrito

  Escenario: Agregar múltiples productos al carrito
    Cuando el usuario agrega "Sauce Labs Backpack" al carrito
    Y el usuario agrega "Sauce Labs Bike Light" al carrito
    Y el usuario agrega "Sauce Labs Bolt T-Shirt" al carrito
    Entonces el contador del carrito debe mostrar "3"
    Y el carrito debe contener 3 productos

  Escenario: Eliminar producto del carrito
    Cuando el usuario agrega "Sauce Labs Backpack" al carrito
    Y el usuario accede al carrito
    Y el usuario elimina "Sauce Labs Backpack" del carrito
    Entonces el contador del carrito debe mostrar "0"
    Y el carrito debe estar vacío

  Esquema del escenario: Agregar diferentes productos
    Cuando el usuario agrega "<producto>" al carrito
    Entonces el contador del carrito debe mostrar "1"
    Y el producto "<producto>" debe estar visible en el carrito

    Ejemplos:
      | producto                  |
      | Sauce Labs Backpack       |
      | Sauce Labs Bike Light     |
      | Sauce Labs Bolt T-Shirt   |
      | Sauce Labs Fleece Jacket  |

  Escenario: Verificar persistencia del carrito
    Cuando el usuario agrega "Sauce Labs Backpack" al carrito
    Y el usuario navega a otra página del sitio
    Y el usuario regresa a la página de inventario
    Entonces el contador del carrito debe seguir mostrando "1"

