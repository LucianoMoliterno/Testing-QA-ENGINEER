describe('Búsqueda en Google', () => {
  it('Busca "Cypress testing" en Google', () => {
    cy.visit('https://www.google.com');

    // Escribimos en la barra de búsqueda
    cy.get('[name="q"]').type('Cypress testing{enter}');

    // Verificamos que aparecen resultados
    cy.get('#search').should('exist');
  });
});
