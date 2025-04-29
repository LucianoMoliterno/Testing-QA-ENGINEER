
describe('Prueba de Login', () => {
    it('Iniciar sesión con credenciales correctas', () => {
      cy.visit('https://example.cypress.io/commands/actions');
  
      // Escribir el usuario y la contraseña
      cy.get('#email1').type('usuario@ejemplo.com');
      cy.get('#password1').type('password123');
  
      // Enviar el formulario
      cy.get('.action-form').submit();
  
      // Verificar que el login fue exitoso (esto depende del sitio, pero en este caso revisamos un mensaje)
      cy.contains('Your form has been submitted!').should('be.visible');
    });
  });
  