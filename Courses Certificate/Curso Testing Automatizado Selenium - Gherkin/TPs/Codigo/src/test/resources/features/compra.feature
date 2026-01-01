Feature: Compra con tarjeta de crédito

  Background:
    Given el cliente navega a la tienda "Remeras Shop"
    And el carrito está vacío

  Scenario: Compra exitosa con cupón y tarjeta de crédito
    When el cliente agrega al carrito la remera "Remera Negra Básica" talle "M" color "negro" cantidad 2
    And el cliente agrega al carrito la remera "Remera Blanca Premium" talle "L" color "blanco" cantidad 1
    And el cliente aplica el cupón "CUPON10"
    And el cliente inicia el checkout
    And el cliente completa sus datos de contacto y envío con nombre "Juan Pérez", email "juan.perez@test.com", teléfono "3515555555", dirección "Av. Siempre Viva 123", ciudad "Córdoba" y código postal "5000"
    And el cliente selecciona el método de envío "normal"
    And el cliente selecciona el método de pago "Tarjeta de crédito"
    And el cliente ingresa la tarjeta número "4111111111111111" vencimiento "12/30" y cvv "123"
    And el cliente confirma la compra
    Then el sistema muestra el estado de pago "Pago confirmado"
    And el sistema muestra un número de pedido con prefijo "ORD-"
    And el resumen del pedido es visible
    And la URL contiene "/confirmation"
    And el botón "Volver a productos" está visible y habilitado