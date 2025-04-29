describe('Pruebas de Login con datos dinámicos', () => {
  beforeEach(() => {
    cy.visit('https://www.saucedemo.com/');
  });

  it('Login con usuario válido', function () {
    cy.fixture('usuarios').then((datos) => {
      cy.get('[data-test="username"]').type(datos.usuarioValido.username);
      cy.get('[data-test="password"]').type(datos.usuarioValido.password);
      cy.get('[data-test="login-button"]').click();
      cy.url().should('include', '/inventory.html');
    });
  });

  it('Login con usuario inválido', function () {
    cy.fixture('usuarios').then((datos) => {
      cy.get('[data-test="username"]').type(datos.usuarioInvalido.username);
      cy.get('[data-test="password"]').type(datos.usuarioInvalido.password);
      cy.get('[data-test="login-button"]').click();
      cy.get('[data-test="error"]').should('be.visible');
    });
  });
});

  