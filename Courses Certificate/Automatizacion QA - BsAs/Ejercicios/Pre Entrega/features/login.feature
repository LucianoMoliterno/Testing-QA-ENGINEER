# language: es
# Autor: Luciano Moliterno
# Funcionalidad: Autenticación en SauceDemo

@ui
Característica: Login en SauceDemo
  Como usuario del sistema
  Quiero poder autenticarme con mis credenciales
  Para acceder a la tienda online

  Antecedentes:
    Dado que el usuario está en la página de login de SauceDemo

  @smoke
  Escenario: Login exitoso con credenciales válidas
    Cuando el usuario ingresa el nombre de usuario "standard_user"
    Y el usuario ingresa la contraseña "secret_sauce"
    Y el usuario hace clic en el botón de login
    Entonces el usuario debe ser redirigido a la página de inventario
    Y el usuario debe ver el título "Products" en la página

  Esquema del escenario: Login con credenciales inválidas
    Cuando el usuario ingresa el nombre de usuario "<usuario>"
    Y el usuario ingresa la contraseña "<password>"
    Y el usuario hace clic en el botón de login
    Entonces el usuario debe ver el mensaje de error "<mensaje_error>"

    Ejemplos:
      | usuario        | password       | mensaje_error                                                                  |
      | invalid_user   | secret_sauce   | Epic sadface: Username and password do not match any user in this service     |
      | standard_user  | wrong_password | Epic sadface: Username and password do not match any user in this service     |
      |                |                | Epic sadface: Username is required                                             |

  Escenario: Login con usuario bloqueado
    Cuando el usuario ingresa el nombre de usuario "locked_out_user"
    Y el usuario ingresa la contraseña "secret_sauce"
    Y el usuario hace clic en el botón de login
    Entonces el usuario debe ver el mensaje de error "Epic sadface: Sorry, this user has been locked out."

  Escenario: Login con campos vacíos
    Cuando el usuario hace clic en el botón de login sin ingresar credenciales
    Entonces el usuario debe ver el mensaje de error "Epic sadface: Username is required"

  Escenario: Login con solo usuario sin contraseña
    Cuando el usuario ingresa el nombre de usuario "standard_user"
    Y el usuario hace clic en el botón de login sin ingresar contraseña
    Entonces el usuario debe ver el mensaje de error "Epic sadface: Password is required"

