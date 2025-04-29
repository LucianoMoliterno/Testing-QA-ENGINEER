Feature: Registro de usuarios
    Como un nuevo usuario
    Quiero registrarme en el sistema
    Para poder acceder a las funciones personalizadas

Background: 
    Given estoy en el navegador de Opera

    #Comentario
    @Scenario1 @google

Scenario Outline: Registro de usuario exitoso
    Given estoy en la pagina de registro
    When completo el formulario de registro con "<nombre>" y "<apellido>"
    And hago click en el boton de registro 
    Then deberia ver un mensaje de bienvenida

Examples:
    | Nombre |Apellido|
    |Luciano |Moliterno|
    |Matias  |Vainonis|
    |Santiago|Silveira|

 @Scenario2 @facebook

Scenario Outline: Registro de usuario exitoso
    Given estoy en la pagina de registro
    When completo el formulario de registro con "<nombre>" y "<apellido>"
    And hago click en el boton de registro 
    Then deberia ver un mensaje de bienvenida

Examples:
    | Nombre |Apellido|
    |Luciano |Moliterno|
    |Matias  |Vainonis|
    |Santiago|Silveira|
